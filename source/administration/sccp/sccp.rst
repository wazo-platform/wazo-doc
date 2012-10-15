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

.. warning::

   You must `reload the chan_sccp module`_ for the settings to be applied.

At this point you should have a fully functional DHCP server that provides IP address to your phones.
Depending on what type of CISCO phone you have, you need to install the plugin sccp-legacy, sccp-9.2.1 or both. Please refer to the :ref:`Provisionning page <cisco-provisioning>` for more information on how to install CISCO firmwares.

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

.. warning::

   Direct media is currently only supported between SCCP phones on a same XiVO.

   If your are using your SCCP phones to make/receive calls through a SIP trunk
   for example, then you must disable the direct media option.


.. _reload the chan_sccp module:

Reloading the chan_sccp module
------------------------------

You must manually do a ``module reload chan_sccp.so`` via the Asterisk CLI if you want to:

* Apply the SCCP general settings configuration
* Remove a device from the configuration
* Add a voicemail on an already configured user
* Change the language of an already configured user

Be warned that this command will disconnect all SCCP phones and hence all current phone calls will be lost.


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
| Group pickup                 | Not yet   |
+------------------------------+-----------+
| Hotline (auto-provisioning)  | Not yet   |
+------------------------------+-----------+
| Speed dial                   | Not yet   |
+------------------------------+-----------+
| Multi line                   | Not yet   |
+------------------------------+-----------+
| Codec selection              | Not yet   |
+------------------------------+-----------+
| Do not disturb (DND)         | Not yet   |
+------------------------------+-----------+
| NAT traversal                | Not yet   |
+------------------------------+-----------+


Telephone
---------

+-------------+-------------+------------------+
| Device type | Supported   | Firmware version |
+=============+=============+==================+
| 7905        | Should work |                  |
+-------------+-------------+------------------+
| 7906        | Should work |                  |
+-------------+-------------+------------------+
| 7911        | Yes         | SCCP11.8-5-3S    |
+-------------+-------------+------------------+
| 7912        | Yes         | 8.0.4(080108A)   |
+-------------+-------------+------------------+
| 7940        | Yes         | 8.1(2.0)         |
+-------------+-------------+------------------+
| 7941        | Yes         | SCCP41.9-0-3S    |
+-------------+-------------+------------------+
| 7942        | Yes         | SCCP42.9-0-3S    |
+-------------+-------------+------------------+
| 7941GE      | Yes         | SCCP41.9-0-3S    |
+-------------+-------------+------------------+
| 7960        | Yes         | 8.1(2.0)         |
+-------------+-------------+------------------+
| 7961        | Yes         | SCCP41.9-0-3S    |
+-------------+-------------+------------------+
| 7962        | Yes         | SCCP42.9-0-3S    |
+-------------+-------------+------------------+

An unsupported device won't be able to connect to Asterisk (channel sccp) at all.
