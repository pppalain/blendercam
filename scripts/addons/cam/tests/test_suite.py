import difflib
import unittest
import subprocess
import os

class BlenderCAMTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_dir = os.getcwd()
        cls.generator_path = os.path.join(cls.original_dir, "gcode_generator.py")

        cls.blend_test_cases = cls.get_test_cases()

    @staticmethod
    def get_test_cases():
        test_cases = []
        for root, _, files in os.walk('test_data'):
            subdir_name = os.path.basename(root)
            blend_file = gcode_files = None

            for file in files:
                if file.endswith('.blend'):
                    blend_file = file
                elif file.startswith('_') and file.endswith('.gcode'):
                    gcode_files = gcode_files or []
                    gcode_files.append(file)

            if blend_file and gcode_files:
                test_cases.append({
                    'subdir_name': subdir_name,
                    'blend_file': blend_file,
                    'gcode_files': gcode_files
                })
        return test_cases

    @staticmethod
    def get_gcode_from_file(file):
        with open(file, 'r') as f:
            return ''.join(f.readlines()[1:])

    @staticmethod
    def get_diff(file1, file2, num_lines=10):
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            diff = difflib.unified_diff(
                f1.readlines()[1:],  # skip first line
                f2.readlines()[1:],  # skip first line
                fromfile=file1,
                tofile=file2,
            )
        return ''.join(list(diff)[:num_lines])

    def execute_blender(self, blend_file):
        command = f'blender -b "{blend_file}" -P "{self.generator_path}"'
        subprocess.run(command, shell=True, check=True)

    def run_test_case(self, test_case):
        # Start in the original working directory
        os.chdir(self.original_dir)

        blend_dir = os.path.join('test_data', test_case["subdir_name"])
        os.chdir(blend_dir)
        self.execute_blender(test_case["blend_file"])

        # Compare the generated and expected gcode for each operation
        for gcode_file in test_case['gcode_files']:
            with self.subTest(operation=f"{test_case['subdir_name']}/{gcode_file}"):
                try:
                    generated = self.get_gcode_from_file(gcode_file[1:])
                    expected = self.get_gcode_from_file(gcode_file)
                    self.assertMultiLineEqual(generated, expected,
                        msg = "\n"+self.get_diff(gcode_file[1:], gcode_file))
                finally:
                    os.remove(gcode_file[1:])  # Cleanup generated file

if __name__ == '__main__':
    # Add a test method for each test case to the TestCase class
    for test_case in BlenderCAMTest.get_test_cases():
        test_func = lambda self, tc=test_case: self.run_test_case(tc)
        setattr(BlenderCAMTest, f'test_{test_case["subdir_name"]}', test_func)

    unittest.main()