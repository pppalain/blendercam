from pathlib import Path
import shutil


def zip_extension():
    version_file = Path(__file__).parent.parent / "version.py"
    with open(version_file) as f:
        lines = f.readlines()
        version = lines[0].split("(")[1].replace(",", "")
    major, minor, patch = version[0], version[1], version[2]

    extension_name = f"fabex-{major}.{minor}.{patch}"
    path = Path(__file__).parent.parent
    shutil.make_archive(extension_name, "zip", path)


def activate_dependencies(self):
    import bpy

    bpy.context.preferences.system.use_online_access = True
    bpy.ops.extensions.repo_sync_all(use_active_only=False)

    dependencies = [
        "curve_tools",
        "simplify_curves_plus",
        "stl_format_legacy",
        "extra_mesh_objects",
        "extra_curve_objectes",
        "print3d_toolbox",
    ]

    for dependency in dependencies:
        try:
            bpy.ops.preferences.addon_enable(module=f"bl_ext.blender_org.{dependency}")
        except RuntimeError:
            bpy.ops.extensions.package_install(repo_index=0, pkg_id=dependency)

    addons = bpy.context.preferences.addons
    self.modules = [addon.module for addon in addons]


def get_modules(self):
    import bpy

    addons = bpy.context.preferences.addons
    self.modules = [addon.module for addon in addons]


def install_extension():
    import bpy

    version_file = Path(__file__).parent.parent / "version.py"
    with open(version_file) as f:
        lines = f.readlines()
        version = lines[0].split("(")[1].replace(",", "")
    major, minor, patch = version[0], version[1], version[2]
    path = str(Path(__file__).parent.parent.parent / f"fabex-{major}.{minor}.{patch}.zip")
    bpy.ops.extensions.package_install_files(filepath=path, repo="user_default")


def activate_engine(self):
    import bpy

    # Set the Render Engine to Fabex
    scene = bpy.context.scene
    scene.render.engine = "FABEX_RENDER"
    self.engine = scene.render.engine


def add_collections():
    """Adds color-coded Collection folders to the scene.

    This function adds three collections to aid in scene management.
    Bridges, Paths and Simulations are now auto-sorted into their
    own collections upon creation, which can be shown or hidden as
    groups.
    """
    import bpy

    context = bpy.context
    data = bpy.data
    collections = data.collections
    cam_names = context.scene.cam_names
    path_prefix = cam_names.path_prefix
    simulation_prefix = cam_names.simulation_prefix

    scene_collection = context.scene.collection
    default_collection = collections["Collection"]
    fabex_collections = [
        ("Bridges (Tabs)", "COLOR_06"),
        ("Paths", "COLOR_04"),
        ("Simulations", "COLOR_05"),
    ]

    for collection, color in fabex_collections:
        if collection not in collections:
            collections.new(collection)
            scene_collection.children.link(collections[collection])
            collections[collection].color_tag = color

    bridges_collection = collections["Bridges (Tabs)"]
    paths_collection = collections["Paths"]
    simulations_collection = collections["Simulations"]

    children = default_collection.children
    for child in children:
        prefix = child.name.startswith
        if prefix("bridge"):
            bridges_collection.children.link(child)
            default_collection.children.unlink(child)

    objects = default_collection.objects
    for obj in objects:
        prefix = obj.name.startswith
        if prefix(path_prefix):
            try:
                paths_collection.objects[obj.name]
            except RuntimeError:
                paths_collection.objects.link(obj)
        if prefix(simulation_prefix):
            try:
                simulations_collection.objects[obj.name]
            except RuntimeError:
                simulations_collection.objects.link(obj)
        if prefix in ["bridge", path_prefix, simulation_prefix]:
            default_collection.objects.unlink(obj)


def run_test_file(test):
    from pathlib import Path
    import bpy

    path = str(Path(__file__).parent / "test_data" / test / f"{test}.blend")
    bpy.ops.wm.open_mainfile(filepath=path)
    scene = bpy.context.scene
    operations = scene.cam_operations
    # Set the active operation using the index
    for i, operation in enumerate(operations):
        scene.cam_active_operation = i
        # Run the calculate_cam_path() operator
        bpy.ops.object.calculate_cam_path()

    return [obj.name for obj in bpy.data.objects]


# def build_extension():
#     source_dir = str(Path(__file__).parent.parent)
#     output_dir = str(Path(__file__).parent.parent.parent)

#     subprocess.run(
#         [
#             "blender",
#             "--background",
#             "--factory-startup",
#             "--command",
#             "extension",
#             "build",
#             "--source-dir",
#             source_dir,
#             "--output-dir",
#             output_dir,
#             # "--split-platforms",
#         ],
#     )
