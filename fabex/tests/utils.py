from pathlib import Path
import subprocess
import shutil

path_to_blender_executable = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"

blender = path_to_blender_executable if shutil.which("blender") is None else "blender"

# G-code Generator script, stripped down
GCODE_SCRIPT = """
import sys
import warnings
from pathlib import Path
import os
import zipfile

version_file = Path(__file__).parent.parent / "version.py"
with open(version_file) as f:
    lines = f.readlines()
    version = lines[0].split("(")[1].replace(",", "")
major, minor, patch = version[0], version[1], version[2]

extension_name = f"fabex-{major}.{minor}.{patch}.zip"
path = Path(__file__).parent.parent.parent / extension_name
file = zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED)
file.close()
bpy.ops.extensions.package_install_files(filepath=path, repo="user_default")

# Set the Render Engine to Fabex
scene = bpy.context.scene
scene.render.engine = "FABEX_RENDER"

operations = scene.cam_operations

for i, operation in enumerate(operations):
    # Set the active operation using the index
    scene.cam_active_operation = i

    # Run the calculate_cam_path() operator
    bpy.ops.object.calculate_cam_path()

sys.exit(0)
"""


def zip_extension():
    version_file = Path(__file__).parent.parent / "version.py"
    with open(version_file) as f:
        lines = f.readlines()
        version = lines[0].split("(")[1].replace(",", "")
    major, minor, patch = version[0], version[1], version[2]

    extension_name = f"fabex-{major}.{minor}.{patch}"
    path = Path(__file__).parent.parent
    shutil.make_archive(extension_name, "zip", path)


def activate_dependencies(self):
    import bpy

    bpy.context.preferences.system.use_online_access = True
    bpy.ops.extensions.repo_sync_all(use_active_only=False)

    dependencies = [
        "curve_tools",
        "simplify_curves_plus",
        "stl_format_legacy",
        "extra_mesh_objects",
        "extra_curve_objectes",
        "print3d_toolbox",
    ]

    for dependency in dependencies:
        try:
            bpy.ops.preferences.addon_enable(module=f"bl_ext.blender_org.{dependency}")
        except:
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
