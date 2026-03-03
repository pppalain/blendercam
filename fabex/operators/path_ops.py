"""Fabex 'ops.py' © 2012 Vilem Novak

Blender Operator definitions are in this file.
They mostly call the functions from 'utils.py'
"""

from importlib import import_module
from math import pi
import os
import subprocess
import textwrap
import threading
import time
import traceback

import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    StringProperty,
    FloatProperty,
)
from bpy.types import Operator

from .async_op import (
    AsyncCancelledException,
    AsyncOperatorMixin,
)

from .. import __package__ as base_package
from ..constants import was_hidden_dict
from ..exception import CamException
from ..gcode.gcode_export import export_gcode_path
from ..toolpath import get_path

from ..utilities.async_utils import progress_async
from ..utilities.logging_utils import log
from ..utilities.shapely_utils import (
    shapely_to_curve,
    chunks_to_shapely,
)
from ..utilities.simple_utils import (
    activate,
    add_to_group,
    safe_filename,
)
from ..utilities.thread_utils import (
    threadCom,
    thread_read,
    timer_update,
)
from ..utilities.machine_utils import add_machine_area_object
from ..utilities.bounds_utils import get_bounds_worldspace
from ..utilities.operation_utils import (
    chain_valid,
    source_valid,
    reload_paths,
    get_chain_operations,
)


