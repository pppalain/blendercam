from unittest import TestCase

from .utils import (
    build_extension,
    install_extension,
    activate_engine,
    blender,
)


class FabexOpPresetTest(TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        install_extension()
        import bpy

        self.op_preset = len(bpy.utils.preset_paths("cam_operations"))

    def test_op_preset(self):
        self.assertTrue(self.op_preset == 1)


class FabexMachinePresetTest(TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        activate_engine(self)
        import bpy

        self.machine_preset = len(bpy.utils.preset_paths("cam_machines"))

    def test_machine_preset(self):
        self.assertTrue(self.machine_preset == 1)


class FabexCutterPresetTest(TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        activate_engine(self)
        import bpy

        self.cutter_preset = len(bpy.utils.preset_paths("cam_machines"))

    def test_cutter_preset(self):
        self.assertTrue(self.cutter_preset == 1)
