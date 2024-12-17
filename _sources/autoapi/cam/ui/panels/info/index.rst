cam.ui.panels.info
==================

.. py:module:: cam.ui.panels.info

.. autoapi-nested-parse::

   Fabex 'info.py'

   'CAM Info & Warnings' properties and panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.info.CAM_INFO_Properties
   cam.ui.panels.info.CAM_INFO_Panel


Module Contents
---------------

.. py:class:: CAM_INFO_Properties

   Bases: :py:obj:`bpy.types.PropertyGroup`


   .. py:attribute:: warnings
      :type:  StringProperty(name='Warnings', description='Warnings', default='', update=update_operation)


   .. py:attribute:: chipload
      :type:  FloatProperty(name='Chipload', description='Calculated chipload', default=0.0, unit='LENGTH', precision=CHIPLOAD_PRECISION)


   .. py:attribute:: duration
      :type:  FloatProperty(name='Estimated Time', default=0.01, min=0.0, max=MAX_OPERATION_TIME, precision=PRECISION, unit='TIME')


.. py:class:: CAM_INFO_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'TOOLS'



   .. py:attribute:: bl_options


   .. py:attribute:: bl_label
      :value: 'Info & Warnings'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_INFO'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:attribute:: always_show_panel
      :value: True



   .. py:method:: draw(context)