class PathsBackground(Operator):
    """Calculate CAM Paths in Background. File Has to Be Saved Before."""

    bl_idname = "object.calculate_cam_paths_background"
    bl_label = "Calculate CAM Paths in Background"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        """Execute the CAM operation in the background.

        This method initiates a background process to perform CAM operations
        based on the current scene and active CAM operation. It sets up the
        necessary paths for the script and starts a subprocess to handle the
        CAM computations. Additionally, it manages threading to ensure that
        the main thread remains responsive while the background operation is
        executed.

        Args:
            context: The context in which the operation is executed.

        Returns:
            dict: A dictionary indicating the completion status of the operation.
        """

        s = bpy.context.scene
        o = s.cam_operations[s.cam_active_operation]
        self.operation = o
        o.computing = True
        bpath = bpy.app.binary_path
        fpath = bpy.data.filepath

        for p in bpy.utils.script_paths():
            scriptpath = p + os.sep + "addons" + os.sep + "cam" + os.sep + "backgroundop.py"

            log.info(scriptpath)

            if os.path.isfile(scriptpath):
                break

        proc = subprocess.Popen(
            [bpath, "-b", fpath, "-P", scriptpath, "--", "-o=" + str(s.cam_active_operation)],
            bufsize=1,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        tcom = threadCom(o, proc)
        readthread = threading.Thread(target=thread_read, args=([tcom]), daemon=True)
        readthread.start()
        # self.__class__.cam_processes=[]

        if not hasattr(bpy.ops.object.calculate_cam_paths_background.__class__, "cam_processes"):
            bpy.ops.object.calculate_cam_paths_background.__class__.cam_processes = []

        bpy.ops.object.calculate_cam_paths_background.__class__.cam_processes.append(
            [readthread, tcom]
        )
        return {"FINISHED"}


class KillPathsBackground(Operator):
    """Remove CAM Path Processes in Background."""

    bl_idname = "object.kill_calculate_cam_paths_background"
    bl_label = "Kill Background Computation of an Operation"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        """Execute the CAM operation in the given context.

        This method retrieves the active CAM operation from the scene and
        checks if there are any ongoing processes related to CAM path
        calculations. If such processes exist and match the current operation,
        they are terminated. The method then marks the operation as not
        computing and returns a status indicating that the execution has
        finished.

        Args:
            context: The context in which the operation is executed.

        Returns:
            dict: A dictionary with a status key indicating the result of the execution.
        """

        s = bpy.context.scene
        o = s.cam_operations[s.cam_active_operation]
        self.operation = o

        if hasattr(bpy.ops.object.calculate_cam_paths_background.__class__, "cam_processes"):
            processes = bpy.ops.object.calculate_cam_paths_background.__class__.cam_processes

            for p in processes:
                tcom = p[1]

                if tcom.opname == o.name:
                    processes.remove(p)
                    tcom.proc.kill()
                    o.computing = False

        return {"FINISHED"}


async def _calc_path(operator, context):
    """Calculate the path for a given operator and context.

    This function processes the current scene's CAM operations based on
    the specified operator and context. It handles different geometry
    sources, checks for valid operation parameters, and manages the
    visibility of objects and collections. The function also retrieves the
    path using an asynchronous operation and handles any exceptions that may
    arise during this process. If the operation is invalid or if certain
    conditions are not met, appropriate error messages are reported to the
    operator.

    Args:
        operator (bpy.types.Operator): The operator that initiated the path calculation.
        context (bpy.types.Context): The context in which the operation is executed.

    Returns:
        tuple: A tuple indicating the status of the operation.
            Returns {'FINISHED', True} if successful,
            {'FINISHED', False} if there was an error,
            or {'CANCELLED', False} if the operation was cancelled.
    """

    s = bpy.context.scene
    o = s.cam_operations[s.cam_active_operation]

    # Log operation settings at start for debugging
    log.info("=" * 60)
    log.info(f"Operation Start: {o.name}")
    log.info("=" * 60)

    log.info("[Operation Setup]")
    if o.geometry_source == "OBJECT":
        log.info(f"Object = {o.object_name}")
    elif o.geometry_source == "COLLECTION":
        log.info(f"Collection = {o.collection_name}")
    else:
        log.info(f"Image = {o.source_image_name}")
    log.info(f"Axis Count = {o.machine_axes} axis")
    if o.machine_axes == "4":
        log.info(f"Strategy = {o.strategy_4_axis}")
        log.info(f"Rotary Axis 1 = {o.rotary_axis_1}")
    elif o.machine_axes == "5":
        log.info(f"Strategy = {o.strategy_5_axis}")
        log.info(f"Rotary Axis 1 = {o.rotary_axis_1}")
        log.info(f"Rotary Axis 2 = {o.rotary_axis_2}")
    else:
        log.info(f"Strategy = {o.strategy}")
    if o.strategy == "CUTOUT":
        log.info(f"Cut Type = {o.cut_type}")
        log.info(f"Outlines Count = {o.outlines_count}")
        log.info(f"Overshoot = {o.straight}")
        log.info(f"Lead In = {o.lead_in * 1000:.3f} mm")
        log.info(f"Lead Out = {o.lead_out * 1000:.3f} mm")
        log.info(f"Skin = {o.skin * 1000:.3f} mm")
        log.info(f"Stepover = {o.distance_between_paths * 1000:.3f} mm")
    elif o.strategy == "WATERLINE":
        log.info(f"Skin = {o.skin * 1000:.3f} mm")
        log.info(f"Waterline Fill = {o.waterline_fill}")
        log.info(f"Waterline Project = {o.waterline_project}")
        log.info(f"Stepover = {o.distance_between_paths * 1000:.3f} mm")
    elif o.strategy == "CARVE":
        log.info(f"Carve Depth = {o.carve_depth * 1000:.3f} mm")
        log.info(f"Skin = {o.skin * 1000:.3f} mm")
        log.info(f"Detail = {o.distance_along_paths * 1000:.3f} mm")
    elif o.strategy == "MEDIAL_AXIS":
        log.info(f"Threshold = {o.medial_axis_threshold * 1000:.3f} mm")
        log.info(f"Detail Size = {o.medial_axis_subdivision * 1000:.3f} mm")
        log.info(f"Add Pocket = {o.add_pocket_for_medial}")
        log.info(f"Add Medial Mesh = {o.add_mesh_for_medial}")
    elif o.strategy == "DRILL":
        log.info(f"Drill Type = {o.drill_type}")
    elif o.strategy == "POCKET":
        log.info(f"Pocket Type = {o.pocket_type}")
        log.info(f"Pocket Start = {o.pocket_option}")
        log.info(f"Skin = {o.skin * 1000:.3f} mm")
        log.info(f"Pocket to Curve = {o.pocket_to_curve}")
        log.info(f"Stepover = {o.distance_between_paths * 1000:.3f} mm")
    else:
        log.info(f"Inverse Milling = {o.inverse}")
        log.info(f"Skin = {o.skin * 1000:.3f} mm")
        if o.strategy in ["PARALLEL", "CROSS"]:
            log.info(f"Parallel Angle = {o.parallel_angle * 180 / pi:.1f} deg")
        log.info(f"Stepover = {o.distance_between_paths * 1000:.3f} mm")
        log.info(f"Detail = {o.distance_along_paths * 1000:.3f} mm")

    log.info("[A & B Axes]")
    if o.enable_a_axis:
        log.info(
            f"A Axis = Enabled, Angle = {o.rotation_a * 180 / pi:.1f} deg, A Along X = {o.a_along_x}"
        )
    else:
        log.info("A Axis = Disabled")
    if o.enable_b_axis:
        log.info(f"B Axis = Enabled, Angle = {o.rotation_b * 180 / pi:.1f} deg")
    else:
        log.info("B Axis = Disabled")

    log.info("[Array]")
    if o.array:
        log.info(
            f"Array = Enabled, X: {o.array_x_count} x {o.array_x_distance * 1000:.3f} mm, Y: {o.array_y_count} x {o.array_y_distance * 1000:.3f} mm"
        )
    else:
        log.info("Array = Disabled")

    log.info("[Bridges]")
    if o.use_bridges:
        log.info(
            f"Bridges = Enabled, Width = {o.bridges_width * 1000:.3f} mm, Height = {o.bridges_height * 1000:.3f} mm"
        )
        log.info(f"Bridge Collection = {o.bridges_collection_name or 'None'}")
        log.info(f"Use Bridge Modifiers = {o.use_bridge_modifiers}")
    else:
        log.info("Bridges = Disabled")

    log.info("[Optimisation]")
    log.info(f"Exact Mode = {o.optimisation.use_exact}")
    if o.optimisation.use_exact:
        log.info(f"Sim Detail = {o.optimisation.simulation_detail * 1000:.4f} mm")
        log.info(f"Offset Detail = {o.optimisation.circle_detail}")
        log.info(f"Use OpenCamLib = {o.optimisation.use_opencamlib}")
    else:
        log.info(f"Detail Size = {o.optimisation.pixsize * 1000:.4f} mm")
    log.info(f"Simplify G-Code = {o.remove_redundant_points}")
    log.info(f"Use Mesh Modifiers = {o.use_modifiers}")
    log.info(f"Hide All Others = {o.hide_all_others}")
    log.info(f"Parent Path to Object = {o.parent_path_to_object}")
    log.info(
        f"Reduce Path Points = {o.optimisation.optimize}, Threshold = {o.optimisation.optimize_threshold:.2f} μm"
    )

    log.info("[Operation Area]")
    log.info(f"Safe Height = {o.movement.free_height * 1000:.3f} mm")
    log.info(f"Depth Start = {o.max_z * 1000:.3f} mm")
    log.info(f"Depth Max = {o.min_z_from}")
    if o.min_z_from == "CUSTOM":
        log.info(f"Depth End = {o.min_z * 1000:.3f} mm")
    if o.strategy in ["BLOCK", "SPIRAL", "CIRCLES", "PARALLEL", "CROSS"]:
        log.info(f"Surfaces = {o.ambient_behaviour}")
        if o.ambient_behaviour == "AROUND":
            log.info(f"Ambient Radius = {o.ambient_radius * 1000:.3f} mm")
        log.info(f"Cutter stays in Ambient Limits = {o.ambient_cutter_restrict}")
    if o.strategy in ["BLOCK", "SPIRAL", "CIRCLES", "PARALLEL", "CROSS", "WATERLINE"]:
        limit_name = o.limit_curve.name if o.limit_curve else "None"
        log.info(f"Limit Curve = {o.use_limit_curve}, Curve = {limit_name}")
    log.info(f"Layers = {o.use_layers}, Layer Height = {o.stepdown * 1000:.3f} mm")

    log.info("[Movement]")
    log.info(f"Milling Type = {o.movement.type}")
    log.info(f"Cutter Spin = {o.movement.spindle_rotation}")
    log.info(f"Stay Low = {o.movement.stay_low}")
    if o.strategy in ["PARALLEL", "CROSS"]:
        log.info(f"Parallel Step Back = {o.movement.parallel_step_back}")
    log.info(f"G64 Geometry = {o.movement.useG64}")
    if o.movement.useG64:
        log.info(f"G64 Tolerance = {o.movement.G64 * 1000:.3f} mm")
    log.info(
        f"Protect Vertical = {o.movement.protect_vertical}, Angle Limit = {o.movement.protect_vertical_limit * 180 / pi:.1f} deg"
    )

    log.info("[Feedrate]")
    log.info(f"Feedrate = {o.feedrate * 1000:.1f} mm/min")
    log.info(f"Spindle RPM = {o.spindle_rpm:.0f}")
    log.info(f"Plunge Speed = {o.plunge_feedrate:.1f}%")
    log.info(f"Plunge Angle = {o.plunge_angle * 180 / pi:.1f} deg")

    log.info("[Cutter]")
    log.info(f"Type = {o.cutter_type}")
    log.info(f"Diameter = {o.cutter_diameter * 1000:.3f} mm")
    if o.cutter_type == "BALLCONE":
        log.info(f"Ball Radius = {o.ball_radius * 1000:.3f} mm")
    if o.cutter_type == "BULLNOSE":
        log.info(f"Bull Corner Radius = {o.bull_corner_radius * 1000:.3f} mm")
    if o.cutter_type == "CYLCONE":
        log.info(f"Cyl Bottom Diameter = {o.cylcone_diameter * 1000:.3f} mm")
    if o.cutter_type in ["VCARVE", "BALLCONE", "BULLNOSE", "CYLCONE"]:
        log.info(f"Tip Angle = {o.cutter_tip_angle:.1f} deg")
    log.info(f"Flutes = {o.cutter_flutes}")
    log.info(f"Tool Number = {o.cutter_id}")
    log.info("-" * 60)

    # Guard: prevent using a generated CAM path object as geometry source
    if o.geometry_source == "OBJECT":
        path_prefix = s.cam_names.path_prefix
        if o.object_name.startswith(path_prefix):
            selected_name = o.object_name

            # Try to auto-correct by finding which operation generated this path object
            correct_object_name = None
            for other_op in s.cam_operations:
                if other_op.path_object_name == selected_name:
                    if other_op.object_name and other_op.object_name in bpy.data.objects:
                        correct_object_name = other_op.object_name
                        break

            if correct_object_name:
                log.warning(
                    f"Auto-correcting object source: '{selected_name}' → '{correct_object_name}'"
                )
                o.object_name = correct_object_name
                operator.report(
                    {"WARNING"},
                    f"Object auto-corrected from '{selected_name}' to '{correct_object_name}'",
                )
            else:
                # Cannot recover - show error popup and cancel
                msg = (
                    f"Wrong object selected: '{selected_name}' is a CAM path object. "
                    "Delete this operation and create a new one with the correct source mesh selected."
                )
                log.error(msg)

                def draw_cam_object_error(self_menu, context):
                    layout = self_menu.layout
                    col = layout.column(align=True)
                    col.label(text="Wrong object selected!", icon="ERROR")
                    col.separator()
                    col.label(text=f"'{selected_name}' is a CAM path object.")
                    col.label(text="You may not use a CAM path as geometry source.")
                    col.separator()
                    col.label(text="The object name is stored in the operation.", icon="INFO")
                    col.label(text="Delete this operation and create a new one")
                    col.label(text="with the correct source mesh selected.")

                bpy.context.window_manager.popup_menu(
                    draw_cam_object_error,
                    title="CAM Object Selected - Operation Cancelled",
                    icon="ERROR",
                )
                operator.report({"ERROR"}, msg)
                return {"FINISHED", False}

    if o.geometry_source == "OBJECT":
        ob = bpy.data.objects[o.object_name]
        ob.hide_set(False)

    if o.geometry_source == "COLLECTION":
        obc = bpy.data.collections[o.collection_name]
        for ob in obc.objects:
            ob.hide_set(False)

    if o.strategy == "CARVE":
        curvob = bpy.data.objects[o.curve_source]
        curvob.hide_set(False)

    # if o.strategy == 'WATERLINE':
    #     ob = bpy.data.objects[o.object_name]
    #     ob.select_set(True)
    #     bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    path_name = s.cam_names.path_name_full
    mesh = bpy.data.meshes.get(path_name)

    if mesh:
        bpy.data.meshes.remove(mesh)

    text = "Operation can't be performed, see Warnings for info"

    if not o.valid:
        operator.report({"ERROR_INVALID_INPUT"}, text)
        progress_async(text)
        return {"FINISHED", False}

    # check for free movement height < maxz and return with error
    if o.movement.free_height < o.max_z:
        operator.report(
            {"ERROR_INVALID_INPUT"},
            "Free Movement Height Is Less than Operation Depth Start \n Correct and Try Again.",
        )
        progress_async("Operation Can't Be Performed, See Warnings for Info")
        return {"FINISHED", False}

    if o.computing:
        return {"FINISHED", False}

    o.operator = operator

    if o.use_layers:
        o.movement.parallel_step_back = False

    try:
        await get_path(context, o)
        log.info("Got Path Okay")

        # Restore source mesh as active object so that adding a new operation
        # auto-picks the source mesh rather than the generated CAM path
        if o.geometry_source == "OBJECT" and o.object_name in bpy.data.objects:
            source_ob = bpy.data.objects[o.object_name]
            bpy.ops.object.select_all(action="DESELECT")
            source_ob.select_set(True)
            bpy.context.view_layer.objects.active = source_ob
            log.info(f"Restored active object to source mesh: {o.object_name}")

    except CamException as e:
        log.error(e)
        traceback.print_tb(e.__traceback__)
        error_str = "\n".join(textwrap.wrap(str(e), width=80))
        operator.report({"ERROR"}, error_str)
        return {"FINISHED", False}

    except AsyncCancelledException as e:
        log.warning(e)
        return {"CANCELLED", False}

    except Exception as e:
        log.error(f"FAIL {e}")
        traceback.print_tb(e.__traceback__)
        operator.report({"ERROR"}, str(e))
        return {"FINISHED", False}

    coll = bpy.data.collections.get("RigidBodyWorld")

    if coll:
        bpy.data.collections.remove(coll)

    return {"FINISHED", True}


class CalculatePath(Operator, AsyncOperatorMixin):
    """Calculate CAM Paths"""

    bl_idname = "object.calculate_cam_path"
    bl_label = "Calculate CAM Paths"
    bl_options = {"REGISTER", "UNDO", "BLOCKING"}

    def __init__(self, *args, **kwargs):
        Operator.__init__(self, *args, **kwargs)
        AsyncOperatorMixin.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)

    @classmethod
    def poll(cls, context):
        """Check if the current CAM operation is valid.

        This method checks the active CAM operation in the given context and
        determines if it is valid. It retrieves the active operation from the
        scene's CAM operations and validates it using the `isValid` function.
        If the operation is valid, it returns True; otherwise, it returns False.

        Args:
            context (Context): The context containing the scene and CAM operations.

        Returns:
            bool: True if the active CAM operation is valid, False otherwise.
        """

        s = context.scene
        o = s.cam_operations[s.cam_active_operation] if len(s.cam_operations) > 0 else None

        if o is not None:
            if source_valid(o, context):
                return True
        return False

    async def execute_async(self, context):
        """Execute an asynchronous calculation of a path.

        This method performs an asynchronous operation to calculate a path based
        on the provided context. It awaits the result of the calculation and
        prints the success status along with the return value. The return value
        can be used for further processing or analysis.

        Args:
            context (Any): The context in which the path calculation is to be executed.

        Returns:
            Any: The result of the path calculation.
        """

        retval, success = await _calc_path(self, context)
        log.info(f"CALCULATED PATH (success={success},retval={retval})")

        # Import the Gcode file to Blender's Text Editor for inspection
        active_op = context.scene.cam_active_operation
        operation = context.scene.cam_operations[active_op]

        m = context.scene.cam_machine

        processor_extension = {
            "ANILAM": ("anilam_crusader_m", ".tap"),
            "CENTROID": ("centroid1", ".tap"),
            "EMC": ("emc2b", ".ngc"),
            "FADAL": ("fadal", ".tap"),
            "GRAVOS": ("gravos", ".nc"),
            "GRBL": ("grbl", ".gcode"),
            "HM50": ("hm50", ".tap"),
            "HEIDENHAIN": ("heiden", ".H"),
            "HEIDENHAIN530": ("heiden530", ".H"),
            "ISO": ("iso", ".tap"),
            "LYNX_OTTER_O": ("lynx_otter_o", ".nc"),
            "MACH3": ("mach3", ".tap"),
            "SHOPBOT MTC": ("shopbot_mtc", ".sbp"),
            "SIEGKX1": ("siegkx1", ".tap"),
            "TNC151": ("tnc151", ".tap"),
            "USER": {"user", ".gcode"},
            "WIN-PC": ("winpc", ".din"),
        }

        module = f".post_processors.{processor_extension[m.post_processor][0]}"
        postprocessor = import_module(module, base_package)
        extension = processor_extension[m.post_processor][1]

        name_raw = operation.name if operation.link_operation_file_names else operation.filename
        name = safe_filename(name_raw)
        export_location = context.scene.cam_names.default_export_location
        if export_location:
            basefilename = export_location + name + extension
        else:
            basefilename = (
                bpy.data.filepath[: -len(bpy.path.basename(bpy.data.filepath))] + name + extension
            )

        log.info(basefilename)
        bpy.ops.text.open(filepath=basefilename)

        try:
            areas = bpy.data.workspaces["Scripting"].screens["Scripting"].areas
            text_editor = [area.spaces[0] for area in areas if area.type == "TEXT_EDITOR"][0]

            with context.temp_override(space=text_editor):
                text_editor.text = bpy.data.texts[f"{name}{extension}"]

        except IndexError:
            pass

        return retval


