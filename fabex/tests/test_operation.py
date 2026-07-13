from unittest import TestCase

from .utils import (
    zip_extension,
    install_extension,
    activate_engine,
    add_collections,
    blend_filepath,
)


class AddOperationTest(TestCase):
    """Test that a  operation can be added."""

    def setUp(self):
        import bpy

        zip_extension()
        install_extension()
        activate_engine(self)
        bpy.ops.wm.read_homefile()
        add_collections()
        bpy.ops.scene.cam_operation_add()

        scene = bpy.context.scene
        self.operations = [operation.name for operation in scene.cam_operations]
        self.operation = scene.cam_operations[scene.cam_active_operation]

    def test_add_operation(self):
        self.assertIn("Op_Cube_1", self.operations)

    def test_available_strategies(self):
        strategies = [
            "CUTOUT",
            "POCKET",
            "DRILL",
            "PARALLEL",
            "CROSS",
            "BLOCK",
            "SPIRAL",
            "CIRCLES",
            "OUTLINEFILL",
            "CARVE",
            "WATERLINE",
            "CURVE",
            "MEDIAL_AXIS",
        ]
        for strat in strategies:
            self.operation.strategy = strat
            self.assertTrue(self.operation.strategy == strat)


class CalculatePathTest(TestCase):
    """Test that a  operation can be added."""

    def setUp(self):
        import bpy

        install_extension()
        activate_engine(self)
        bpy.ops.wm.read_homefile()
        add_collections()
        bpy.ops.scene.cam_operation_add()
        bpy.ops.object.calculate_cam_path()

    def test_calculate_path(self):
        import bpy

        data = bpy.data
        objects = [obj.name for obj in data.objects]

        self.assertIn("cam_path_Op_Cube_1", objects)


class BlendFileTest(TestCase):
    """Test that an operation can be added."""

    def setUp(self):
        import bpy

        install_extension()
        activate_engine(self)
        path = blend_filepath(test="simple_cutout")
        bpy.ops.wm.open_mainfile(filepath=path)
        bpy.ops.object.calculate_cam_path()

    def test_cutout_blend(self):
        import bpy

        data = bpy.data
        objects = [obj.name for obj in data.objects]

        self.assertIn("cam_path_Op_Cutout", objects)
