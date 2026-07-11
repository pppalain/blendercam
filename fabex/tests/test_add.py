import unittest
from pathlib import Path
import subprocess
import time
import os
import shutil

# import pytest
# import asyncio

from .test_install import activate_dependencies
from .utils import (
    build_extension,
    install_extension,
    activate_engine,
    blender,
)


class FabexAddOpTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        activate_engine(self)
        import bpy

        s = bpy.context.scene
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        # s.objects[o.name].select_set(state=True)
        bpy.context.view_layer.objects.active = bpy.context.view_layer.objects["Cube"]

        # bpy.context.view_layer.objects["Cube"].select_set(True)
        bpy.ops.scene.cam_operation_add()

    def test_path(self):
        import bpy

        scene = bpy.context.scene
        operations = [operation.name for operation in scene.cam_operations]

        self.assertIn("Op_Cube_1", operations)

    def tearDown(self):
        import bpy

        bpy.ops.wm.quit_blender()


class FabexAddSignPlateTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        import bpy

        bpy.ops.object.curve_plate()

    def test_sign_plate(self):
        import bpy

        objects = [obj.name for obj in bpy.data.objects]

        self.assertIn("plate", objects)

    def tearDown(self):
        import bpy

        bpy.ops.wm.quit_blender()


class FabexSilhouetteTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        import bpy

        s = bpy.context.scene
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        # s.objects[o.name].select_set(state=True)
        bpy.context.view_layer.objects.active = bpy.context.view_layer.objects["Cube"]

        bpy.ops.object.silhouette()

    def test_silhouette(self):
        import bpy

        objects = [obj.name for obj in bpy.data.objects]

        self.assertIn("Cube_silhouette", objects)


class FabexSilhouetteOffsetTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        import bpy

        s = bpy.context.scene
        bpy.ops.object.select_all(action="DESELECT")
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        # s.objects[o.name].select_set(state=True)
        bpy.context.view_layer.objects.active = bpy.context.view_layer.objects["Cube"]

        bpy.ops.object.silhouette_offset()

    def test_silhouette_offset(self):
        import bpy

        objects = [obj.name for obj in bpy.data.objects]

        self.assertIn("Cube_offset_0.003", objects)


class FabexAddDrawerTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.object.curve_drawer()

    def test_sign_plate(self):
        import bpy

        objects = [obj.name for obj in bpy.data.objects]
        drawers = [
            "drawer_back",
            "drawer_bottom",
            "drawer_front",
            "drawer_side",
        ]

        for drawer in drawers:
            self.assertIn(drawer, objects)


class FabexAddInterlockTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.object.curve_interlock()

    def test_interlock(self):
        import bpy

        objects = [obj.name for obj in bpy.data.objects]

        self.assertIn("_groove", objects)


class FabexAddPuzzleJointsTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.object.curve_puzzle()

    def test_puzzle_joints(self):
        import bpy

        objects = [obj.name for obj in bpy.data.objects]

        self.assertIn("curved_t", objects)


class FabexAddGearTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.object.curve_gear()

    def test_gear(self):
        import bpy

        objects = [obj.name for obj in bpy.data.objects]

        self.assertTrue([obj.startswith("gear") for obj in objects])


# class FabexCalculatePathTest(unittest.IsolatedAsyncioTestCase):
#     """Test that a Fabex operation can be added."""

#     def setUp(self):
#         install_extension()
#         activate_engine(self)
#         import bpy

#         bpy.context.view_layer.objects["Cube"].select_set(True)
#         bpy.ops.scene.cam_operation_add()
#         bpy.ops.object.calculate_cam_path()

#     # async def calculate_path(self):
#     #     import bpy

#     #     bpy.ops.object.calculate_cam_path()

#     @pytest.mark.asyncio
#     async def test_path(self):
#         # await _calc_path
#         import bpy

#         data = bpy.data
#         objects = [obj.name for obj in data.objects]

#         self.assertIn("Cube", bpy.data.objects)
