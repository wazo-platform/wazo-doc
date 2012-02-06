.. _devices:

*****************
Supported devices
*****************

.. XXX show which one have not been tested

Aastra
------

6700i and 9000i series:

- 6730i
- 6731i
- 6739i
- 6751i
- 6753i
- 6755i
- 6757i
- 6757i CT
- 9143i
- 9480i
- 9480i CT

The M670i and M675i expansion modules are supported.

Alcatel-Lucent
--------------

IP Touch series:

- 4008 Extended Edition
- 4018 Extended Edition

Note that you *must not* download the firmware for these phones unless you
agree to the fact it comes from a non-official source.

For the plugins to work fully, you need these additional packages::

   apt-get install p7zip python-pexpect telnet

Avaya
-----

1200 series IP Deskpones (previsouly known as Nortel IP Phones):

- 1220 IP
- 1230 IP

Cisco
-----

Cisco Small Business SPA300 series:

- SPA301
- SPA303

Cisco Small Business SPA500 series:

- SPA501G
- SPA502G
- SPA504G
- SPA508G
- SPA509G
- SPA525G
- SPA525G2

The SPA500 expansion module is supported.

Cisco Small Business IP Phones (previsouly known as Linksys IP Phones)

- SPA901
- SPA921
- SPA922
- SPA941
- SPA942
- SPA962

The SPA932 expansion module is supported.

ATAs:

- PAP2T
- SPA2102
- SPA3102
- SPA8000
- SPA8800

Gigaset
-------

Also known as Siemens.

- C470 IP
- C475 IP
- C590 IP
- C595 IP
- C610 IP
- C610A IP
- S675 IP
- S685 IP
- N300 IP
- N300A IP
- N510 IP PRO

Jitsi
-----

- Jitsi (previsouly known as SIP Communicator)

Polycom
-------

SoundPoint IP:

- SPIP301
- SPIP320
- SPIP321
- SPIP330
- SPIP331
- SPIP335
- SPIP430
- SPIP450
- SPIP501
- SPIP550
- SPIP560
- SPIP600
- SPIP601
- SPIP650
- SPIP670

SoundStation IP:

- SPIP4000
- SPIP5000
- SPIP6000
- SPIP7000

Others:

- VVX1500

Snom
----

- 300
- 320
- 360
- 370
- 820
- 821
- 870

There's a few known issues with the provisioning of Snom phones in XiVO:

- Synchronization doesn't work reliably. Often, the phones will get stuck at
  some stage of their boot process. The solution is to either reboot the phone via the
  phone UI or by power cycling it.
- After a factory reset of a phone, if no language and timezone are set for the
  "default config device" in :menuselection:`XiVO --> Configuration --> Provisioning --> Template device`,
  you will be forced to select a default language and timezone on the phone UI.

Technicolor
-----------

Previously known as Thomson:

- ST2022
- ST2030
- TB30

Yealink
-------

- T12P
- T20P
- T22P
- T26P
- T28P

For the plugins to work fully, you need to add the ``non-free`` repository
in ``/etc/apt/sources.list`` and then::

   apt-get update
   apt-get install unrar

Zenitel
-------

- IP station
