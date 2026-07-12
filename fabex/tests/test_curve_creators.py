from unittest import TestCase

from .utils import (
    activate_dependencies,
    zip_extension,
    install_extension,
    activate_engine,
    blender,
)


class SignPlateTest(TestCase):
    """Test that a Sign Plate Curve can be added."""

    def setUp(self):
        zip_extension()
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_plate()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_sign_plate(self):
        self.assertIn("plate", self.objects)


class DrawerTest(TestCase):
    """Test that a Drawer Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_drawer()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.drawers = [
            "drawer_back",
            "drawer_bottom",
            "drawer_front",
            "drawer_side",
        ]

    def test_sign_plate(self):
        for drawer in self.drawers:
            self.assertIn(drawer, self.objects)


class MortiseTest(TestCase):
    """Test that an Interlock Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_interlock()
        bpy.ops.object.curve_mortise()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_mortise(self):
        self.assertIn("mortise", self.objects)


class InterlockTest(TestCase):
    """Test that an Interlock Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_interlock()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_interlock(self):
        self.assertIn("_groove", self.objects)


class PuzzleJointsTest(TestCase):
    """Test that a Puzzle Joint can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_puzzle()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_puzzle_joints(self):
        self.assertIn("curved_t", self.objects)


class SineTest(TestCase):
    """Test that a Sine Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.sine()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_sine(self):
        self.assertIn("Periodic Wave", self.objects)


class LissajousTest(TestCase):
    """Test that a Lissajous Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.lissajous()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_lissajous(self):
        self.assertIn("Lissajous", self.objects)


class HypotrochoidTest(TestCase):
    """Test that a Hypotrochoid Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.hypotrochoid()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_hypotrochoid(self):
        self.assertIn("Hypotrochoid", self.objects)


class CustomTest(TestCase):
    """Test that a Custom Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.customcurve()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_custom(self):
        self.assertIn("Custom", self.objects)


class CrosshatchTest(TestCase):
    """Test that a Crosshatch Curve can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.curve.primitive_bezier_circle_add()
        bpy.ops.object.curve_hatch()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_crosshatch(self):
        self.assertIn("BézierCircle_crosshatch", self.objects)


class GearTest(TestCase):
    """Test that a Gear can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.object.select_all(action="SELECT")
        bpy.ops.object.delete()
        bpy.ops.object.curve_gear()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_gear(self):
        self.assertTrue([obj.startswith("gear") for obj in self.objects])


class FlatConeTest(TestCase):
    """Test that a Flat Cone can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.object.curve_flat_cone()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_flat_cone(self):
        self.assertIn("flat_cone", self.objects)
