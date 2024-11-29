cam.ui.panels.machine
=====================

.. py:module:: cam.ui.panels.machine

.. autoapi-nested-parse::

   Fabex 'machine.py'

   'CAM Machine' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.machine.CAM_MACHINE_Panel


Module Contents
---------------

.. py:class:: CAM_MACHINE_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Machine Panel


   .. py:attribute:: bl_space_type
      :value: 'PROPERTIES'



   .. py:attribute:: bl_region_type
      :value: 'WINDOW'



   .. py:attribute:: bl_context
      :value: 'render'



   .. py:attribute:: bl_label
      :value: '[ Machine ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_MACHINE'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:attribute:: always_show_panel
      :value: True



   .. py:method:: draw(context)


