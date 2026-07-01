import unittest
from pathlib import Path
import subprocess

blender = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"


def build_extension(blender):
    # source_dir = str(Path(__file__).parent.parent / "fabex")
    # output_dir = str(Path(__file__).parent.parent)

    source_dir = str(Path(__file__).parent.parent)
    output_dir = str(Path(__file__).parent.parent.parent)

    subprocess.run(
        [
            blender,
            "--background",
            "--factory-startup",
            "--command",
            "extension",
            "build",
            "--source-dir",
            source_dir,
            "--output-dir",
            output_dir,
            # "--split-platforms",
        ],
    )


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

    # # quit Blender after running
    # import bpy

    # bpy.ops.wm.quit_blender()
