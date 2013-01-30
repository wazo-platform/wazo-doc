*********
Directory
*********

Overview
========

The directory xlet allows the users to search for entries in the xivo directories and the list of xivo users.


Usage
=====

The list of entries in the xlet is searched using the top field. Entries are filtered by
name and number. The entry list will initally appear as empty.


Phonebook
=========

Phonebook searches are triggered after the user has entered 3 characters. Results from remote
directories will appear after 1 second.


Configuration
-------------


Context
^^^^^^^

The directory xlet uses a special context named  *__switchboard_directory*. This context has to
be added as an `internal` context with no number range on the
:menuselection:`Services --> IPBX --> IPBX configuration --> Contexts` page.

.. figure:: ./images/switchboard_directory_context.png


Display filter
^^^^^^^^^^^^^^

A new display filter must be created for the directory xlet.

.. figure:: ./images/directory_display_filter.png

The following fields must be configurered for entries to be displayed in the xlet:

#. *name* is displayed in the *Name* column of the xlet
#. *number_office* is displayed in the *Number* column with a phone icon in the xlet
#. *number_mobile* is displayed in the *Number* column with a mobile icon in the xlet
#. *number_...* any other field starting with *number_* will be displayed in the *Number* column of the xlet with a generic directory icon

The values in the *Display format* column contain values that are created in the *Directory Definition*


Context and filter association
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The new *Display filter* has to be assigned to the *__switchboard_directory* context

.. figure:: ./images/context_directory_association.png

You can then choose which directories will be searched by the Xlet.

.. note:: You must **not select internal** directory, as it is already handled.


LDAP Configuration
------------------

To search in ldap directories, you must have an LDAP server configured. See :ref:`ldap` for more details.

LDAP filter
^^^^^^^^^^^

If you already have an LDAP filter configured for the *Remote directory* Xlet, you can use it.

If not, you must add an LDAP filter in :menuselection:`IPBX --> IPBX configuration --> LDAP filters`.

.. figure:: ./images/ldap_filter_configuration.png
.. figure:: ./images/ldap_filter_attributes.png

The *Display name* attributes and phone number must be configured as shown above.

Directory definition
^^^^^^^^^^^^^^^^^^^^

A new directory definition must be added:

.. figure:: ./images/ldap_directory_definition.png

These fields are mandatory:

* firstname
* lastname
* phone

The direct match field must be a comma-separated list of the field values.

Include the new directory for lookup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You must add the new LDAP filter in the directory list. See `Context and filter association`_ for more details.
