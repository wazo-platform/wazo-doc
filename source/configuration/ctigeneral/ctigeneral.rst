**********
CTI Server
**********

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
