from unittest import TestCase

import bpy

from .utils import (
    activate_dependencies,
    zip_extension,
    install_extension,
)


class CurveCreatorsTest(TestCase):
    """Test the Curve Creator Operators"""

    @classmethod
    def setUpClass(self):
        activate_dependencies(self)
        zip_extension()
        install_extension()

    def setUp(self):
        bpy.ops.wm.read_homefile()

    def test_sign_plate(self):
        bpy.ops.object.curve_plate()
        self.assertIn("plate", bpy.data.objects)

    def test_drawer(self):
        bpy.ops.object.curve_drawer()
        self.drawers = [
            "drawer_back",
            "drawer_bottom",
            "drawer_front",
            "drawer_side",
        ]
        for drawer in self.drawers:
            self.assertIn(drawer, bpy.data.objects)

    def test_mortise(self):
        bpy.ops.object.curve_interlock()
        bpy.ops.object.curve_mortise()
        self.assertIn("mortise", bpy.data.objects)

    def test_interlock(self):
        bpy.ops.object.curve_interlock()
        self.assertIn("_groove", bpy.data.objects)

    def test_puzzle_joints(self):
        bpy.ops.object.curve_puzzle()
        self.assertIn("curved_t", bpy.data.objects)

    def test_sine(self):
        bpy.ops.object.sine()
        self.assertIn("Periodic Wave", bpy.data.objects)

    def test_lissajous(self):
        bpy.ops.wm.read_homefile()
        bpy.ops.object.lissajous()
        self.assertIn("Lissajous", bpy.data.objects)

    def test_hypotrochoid(self):
        bpy.ops.object.hypotrochoid()
        self.assertIn("Hypotrochoid", bpy.data.objects)

    def test_custom(self):
        bpy.ops.object.customcurve()
        self.assertIn("Custom", bpy.data.objects)

    def test_crosshatch(self):
        bpy.ops.curve.primitive_bezier_circle_add()
        bpy.ops.object.curve_hatch()
        self.assertIn("BézierCircle_crosshatch", bpy.data.objects)

    def test_gear(self):
        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()
        bpy.ops.object.curve_gear()
        self.assertTrue([obj.name.startswith("gear") for obj in bpy.data.objects])

    def test_flat_cone(self):
        bpy.ops.object.curve_flat_cone()
        self.assertIn("flat_cone", bpy.data.objects)
