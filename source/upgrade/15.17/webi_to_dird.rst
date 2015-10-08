.. _upgrade-notes-webi-to-dird:

************************************
Phone Remote Directory Upgrade Notes
************************************

If you are not using the remote directory from your phones, you can safely skip this page.

Starting from XiVO 15.17, the remote directory used by the phones is now provided by the new
directory service, composed principally of :ref:`xivo-dird <xivo-dird>` and :ref:`xivo-dird-phoned
<xivo-dird-phoned>`. It was previously provided by the XiVO web interface.

This brings a few changes for the administrators, the biggest one being that lookup from both the
XiVO client and phones are now configured at the same place, namely the (incorrectly named)
:menuselection:`Services --> CTI Server --> Directories` section, with some advanced configuration
only available in the configuration files. This means that lookup from the phones can now also
display results from CSV or web services directories. For details on how to configure directories,
refer to the :ref:`directories` page.

For users, the biggest change is that they can now consult their personal contacts (that they added
from their XiVO client) when doing a search from their phone.


Changes
=======

Web Interface - LDAP Filters
----------------------------

The following options have been removed from the web interface, in the :menuselection:`Services -->
IPBX --> LDAP filters` page:

* the ``Phone number type`` field
* the ``Attributes`` tab

The phone number type is now configurable on a per source basis (and for all type of source, not
just LDAP), in :menuselection:`Services --> CTI Server --> Directories`. For example, if you have
LDAP records with the attribute ``telephoneNumber`` that you want to be displayed on your phone with
the suffix "(Office)", just make sure that your directory definition is configured with a field
named ``phone_office`` with the value ``{telephoneNumber}``.

By default, the following fields are available:

* ``phone``: doesn't add a suffix
* ``phone_office``: add a "(Office)" suffix
* ``phone_mobile``: add a "(Mobile)" suffix
* ``phone_home``: add a "(Home)" suffix
* ``phone_other``: add a "(Other)" suffix

.. note:: These fields will automatically be added in your LDAP directory definitions during the upgrade,
   so you may only need to `review your directory configuration`_.

This list of fields and the suffix associated to it is currently only configurable in the
:ref:`xivo-dird configuration files <dird-configuration-file>`, in the :ref:`views/displays_phone
<dird-config-displays_phone>` section.

This is causing 2 functional changes:

* Previously, the suffix displayed was translated in function of the phone's language. This is not
  possible anymore, and you'll have to edit the configuration files if you want the suffix to be in
  a different language than english.
* For "custom" phone number type, you'll have to add a new entry in the configuration files and
  add the correspond field in the directory definition.

In XiVO 15.16, the ``Attributes`` tab would allow a "fallback" mechanism, where if an LDAP attribute
for a record was missing/empty, another attribute would be used. In XiVO 15.17, this mechanism is
available (for all type of sources) by mapping the first attribute to a field name ``phone``, the
second to a field name ``phone1``, etc. The fallback mechanism is available on the fields ``phone``,
``phone_office``, ``phone_mobile``, ``phone_home``, ``phone_other`` and ``display_name``.


Web Interface - Phonebook
-------------------------

The following options have  been removed from the web interface, in the :menuselection:`Services -->
IPBX --> Phonebook` page:

* the ``LDAP filters`` tab

LDAP sources used for lookup from the phone are now selected in the same place as for the XiVO
client, i.e. in :menuselection:`Services --> CTI Services --> Direct directories`.  A consequence of
that is that it's not possible anymore to have sources only used for lookup from phone and other
sources only used for lookup from the XiVO client.

.. note:: The LDAP filters that were used for phone lookup will be automatically added to all the
   profiles during the upgrade.


Additional Upgrade Steps
========================

After upgrading your XiVO to 15.17 or later, you should do the following steps.


Upgrade Your Provisioning Plugins
---------------------------------

This step is optional, although strongly recommended.

For the users to be able to search their personal contacts from their phone, the phone
configuration needs to be updated. This means:

#. Installing new xivo-provd plugins or upgrading existing plugins
#. Restarting all affected phones

See the :ref:`provisioning <provisioning>` section for more information on installing or upgrading
plugins.

Here's the list of plugins which have received modifications to be compatible with the new directory
service:

+--------------------------------+---------+
| Name                           | Version |
+================================+=========+
| xivo-aastra-3.3.1-SP4          | 1.5     |
+--------------------------------+---------+
| xivo-aastra-4.1.0              | 1.5     |
+--------------------------------+---------+
| xivo-cisco-sccp-9.0.3          | 0.8     |
+--------------------------------+---------+
| xivo-cisco-sccp-cipc-2.1.2     | 0.8     |
+--------------------------------+---------+
| xivo-cisco-sccp-legacy         | 0.8     |
+--------------------------------+---------+
| xivo-cisco-sccp-wireless-1.4.5 | 0.8     |
+--------------------------------+---------+
| xivo-cisco-spa-7.5.5           | 0.12    |
+--------------------------------+---------+
| xivo-cisco-spa-legacy          | 0.12    |
+--------------------------------+---------+
| xivo-polycom-4.0.4             | 1.4     |
+--------------------------------+---------+
| xivo-polycom-5.3.0             | 1.5     |
+--------------------------------+---------+
| xivo-snom-8.7.5.17             | 1.5     |
+--------------------------------+---------+
| xivo-technicolor-ST2022-4.78-1 | 0.4     |
+--------------------------------+---------+
| xivo-technicolor-ST2030-2.74   | 0.3     |
+--------------------------------+---------+
| xivo-technicolor-TB30-1.74.0   | 0.3     |
+--------------------------------+---------+
| xivo-yealink-v70               | 1.24    |
+--------------------------------+---------+
| xivo-yealink-v72               | 1.24    |
+--------------------------------+---------+
| xivo-yealink-v73               | 1.24    |
+--------------------------------+---------+
| xivo-yealink-v80               | 1.24    |
+--------------------------------+---------+

Plugins with greater version number or greater firmware-version number are also compatible.

If the xivo-provd plugins are not updated or the phone are not rebooted, the user will by default
only be able to search in the "internal" and "xivodir" directory definitions. If you want to add or
remove sources for these phones, you'll need to edit xivo-dird configuration files.  More precisely,
you'll need to edit the sources associated to the profile named ``default_phone``.


Update Your Firewall Rules
--------------------------

If there's a firewall (or a NAT equipement) between your XiVO and your phones, you must know that
the port used for the directory lookup from the phone has changed from port TCP/80 to port TCP/9498.
The new port is going to be used only by phones which are using a compatible plugins (see list
above) and have been rebooted; otherwise, the port TCP/80 will still be used.


Review Your Directory Configuration
-----------------------------------

During the upgrade, new LDAP directory definitions might be created and fields to existing one might be
added.

For example, if you had an LDAP filter which was used for directory lookup from your phones, then a
corresponding LDAP directory definition will be created if nonexistent, and otherwise be updated to
make sure the ``display_name`` and ``phone_office`` (or another field, depending on the phone number
type of your LDAP filter) fields are defined. The directory definition will also be added to all the
direct directories entries, i.e. added to all items in the :menuselection:`Services --> CTI Server
--> Direct directories` page.

If you were using LDAP filters with custom phone number types, the custom part will be lost, and to
get back the same behaviour, you'll need to modify xivo-dird configuration files and update the
field's name in your directory definition.

Also, if you have other directory defintions that you now want to use from your phones (e.g. CSV
directories), make sure that their configuration is working, i.e. that they have a ``display_name``
and ``phone`` fields.  During the upgrade, these fields are automatically added to the directory
defintion "xivodir", "internal" and for LDAP source, like described above.
