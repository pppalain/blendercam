cam.ui.panels.chains
====================

.. py:module:: cam.ui.panels.chains

.. autoapi-nested-parse::

   Fabex 'chains.py'

   'CAM Chains' panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.chains.CAM_UL_operations
   cam.ui.panels.chains.CAM_UL_chains
   cam.ui.panels.chains.CAM_CHAINS_Panel


Module Contents
---------------

.. py:class:: CAM_UL_operations

   Bases: :py:obj:`bpy.types.UIList`


   .. py:method:: draw_item(context, layout, data, item, icon, active_data, active_propname, index)


.. py:class:: CAM_UL_chains

   Bases: :py:obj:`bpy.types.UIList`


   .. py:method:: draw_item(context, layout, data, item, icon, active_data, active_propname, index)


.. py:class:: CAM_CHAINS_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Chains Panel


   .. py:attribute:: bl_space_type
      :value: 'PROPERTIES'



   .. py:attribute:: bl_region_type
      :value: 'WINDOW'



   .. py:attribute:: bl_context
      :value: 'render'



   .. py:attribute:: bl_label
      :value: '[ Chains ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_CHAINS'



   .. py:attribute:: bl_options


   .. py:attribute:: panel_interface_level
      :value: 1



   .. py:attribute:: always_show_panel
      :value: True



   .. py:method:: draw(context)


