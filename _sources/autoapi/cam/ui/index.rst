cam.ui
======

.. py:module:: cam.ui

.. autoapi-nested-parse::

   Fabex 'ui.__init__.py' © 2012 Vilem Novak

   Import UI, Register and Unregister Classes



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/cam/ui/legacy_ui/index
   /autoapi/cam/ui/panels/index


Attributes
----------

.. autoapisummary::

   cam.ui.classes


Classes
-------

.. autoapisummary::

   cam.ui.CAM_AREA_Panel
   cam.ui.CAM_CHAINS_Panel
   cam.ui.CAM_UL_chains
   cam.ui.CAM_UL_operations
   cam.ui.CAM_BLANK_Panel
   cam.ui.CAM_CUTTER_Panel
   cam.ui.CAM_FEEDRATE_Panel
   cam.ui.CAM_GCODE_Panel
   cam.ui.CAM_INFO_Panel
   cam.ui.CAM_INFO_Properties
   cam.ui.CAM_INTERFACE_Properties
   cam.ui.CAM_MACHINE_Panel
   cam.ui.CAM_MATERIAL_Panel
   cam.ui.CAM_MATERIAL_PositionObject
   cam.ui.CAM_MATERIAL_Properties
   cam.ui.CAM_MOVEMENT_Panel
   cam.ui.CAM_MOVEMENT_Properties
   cam.ui.CAM_OPERATION_PROPERTIES_Panel
   cam.ui.CAM_OPERATIONS_Panel
   cam.ui.CAM_OPTIMISATION_Panel
   cam.ui.CAM_OPTIMISATION_Properties
   cam.ui.CAM_Popup_Panel
   cam.ui.VIEW3D_PT_tools_curvetools
   cam.ui.VIEW3D_PT_tools_create
   cam.ui.WM_OT_gcode_import


Functions
---------

.. autoapisummary::

   cam.ui.draw_interface
   cam.ui.progress_bar
   cam.ui.register
   cam.ui.unregister


Package Contents
----------------

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


.. py:class:: CAM_UL_chains

   Bases: :py:obj:`bpy.types.UIList`


   .. py:method:: draw_item(context, layout, data, item, icon, active_data, active_propname, index)


.. py:class:: CAM_UL_operations

   Bases: :py:obj:`bpy.types.UIList`


   .. py:method:: draw_item(context, layout, data, item, icon, active_data, active_propname, index)


.. py:class:: CAM_BLANK_Panel

   Bases: :py:obj:`bpy.types.Panel`


   CAM Blank Panel


   .. py:attribute:: bl_idname
      :value: 'CAM_PT_blank'



   .. py:attribute:: bl_label
      :value: ''



   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_options


   .. py:method:: draw(context)


.. py:class:: CAM_CUTTER_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Cutter Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Cutter ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_CUTTER'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw(context)


.. py:class:: CAM_FEEDRATE_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Feedrate Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Feedrate ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_FEEDRATE'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw(context)


.. py:class:: CAM_GCODE_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Operation G-code Options Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Operation G-code ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_GCODE'



   .. py:attribute:: panel_interface_level
      :value: 1



   .. py:method:: draw(context)


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


.. py:class:: CAM_INFO_Properties

   Bases: :py:obj:`bpy.types.PropertyGroup`


   .. py:attribute:: warnings
      :type:  StringProperty(name='Warnings', description='Warnings', default='', update=update_operation)


   .. py:attribute:: chipload
      :type:  FloatProperty(name='Chipload', description='Calculated chipload', default=0.0, unit='LENGTH', precision=CHIPLOAD_PRECISION)


   .. py:attribute:: duration
      :type:  FloatProperty(name='Estimated Time', default=0.01, min=0.0, max=MAX_OPERATION_TIME, precision=PRECISION, unit='TIME')


