from unittest import TestCase

from .utils import (
    zip_extension,
    install_extension,
    activate_engine,
)


class FabexPresetTest(TestCase):
    """Test that a  operation can be added."""

    @classmethod
    def setUpClass(self):
        zip_extension()
        install_extension()
        activate_engine(self)

    def test_op_preset(self):
        import bpy

        self.op_preset = len(bpy.utils.preset_paths("cam_operations"))
        self.assertTrue(self.op_preset > 0)

    def test_machine_preset(self):
        import bpy

        self.machine_preset = len(bpy.utils.preset_paths("cam_machines"))
        self.assertTrue(self.machine_preset > 0)

    def test_cutter_preset(self):
        import bpy

        self.cutter_preset = len(bpy.utils.preset_paths("cam_cutters"))
        self.assertTrue(self.cutter_preset > 0)
