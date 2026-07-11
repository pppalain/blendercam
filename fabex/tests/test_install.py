from unittest import TestCase

from .utils import (
    build_extension,
    activate_dependencies,
    activate_engine,
    install_extension,
    get_modules,
    blender,
)


class FabexDependencyTest(TestCase):
    """Test Addon Dependencies - Curve Tools, Simplify Curves+, STL Format (Legacy), Extra Curve Objectes
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

    def test_extra_curve_objectes(self):
        self.assertIn(
            "bl_ext.blender_org.extra_curve_objectes",
            self.modules,
        )


class FabexInstallTest(TestCase):
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


class FabexDisableTest(TestCase):
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


class FabexEnableTest(TestCase):
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


class FabexEngineTest(TestCase):
    """Test that the Fabex Engine is available in the Scene."""

    def setUp(self):
        build_extension(blender)
        install_extension()
        activate_engine(self)

    def test_engine(self):
        self.assertTrue(self.engine == "FABEX_RENDER")
