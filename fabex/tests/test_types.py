from unittest import TestCase

from .utils import (
    zip_extension,
    install_extension,
    activate_engine,
)


class FabexTypeTest(TestCase):
    """Test that a  operation can be added."""

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

    def setUp(self):
        install_extension()
        activate_engine(self)

    def test_ui_types(self):
        """Check if add-on panel exists"""
        import bpy

        for panel in self.classes:
            self.assertTrue(hasattr(bpy.types, panel))
