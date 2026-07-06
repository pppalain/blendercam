import unittest
from pathlib import Path

import bpy

# from .constants import BLENDER

# Path to the 'fabex' directory
# __init__.py / tests / fabex
fabex_path = str(Path(__file__).parent.parent)
test_path = str(Path(__file__).parent)

if __name__ == "__main__":
    if __package__ is None:
        import sys

        sys.path.append(fabex_path)
        from tests.base import build_extension, blender
    else:
        from .base import build_extension, blender

    # Build fresh copy of extension
    build_extension(blender)

    # Queue and run tests
    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir=test_path,
        pattern="test*.py",
        top_level_dir="fabex",
    )
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # quit Blender after running
    bpy.ops.wm.quit_blender()
