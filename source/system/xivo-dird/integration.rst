.. _xivo-dird-integration:

**********************************************
Integration of XiVO dird with the rest of XiVO
**********************************************

Configuration values
====================

Views
-----

In the :ref:`main configuration file <configuration-file>` of xivo-dird in the ``views`` section, the
following keys are interpreted and displayed in xlet people of the XiVO Client:

``title``
   The ``title`` will be shown as a header for the column

``type``
   * ``agent``: the field value will be ignored and replaced by an icon showing the status of the
     agent assigned to the contact (e.g. green icon for logged agent, red icon for unlogged agent,
     ...)
   * ``mobile``: a dropdown action on the ``number`` field will be added to call the field value.
     Currently, only the last ``mobile`` field will be displayed.
   * ``name``: a decoration will be added to the field value (typically a color dot) showing the
     presence status of the contact (e.g. Disconnected, Available, Away, ...)
   * ``number``: the field value will be:

      * added a decoration (typically a color dot) showing the status of the phone of the contact
        (e.g. Offline, Ringing, Talking, ...)
      * replaced with a button to call the contact with your phone when using the mouse
