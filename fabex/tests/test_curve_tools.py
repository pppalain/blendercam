from unittest import TestCase

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
        import bpy

        bpy.ops.wm.read_homefile()

    def test_silhouette(self):
        import bpy

        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("Cube_silhouette", self.objects)

    def test_silhouette_offset(self):
        import bpy

        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette_offset()
        self.objects = [obj.name for obj in bpy.data.objects]
        self.assertIn("Cube_offset_0.003", self.objects)
