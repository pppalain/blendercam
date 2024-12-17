cam.ui.panels.cutter
====================

.. py:module:: cam.ui.panels.cutter

.. autoapi-nested-parse::

   Fabex 'cutter.py'

   'CAM Cutter' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.cutter.CAM_CUTTER_Panel


Module Contents
---------------

.. py:class:: CAM_CUTTER_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Cutter Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Cutter ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_CUTTER'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw(context)


