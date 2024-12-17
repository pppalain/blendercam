cam.ui.panels.popup
===================

.. py:module:: cam.ui.panels.popup


Classes
-------

.. autoapisummary::

   cam.ui.panels.popup.CAM_Popup_Panel


Module Contents
---------------

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


