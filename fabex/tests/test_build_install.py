import unittest
from pathlib import Path
import subprocess
import time


def blender_command(blender, command):
    path = "test_func.py"
    Path(path).write_text(command)

    subprocess.run(
        [
            blender,
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


# class FabexCalculatePathTest(unittest.TestCase):
#     """Test that a Fabex operation can be added."""

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

#         self.assertIn("cam_path_Op_Cube_1", objects)
