import unittest
from pathlib import Path
import subprocess
import time
import os
import shutil

from .base import build_extension

path_to_blender_executable = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"

blender = path_to_blender_executable if shutil.which("blender") is None else "blender"


def blender_command(blender, command):
    path = "test_func.py"
    Path(path).write_text(command)

    subprocess.run(
        [
            "blender",
            "--background",
            "--factory-startup",
            "--python",
            path,
        ],
        shell=False,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    Path.unlink(path)


def activate_dependencies(self):
    import bpy

    bpy.context.preferences.system.use_online_access = True
    bpy.ops.extensions.repo_sync_all(use_active_only=False)

    dependencies = [
        "curve_tools",
        "simplify_curves_plus",
        "stl_format_legacy",
    ]

    addons = bpy.context.preferences.addons

    for dependency in dependencies:
        if dependency in addons:
            bpy.ops.preferences.addon_enable(module=f"bl_ext.blender_org.{dependency}")
        else:
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


class FabexDependencyTest(unittest.TestCase):
    """Test Addon Dependencies - Curve Tools, Simplify Curves+, STL Format (Legacy)
    Sets Online Access to True and downloads the required addons.
    Individual test functions check for each addon in Preferences.
    """

    def setUp(self):
        activate_dependencies(self)

    def test_curve_tools(self):
        """Check for Curve Tools addon"""
        self.assertIn(
            "bl_ext.blender_org.curve_tools",
            self.modules,
        )

    def test_simplify_curves_plus(self):
        """Check for Simplify Curves Plus addon"""
        self.assertIn(
            "bl_ext.blender_org.simplify_curves_plus",
            self.modules,
        )

    def test_stl_format_legacy(self):
        """Check for STL Format Legacy addon"""
        self.assertIn(
            "bl_ext.blender_org.stl_format_legacy",
            self.modules,
        )


class FabexInstallTest(unittest.TestCase):
    """Test Installation of addon, uses the zip created in the __init__"""

    def setUp(self):
        build_extension(blender)
        install_extension()
        get_modules(self)

    def test_install(self):
        self.assertIn(
            "bl_ext.user_default.fabex",
            self.modules,
        )

    def tearDown(self):
        import bpy

        bpy.ops.wm.quit_blender()


# @unittest.skip("Disable")
class FabexDisableTest(unittest.TestCase):
    """Test Disabling the addon"""

    def setUp(self):
        import bpy

        bpy.ops.preferences.addon_disable(module="bl_ext.user_default.fabex")
        get_modules(self)

    def test_disable(self):
        self.assertNotIn(
            "bl_ext.user_default.fabex",
            self.modules,
        )


# @unittest.skip("Enable")
class FabexEnableTest(unittest.TestCase):
    """Test Enabling the addon"""

    def setUp(self):
        import bpy

        bpy.ops.preferences.addon_enable(module="bl_ext.user_default.fabex")
        get_modules(self)

    def test_enable(self):
        self.assertIn(
            "bl_ext.user_default.fabex",
            self.modules,
        )


class FabexEngineTest(unittest.TestCase):
    """Test that the Fabex Engine is available in the Scene."""

    def setUp(self):
        activate_engine(self)

    def test_engine(self):
        self.assertTrue(self.engine == "FABEX_RENDER")
