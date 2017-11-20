.. index:: single:Wazo Client

***********
Wazo Client
***********

What is the Wazo Client
=======================

The Wazo Client is an application that you install on your computer and is connected to the Wazo
server. This application offers the following features:

* search contacts and show their presence, phone status
* make calls through your phone (the Wazo Client is **NOT** a softphone, it is complementary to the
  phone)
* access your voicemail through your phone
* enable call forwards, call filtering
* show the history of your calls
* list conference rooms and members
* send faxes

It also offers some call center features:

* show screen popups or open URLs when you receive/answer a call
* list agents, queues, calls in queues
* login/logoff, pause/unpause other agents (for supervisors)
* listen/whisper to agents through you phone (for supervisors)

A lot of those features are modular and may be enabled for each user by choosing which :ref:`Xlets
<xlet-list>` they can see.

Getting the Wazo Client
=======================

Binaries of the Wazo Client are available on our mirror. (`latest version`_) (`all versions`_)

.. _all versions: http://mirror.wazo.community/iso/archives
.. _latest version: http://mirror.wazo.community/iso/wazo-current

.. _cti_client_compatibility:

Versions
--------

Here is the compatibility table between Wazo server and Wazo Client:

+--------------------+---------------------------------+
| Server             | Compatible with client          |
+====================+=================================+
| Until 16.12        | Identical version as the server |
+--------------------+---------------------------------+
| 16.13 to 17.15     | 16.13, 17.13, 17.14, 17.15      |
+--------------------+---------------------------------+
| 17.16 and later    | 17.16 and later                 |
+--------------------+---------------------------------+


Download
--------

Choose the version you want and in the right directory, get :

* the ``.exe`` file for Windows
* the ``.deb`` file for Ubuntu or Debian (i386 or amd64, depending on your computer)
* the ``.dmg`` file for Mac OS

For Windows, double-click on the file and follow the instructions. You can also install it silently::

   wazoclient-17.XX-x86.exe /S

For Ubuntu/Debian, double-click on the file or execute the following command::

   $ gdebi wazoclient-*.deb

For Mac OS, double-click on the file and drag-and-drop the inner file on the
Application entry of the Finder.

The Wazo Client should then be available in the applications menu of each platform.

If you want to build your own Wazo Client, see :ref:`build_wazoclient`.

.. index:: Xlets

Connection to the server
========================

To connect to the server using the Wazo Client you need a user name, a password and the server's
address. Optionally, it is possible to login an agent while connecting to the server.

.. figure:: images/login_window.png
   :scale: 85%

.. _xlet-list:

Xlets
=====

Xlets are features of the Wazo Client. It is the contraction of XiVO applets. To select which xlets
are displayed in your client, see :ref:`cti-profiles`.

.. toctree::
   :maxdepth: 1

   Conference xlet <xlets/conference>
   Directory xlet <xlets/directory>
   Fax xlet <xlets/fax>
   History xlet <xlets/history>
   Identity xlet <xlets/identity>
   People xlet <xlets/people>
   Service xlet <xlets/service>


Configuration
=============

The Wazo Client configuration options can be accessed under :menuselection:`Wazo Client --> Configure`.


Connection Configuration
------------------------

.. figure:: images/configuration_connection.png
   :scale: 85%

This page allows the user to set his network information to connect to the xivo-ctid server.

* `Server` is the IP address of the server.
* `Backup server` is the IP address of the backup server.
* `Port` is the port on which xivo-ctid is listening for connections. (default: 5003)
* `STARTTLS` is used to specify that a secure connect should be used

.. note::

   To use STARTTLS, the server needs to be configured to :ref:`accept encrypted connection <ctid-encryption>`.


Handling callto: and tel: URLs
==============================

The Wazo Client can handle telephone number links that appear in web pages. The client will
automatically dial the number when you click on a link.

.. note:: You must already be logged in for automatic dialing to work, otherwise the client will
           simply start up and wait for you to log in.

.. warning:: The option in the Wazo Client :menuselection:`Advanced --> Allow multiple instances
             of Wazo Client` must be disabled, else you will launch one new Wazo Client with every click.

Mac OS
------

``callto:`` links will work out-of-the-box in Safari and other web browsers
after installing the client.

``tel:`` links will open FaceTime after installing the client. To make the
Wazo Client the default application to open ``tel:`` URLs in Safari.

1. Open the FaceTime application
2. Connect using your apple account
3. Open the FaceTime preferences
4. Change the *Default for calls* entry to *wazoclient.app*


.. figure:: images/facetime_preference.png


.. note:: The ``tel:`` URL works out-of-the-box in versions of mac osx before 10.10.


Windows
-------

Wazo Client is associated with ``callto:`` and ``tel:`` upon installation. Installing other
applications afterward could end up overriding these associations.

* Windows Vista: :menuselection:`Start menu --> Control Panel --> Default Programs`, subsection Protocols
* Windows 7: :menuselection:`Start menu --> Control Panel --> Default Programs`, subsection Protocols
* Windows 10: :menuselection:`Start menu --> Settings --> System --> Default apps --> Choose default apps by protocol`

.. figure:: images/windows_default_programs.png
   :scale: 85%


Ubuntu
------

Currently, ``callto:`` or ``tel:`` links are only supported in Firefox. There is no configuration
needed.

GNU/Linux Debian
----------------

Currently, ``callto:`` or ``tel:`` links are only supported in Firefox. If the Wazo Client is not
listed in the proposition when you open the link, browse your files to find
:file:`/usr/bin/wazoclient`.

Manual association in Firefox
-----------------------------

If, for some reason, Firefox does not recognize ``callto:`` or ``tel:`` URIs you can manually
associate them to the Wazo Client using the following steps:

1. Type ``about:config`` in the URL bar
2. Click the *I'll be careful, I promise !* button to close the warning
3. Right-click anywhere in the list and select *New -> Boolean*
4. Enter ``network.protocol-handler.external.callto`` as preference name
5. Select ``false`` as value
6. Repeat steps 3 to 6, but replace ``callto`` by ``tel`` at step 4

The next time that you click on a telephone link, Firefox will ask you to choose an application. You
will then be able to choose the Wazo Client for handling telephone numbers.
