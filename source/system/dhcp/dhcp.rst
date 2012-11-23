*******************
DHCP Server
*******************

XiVO includes a DHCP server that must be used to address telephony devices (:ref:`Basic Configuration <dhcpd-config>`) of the VOIP subnet.
This section describes how to configure DHCP server for other subnets or with advanced options.


Activation of DHCP server
=========================

DHCP Server can be activated through the XiVO Web Interface :menuselection:`Configuration --> Network --> DHCP` :

.. figure:: img/dhcp.png
   :scale: 85%

   :menuselection:`Configuration --> Network --> DHCP`

By default, it will only answer to DHCP requests coming from the VoIP subnet (defined in the :menuselection:`Configuration --> Network --> Interfaces` section). If you need to activate DHCP server on an other interface, you have to fill the *Extra network interfaces* field::
  Example: ``eth0``

After saving your modifications, you need to click on *Apply system configuration* for them to be applied.

DHCP-Relay 
==========

If your telephony devices aren't located on the same site and the same broadcast domain as the XiVO DHCP server, you'll have to add the option *DHCP Relay* to the site's router.
This parameter will permit the DHCP request from distant devices to be transmitted to the IP address you specify as DHCP Relay.

.. warning::
  Please make sure that the IP address used as DHCP Relay is one of the XiVO interface, and that this interface is configured to listen to DHCP request (as decribe in previous part). Also verify that routing is good between the distant router and the choosen interface, otherwise DHCP request will never arrive to the server.


Configuring DHCP server for other subnets
=========================================

This section describes how to configure XiVO to make DHCP server for other subnets that the VOIP subnet. As you can't use the Web Interface to declare other subnet (for example to address DATA subnet, or a VOIP subnet  that isn't on the same site that XiVO server), you'll have to do the following configuration in Command Line Interface.

Creating "extra subnet" configuration files
-------------------------------------------

First thing to do is to create a directory and to copy into it the configuration files ::

   mkdir /etc/dhcp/dhcpd_sites/
   cp /etc/dhcp/dhcpd_subnet.conf /etc/dhcp/dhcpd_sites/dhpcd_siteXXX.conf 
   cp /etc/dhcp/dhcpd_subnet.conf /etc/dhcp/dhcpd_sites/dhpcd_lanDATA.conf  

.. note::
  In this case we'll create 2 files for 2 differents subnets. You can change the name of the files, and create as many files as you want in the folder /etc/dhcp/dhcpd_sites/ . Just adapt this procedure by changing the name of the file in the diferent links

After creating one or several files in /etc/dhcp/dhcpd_sites/, you have to edit the file dhcpd_extra.conf and add one or several lines::

  include "/etc/dhcp/dhcpd_sites/dhpcd_siteXXX.conf";
  include "/etc/dhcp/dhcpd_sites/dhpcd_lanDATA.conf";
  ....

Adjusting Options of the DHCP server
------------------------------------

Once you have created the subnet in the DHCP server, you must edit each configuration file (/etc/dhcp/dhcpd_sites/dhcpd_siteXXX.conf) and modify the different parameters.
In section **\subnet**, write the IP subnet and change the following options (underlined fields in the example) :

``subnet 172.30.8.0 netmask *\255.255.255.0* {``

* subnet-mask:

``option subnet-mask 255.255.255.0;``

* broadcast-address :

``option broadcast-address 172.30.8.255;``

* routers (specify IP address of the router(s) that will be the default gateway of the site):

``option routers 172.30.8.1;``

In section **\Pool**, modify the options :

* log (add the name of the site or of the subnet) :

``log(concat("[", binary-to-ascii(16, 8, ":", hardware), "] POOL VoIP Site XXX"));``

* range (it will define the range of IP address the DHCP server can use to address the devices of that subnet) :

``range 172.30.8.10 172.30.8.200;``


.. warning::
  XiVO only answers to DHCP requests from :ref:`supported devices <devices>`. In case of you need to address other equipment, use the option *allow unknown-clients;* in the /etc/dhcp/dhcpd_sites/XXX.conf file


At this point, you can apply the changes of the DHCP server with the command ::
  /etc/init.d/isc-dhcp-server restart
  
After that, XiVO will start to address the devices located on other site or other subnet that the VOIP subnet. You will see in /var/log/daemong.log all the DHCP requests receided and how they are managed by XiVO.

