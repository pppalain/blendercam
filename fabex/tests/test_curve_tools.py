from unittest import TestCase

import bpy

from .utils import (
    zip_extension,
    install_extension,
)


class CurveToolsTest(TestCase):
    """Test that a Silhouette Curve can be added."""

    @classmethod
    def setUpClass(self):
        zip_extension()
        install_extension()

    def setUp(self):
        bpy.ops.wm.read_homefile()

    def test_silhouette(self):
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette()
        self.assertIn("Cube_silhouette", bpy.data.objects)

    def test_silhouette_offset(self):
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette_offset()
        self.assertIn("Cube_offset_0.003", bpy.data.objects)

    def test_curve_boolean(self):
        bpy.ops.curve.primitive_bezier_circle_add()
        bpy.ops.curve.primitive_bezier_curve_add()
        bpy.context.scene.objects["BézierCircle"].select_set(True)
        bpy.ops.object.curve_boolean()
        self.assertIn("boolean", bpy.data.objects)

    def test_convex_hull(self):
        bpy.ops.curve.primitive_bezier_circle_add()
        bpy.ops.object.convex_hull()
        self.assertIn("ConvexHull", bpy.data.objects)

    def test_curve_intarsion(self):
        bpy.ops.curve.primitive_bezier_circle_add()
        bpy.ops.object.curve_intarsion()
        objects = [
            "intarsion_pocket",
            "intarsion_profile",
        ]
        for obj in objects:
            self.assertIn(obj, bpy.data.objects)

    def test_overcuts_simple(self):
        bpy.ops.object.curve_drawer()
        bpy.ops.object.curve_overcuts()
        self.assertIn("drawer_bottom_overcuts", bpy.data.objects)

    def test_overcuts_bone(self):
        bpy.ops.object.curve_drawer()
        bpy.ops.object.curve_overcuts_b()
        self.assertIn("drawer_bottom_overcuts", bpy.data.objects)
