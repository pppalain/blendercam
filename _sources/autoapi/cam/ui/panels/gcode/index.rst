cam.ui.panels.gcode
===================

.. py:module:: cam.ui.panels.gcode

.. autoapi-nested-parse::

   Fabex 'gcode.py'

   'CAM G-code Options' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.gcode.CAM_GCODE_Panel


Module Contents
---------------

.. py:class:: CAM_GCODE_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Operation G-code Options Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Operation G-code ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_GCODE'



   .. py:attribute:: panel_interface_level
      :value: 1



   .. py:method:: draw(context)


