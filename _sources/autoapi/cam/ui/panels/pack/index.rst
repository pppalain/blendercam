cam.ui.panels.pack
==================

.. py:module:: cam.ui.panels.pack

.. autoapi-nested-parse::

   Fabex 'pack.py'

   'Pack Curves on Sheet' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.pack.CAM_PACK_Panel


Module Contents
---------------

.. py:class:: CAM_PACK_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Pack Panel


   .. py:attribute:: bl_space_type
      :value: 'PROPERTIES'



   .. py:attribute:: bl_region_type
      :value: 'WINDOW'



   .. py:attribute:: bl_context
      :value: 'render'



   .. py:attribute:: bl_label
      :value: '[ Pack ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_PACK'



   .. py:attribute:: bl_options


   .. py:attribute:: panel_interface_level
      :value: 2



   .. py:attribute:: use_property_split
      :value: True



   .. py:method:: draw(context)


