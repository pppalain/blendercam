cam.ui.panels.optimisation
==========================

.. py:module:: cam.ui.panels.optimisation

.. autoapi-nested-parse::

   Fabex 'optimisation.py'

   'CAM Optimisation' properties and panel in Properties > Render



Classes
-------

.. autoapisummary::

   cam.ui.panels.optimisation.CAM_OPTIMISATION_Properties
   cam.ui.panels.optimisation.CAM_OPTIMISATION_Panel


Module Contents
---------------

.. py:class:: CAM_OPTIMISATION_Properties

   Bases: :py:obj:`bpy.types.PropertyGroup`


   .. py:attribute:: optimize
      :type:  BoolProperty(name='Reduce Path Points', description='Reduce path points', default=True, update=update_operation)


   .. py:attribute:: optimize_threshold
      :type:  FloatProperty(name='Reduction Threshold in μm', default=0.2, min=1e-09, max=1000, precision=20, update=update_operation)


   .. py:attribute:: use_exact
      :type:  BoolProperty(name='Use Exact Mode', description='Exact mode allows greater precision, but is slower with complex meshes', default=True, update=update_exact_mode)


   .. py:attribute:: imgres_limit
      :type:  IntProperty(name='Maximum Resolution in Megapixels', default=16, min=1, max=512, description='Limits total memory usage and prevents crashes. Increase it if you know what are doing', update=update_zbuffer_image)


   .. py:attribute:: pixsize
      :type:  FloatProperty(name='Sampling Raster Detail', default=0.0001, min=1e-05, max=0.1, precision=PRECISION, unit='LENGTH', update=update_zbuffer_image)


   .. py:attribute:: use_opencamlib
      :type:  BoolProperty(name='Use OpenCAMLib', description='Use OpenCAMLib to sample paths or get waterline shape', default=False, update=update_opencamlib)


   .. py:attribute:: exact_subdivide_edges
      :type:  BoolProperty(name='Auto Subdivide Long Edges', description='This can avoid some collision issues when importing CAD models', default=False, update=update_exact_mode)


   .. py:attribute:: circle_detail
      :type:  IntProperty(name='Detail of Circles Used for Curve Offsets', default=64, min=12, max=512, update=update_operation)


   .. py:attribute:: simulation_detail
      :type:  FloatProperty(name='Simulation Sampling Raster Detail', default=0.0002, min=1e-05, max=0.01, precision=PRECISION, unit='LENGTH', update=update_operation)


.. py:class:: CAM_OPTIMISATION_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Optimisation Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Optimisation ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_OPTIMISATION'



   .. py:attribute:: panel_interface_level
      :value: 2



   .. py:method:: draw(context)