.. py:class:: CAM_INTERFACE_Properties

   Bases: :py:obj:`bpy.types.PropertyGroup`


   .. py:attribute:: level
      :type:  EnumProperty(name='Interface', description='Choose visible options', items=[('0', 'Basic', 'Only show essential options', '', 0), ('1', 'Advanced', 'Show advanced options', '', 1), ('2', 'Complete', 'Show all options', '', 2), ('3', 'Experimental', 'Show experimental options', 'EXPERIMENTAL', 3)], default='0', update=update_interface)


   .. py:attribute:: shading
      :type:  EnumProperty(name='Shading', description='Choose viewport shading preset', items=[('DEFAULT', 'Default', 'Standard viewport shading'), ('DELUXE', 'Deluxe', 'Cavity, Curvature, Depth of Field, Shadows & Object Colors'), ('CLEAN_DEFAULT', 'Clean Default', 'Standard viewport shading with no overlays'), ('CLEAN_DELUXE', 'Clean Deluxe', 'Deluxe shading with no overlays'), ('PREVIEW', 'Preview', 'HDRI Lighting Preview')], default='DEFAULT', update=update_shading)


   .. py:attribute:: layout
      :type:  EnumProperty(name='Layout', description='Presets for all panel locations', items=[('CLASSIC', 'Classic', 'Properties Area holds most panels, Tools holds the rest'), ('MODERN', 'Modern', 'Properties holds Main panels, Sidebar holds Operation panels, Tools holds Tools'), ('USER', 'User', 'Define your own locations for panels')], default='MODERN', update=update_layout)


   .. py:attribute:: main_location
      :type:  EnumProperty(name='Main Panels', description='Location for Chains, Operations, Material, Machine, Pack, Slice Panels', items=[('PROPERTIES', 'Properties', 'Default panel location is the Render tab of the Properties Area'), ('SIDEBAR', 'Sidebar (N-Panel)', 'Common location for addon UI, press N to show/hide'), ('TOOLS', 'Tools (T-Panel)', "Blender's Tool area, press T to show/hide")], default='PROPERTIES', update=update_user_layout)


   .. py:attribute:: operation_location
      :type:  EnumProperty(name='Operation Panels', description='Location for Setup, Area, Cutter, Feedrate, Optimisation, Movement, G-code', items=[('PROPERTIES', 'Properties', 'Default panel location is the Render tab of the Properties Area'), ('SIDEBAR', 'Sidebar (N-Panel)', 'Common location for addon UI, press N to show/hide'), ('TOOLS', 'Tools (T-Panel)', "Blender's Tool area, press T to show/hide")], default='SIDEBAR', update=update_user_layout)


   .. py:attribute:: tools_location
      :type:  EnumProperty(name='Tools Panels', description='Location for Curve Tools, Curve Creators, Info', items=[('PROPERTIES', 'Properties', 'Default panel location is the Render tab of the Properties Area'), ('SIDEBAR', 'Sidebar (N-Panel)', 'Common location for addon UI, press N to show/hide'), ('TOOLS', 'Tools (T-Panel)', "Blender's Tool area, press T to show/hide")], default='TOOLS', update=update_user_layout)


.. py:function:: draw_interface(self, context)

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


.. py:class:: CAM_MATERIAL_PositionObject

   Bases: :py:obj:`bpy.types.Operator`


   .. py:attribute:: bl_idname
      :value: 'object.material_cam_position'



   .. py:attribute:: bl_label
      :value: 'Position Object for CAM Operation'



   .. py:attribute:: bl_options


   .. py:method:: execute(context)


   .. py:method:: draw(context)


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


.. py:class:: CAM_MOVEMENT_Panel

   Bases: :py:obj:`cam.ui.panels.buttons_panel.CAMButtonsPanel`, :py:obj:`bpy.types.Panel`


   CAM Movement Panel


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'UI'



   .. py:attribute:: bl_category
      :value: 'CNC'



   .. py:attribute:: bl_label
      :value: '[ Movement ]'



   .. py:attribute:: bl_idname
      :value: 'WORLD_PT_CAM_MOVEMENT'



   .. py:attribute:: panel_interface_level
      :value: 0



   .. py:method:: draw(context)


