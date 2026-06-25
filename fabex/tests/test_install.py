import unittest
import subprocess
from pathlib import Path


class FabexDependencyTest(unittest.TestCase):
    """Test Addon Dependencies - Curve Tools, Simplify Curves+, STL Format (Legacy)
    Sets Online Access to True and downloads the required addons.
    Individual test functions check for each addon in Preferences.
    """

    def setUp(self):
        import bpy

        bpy.context.preferences.system.use_online_access = True
        bpy.ops.extensions.repo_sync_all(use_active_only=False)

        addons = bpy.context.preferences.addons
        modules = [addon.module for addon in addons]
        dependencies = [
            "curve_tools",
            "simplify_curves_plus",
            "stl_format_legacy",
        ]
        for dependency in dependencies:
            bpy.ops.extensions.package_install(repo_index=0, pkg_id=dependency)

    def test_curve_tools(self):
        """Check for Curve Tools addon"""
        import bpy

        addons = bpy.context.preferences.addons
        modules = [addon.module for addon in addons]
        self.assertIn(f"bl_ext.blender_org.curve_tools", modules)

    def test_simplify_curves_plus(self):
        """Check for Simplify Curves Plus addon"""
        import bpy

        addons = bpy.context.preferences.addons
        modules = [addon.module for addon in addons]
        self.assertIn(f"bl_ext.blender_org.simplify_curves_plus", modules)

    def test_stl_format_legacy(self):
        """Check for STL Format Legacy addon"""
        import bpy

        addons = bpy.context.preferences.addons
        modules = [addon.module for addon in addons]
        self.assertIn(f"bl_ext.blender_org.stl_format_legacy", modules)


class FabexInstallTest(unittest.TestCase):
    """Test Installation of addon, uses the zip created in the __init__"""

    def setUp(self):
        import bpy

        version_file = Path(__file__).parent.parent / "version.py"
        with open(version_file) as f:
            lines = f.readlines()
            version = lines[0].split("(")[1].replace(",", "")
        major, minor, patch = version[0], version[1], version[2]
        path = str(Path(__file__).parent.parent.parent / f"fabex-{major}.{minor}.{patch}.zip")
        bpy.ops.extensions.package_install_files(filepath=path, repo="user_default")

    def test_install(self):
        import bpy

        addons = bpy.context.preferences.addons
        modules = [addon.module for addon in addons]
        self.assertIn(f"bl_ext.user_default.fabex", modules)

    def tearDown(self):
        import bpy

        bpy.ops.wm.quit_blender()


# @unittest.skip("Disable")
class FabexDisableTest(unittest.TestCase):
    """Test Disabling the addon"""

    def setUp(self):
        import bpy

        bpy.ops.preferences.addon_disable(module="bl_ext.user_default.fabex")

    def test_disable(self):
        import bpy

        addons = bpy.context.preferences.addons
        modules = [addon.module for addon in addons]
        self.assertNotIn(f"bl_ext.user_default.fabex", modules)


# @unittest.skip("Enable")
class FabexEnableTest(unittest.TestCase):
    """Test Enabling the addon"""

    def setUp(self):
        import bpy

        bpy.ops.preferences.addon_enable(module="bl_ext.user_default.fabex")

    def test_disable(self):
        import bpy

        addons = bpy.context.preferences.addons
        modules = [addon.module for addon in addons]
        self.assertIn(f"bl_ext.user_default.fabex", modules)


class FabexEngineTest(unittest.TestCase):
    """Test that the Fabex Engine is available in the Scene."""

    def setUp(self):
        import bpy

        # Set the Render Engine to Fabex
        scene = bpy.context.scene
        scene.render.engine = "FABEX_RENDER"
        self.engine = scene.render.engine

    def test_engine(self):
        self.assertTrue(self.engine == "FABEX_RENDER")
