.. _postinstall:

.. index::
   single:post installation

***********************
Post Installation Steps
***********************

Configuring the CTI Server
==========================

The CTI server configuration options can be found in the web-interface under the services tab. Most default options should be sufficient for most use cases but it's still possible to make some changes.


General options
---------------

The general options allow the administrator to manage network connections between the CTI server and other services and clients.

The section named AMI connection allow the administrator to configure the information that is required to connect to the Asterisk Manager Interface (AMI). These fields should match the entries in `/etc/asterisk/manager.conf`.

.. image:: images/ami_connection.png

The section named Listening Ports allows the administrator to specify listening addresses and ports for the CTI server's interfaces.

* Fast AGI is the CTI server's entry point for the Asterisk dialplan. This address and port have nothing to do with the listening port and address of xivo-agid.
* CTI and CTIs are for the client's connection and secure connection respectively.
* Web Interface is for the port used to receive events from the XiVO web interface
* Info server a debugging console to do some introspection on the state of the CTI server
* Announce is used to notify the CTI server when a dialplan reload is requested

.. image:: images/listening_ports.png

The timeout section allow the administrator to configure multiple timeouts.

* Update period is a poll delay to retrieve new information from the web services.
* Socket timeout is the default timeout used for network connections.
* Login timeout is the timeout before a CTI connection is dropped if the authentication is not completed.

.. image:: images/cti_timeout.png

Parting options are used to isolate XiVO users from each other. These options should be used when using the same XiVO for different enterprises.

Context separation is based on the user's line context. This mean that a user with no line is not the member of any context and will not be able to do anything with the CTI client.

.. image:: images/parting_options.png


.. index:: VOIP, network interfaces

Configuring Network Interfaces
==============================

You **must** configure your network interfaces directly from the XiVO web interface via the
*Configuration / Network / Interfaces* page.

.. index::
   single:DHCP
   
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

.. image:: images/netiface_list_post_wizard.png

Listing the network interfaces

To add and configure it, we click on the small plus button next to it, and we get to this page:


.. image:: images/netiface_edit_physical_empty.png

Configure physical interface

In our case, since we want to configure this interface with static information (i.e. not via DHCP), we fill the following fields:

.. image:: images/netiface_edit_physical_filled.png
 
Configure physical interface

Note that since our ''eth0'' network interface already has a default gateway,
we do not enter information in the ''Default gateway'' field for our ''eth1'' interface.

Once we click on ''Save'', the XiVO will put the ''Apply network configuration'' button in bold.

To reconfigure the given network interface with the new information, you click on it.

.. figure:: images/netiface_notify_change.png
   :figclass: align-center

   Apply after modify interface


.. index::
   single:VLAN

Adding a VLAN interface
-----------------------

First, we see there's already a configured network interface on our system:

.. image:: images/netiface_list_configured.png

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

.. note:: Do not forget after you finish the configuration of the network to apply it with the button: **Apply network configuration**

After applying the network configuration:

.. figure:: images/netiface_list_virtual_after_apply.png
   :figclass: align-center

   Listing the network interfaces
