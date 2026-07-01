from pathlib import Path
import subprocess
import tempfile

blender = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"
command = "print('Chungus')"


def blender_command(blender, command):

    path = "test_func.py"
    temp_file = Path(path).write_text(command)

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