class PathsAll(Operator):
    """Calculate All CAM Paths"""

    bl_idname = "object.calculate_cam_paths_all"
    bl_label = "Calculate All CAM Paths"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        """Execute CAM operations in the current Blender context.

        This function iterates through the CAM operations defined in the
        current scene and executes the background calculation for each
        operation. It sets the active CAM operation index and prints the name
        of each operation being processed. This is typically used in a Blender
        add-on or script to automate CAM path calculations.

        Args:
            context (bpy.context): The current Blender context.

        Returns:
            dict: A dictionary indicating the completion status of the operation,
                typically {'FINISHED'}.
        """

        i = 0
        for o in bpy.context.scene.cam_operations:
            bpy.context.scene.cam_active_operation = i
            log.info(f"\nCalculating Path : {o.name}")
            log.info("\n")
            bpy.ops.object.calculate_cam_paths_background()
            i += 1

        return {"FINISHED"}

    def draw(self, context):
        """Draws the user interface elements for the operation selection.

        This method utilizes the Blender layout system to create a property
        search interface for selecting operations related to CAM
        functionalities. It links the current instance's operation property to
        the available CAM operations defined in the Blender scene.

        Args:
            context (bpy.context): The context in which the drawing occurs,
        """

        layout = self.layout
        layout.prop_search(self, "operation", bpy.context.scene, "cam_operations")


