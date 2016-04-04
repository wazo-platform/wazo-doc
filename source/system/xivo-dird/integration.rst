.. _xivo-dird-integration:

**********************************************
Integration of XiVO dird with the rest of XiVO
**********************************************

Configuration values
====================

.. _dird-integration-views:

Views
-----

In the directory displays (also in the :ref:`main configuration file <dird-configuration-file>` of xivo-dird, in the ``views`` section), the
following keys are interpreted and displayed in xlet people of the XiVO Client:

``title``
   The ``title`` will be shown as a header for the column

``type``
   * ``agent``: the field value will be ignored and replaced by an icon showing the status of the
     agent assigned to the contact (e.g. green icon for logged agent, red icon for unlogged agent,
     ...)
   * ``callable``: a dropdown action on the ``number`` field will be added to call the field value.
   * ``email``: a dropdown action on the ``number`` field will be added to send an email to the
     field value.
   * ``favorite``: the boolean field value will be replaced by an icon showing if the status is
     favorite (yellow star filled) or not (yellow star empty).
   * ``name``: a decoration will be added to the field value (typically a color dot) showing the
     presence status of the contact (e.g. Disconnected, Available, Away, ...)
   * ``number``: only one number type can be defined per profile. The field value will be:

      * added a decoration (typically a color dot) showing the status of the phone of the contact
        (e.g. Offline, Ringing, Talking, ...)
      * replaced with a button to call the contact with your phone when using the mouse

   * ``personal``: the boolean field value will be used to show a deletion action for the contact
   * ``voicemail``: the voicemail number of the contact

See :ref:`15_19_people_xlet_upgrade_notes` for an example with screenshots.


.. _personal-contact-attributes:

Personal contacts
-----------------

Here are the list of available attributes of a personal contact:

* ``id``
* ``company``
* ``email``
* ``fax``
* ``firstname``
* ``lastname``
* ``mobile``
* ``number``


To be able to edit and delete personal contacts, you need a column of type `personal` in your display.

Adding the `personal` column to your display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the web interface under :menuselection:`Services --> CTI Server --> Directories --> Display filters`.

#. Edit the filter on which you which to enable favorites.
#. Add a column with the type `personal` and display format `personal`.



Favorites
---------

Enabling favorites in the XiVO client.

* Add a `unique_column` to your sources.
* Add a `favorite` column to your display


Adding a `unique_column` to your sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The web interface does not allow the administrator to specify the `unique_column` and
`unique_column_format`. To add these configuration options, add a file to `/etc/xivo-dird/sources.d`
containing *the same name* than the directory definition and all missing fields.

Example:

Given an :ref:`dird-backend-ldap` directory source using Active Directory named ``myactivedirectory``:

.. image:: images/active-directory-unique.png

Add a file :file:`/etc/xivo-dird/sources.d/myactivedirectory.yml` with the following content to
enable favorites on this source.

.. code-block:: yaml

    name: myactivedirectory  # the same name than the directory definition
    unique_column: objectGUID
    unique_column_format: binary_uuid


Adding the `favorite` column to your display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the web interface under :menuselection:`Services --> CTI Server --> Directories --> Display filters`.

#. Edit the filter on which you which to enable favorites.
#. Add a column with the type `favorite` and display format `favorite`.


Customizing sources
-------------------

Some configuration options are not available in the web interface. To add configuration to a source
that is configured in the web interface, create a file in `/etc/xivo-dird/sources.d/` with the key
`name` matching your web interface configuration and add all missing fields.

Example:

adding a timeout configuration to a CSV web service source

.. code-block:: yaml

    name: my_csv_web_service
    timeout: 16
