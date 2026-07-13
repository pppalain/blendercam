from unittest import TestCase

from .utils import (
    zip_extension,
    install_extension,
    activate_engine,
)


class FabexTypeTest(TestCase):
    """Test that a  operation can be added."""

    def setUp(self):
        install_extension()
        activate_engine(self)

    def test_ui_types(self):
        """Check if UI classes exist"""
        import bpy

        classes = [
            "TOPBAR_MT_import_gcode",
            "VIEW3D_MT_tools_add",
            "CAM_CUTTER_MT_presets",
            "CAM_OPERATION_MT_presets",
            "CAM_MACHINE_MT_presets",
            "CAM_UL_operations",
            "CAM_UL_chains",
            "VIEW3D_MT_PIE_CAM",
            "VIEW3D_MT_PIE_Operation",
            "VIEW3D_MT_PIE_Chains",
            "VIEW3D_MT_PIE_PackSliceRelief",
        ]

        for cls in classes:
            self.assertTrue(hasattr(bpy.types, cls))

    def test_scene_props(self):
        """Check if Property classes exist"""
        import bpy

        classes = [
            "cam_active_chain",
            "cam_active_operation",
            "cam_chains",
            "gcode_output_type",
            "cam_machine",
            "cam_material",
            "cam_text",
            "interface",
            "cam_names",
            # Machine Presets
            "avidcnc",
            "carbide3d",
            "cnc4all",
            "inventables",
            "millright",
            "onefinity",
            "ooznest",
            "sienci",
            "user_machine",
            # Cutter Presets
            "idcwoodcraft",
            "cadence",
            "user_cutter",
            # Operation Presets
            "finishing",
            "roughing",
            "user_operation",
            "operation_preset",
        ]

        for cls in classes:
            self.assertTrue(hasattr(bpy.context.scene, cls))

    def test_operator_types(self):
        """Check if Operator classes exist"""
        import bpy

        classes = [
            "object.curve_boolean",
            "object.convex_hull",
            "object.curve_intarsion",
            "object.curve_overcuts",
            "object.curve_overcuts_b",
            "object.silhouette",
            "object.silhouette_offset",
            "object.curve_remove_doubles",
            "object.mesh_get_pockets",
            "object.cam_pack_objects",
            "object.cam_slice_objects",
            "object.calculate_cam_path",
            "object.cam_simulate",
            "object.material_cam_position",
            "object.calculate_cam_paths_chain",
            "object.cam_export_paths_chain",
            "object.cam_simulate_chain",
            "object.curve_plate",
            "object.curve_drawer",
            "object.curve_mortise",
            "object.curve_interlock",
            "object.curve_puzzle",
            "object.sine",
            "object.lissajous",
            "object.hypotrochoid",
            "object.customcurve",
            "object.curve_hatch",
            "object.curve_gear",
            "object.curve_flat_cone",
            "scene.calculate_bas_relief",
            "scene.cam_chain_add",
            "scene.cam_chain_remove",
            "scene.cam_chain_operation_add",
            "scene.cam_chain_operation_remove",
            "scene.cam_operation_add",
            "scene.cam_operation_copy",
            "scene.cam_operation_remove",
            "scene.cam_operation_move",
            "render.cam_preset_operation_add",
        ]

        for cls in classes:
            self.assertTrue(hasattr(bpy.ops, cls))
