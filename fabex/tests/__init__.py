import unittest
from pathlib import Path
import shutil

import bpy

# Blender Executable
# Will use 'blender' if Blender is available on PATH
# blender = "blender"
# Otherwise supply the path to the Blender executable
path_to_blender_executable = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"

blender = path_to_blender_executable if shutil.which("blender") is None else "blender"

# Path to the 'fabex' directory
# __init__.py / tests / fabex
fabex_path = str(Path(__file__).parent.parent)
test_path = str(Path(__file__).parent)

if __name__ == "__main__":
    if __package__ is None:
        import sys

        sys.path.append(fabex_path)
        from tests.base import build_extension
    else:
        from .base import build_extension

    # Build fresh copy of extension
    build_extension(blender)

    # Queue and run tests
    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir=test_path,
        pattern="test*.py",
        # top_level_dir="fabex",
    )
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # quit Blender after running
    bpy.ops.wm.quit_blender()
