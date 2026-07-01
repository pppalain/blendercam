import unittest
from pathlib import Path

import bpy

from .base import build_extension, blender


if __name__ == "__main__":
    # Build fresh copy of extension
    build_extension(blender)

    # Queue and run tests
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing
    path = str(Path(__file__).parent.parent / "tests")
    suite = loader.discover(path)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # quit Blender after running
    bpy.ops.wm.quit_blender()
