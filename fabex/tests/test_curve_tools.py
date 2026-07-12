from unittest import TestCase

from .utils import (
    activate_dependencies,
    zip_extension,
    install_extension,
    activate_engine,
    blender,
)


class SilhouetteTest(TestCase):
    """Test that a Silhouette Curve can be added."""

    def setUp(self):
        zip_extension()
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_silhouette(self):
        self.assertIn("Cube_silhouette", self.objects)


class SilhouetteOffsetTest(TestCase):
    """Test that an Offset Silhouette can be added."""

    def setUp(self):
        zip_extension()
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.context.view_layer.objects["Cube"].select_set(state=True)
        bpy.ops.object.silhouette_offset()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_silhouette_offset(self):
        self.assertIn("Cube_offset_0.003", self.objects)