.. py:class:: CAM_MOVEMENT_Properties

   Bases: :py:obj:`bpy.types.PropertyGroup`


   .. py:attribute:: type
      :type:  EnumProperty(name='Movement Type', items=(('CONVENTIONAL', 'Conventional (Up)', 'Cutter rotates against the direction of the feed'), ('CLIMB', 'Climb (Down)', 'Cutter rotates with the direction of the feed'), ('MEANDER', 'Meander (Zig Zag)', 'Cutting is done both with and against the rotation of the spindle')), description='movement type', default='CLIMB', update=update_operation)


   .. py:attribute:: insideout
      :type:  EnumProperty(name='Direction', items=(('INSIDEOUT', 'Inside out', 'a'), ('OUTSIDEIN', 'Outside in', 'a')), description='Approach to the piece', default='INSIDEOUT', update=update_operation)


   .. py:attribute:: spindle_rotation
      :type:  EnumProperty(name='Spindle Rotation', items=(('CW', 'Clockwise', 'a'), ('CCW', 'Counter clockwise', 'a')), description='Spindle rotation direction', default='CW', update=update_operation)


   .. py:attribute:: free_height
      :type:  FloatProperty(name='Safe Height', description='Height where the machine can freely move without hitting the workpiece', default=0.01, min=0.0, max=32, precision=PRECISION, unit='LENGTH', update=update_operation)


   .. py:attribute:: useG64
      :type:  BoolProperty(name='G64 Trajectory', description='Use only if your machine supports G64 code. LinuxCNC and Mach3 do', default=False, update=update_operation)


   .. py:attribute:: G64
      :type:  FloatProperty(name='Path Control Mode with Optional Tolerance', default=0.0001, min=0.0, max=0.005, precision=PRECISION, unit='LENGTH', update=update_operation)


   .. py:attribute:: parallel_step_back
      :type:  BoolProperty(name='Parallel Step Back', description='For roughing and finishing in one pass: mills material in climb mode, then steps back and goes between 2 last chunks back', default=False, update=update_operation)


   .. py:attribute:: helix_enter
      :type:  BoolProperty(name='Helix Enter - EXPERIMENTAL', description='Enter material in helix', default=False, update=update_operation)


   .. py:attribute:: ramp_in_angle
      :type:  FloatProperty(name='Ramp-in Angle', default=pi / 6, min=0, max=pi * 0.4999, precision=1, subtype='ANGLE', unit='ROTATION', update=update_operation)


   .. py:attribute:: helix_diameter
      :type:  FloatProperty(name='Helix Diameter - % of Cutter Diameter', default=90, min=10, max=100, precision=1, subtype='PERCENTAGE', update=update_operation)


   .. py:attribute:: ramp
      :type:  BoolProperty(name='Ramp-in - EXPERIMENTAL', description='Ramps down the whole contour, so the cutline looks like helix', default=False, update=update_operation)


   .. py:attribute:: Zigzag_ramp
      :type:  BoolProperty(name='Zigzag_ramp - EXPERIMENTAL', description='Ramps down the whole contour, so the cutline looks like zigzag_', default=False, update=update_operation)


   .. py:attribute:: ramp_out
      :type:  BoolProperty(name='Ramp-out - EXPERIMENTAL', description='Ramp out to not leave mark on surface', default=False, update=update_operation)


   .. py:attribute:: ramp_out_angle
      :type:  FloatProperty(name='Ramp-out Angle', default=pi / 6, min=0, max=pi * 0.4999, precision=1, subtype='ANGLE', unit='ROTATION', update=update_operation)


   .. py:attribute:: retract_tangential
      :type:  BoolProperty(name='Retract Tangential - EXPERIMENTAL', description='Retract from material in circular motion', default=False, update=update_operation)


   .. py:attribute:: retract_radius
      :type:  FloatProperty(name='Retract Arc Radius', default=0.001, min=1e-06, max=100, precision=PRECISION, unit='LENGTH', update=update_operation)


   .. py:attribute:: retract_height
      :type:  FloatProperty(name='Retract Arc Height', default=0.001, min=0.0, max=100, precision=PRECISION, unit='LENGTH', update=update_operation)


   .. py:attribute:: stay_low
      :type:  BoolProperty(name='Stay Low if Possible', default=True, update=update_operation)


   .. py:attribute:: merge_dist
      :type:  FloatProperty(name='Merge Distance - EXPERIMENTAL', default=0.0, min=0.0, max=0.1, precision=PRECISION, unit='LENGTH', update=update_operation)


   .. py:attribute:: protect_vertical
      :type:  BoolProperty(name='Protect Vertical', description='The path goes only vertically next to steep areas', default=True, update=update_operation)


   .. py:attribute:: protect_vertical_limit
      :type:  FloatProperty(name='Verticality Limit', description='What angle is already considered vertical', default=pi / 45, min=0, max=pi * 0.5, precision=0, subtype='ANGLE', unit='ROTATION', update=update_operation)


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


