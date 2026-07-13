from unittest import TestCase

from .utils import (
    activate_dependencies,
    install_extension,
)


class BasReliefTest(TestCase):
    """Test that a Bas Relief Mesh can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()
        import bpy

        bpy.ops.wm.read_homefile()
        bpy.ops.scene.calculate_bas_relief()
        self.objects = [obj.name for obj in bpy.data.objects]

    def test_crosshatch(self):
        self.assertIn("BasReliefMesh", self.objects)
