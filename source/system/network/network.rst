*******
Network
*******

.. index:: network

You **must** configure your network interfaces directly from the XiVO web interface via the
:menuselection:`Configuration --> Network --> Interfaces` page.

The Voip interface is used by the DHCP server and the provisioning server.


How-to
------

You can only have one VoIP interface, which is eth0 by default. This interface is configured during the wizard.

The DHCP server and provisioning server, among other, use information from the VoIP interface in its configuration.
For example, the DHCP server will only listen on the VoIP interface per default.

To change this interface, you must either create a new one or edit an existing one and change its type to VoIP.
The type of the old interface will automatically be changed to the 'data' type.


Configuring a physical interface
--------------------------------
In this example, we'll add and configure the *eth1* network interface on our XiVO.

First, we see there's already an unconfigured network interface named ''eth1'' on our system:

.. figure:: images/netiface_list_post_wizard.png

Listing the network interfaces

To add and configure it, we click on the small plus button next to it, and we get to this page:

.. figure:: images/netiface_edit_physical_empty.png

Configure physical interface

In our case, since we want to configure this interface with static information (i.e. not via DHCP), 
we fill the following fields:

.. figure:: images/netiface_edit_physical_filled.png
 
Configure physical interface

Note that since our ''eth0'' network interface already has a default gateway,
we do not enter information in the ''Default gateway'' field for our ''eth1'' interface.

Once we click on ''Save'', the XiVO will put the ''Apply network configuration'' button in bold.

To reconfigure the given network interface with the new information, you click on it.

.. figure:: images/netiface_notify_change.png
   :figclass: align-center

   Apply after modify interface


.. index:: single:VLAN

Adding a VLAN interface
-----------------------

First, we see there's already a configured network interface on our system:

.. figure:: images/netiface_list_configured.png

Listing the network interfaces

To add and configure a new VLAN interface, we click on the small plus button in the top right corner,

.. figure:: images/utils_add_button.png
   :figclass: align-center
   
   Adding button

and we get to this page:

.. figure:: images/netiface_add_virtual_empty.png
   :figclass: align-center
   
   Adding a new virtual interface

In our case, since we want to configure this interface with static information:

.. figure:: images/netiface_add_virtual_filled.png
   :figclass: align-center

   Adding a new virtual interface

Click on **Save** list the network interfaces:

.. figure:: images/netiface_list_new_virtual.png
   :figclass: align-center
      
   Listing the network interfaces

- The new virtual interface has been successfully created.

.. note:: 
   Do not forget after you finish the configuration of the network to apply it with the button: 
   **Apply network configuration**

After applying the network configuration:

.. figure:: images/netiface_list_virtual_after_apply.png
   :figclass: align-center

   Listing the network interfaces


Add static network routes
-------------------------

Static route can't be currently added via the web interface.
If you want static routes in your XiVO you should do the following the steps described below.
It would ensure that your static routes are applied at startup (in fact each time a network interface goes up).

#. Create the file ``/etc/network/if-up.d/xivo-routes``::

    touch /etc/network/if-up.d/xivo-routes
    chmod 755 /etc/network/if-up.d/xivo-routes

#. Insert the following content::

    #!/bin/sh

    ip route add <destination> via <gateway> 
    ip route add <destination> via <gateway>

.. note:: 
   <destination> and <gateway> should be replaced by your specific configuration.
   For example `192.168.50.128/25 via 192.168.17.254`
   or `91.195.18.20 via 192.168.17.254`

