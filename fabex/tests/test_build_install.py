import unittest

if __package__ is None:
    import sys

    sys.path.append(fabex_path)
    from tests.base import (
        activate_dependencies,
        activate_engine,
        get_modules,
        install_extension,
    )
else:
    from .base import (
        activate_dependencies,
        activate_engine,
        get_modules,
        install_extension,
    )


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


class FabexAddOpTest(unittest.TestCase):
    """Test that a Fabex operation can be added."""

    def setUp(self):
        install_extension()
        activate_engine(self)
        import bpy

        bpy.context.view_layer.objects["Cube"].select_set(True)
        bpy.ops.scene.cam_operation_add()

    def test_path(self):
        import bpy

        scene = bpy.context.scene
        operations = [operation.name for operation in scene.cam_operations]

        self.assertIn("Op_Cube_1", operations)
