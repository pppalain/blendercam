cam.ui.panels.feedrate
======================

.. py:module:: cam.ui.panels.feedrate

.. autoapi-nested-parse::

   Fabex 'feedrate.py'

   'CAM Feedrate' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.feedrate.CAM_FEEDRATE_Panel


Module Contents
---------------

.. py:class:: CAM_FEEDRATE_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Feedrate Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Feedrate ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_FEEDRATE'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw(context)