class PathsChain(Operator, AsyncOperatorMixin):
    """Calculate a Chain and Export the G-code Alltogether."""

    bl_idname = "object.calculate_cam_paths_chain"
    bl_label = "Calculate CAM Paths in Current Chain and Export Chain G-code"
    bl_options = {"REGISTER", "UNDO", "BLOCKING"}

    def __init__(self, *args, **kwargs):
        Operator.__init__(self, *args, **kwargs)
        AsyncOperatorMixin.__init__(self, *args, **kwargs)
        super().__init__(*args, **kwargs)

    @classmethod
    def poll(cls, context):
        """Check the validity of the active CAM chain in the given context.

        This method retrieves the active CAM chain from the scene and checks
        its validity using the `isChainValid` function. It returns a boolean
        value indicating whether the CAM chain is valid or not.

        Args:
            context (Context): The context containing the scene and CAM chain information.

        Returns:
            bool: True if the active CAM chain is valid, False otherwise.
        """

        s = context.scene
        if len(s.cam_chains) > 0:
            chain = s.cam_chains[s.cam_active_chain]
            return chain_valid(chain, context)[0]
        else:
            return False

    async def execute_async(self, context):
        """Execute asynchronous operations for CAM path calculations.

        This method sets the object mode for the Blender scene and processes a
        series of CAM operations defined in the active CAM chain. It
        reports the progress of each operation and handles any exceptions that
        may occur during the path calculation. After successful calculations, it
        exports the resulting mesh data to a specified G-code file.

        Args:
            context (bpy.context): The Blender context containing scene and

        Returns:
            dict: A dictionary indicating the result of the operation,
            typically {'FINISHED'}.
        """

        s = context.scene

        # Ensure there is an active object, and force Object Mode
        if not context.mode == "OBJECT":
            operations = context.scene.cam_operations
            active_operation = operations[context.scene.cam_active_operation]
            context_object = context.scene.objects[active_operation.object_name]
            context.view_layer.objects.active = context_object
            bpy.ops.object.mode_set(mode="OBJECT")

        chain = s.cam_chains[s.cam_active_chain]
        chainops = get_chain_operations(chain)
        meshes = []

        try:
            for i in range(0, len(chainops)):
                s.cam_active_operation = s.cam_operations.find(chainops[i].name)
                self.report({"INFO"}, f"Calculating Path: {chainops[i].name}")
                result, success = await _calc_path(self, context)

                if not success and "FINISHED" in result:
                    self.report({"ERROR"}, f"Couldn't Calculate Path: {chainops[i].name}")

        except Exception as e:
            log.error(f"FAIL {e}")
            traceback.print_tb(e.__traceback__)
            self.report({"ERROR"}, str(e))
            return {"FINISHED"}

        for o in chainops:
            path_prefix = bpy.context.scene.cam_names.path_prefix
            meshes.append(bpy.data.objects[f"{path_prefix}_{o.name}"].data)

        export_gcode_path(chain.filename, meshes, chainops)
        return {"FINISHED"}


