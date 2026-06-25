from pathlib import Path
import unittest

import subprocess
from pathlib import Path

# Blender Executable
# Use 'blender' if Blender is available on PATH
# blender = "blender"

# Otherwise supply the path to the Blender executable
blender = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"

# To run the tests use the following command:
# blender --background --factory-startup  --python /path/to/this/__init__.py


def build_extension(blender):
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
    path = str(Path(__file__).parent)
    suite = loader.discover(path)
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # quit Blender after running
    import bpy

    bpy.ops.wm.quit_blender()
