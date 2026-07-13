from unittest import TestCase
import asyncio

from .utils import (
    activate_dependencies,
    zip_extension,
    install_extension,
    activate_engine,
    blender,
)


class AddOperationTest(TestCase):
    """Test that a  operation can be added."""

    def setUp(self):
        zip_extension()
        install_extension()
        activate_engine(self)
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.scene.cam_operation_add()

        scene = bpy.context.scene
        self.operations = [operation.name for operation in scene.cam_operations]
        self.operation = scene.cam_operations[scene.cam_active_operation]

    def test_path(self):
        self.assertIn("Op_Cube_1", self.operations)

        # strategies = [
        #     'CUTOUT',
        #     'POCKET',
        #     'DRILL',
        #     'PARALLEL',
        #     'CROSS',
        #     'BLOCK',
        #     'SPIRAL',
        #     'CIRCLES',
        #     'OUTLINEFILL',
        #     'CARVE',
        #     'WATERLINE',
        #     'CURVE',
        #     'MEDIAL_AXIS',
        # ]

    def test_cutout_available(self):
        self.operation.strategy = "CUTOUT"
        self.assertTrue(self.operation.strategy == "CUTOUT")


# class CalculatePathTest(TestCase):
#     """Test that a  operation can be added."""

#     def setUp(self):
#         install_extension()
#         activate_engine(self)
#         import bpy

#         bpy.context.view_layer.objects["Cube"].select_set(True)
#         bpy.ops.scene.cam_operation_add()
#         bpy.ops.object.calculate_cam_path()

#     def test_path(self):
#         import bpy

#         data = bpy.data
#         objects = [obj.name for obj in data.objects]

#         self.assertIn("Cube", bpy.data.objects)
