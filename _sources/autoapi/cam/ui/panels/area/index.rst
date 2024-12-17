cam.ui.panels.area
==================

.. py:module:: cam.ui.panels.area

.. autoapi-nested-parse::

   Fabex 'area.py'

   'CAM Operation Area' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.area.CAM_AREA_Panel


Module Contents
---------------

.. py:class:: CAM_AREA_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Operation Area Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Operation Area ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_OPERATION_AREA'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw(context)


