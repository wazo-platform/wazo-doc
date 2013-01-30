.. index:: single:XiVO CTI Client


**********
CTI Client
**********

This section describes the CTI Client and its various xlets

Getting the XiVO Client
=======================

Binaries of the XiVO Client are available on our `mirror`_.

.. _mirror: http://downloads.xivo.fr/xivo_cti_client

.. warning::

   The installed version of the XiVO Client must match the XiVO server's version installation. With our current architecture, there is no way to guarantee that the XiVO server will be retro-compatible with older versions of the XiVO Client. Non-matching XiVO server and XiVO Clients versions will bring inconsistencies.

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

.. _xlet-list:

Xlets
=====

Xlets are features of the CTI Client. It is the contraction of XiVO applets.

.. toctree::
   :maxdepth: 1

   Conference xlet <xlets/conference>
   Contact xlet <xlets/contact>
   Directory xlet <xlets/directory>
   Fax xlet <xlets/fax>
   History xlet <xlets/history>
   Local directory xlet <xlets/localdir>
   Remote Directory xlet <xlets/remote_directory>
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

Handling callto: and tel: URLs
==============================

The XiVO client can handle telephone number links that appear in web pages. The client will automatically dial
the number when you click on a link.

.. note:: You must already be logged in for automatic dialing to work, otherwise the client will simply start up and wait for you to log in.

.. warning:: The option in the XiVO Client :menuselection:`GUI Options --> Allow multiple instances of XiVO Client` must be disabled, else you will launch one new XiVO Client with every click.

Mac OS
------

``callto:`` and ``tel:`` links will work out-of-the-box in Safari and other web browsers after installing the client.

Windows
-------

The following popups might appear When you open a ``callto:`` or ``tel:`` link for the first time in Internet Explorer:

.. figure:: images/ie_warning_1.png
.. figure:: images/ie_warning_2.png

Simply click on *allow* to dial the number using the XiVO client.

.. note:: If you do not want these warnings to appear each time, do not forget to check/uncheck the checkbox at the bottom of the popups.

Ubuntu
------

There is no configuration needed.

GNU/Linux Debian
----------------

If the XiVO Client is not listed in the proposition when you open the link,
browse your files to find :file:`/usr/bin/xivoclient`.

Manual association in firefox
-----------------------------

If, for some reason, firefox does not recognize ``callto:`` or ``tel:`` URIs you can manually associate them to the XiVO client using the following steps:

1. Type ``about:config`` in the URL bar
2. Click the *I'll be careful, I promise !* button to close the warning
3. Right-click anywhere in the list and select *New -> Boolean*
4. Enter ``network.protocol-handler.external.callto`` as preference name
5. Select ``false`` as value
6. Repeat steps 3 to 6, but replace ``callto`` by ``tel`` at step 4

The next time that you click on a telephone link, firefox will ask you to choose an application. You will then be able to choose the XiVO client for handling telephone numbers.
