*******************
DHCP Server
*******************

XiVO includes a DHCP server that must be used to address telephony devices 
(:ref:`Basic Configuration <dhcpd-config>`) of the VOIP subnet.
This section describes how to configure DHCP server for other subnets or with advanced options.


Activation of DHCP server
=========================

DHCP Server can be activated through the XiVO Web Interface 
:menuselection:`Configuration --> Network --> DHCP` :

.. figure:: img/dhcp.png
   :scale: 85%

   :menuselection:`Configuration --> Network --> DHCP`

By default, it will only answer to DHCP requests coming from the VoIP subnet (defined in the 
:menuselection:`Configuration --> Network --> Interfaces` section). If you need to activate DHCP server
on an other interface, you have to fill the *Extra network interfaces* field with, for example : ``eth0``

After saving your modifications, you need to click on *Apply system configuration* for them to be applied.


Change default gateway for DHCP
===============================

By default, the XiVO DHCP server gives the XiVO IP address in the router option.
To change this you must create a custom-template:

#. Create a custom template for the :file:`dhcpd_subnet.conf.head` file::

     mkdir -p /etc/xivo/custom-templates/dhcp/etc/dhcp/
     cd /etc/xivo/custom-templates/dhcp/etc/dhcp/
     cp /usr/share/xivo-config/templates/dhcp/etc/dhcp/dhcpd_subnet.conf.head .

#. Edit the custom template::

     vim dhcpd_subnet.conf.head

#. In the file, replace the string ``#XIVO_NET4_IP#`` by the router of your VoIP network, for example::

     option routers 192.168.2.254;

#. Re-generate the dhcp configuration::

     xivo-update-config

DHCP server should have been restarted and should now give the new router option.


Configuring DHCP server to serve unknown hosts
==============================================

By default, the XiVO DHCP server serves only known hosts. That is:

* either hosts which MAC address prefix (the `OUI <http://en.wikipedia.org/wiki/Organizationally_unique_identifier>`_) is known 
* or hosts which Vendor Identifier is known

Known OUIs and Vendor Class Identifiers are declared in :file:`/etc/dhcpd/dhcpd_update/*` files.

If you want your XiVO DHCP server to serve also unknown hosts (like PCs) follow these instructions:

#. Create a custom template for the :file:`dhcpd_subnet.conf.tail` file::
     
     mkdir -p /etc/xivo/custom-templates/dhcp/etc/dhcp/
     cd /etc/xivo/custom-templates/dhcp/etc/dhcp/
     cp /usr/share/xivo-config/templates/dhcp/etc/dhcp/dhcpd_subnet.conf.tail .

#. Edit the custom template::

     vim dhcpd_subnet.conf.tail

#. And add the following line at the head of the file::
   
     allow unknown-clients;

#. Re-generate the dhcp configuration::

     xivo-update-config

DHCP server should have been restarted and should now serve all network equipments.


DHCP-Relay 
==========

If your telephony devices aren't located on the same site and the same broadcast domain as the XiVO 
DHCP server, you will have to add the option *DHCP Relay* to the site's router.
This parameter will permit the DHCP requests from distant devices to be transmitted to the IP address 
you specify as DHCP Relay.

.. warning::
  Please make sure that the IP address used as DHCP Relay is one of the XiVO interface, and that this 
  interface is configured to listen to DHCP requests (as decribed in previous part). 
  Also verify that routing is configured between the distant router and the choosen interface, otherwise 
  DHCP requests will never reach the XiVO server.


Configuring DHCP server for other subnets
=========================================

This section describes how to configure XiVO to serve other subnets that the VOIP subnet. 
As you can't use the Web Interface to declare other subnets (for example to address DATA subnet, or a 
VOIP subnet that isn't on the same site that XiVO server), you'll have to do the following 
configuration in Command Line Interface.


Creating "extra subnet" configuration files
-------------------------------------------

First thing to do is to create a directory and to copy into it the configuration files::

   mkdir /etc/dhcp/dhcpd_sites/
   cp /etc/dhcp/dhcpd_subnet.conf /etc/dhcp/dhcpd_sites/dhcpd_siteXXX.conf 
   cp /etc/dhcp/dhcpd_subnet.conf /etc/dhcp/dhcpd_sites/dhcpd_lanDATA.conf  

.. note::
  In this case we'll create 2 files for 2 differents subnets. 
  You can change the name of the files, and create as many files as you want in the 
  folder :file:`/etc/dhcp/dhcpd_sites/`. 
  Just adapt this procedure by changing the name of the file in the different links.

After creating one or several files in :file:`/etc/dhcp/dhcpd_sites/`, you have to edit the file 
:file:`/etc/dhcp/dhcpd_extra.conf` and add the according include statement like::

  include "/etc/dhcp/dhcpd_sites/dhcpd_siteXXX.conf";
  include "/etc/dhcp/dhcpd_sites/dhcpd_lanDATA.conf";


Adjusting Options of the DHCP server
------------------------------------

Once you have created the subnet in the DHCP server, you must edit each configuration file 
(the files in :file:`/etc/dhcp/dhcpd_sites/`) and modify the different parameters.
In section **subnet**, write the IP subnet and change the following options (underlined fields in the example)::

   subnet 172.30.8.0 netmask 255.255.255.0 {

* subnet-mask::
    
    option subnet-mask 255.255.255.0;

* broadcast-address::
    
    option broadcast-address 172.30.8.255;

* routers (specify the IP address of the router that will be the default gateway of the site)::
    
    option routers 172.30.8.1;

In section **pool**, modify the options::

   pool {

* log (add the name of the site or of the subnet)::
    
    log(concat("[", binary-to-ascii(16, 8, ":", hardware), "] POOL VoIP Site XXX"));

* range (it will define the range of IP address the DHCP server can use to address the devices of that subnet)::
    
    range 172.30.8.10 172.30.8.200;


.. warning::
  XiVO only answers to DHCP requests from :ref:`supported devices <devices>`. 
  In case of you need to address other equipment, use the option *allow unknown-clients;* 
  in the :file:`/etc/dhcp/dhcpd_sites/` files


At this point, you can apply the changes of the DHCP server with the command::

  /etc/init.d/isc-dhcp-server restart
  
After that, XiVO will start to serve the DHCP requests of the devices located on other site or other 
subnet than the VOIP subnet. You will see in :file:`/var/log/daemon.log` all the DHCP requests receided 
and how they are handled by XiVO.

