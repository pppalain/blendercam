import difflib
import os
import subprocess
import sys
import unittest
import shutil
from pathlib import Path

# G-code Generator script, stripped down
GCODE_SCRIPT = """
import sys
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

path_to_blender_executable = "/home/spex/Documents/Blender/Releases/blender-5.1.2-linux-x64/blender"

blender = path_to_blender_executable if shutil.which("blender") is None else "blender"


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


def install_extension():
    import bpy

    version_file = Path(__file__).parent.parent / "version.py"
    with open(version_file) as f:
        lines = f.readlines()
        version = lines[0].split("(")[1].replace(",", "")
    major, minor, patch = version[0], version[1], version[2]
    path = str(Path(__file__).parent.parent.parent / f"fabex-{major}.{minor}.{patch}.zip")
    bpy.ops.extensions.package_install_files(filepath=path, repo="user_default")


def activate_engine():
    import bpy

    # Set the Render Engine to Fabex
    scene = bpy.context.scene
    scene.render.engine = "FABEX_RENDER"


# @unittest.skip("Old Gcode Test")
class FabexGcodeTest(unittest.TestCase):
    def setUp():
        install_extension()

    @classmethod
    def setUpClass(cls):
        cls.original_dir = os.getcwd()
        # cls.generator_path = os.path.join(cls.original_dir, "gcode_generator.py")
        cls.blend_test_cases = cls.get_test_cases()

    @staticmethod
    def get_test_cases():
        test_cases = []
        for root, _, files in os.walk("test_data"):
            subdir_name = os.path.basename(root)
            blend_file = gcode_files = None

            for file in files:
                if file.endswith(".blend"):
                    blend_file = file
                elif file.startswith("_") and (file.endswith(".gcode") or file.endswith(".tap")):
                    gcode_files = gcode_files or []
                    gcode_files.append(file)

            if blend_file and gcode_files:
                test_cases.append(
                    {
                        "subdir_name": subdir_name,
                        "blend_file": blend_file,
                        "gcode_files": gcode_files,
                    }
                )
        return test_cases

    @staticmethod
    def get_gcode_from_file(file):
        with open(file, "r") as f:
            return "".join(f.readlines()[1:])

    @staticmethod
    def get_diff(file1, file2, num_lines=10):
        with open(file1, "r") as f1, open(file2, "r") as f2:
            diff = difflib.unified_diff(
                f1.readlines()[1:],  # skip first line
                f2.readlines()[1:],  # skip first line
                fromfile=file1,
                tofile=file2,
            )
        return "".join(list(diff)[:num_lines])

    def execute_blender(self, blend_file):
        path = "test_func.py"
        Path(path).write_text(GCODE_SCRIPT)
        command = f'{blender} -noaudio -b "{blend_file}" -P "{path}"'
        print(f"Executing: {command}")
        subprocess.run(command, shell=True, check=True)
        Path.unlink(path)

    def run_test_case(self, test_case):
        # Start in the original working directory
        os.chdir(self.original_dir)
        blend_dir = os.path.join("test_data", test_case["subdir_name"])
        os.chdir(blend_dir)
        self.execute_blender(test_case["blend_file"])

        # Compare the generated and expected gcode for each operation
        for gcode_file in test_case["gcode_files"]:
            with self.subTest(operation=f"{test_case['subdir_name']}//{gcode_file}"):
                generated = self.get_gcode_from_file(gcode_file[1:])
                expected = self.get_gcode_from_file(gcode_file)

                if sys.platform == "darwin" and os.path.exists(gcode_file + ".mac"):
                    # bullet physics gives slightly different results on mac sometimes...
                    # this is something we can't fix, so compare against mac generated test
                    # file
                    print(f"Using Mac Test File {len(expected)} {len(generated)}")
                    expected = self.get_gcode_from_file(gcode_file + ".mac")
                    self.assertMultiLineEqual(
                        generated,
                        expected,
                        msg="\n" + self.get_diff(gcode_file[1:], gcode_file + ".mac"),
                    )

                else:
                    self.assertMultiLineEqual(
                        generated,
                        expected,
                        msg="\n" + self.get_diff(gcode_file[1:], gcode_file),
                    )

                os.remove(gcode_file[1:])  # cleanup generated file unless test fails


if __name__ == "__main__":
    # build_extension(blender)
    # install_extension()
    # activate_engine()
    # # Add a test method for each test case to the TestCase class
    for test_case in FabexGcodeTest.get_test_cases():

        def test_func(self, tc=test_case):
            return self.run_test_case(tc)

        setattr(FabexGcodeTest, f'test_{test_case["subdir_name"]}', test_func)

    unittest.main()
