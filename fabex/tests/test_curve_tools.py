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