.. py:class:: CAM_Popup_Panel

   Bases: :py:obj:`bpy.types.Operator`


   .. py:attribute:: bl_idname
      :value: 'cam.popup'



   .. py:attribute:: bl_label
      :value: ''



   .. py:attribute:: text
      :type:  StringProperty(name='text', default='')


   .. py:method:: execute(context)


   .. py:method:: invoke(context, event)


   .. py:method:: draw(context)


.. py:class:: VIEW3D_PT_tools_curvetools

   Bases: :py:obj:`bpy.types.Panel`


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'TOOLS'



   .. py:attribute:: bl_context
      :value: 'objectmode'



   .. py:attribute:: bl_label
      :value: '[ Curve Tools ]'



   .. py:method:: draw(context)


.. py:class:: VIEW3D_PT_tools_create

   Bases: :py:obj:`bpy.types.Panel`


   .. py:attribute:: bl_space_type
      :value: 'VIEW_3D'



   .. py:attribute:: bl_region_type
      :value: 'TOOLS'



   .. py:attribute:: bl_context
      :value: 'objectmode'



   .. py:attribute:: bl_label
      :value: '[ Curve Creators ]'



   .. py:method:: draw(context)


.. py:class:: WM_OT_gcode_import

   Bases: :py:obj:`bpy.types.Operator`, :py:obj:`bpy_extras.io_utils.ImportHelper`


   Import G-code, Travel Lines Don't Get Drawn


   .. py:attribute:: bl_idname
      :value: 'wm.gcode_import'



   .. py:attribute:: bl_label
      :value: 'Import G-code'



   .. py:attribute:: filename_ext
      :value: '.txt'



   .. py:attribute:: filter_glob
      :type:  StringProperty(default='*.*', options={'HIDDEN'}, maxlen=255)


   .. py:attribute:: split_layers
      :type:  BoolProperty(name='Split Layers', description='Save every layer as single Objects in Collection', default=False)


   .. py:attribute:: subdivide
      :type:  BoolProperty(name='Subdivide', description="Only Subdivide gcode segments that are bigger than 'Segment length' ", default=False)


   .. py:attribute:: output
      :type:  EnumProperty(name='Output Type', items=(('mesh', 'Mesh', 'Make a mesh output'), ('curve', 'Curve', 'Make curve output')), default='curve')


   .. py:attribute:: max_segment_size
      :type:  FloatProperty(name='', description='Only Segments bigger than this value get subdivided', default=0.001, min=0.0001, max=1.0, unit='LENGTH')


   .. py:method:: execute(context)


.. py:data:: classes

.. py:function:: progress_bar(self, context)

.. py:function:: register()

.. py:function:: unregister()

