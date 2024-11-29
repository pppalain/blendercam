cam.ui.panels.operations
========================

.. py:module:: cam.ui.panels.operations

.. autoapi-nested-parse::

   Fabex 'operations.py'

   'CAM Operations' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.operations.CAM_OPERATIONS_Panel


Module Contents
---------------

.. py:class:: CAM_OPERATIONS_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Operations Panel


   .. py:attribute:: bl_space_type
      :value: 'PROPERTIES'



   .. py:attribute:: bl_region_type
      :value: 'WINDOW'



   .. py:attribute:: bl_context
      :value: 'render'



   .. py:attribute:: bl_label
      :value: '[ Operations ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_OPERATIONS'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:attribute:: always_show_panel
      :value: True



   .. py:method:: draw(context)


