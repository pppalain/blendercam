from unittest import TestCase

import bpy

from .utils import (
    activate_engine,
    install_extension,
    run_test_file,
    zip_extension,
)


class BlendFileTest(TestCase):
    """Test operations from the simple_cutout file."""

    @classmethod
    def setUpClass(self):
        zip_extension()
        install_extension()
        activate_engine(self)

    def test_simple_cutout(self):
        run_test_file("simple_cutout")
        paths = [
            ("cam_path_Op_Cutout", 20),
            ("cam_path_Op_Cutout_Layers", 173),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_first_down(self):
        run_test_file("first_down")
        paths = [
            ("cam_path_first_down", 451),
            ("cam_path_no_first_down", 397),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_min_depth(self):
        run_test_file("min_depth")
        paths = [
            ("cam_path_min_depth_custom", 2573),
            ("cam_path_min_depth_material", 2573),
            ("cam_path_min_depth_object", 2573),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_parallel(self):
        run_test_file("parallel")
        paths = [
            ("cam_path_Op_Parallel_Internal_Exact", 2095),
            ("cam_path_Op_Parallel_OCL", 2159),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_patterns(self):
        run_test_file("patterns")
        paths = [
            ("cam_path_Block", 1392),
            ("cam_path_Circles", 248984),
            ("cam_path_Cross", 4319),
            ("cam_path_Parallel", 58249),
            ("cam_path_Spiral", 249123),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_ramps(self):
        run_test_file("ramps")
        paths = [
            ("cam_path_helix_enter", 9559),
            ("cam_path_HelixEnter", 9559),
            ("cam_path_RampIn", 177413),
            ("cam_path_RampOut", 1650),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_simplify(self):
        run_test_file("simplify")
        paths = [
            ("cam_path_simplify", 1331),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_waterline(self):
        run_test_file("waterline")
        paths = [
            ("cam_path_Waterline_Internal", 13897),
            ("cam_path_Waterline_Internal_Exact", 1571),
            ("cam_path_Waterline_OCL", 4777),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    def test_four_axis(self):
        run_test_file("4axistest")
        paths = [
            ("cam_path_Op_Plane_1", 67),
        ]
        objects = bpy.data.objects
        for path in paths:
            name = path[0]
            vertices = path[1]
            self.assertIn(
                name,
                objects,
                msg=f"{path} not found!",
            )
            self.assertEqual(vertices, len(objects[name].data.vertices))

    # Medial fails due to invalid curve

    #     def test_medial(self):

    #         run_test_file("medial")

    #         paths = [
    #             "cam_path_fern",
    #             "cam_path_fern_curve",
    #             "cam_path_MedialPocket",
    #             "cam_path_Text_MedialPocket",
    #             "cam_path_Text",
    #         ]

    #         for path in paths:
    #             self.assertIn(path, bpy.data.objects, msg=f"Could not calculate {path}")
