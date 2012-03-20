******************
SCCP Configuration
******************

Add a SCCP line
===============

Setting up provisioning
-----------------------

Activating DHCP Server:
 :menuselection:`Configuration --> Network --> DHCP`

Activating DHCP Integration:
 :menuselection:`Configuration --> Provisioning --> General`

Installing a plugin for SCCP Phone:
 :menuselection:`Configuration --> Provisioning --> Plugins`

.. figure:: images/list_plugin.png

  Installing xivo cisco-sccp plugin

::

 At this point you should have a fully functional DHCP server that provides IP address to your phones.
 Depending on what type of CISCO phone you have, you need to install the plugin sccp-legacy, sccp-9.2.1 or both.

::

 Once your plugin is installed, you'll be able to edit which firmwares and locales you need.
 If you are unsure, you can choose all without any problem.
 
.. figure:: images/plugin_installed.png

   Editing the xivo-cisco-sccp-legacy plugin

::

 Now if you connect your first SCCP phone, you should be able to see it in the device list.

Listing the detected devices:
 :menuselection:`Services --> IPBX --> IPBX settings --> Devices`

.. figure:: images/list_device_1.png

   Device list

::

 When connecting a second SCCP phone, the device will be automatically detected as well.

.. figure:: images/list_device_2.png

   Device list
 
::

 The last step is to create a user with a SCCP line.

Creating a user with a SCCP line:
 :menuselection:`Services --> IPBX --> IPBX settings --> Users`

.. figure:: images/add_user.png

   Add a new user

.. figure:: images/edit_user.png

   Edit user informations

::

 Before saving the newly configured user, you need to select the `Lines` menu and add a SCCP line.
 Now, you can save your new user.
 
.. figure:: images/user_add_line.png

   Add a line to a user

::

 Congratulation ! Your SCCP phone is now ready to be called !

.. warning::

 You must manually do "module reload chan_sccp.so" via the Asterisk command line if you want to:

 1- Remove a device from the configuration.

 2- Add a voicemail on an already configured user.

 Please, be warned that this command will disconnect all SCCP phones and hence all current phone calls will be lost.

 This limitation should be removed in the future.
