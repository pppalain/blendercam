import unittest
from pathlib import Path

import bpy

# from .test_suite import FabexGcodeTest

# Path to tests
test_path = str(Path(__file__).parent)

if __name__ == "__main__":
    # Queue and run tests
    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir=test_path,
        pattern="test*.py",
        top_level_dir="fabex",
    )
    # # Add a test method for each test case to the TestCase class
    # for test_case in FabexGcodeTest.get_test_cases():
    #     suite.append(self.run_test_case(test_case))

    # setattr(FabexGcodeTest, f"test_{test_case['subdir_name']}", test_func)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # quit Blender after running
    bpy.ops.wm.quit_blender()
