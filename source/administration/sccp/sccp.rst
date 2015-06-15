******************
SCCP Configuration
******************

Activating DHCP Server:
 :menuselection:`Configuration --> Network --> DHCP`

Activating DHCP Integration:
 :menuselection:`Configuration --> Provisioning --> General`

Installing a plugin for SCCP Phone:
 :menuselection:`Configuration --> Provisioning --> Plugins`

.. figure:: images/list_plugin.png

   Installing xivo cisco-sccp plugin

Review SCCP general settings:
 :menuselection:`Services  --> IPBX --> IPBX settings --> SCCP general settings`

.. figure:: images/general_settings.png

   SCCP general settings

At this point you should have a fully functional DHCP server that provides IP address to your
phones.  Depending on what type of CISCO phone you have, you need to install the plugin sccp-legacy,
sccp-9.0.3 or both.

.. note:: Please refer to the :ref:`Provisioning page <cisco-provisioning>` for more information on
          how to install CISCO firmwares.

Once your plugin is installed, you'll be able to edit which firmwares and locales you need.
If you are unsure, you can choose all without any problem.

.. figure:: images/plugin_installed.png

   Editing the xivo-cisco-sccp-legacy plugin

Now if you connect your first SCCP phone, you should be able to see it in the device list.

Listing the detected devices:
 :menuselection:`Services --> IPBX --> IPBX settings --> Devices`

.. figure:: images/list_device_1.png

   Device list

When connecting a second SCCP phone, the device will be automatically detected as well.

.. figure:: images/list_device_2.png

   Device list

The last step is to create a user with a SCCP line.

Creating a user with a SCCP line:
 :menuselection:`Services --> IPBX --> IPBX settings --> Users`

.. figure:: images/add_user.png

   Add a new user

.. figure:: images/edit_user.png

   Edit user informations

Before saving the newly configured user, you need to select the `Lines` menu and add a SCCP line.
Now, you can save your new user.

.. figure:: images/user_add_line.png

   Add a line to a user

Congratulations ! Your SCCP phone is now ready to be called !


Direct Media
------------

SCCP Phones support directmedia (direct RTP). In order for SCCP phones to use directmedia, one must enable the directmedia option in SCCP general settings:
 :menuselection:`Services  --> IPBX --> IPBX settings --> SCCP general settings`


.. _sccp-features:

Features
--------

+------------------------------+-----------+
| Features                     | Supported |
+==============================+===========+
| Receive call                 | Yes       |
+------------------------------+-----------+
| Initiate call                | Yes       |
+------------------------------+-----------+
| Hangup call                  | Yes       |
+------------------------------+-----------+
| Transfer call                | Yes       |
+------------------------------+-----------+
| Congestion Signal            | Yes       |
+------------------------------+-----------+
| Autoanswer (custom dialplan) | Yes       |
+------------------------------+-----------+
| Call forward                 | Yes       |
+------------------------------+-----------+
| Multi-instance per line      | Yes       |
+------------------------------+-----------+
| Message waiting indication   | Yes       |
+------------------------------+-----------+
| Music on hold                | Yes       |
+------------------------------+-----------+
| Context per line             | Yes       |
+------------------------------+-----------+
| Paging                       | Yes       |
+------------------------------+-----------+
| Direct RTP                   | Yes       |
+------------------------------+-----------+
| Redial                       | Yes       |
+------------------------------+-----------+
| Speed dial                   | Yes       |
+------------------------------+-----------+
| BLF (Supervision)            | Yes       |
+------------------------------+-----------+
| Resync device configuration  | Yes       |
+------------------------------+-----------+
| Do not disturb (DND)         | Yes       |
+------------------------------+-----------+
| Group listen                 | Yes       |
+------------------------------+-----------+
| Caller ID                    | Yes       |
+------------------------------+-----------+
| Connected line ID            | Yes       |
+------------------------------+-----------+
| Group pickup                 | Yes       |
+------------------------------+-----------+
| Auto-provisioning            | Not yet   |
+------------------------------+-----------+
| Multi line                   | Not yet   |
+------------------------------+-----------+
| Codec selection              | Yes       |
+------------------------------+-----------+
| NAT traversal                | Not yet   |
+------------------------------+-----------+
| Type of Service (TOS)        | Manual    |
+------------------------------+-----------+


Telephone
---------

+-------------+-------------+------------------+----------------+
| Device type | Supported   | Firmware version | Timezone aware |
+=============+=============+==================+================+
| 7905        | Should work |                  |                |
+-------------+-------------+------------------+----------------+
| 7906        | Yes         | SCCP11.9-0-3S    | Yes            |
+-------------+-------------+------------------+----------------+
| 7911        | Yes         | SCCP11.9-0-3S    | Yes            |
+-------------+-------------+------------------+----------------+
| 7912        | Yes         | 8.0.4(080108A)   | No             |
+-------------+-------------+------------------+----------------+
| 7920        | Yes         | 3.0.2            | No             |
+-------------+-------------+------------------+----------------+
| 7921        | Yes         | 1.4.5.3          | Yes            |
+-------------+-------------+------------------+----------------+
| 7940        | Yes         | 8.1(2.0)         | No             |
+-------------+-------------+------------------+----------------+
| 7941        | Yes         | SCCP41.9-0-3S    | Yes            |
+-------------+-------------+------------------+----------------+
| 7941GE      | Yes         | SCCP41.9-0-3S    | Yes            |
+-------------+-------------+------------------+----------------+
| 7942        | Yes         | SCCP42.9-0-3S    | Yes            |
+-------------+-------------+------------------+----------------+
| 7960        | Yes         | 8.1(2.0)         | No             |
+-------------+-------------+------------------+----------------+
| 7961        | Yes         | SCCP41.9-0-3S    | Yes            |
+-------------+-------------+------------------+----------------+
| 7962        | Yes         | SCCP42.9-0-3S    | Yes            |
+-------------+-------------+------------------+----------------+
| CIPC        | Yes         | 2.1.2            | Yes            |
+-------------+-------------+------------------+----------------+

An unsupported device won't be able to connect to asterisk at all.

The "Timezone aware" column indicates if the device supports the timezone tag in its configuration
file, i.e. in the file that the device request to the provisioning server when it boots.  If you
have devices that don't support the timezone tag and these devices are in a different timezone than
the one of the XiVO, you can look at `the issue #5161 <https://projects.xivo.io/issues/5161>`_ for
a potential solution.
