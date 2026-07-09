import pathlib
import shutil
import subprocess
import sys
import tempfile

# from fabex.tests.constants import INSTALL_CODE, NUM_RETRIES, BLENDER as blender
# from fabex.tests.base import blender_command

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


NUM_RETRIES = 10

# for x in range(NUM_RETRIES):
#     try:
#         blender_command(blender, INSTALL_CODE)
#         print("Addon Install: Success!")
#         sys.exit(0)

#     except subprocess.CalledProcessError as e:
#         print("Addon Install: Failed!")
#         print(f"Retrying: {e}")
#         print("Command Output:")
#         print("------------------------------")
#         print(e.output)
#         print("------------------------------")

# crash_file = pathlib.Path(line[len("Writing: ") :] for line in str(e.output) if line.startswith("Writing: "))

#         for line in str(e.output):
#             if line.startswith("Writing: "):
#                 crash_file = pathlib.Path(line[len("Writing: ") :])

#                 if crash_file.exists():
#                     print("Crash log:\n================")
#                     print(crash_file.read_text())
#                     print("============================")

# INSTALL_CODE = """
# from pathlib import Path

# import bpy

# version_file = Path(__file__).parent.parent / "version.py"
# with open(version_file) as f:
#     lines = f.readlines()
#     version = lines[0].split("(")[1].replace(",", "")
# major, minor, patch = version[0], version[1], version[2]
# path = str(Path(__file__).parent.parent.parent / f"fabex-{major}.{minor}.{patch}.zip")
# bpy.ops.extensions.package_install_files(filepath=path, repo="user_default")

# """


with tempfile.TemporaryDirectory() as td:
    file = pathlib.Path(td, "install.py")
    file.write_text(INSTALL_CODE)
    command = [shutil.which("blender"), "-b", "-P", str(file)]

    # blender 4.0 installing addon crashes sometimes on mac github actions...
    for x in range(NUM_RETRIES):
        try:
            subprocess.run(
                command,
                shell=False,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            print("Addon Install: Success!")
            sys.exit(0)

        except subprocess.CalledProcessError as e:
            print("Addon Install: Failed!")
            print(f"Retrying: {e}")
            print("Command Output:")
            print("------------------------------")
            print(e.output)
            print("------------------------------")

            for line in str(e.output):
                if line.startswith("Writing: "):
                    crash_file = pathlib.Path(line[len("Writing: ") :])

                    if crash_file.exists():
                        print("Crash log:\n================")
                        print(crash_file.read_text())
                        print("============================")
