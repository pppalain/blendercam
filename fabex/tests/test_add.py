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

        bpy.ops.wm.read_homefile()
        bpy.ops.scene.cam_operation_add()

        scene = bpy.context.scene
        self.operations = [operation.name for operation in scene.cam_operations]

    def test_path(self):
        self.assertIn("Op_Cube_1", self.operations)


class FabexAddSignPlateTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_plate()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_sign_plate(self):
        self.assertIn("plate", self.objects)


class FabexSilhouetteTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_silhouette(self):
        self.assertIn("Cube_silhouette", self.objects)


class FabexSilhouetteOffsetTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette_offset()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_silhouette_offset(self):
        self.assertIn("Cube_offset_0.003", self.objects)


class FabexAddDrawerTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_drawer()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.drawers = [
            "drawer_back",
            "drawer_bottom",
            "drawer_front",
            "drawer_side",
        ]

    def test_sign_plate(self):
        for drawer in self.drawers:
            self.assertIn(drawer, self.objects)


class FabexAddInterlockTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_interlock()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_interlock(self):
        self.assertIn("_groove", self.objects)


class FabexAddPuzzleJointsTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_puzzle()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_puzzle_joints(self):
        self.assertIn("curved_t", self.objects)


class FabexAddGearTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()
        bpy.ops.object.curve_gear()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_gear(self):
        self.assertTrue([obj.startswith("gear") for obj in self.objects])


class FabexAddSineTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.sine()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_sine(self):
        self.assertIn("Periodic Wave", self.objects)


class FabexAddLissajousTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.lissajous()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_lissajous(self):
        self.assertIn("Lissajous", self.objects)


class FabexAddHypotrochoidTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.hypotrochoid()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_puzzle_joints(self):
        self.assertIn("Hypotrochoid", self.objects)


class FabexAddCustomTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        # build_extension(blender)
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.customcurve()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_puzzle_joints(self):
        self.assertIn("Custom", self.objects)


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
