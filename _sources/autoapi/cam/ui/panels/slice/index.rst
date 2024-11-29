cam.ui.panels.slice
===================

.. py:module:: cam.ui.panels.slice

.. autoapi-nested-parse::

   Fabex 'slice.py'

   'Slice Model to Plywood Sheets' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.slice.CAM_SLICE_Panel


Module Contents
---------------

.. py:class:: CAM_SLICE_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Slicer Panel


   .. py:attribute:: bl_space_type
      :value: 'PROPERTIES'



   .. py:attribute:: bl_region_type
      :value: 'WINDOW'



   .. py:attribute:: bl_context
      :value: 'render'



   .. py:attribute:: bl_label
      :value: '[ Slice ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_SLICE'



   .. py:attribute:: bl_options


   .. py:attribute:: panel_interface_level
      :value: 2



   .. py:attribute:: use_property_split
      :value: True



   .. py:method:: draw(context)


