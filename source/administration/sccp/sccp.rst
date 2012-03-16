******************
SCCP Configuration
******************

Add a SCCP line
===============

Setting up provisioning
-----------------------

.. warning::

   You **must** activate DHCP integration in
   :menuselection:`Configuration --> Provisioning --> General`

Once you must install a plugin for SCCP Phone via the
:menuselection:`Configuration --> Provisioning --> Plugins`

.. figure:: images/list_plugin.png

   SCCP Plugins list

Install ``xivo-cisco-sccp-legacy`` plugin

.. figure:: images/plugin_installed.png

   SCCP Plugin cisco legacy installed

Now you can connect your SCCP phone to XiVO.
This device should appear in device list
( :menuselection:`Services --> IPBX --> IPBX settings --> Devices` )


.. figure:: images/list_device_1.png

   Device list 1

If i connect another SCCP phone

.. figure:: images/list_device_2.png

   Device list 2
   

Now create a user with a SCCP line and associate it to a SCCP device.
( :menuselection:`Services --> IPBX --> IPBX settings --> Users` )
