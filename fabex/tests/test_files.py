from unittest import TestCase

from .utils import (
    zip_extension,
    install_extension,
    activate_engine,
    add_collections,
    run_test_file,
)


class BlendFileTest(TestCase):
    """Test operations from the simple_cutout file."""

    @classmethod
    def setUpClass(self):
        install_extension()
        activate_engine(self)

    def test_simple_cutout(self):

        objects = run_test_file("simple_cutout")

        paths = [
            "cam_path_Op_Cutout",
            "cam_path_Op_Cutout_Layers",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_first_down(self):

        objects = run_test_file("first_down")

        paths = [
            "cam_path_first_down",
            "cam_path_no_first_down",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_min_depth(self):

        objects = run_test_file("min_depth")

        paths = [
            "cam_path_min_depth_custom",
            "cam_path_min_depth_material",
            "cam_path_min_depth_object",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_parallel(self):

        objects = run_test_file("parallel")

        paths = [
            "cam_path_Op_Parallel_Internal_Exact",
            "cam_path_Op_Parallel_OCL",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_patterns(self):

        objects = run_test_file("patterns")

        paths = [
            "cam_path_Block",
            "cam_path_Circles",
            "cam_path_Cross",
            "cam_path_Parallel",
            "cam_path_Spiral",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_ramps(self):

        objects = run_test_file("ramps")

        paths = [
            "cam_path_helix_enter",
            "cam_path_HelixEnter",
            "cam_path_RampIn",
            "cam_path_RampOut",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_simplify(self):

        objects = run_test_file("simplify")

        paths = [
            "cam_path_simplify",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_waterline(self):

        objects = run_test_file("waterline")

        paths = [
            "cam_path_Waterline_Internal",
            "cam_path_Waterline_Internal_Exact",
            "cam_path_Waterline_OCL",
        ]

        for path in paths:
            self.assertIn(path, objects)

    def test_four_axis(self):

        objects = run_test_file("4axistest")

        paths = [
            "cam_path_Op_Plane_1",
        ]

        for path in paths:
            self.assertIn(path, objects)

    # Medial fails due to invalid curve

    #     def test_medial(self):

    #         objects = run_test_file("medial")

    #         paths = [
    #             "cam_path_fern",
    #             "cam_path_fern_curve",
    #             "cam_path_MedialPocket",
    #             "cam_path_Text_MedialPocket",
    #             "cam_path_Text",
    #         ]

    #         for path in paths:
    #             self.assertIn(path, objects, msg=f"Could not calculate {path}")
