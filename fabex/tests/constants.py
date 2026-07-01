# Blender Executable
# Use 'blender' if Blender is available on PATH
# blender = "blender"
# Otherwise supply the path to the Blender executable
BLENDER = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"

INSTALL_CODE = f"""
import bpy
bpy.context.preferences.system.use_online_access = True
bpy.ops.extensions.repo_sync_all(use_active_only=False)
bpy.ops.extensions.package_install(repo_index=0, pkg_id="stl_format_legacy")
bpy.ops.extensions.package_install(repo_index=0, pkg_id="simplify_curves_plus")
bpy.ops.extensions.package_install(repo_index=0, pkg_id="curve_tools")
bpy.ops.extensions.package_install_files(filepath='{sys.argv[1]}', repo='user_default')
bpy.ops.wm.save_userpref()
bpy.ops.wm.read_homefile(app_template="")
bpy.ops.script.reload()
bpy.ops.wm.quit_blender()
"""

# G-code Generator script, stripped down
GCODE_SCRIPT = """import sys
import warnings

import bpy

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
