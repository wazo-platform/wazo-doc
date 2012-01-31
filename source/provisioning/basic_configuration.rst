*******************
Basic configuration
*******************

Configuring the DHCP server
---------------------------

XiVO includes a DHCP server that facilitate the auto-provisioning of telephony devices.
It is *not* activated by default.

There's a few things to know about the peculiarities of the included DHCP server:

* it only answer to DHCP requests from :ref:`supported devices <devices>`.
* it only listen on the VoIP network interface

This means that if your phones are on the same broadcast domain than your computers,
and you would like the DHCP server on your XiVO to handle both your phones and your
computers, that won't do it.

The DHCP server is configured via the :menuselection:`Configuration --> Network --> DHCP` page:

Active
   Activate/desactivate the DHCP server.

Pool start
   The lower IP address which will be assigned dynamically. Example: ``10.0.0.10``.

Pool end
   The higher IP address which will be assigned dynamically. Example: ``10.0.0.99``.

Extra network interfaces
   A list of space-separated network interface name. Example: ``eth0``.

   Useful if you have done some custom configuration in the :file:`/etc/dhcp/dhcpd_extra.conf`
   file. You need to explicitly specify the additional interfaces the DHCP server should
   listen on.

Installing a ``provd`` plugin
-----------------------------

