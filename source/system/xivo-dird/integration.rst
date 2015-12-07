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
   * ``number``: the field value will be:

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

The web interface does not allow the administrator to specify the `unique_column` and `unique_column_format`. To add these configuration options, add a file to `/etc/xivo-dird/sources.d` containing the name of the source and all missing fields.

Example:

Given an :ref:`dird-backend-ldap` directory source using active directory, add a file with the following content to enable favorites on this source.

.. code-block:: yaml

    name: activedirectory
    unique_column: objectGUID
    unique_column_format: binary_uuid


Adding the `favorite` column to your display
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the web interface under :menuselection:`Services --> CTI Server --> Directories --> Display filters`.

#. Edit the filter on which you which to enable favorites.
#. Add a column with the type `favorite` and display format `favorite`.


Customizing sources
-------------------

Some configuration options are not available in the web interface. To add configuration to a source that is configured in the web interface, create a file in `/etc/xivo-dird/sources.d/` with the key `name` matching your web interface configuration and add all missing fields.

Example:

adding a timeout configuration to a CSV web service source

.. code-block:: yaml

    name: my_csv_web_service
    timeout: 16


.. _dird-context-separation:

Context separation
------------------

Without context separation, you only need one contact source for all the users of your XiVO.

However, if you need context separation, each context is considered as a separate independant source
of contacts, each with a different context filter. For this, you need:

* one contact source per context (a file in :file:`/etc/xivo-dird/sources.d`), so that we have a
  source containing only the contacts from one context
* one profile per context (equivalent to :menuselection:`Services --> CTI Server --> Directories -->
  Direct directories`) so that users in one context only see people from the same context.

Each source should look like this one, e.g. the context is named ``INSIDE``:

.. code-block:: yaml

    confd_config:
      host: localhost
      https: false
      port: 9487
      timeout: 4
      verify_certificate: false
      version: '1.1'
    first_matched_columns: [exten]
    format_columns:
      directory: "R\xE9pertoire XiVO Interne"
      location: '{description}'
      mobile: '{mobile_phone_number}'
      name: '{firstname} {lastname}'
      number: '{exten}'
      sda: '{userfield}'
      voicemail: '{voicemail_number}'
    searched_columns: [firstname, lastname, userfield, description]
    type: xivo
    unique_column: id
    name: internal_INSIDE  # <--- each source has a different name, one per context
    extra_search_params:
      context: INSIDE      # <--- each source filters users according to one context


The parameters in this file have the same effect than :menuselection:`Configuration --> Directories`
and :menuselection:`Services --> CTI Server --> Directories --> Direct directories` put together.

You may generate these config files from ``xivo-confgen dird/sources.yml``. Be sure to have ``name``
and ``extra_search_params`` correct for each source file.

Now that we have our contact sources, we need our search profiles.

Create a new file to override the profiles generated by *xivo-confgen*. You only need one file,
which will define all your profiles at once.

.. code-block:: sh

    xivo-confgen dird/services.yml >> /etc/xivo-dird/conf.d/001-context-separation.yml


In this file, there is a list of services (favorites, lookup, ...) where each profile has a set of
sources. You need to match one profile to the right internal source for each service. For example,
to have context separation between contexts INSIDE and INDOORS:

.. code-block:: yaml

    services:
      favorites:
        __default_phone:
          sources: [xivodir, internal, ldaptest, personal]
        __switchboard_directory:
          sources: [xivodir, ldaptest, personal]
        INSIDE:
          sources: [xivodir, internal_INSIDE, ldaptest, personal]   # <--- profile INSIDE uses the source internal_INSIDE
        INDOORS:
          sources: [xivodir, internal_INDOORS, ldaptest, personal]  # <--- profile INDOORS uses the source internal_INDOORS
      lookup:
        __default_phone:
          sources: [xivodir, internal, ldaptest, personal]
        __switchboard_directory:
          sources: [xivodir, ldaptest, personal]
        INSIDE:
          sources: [xivodir, internal_INSIDE, ldaptest, personal]   # <--- same HERE
        INDOORS:
          sources: [xivodir, internal_INDOORS, ldaptest, personal]  # <--- and HERE
