from unittest import TestCase

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
        import bpy

        bpy.ops.wm.read_homefile()

    def test_sign_plate(self):
        import bpy

        bpy.ops.object.curve_plate()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("plate", self.objects)

    def test_drawer(self):
        import bpy

        bpy.ops.object.curve_drawer()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.drawers = [
            "drawer_back",
            "drawer_bottom",
            "drawer_front",
            "drawer_side",
        ]

        for drawer in self.drawers:
            self.assertIn(drawer, self.objects)

    def test_mortise(self):
        import bpy

        bpy.ops.object.curve_interlock()
        bpy.ops.object.curve_mortise()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("mortise", self.objects)

    def test_interlock(self):
        import bpy

        bpy.ops.object.curve_interlock()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("_groove", self.objects)

    def test_puzzle_joints(self):
        import bpy

        bpy.ops.object.curve_puzzle()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("curved_t", self.objects)

    def test_sine(self):
        import bpy

        bpy.ops.object.sine()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("Periodic Wave", self.objects)

    def test_lissajous(self):
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.lissajous()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("Lissajous", self.objects)

    def test_hypotrochoid(self):
        import bpy

        bpy.ops.object.hypotrochoid()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("Hypotrochoid", self.objects)

    def test_custom(self):
        import bpy

        bpy.ops.object.customcurve()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("Custom", self.objects)

    def test_crosshatch(self):
        import bpy

        bpy.ops.curve.primitive_bezier_circle_add()
        bpy.ops.object.curve_hatch()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("BézierCircle_crosshatch", self.objects)

    def test_gear(self):
        import bpy

        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()
        bpy.ops.object.curve_gear()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertTrue([obj.startswith("gear") for obj in self.objects])

    def test_flat_cone(self):
        import bpy

        bpy.ops.object.curve_flat_cone()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("flat_cone", self.objects)
