cam.ui.panels.op_properties
===========================

.. py:module:: cam.ui.panels.op_properties

.. autoapi-nested-parse::

   CMC CAM 'op_properties.py'

   'CAM Operation Setup' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.op_properties.CAM_OPERATION_PROPERTIES_Panel


Module Contents
---------------

.. py:class:: CAM_OPERATION_PROPERTIES_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Operation Properties Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Operation Setup ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_OPERATION'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw_overshoot(col)


   .. py:method:: draw(context)


