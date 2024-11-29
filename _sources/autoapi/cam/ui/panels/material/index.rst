cam.ui.panels.material
======================

.. py:module:: cam.ui.panels.material

.. autoapi-nested-parse::

   Fabex 'material.py'

   'CAM Material' properties and panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.material.CAM_MATERIAL_Properties
   cam.ui.panels.material.CAM_MATERIAL_PositionObject
   cam.ui.panels.material.CAM_MATERIAL_Panel


Module Contents
---------------

.. py:class:: CAM_MATERIAL_Properties

   Bases: :py:obj:`bpy.types.PropertyGroup`


   .. py:attribute:: estimate_from_model
      :type:  BoolProperty(name='Estimate Cut Area from Model', description='Estimate cut area based on model geometry', default=True, update=update_material)


   .. py:attribute:: radius_around_model
      :type:  FloatProperty(name='Radius Around Model', description='Increase cut area around the model on X and Y by this amount', default=0.0, unit='LENGTH', precision=PRECISION, update=update_material)


   .. py:attribute:: center_x
      :type:  BoolProperty(name='Center on X Axis', description='Position model centered on X', default=False, update=update_material)


   .. py:attribute:: center_y
      :type:  BoolProperty(name='Center on Y Axis', description='Position model centered on Y', default=False, update=update_material)


   .. py:attribute:: z_position
      :type:  EnumProperty(name='Z Placement', items=(('ABOVE', 'Above', 'Place object vertically above the XY plane'), ('BELOW', 'Below', 'Place object vertically below the XY plane'), ('CENTERED', 'Centered', 'Place object vertically centered on the XY plane')), description='Position below Zero', default='BELOW', update=update_material)


   .. py:attribute:: origin
      :type:  FloatVectorProperty(name='Material Origin', default=(0, 0, 0), unit='LENGTH', precision=PRECISION, subtype='XYZ', update=update_material)


   .. py:attribute:: size
      :type:  FloatVectorProperty(name='Material Size', default=(0.2, 0.2, 0.1), min=0, unit='LENGTH', precision=PRECISION, subtype='XYZ', update=update_material)


.. py:class:: CAM_MATERIAL_PositionObject

   Bases: :py:obj:`bpy.types.Operator`


   .. py:attribute:: bl_idname
      :value: 'object.material_cam_position'



   .. py:attribute:: bl_label
      :value: 'Position Object for CAM Operation'



   .. py:attribute:: bl_options


   .. py:method:: execute(context)


   .. py:method:: draw(context)


.. py:class:: CAM_MATERIAL_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   .. py:attribute:: bl_space_type
      :value: 'PROPERTIES'



   .. py:attribute:: bl_region_type
      :value: 'WINDOW'



   .. py:attribute:: bl_context
      :value: 'render'



   .. py:attribute:: bl_label
      :value: '[ Material ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_MATERIAL'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw(context)


