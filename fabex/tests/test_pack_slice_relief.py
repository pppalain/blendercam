from unittest import TestCase

import bpy

from .utils import (
    activate_dependencies,
    install_extension,
)


class BasReliefTest(TestCase):
    """Test that a Bas Relief Mesh can be added."""

    def setUp(self):
        activate_dependencies(self)
        install_extension()

        bpy.ops.wm.read_homefile()
        bpy.ops.scene.calculate_bas_relief()

    def test_crosshatch(self):
        self.assertIn("BasReliefMesh", bpy.data.objects)
