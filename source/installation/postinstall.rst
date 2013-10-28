*****************
Post installation
*****************

Display called name on internal calls
=====================================

When you call internally another phone of the system you would like your phone to display the name
of the called person (instead of the dialed number only).
To achieve this you must change the following SIP options:

* :menuselection:`Services --> IPBX --> General settings --> SIP Protocol --> Default`:

    * Trust the Remote-Party-ID: yes,
    * Send the Remote-Party-ID: select ``PAI``


.. _callerid_num_normalization:

Incoming caller number display
==============================

The display of caller number on incoming calls depends on what is sent by your operator.
You can modify it via the file :file:`/etc/pf-xivo/asterisk/xivo_in_callerid.conf`.

.. note:: this is this modified caller id number which will be used in the reverse directory lookup

Examples:

* if you use a prefix to dial outgoing numbers (like a 0) you should add a 0 to all the ``add =`` sections,
* you may want to display incoming numbers in E.164 format. For example, you can change the ``[national1]`` section to::

    callerid = ^0[1-9]\d{8}$
    strip = 1
    add = +33

To enable the changesyou have to restart xivo-agid::

    service xivo-agid restart


Time and date
=============

* Configure your locale and default time zone in device template => :menuselection:`Configuration --> Provisioning --> Template Device`
  by editing the default template
* Configure the Timezone in => :menuselection:`Services --> IPBX --> General settings --> Advanced --> Timezone`
* Reconfigure your timezone for the system::

    dpkg-reconfigure tzdata


Codecs
======

You should also select default codecs. It obviously depends on the telco links, the country, the phones, the usage etc.
Here is a typical example for Europe (the main goal in this example is to select *only* G.711 **A-Law** instead of both G.711 A-Law and G.711 µ-Law by default):

* SIP : :menuselection:`Services --> IPBX --> General settings --> SIP Protocol --> Signaling`:

    * Customize codec : activate,
    * Disable codec : All
    * Codec list::

        G.711 A-Law
        G.722
        G.729A
        H.264

* IAX2 : :menuselection:`Services --> IPBX --> General settings -->  IAX Protocol --> Default`:

    * Customize : activate,
    * Disallowed codec : All
    * Codec list::

        G.711 A-Law
        G.722
        G.729A
        H.264
