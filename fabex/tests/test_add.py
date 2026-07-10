import unittest
from pathlib import Path
import subprocess
import time
import os
import shutil

import pytest
import asyncio

from .test_install import activate_dependencies

path_to_blender_executable = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"

blender = path_to_blender_executable if shutil.which("blender") is None else "blender"


def build_extension(blender):
    source_dir = str(Path(__file__).parent.parent)
    output_dir = str(Path(__file__).parent.parent.parent)

    subprocess.run(
        [
            blender,
            "--background",
            "--factory-startup",
            "--command",
            "extension",
            "build",
            "--source-dir",
            source_dir,
            "--output-dir",
            output_dir,
            # "--split-platforms",
        ],
    )


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


# class FabexAddDrawerTest(unittest.TestCase):
#     """Test that a Fabex operation can be added."""

#     def setUp(self):
#         install_extension()
#         import bpy

#         bpy.ops.object.curve_drawer()

#     def test_sign_plate(self):
#         import bpy

#         objects = [obj.name for obj in bpy.data.objects]
#         drawers = [
#             "drawer_back",
#             "drawer_bottom",
#             "drawer_front",
#             "drawer_side",
#         ]

#         # for drawer in drawers:
#         self.assertIn(drawer[0], objects)


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
