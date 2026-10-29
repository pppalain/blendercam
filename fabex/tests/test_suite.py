import difflib
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


class FabexGcodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_dir = os.getcwd()
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
                elif file.startswith("_") and file.endswith(".gcode"):
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
            lines = f.readlines()
            for line in lines:
                if line.startswith("("):
                    lines.remove(line)
            return "".join(lines)

    def execute_blender(self, blend_file):
        path = "test_func.py"
        Path(path).write_text(GCODE_SCRIPT)
        command = f'/home/spex/Documents/Blender/Releases/blender-5.2.0-linux-x64/blender -noaudio -b "{blend_file}" -P "{path}" --factory-startup'
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

                pattern = re.compile(r"(?<!G)[+-]?\d+(?:\.\d+)?", re.IGNORECASE)
                generated_stripped = [float(m.group(0)) for m in pattern.finditer(generated)]
                expected_stripped = [float(m.group(0)) for m in pattern.finditer(expected)]

                for i in range(len(generated_stripped)):
                    self.assertAlmostEqual(
                        generated_stripped[i],
                        expected_stripped[i],
                        delta=0.002,
                    )

                print(f"{generated_stripped[i]:>7} : {expected_stripped[i]} - Line {i}")

                # cleanup generated file unless test fails
                # os.remove(gcode_file[1:])


# if __name__ == "__main__":
#     # # Add a test method for each test case to the TestCase class
#     for test_case in FabexGcodeTest.get_test_cases():

#         def test_func(self, tc=test_case):
#             return self.run_test_case(tc)

#         setattr(FabexGcodeTest, f"test_{test_case['subdir_name']}", test_func)

#     unittest.main()