class PathExportChain(Operator):
    """Calculate a Chain and Export the G-code Together."""

    bl_idname = "object.cam_export_paths_chain"
    bl_label = "Export CAM Paths in Current Chain as G-code"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        """Check the validity of the active CAM chain in the given context.

        This method retrieves the currently active CAM chain from the scene
        context and checks its validity using the `isChainValid` function. It
        returns a boolean indicating whether the active CAM chain is valid or
        not.

        Args:
            context (object): The context containing the scene and CAM chain information.

        Returns:
            bool: True if the active CAM chain is valid, False otherwise.
        """

        s = context.scene
        chain = s.cam_chains[s.cam_active_chain] if len(s.cam_chains) > 0 else None
        return chain_valid(chain, context)[0]

    def execute(self, context):
        """Execute the CAM path export process.

        This function retrieves the active CAM chain from the current scene
        and gathers the mesh data associated with the operations of that chain.
        It then exports the G-code path using the specified filename and the
        collected mesh data. The function is designed to be called within the
        context of a Blender operator.

        Args:
            context (bpy.context): The context in which the operator is executed.

        Returns:
            dict: A dictionary indicating the completion status of the operation,
                typically {'FINISHED'}.
        """

        s = bpy.context.scene
        chain = s.cam_chains[s.cam_active_chain]
        chainops = get_chain_operations(chain)
        meshes = []

        for o in chainops:
            path_prefix = bpy.context.scene.cam_names.path_prefix
            meshes.append(bpy.data.objects[f"{path_prefix}_{o.name}"].data)

        export_gcode_path(chain.filename, meshes, chainops)
        return {"FINISHED"}


class PathExport(Operator):
    """Export G-code. Can Be Used only when the Path Object Is Present"""

    bl_idname = "object.cam_export"
    bl_label = "Export Operation G-code"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        """Execute the CAM operation and export the G-code path.

        This method retrieves the active CAM operation from the current scene
        and exports the corresponding G-code path to a specified filename. It
        prints the filename and relevant operation details to the console for
        debugging purposes. The G-code path is generated based on the CAM
        path data associated with the active operation.

        Args:
            context: The context in which the operation is executed.

        Returns:
            dict: A dictionary indicating the completion status of the operation,
                typically {'FINISHED'}.
        """

        s = bpy.context.scene
        operation = s.cam_operations[s.cam_active_operation]
        path_name = s.cam_names.path_name_full
        name_raw = operation.name if operation.link_operation_file_names else operation.filename
        name = safe_filename(name_raw)

        log.info(f"EXPORTING {name} {bpy.data.objects[path_name].data} {operation}")

        export_gcode_path(name, [bpy.data.objects[path_name].data], [operation])

        return {"FINISHED"}
