.. index:: single:XiVO CTI Client


**********
CTI Client
**********

This section describes the CTI Client and its various xlets

Getting the XiVO Client
=======================

Binaries of the XiVO Client are available on our `mirror`_.

.. _mirror: http://downloads.xivo.fr/xivo_cti_client

Choose the version you want and in the right directory, get :

* the ``.exe`` file for Windows
* the ``.deb`` file for Ubuntu or Debian (i386 or amd64, depending on your computer)
* the ``.dmg`` file for Mac OS

For Windows, double-click on the file and follow the instructions.

For Ubuntu/Debian, double-click on the file or execute the following command::

   $ gdebi xivoclient-*.deb

For Mac OS, double-click on the file and drag-and-drop the inner file on the
Application entry of the Finder.

The XiVO Client should then be available in the applications menu of each platform.

.. index:: Xlets

Connection to the server
========================

To connect to the server using the XiVO client you need a user name, a password and the server's
address. Optionally, it is possible to login an agent while connecting to the server. An option is
available in the configuration, account to show agent login info.

.. figure:: images/login_window.png
   :scale: 85%

Xlets
=====

Xlets are features of the CTI Client. It is the contraction of XiVO applets.

.. toctree::
   :maxdepth: 1

   Agent details xlet <xlets/agent_details>
   Agent list xlet <xlets/agent_list>
   Calls of a Queue <xlets/calls_of_a_queue>
   Contact xlet <xlets/contact>
   Directory xlet <xlets/directory>
   Fax xlet <xlets/fax>
   Local directory xlet <xlets/localdir>
   Service xlet <xlets/service>
   Dial xlet <xlets/dial>

Configuration
=============

The XiVO client configuration options can be accessed under :menuselection:`XiVO client --> configure`.

Connection Configuration
------------------------

.. figure:: images/configuration_connection.png
   :scale: 85%

This page allows the user to set his network information to connect to the xivo-ctid server.

* `Server Host` is the IP adress of the server.
* `Login Port` is the port on wich xivo-ctid is listening for connections. (default: 5003)
* `Encrypt Connection` is the option to encrypt messages between the client and the server. (default port 5013)
* `Try to reconnect` will reconnect the client when the connection is dropped.
* `Try to reconnect interval` is the reconnection delay before the auto-reconnection is tryed.
* `Keep alive interval` is the number of seconds between keepalives messages.
