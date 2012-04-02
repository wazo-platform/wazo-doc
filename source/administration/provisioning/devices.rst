.. _devices:

*****************
Supported Devices
*****************


Aastra
======

6700i and 9000i series:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
6730i    |n|         8          |y|
6731i    |y|         8          |y|
6735i    |y|         26         |y|
6737i    |y|         30         |y|
6739i    |y|         55         |y|
6751i    |n|         |u|        |y|
6753i    |n|         6          |y|
6755i    |y|         26         |y|
6757i    |y|         30         |y|
6757i CT |n|         30         |y|
9143i    |n|         7          |y|
9480i    |n|         6          |y|
9480i CT |n|         6          |y|
======== =========== ========== =================

The M670i and M675i expansion modules are supported.


Alcatel-Lucent
==============

IP Touch series:

====================== =========== ========== =================
Model                  Tested [1]_ Fkeys [2]_ Backup proxy [3]_
====================== =========== ========== =================
4008 Extended Edition  |y|         4          |n|
4018 Extended Edition  |y|         4          |n|
====================== =========== ========== =================

Note that you *must not* download the firmware for these phones unless you
agree to the fact it comes from a non-official source.

For the plugins to work fully, you need these additional packages::

   apt-get install p7zip python-pexpect telnet


Avaya
=====

1200 series IP Deskpones (previsouly known as Nortel IP Phones):

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
1220 IP  |y|         0          |n|
1230 IP  |n|         0          |n|
======== =========== ========== =================



Cisco
=====

Cisco Small Business SPA300 series:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
SPA301   |n|         1          |y|
SPA303   |n|         3          |y|
======== =========== ========== =================

.. note:: Function keys are shared with line keys for all SPA phones

Cisco Small Business SPA500 series:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
SPA501G  |y|         8          |y|
SPA502G  |n|         1          |y|
SPA504G  |y|         4          |y|
SPA508G  |y|         8          |y|
SPA509G  |n|         12         |y|
SPA525G  |y|         5          |y|
SPA525G2 |n|         5          |y|
======== =========== ========== =================

The SPA500 expansion module is supported.

Cisco Small Business IP Phones (previously known as Linksys IP Phones)

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
SPA901   |n|         1          |y|
SPA921   |n|         1          |y|
SPA922   |n|         1          |y|
SPA941   |n|         4          |y|
SPA942   |y|         4          |y|
SPA962   |y|         6          |y|
======== =========== ========== =================

.. note::
   You must install the firmware of each SPA9xx phones you are using since they
   reboot in loop when they can't find their firmware.

The SPA932 expansion module is supported.

ATAs:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
PAP2T    |n|         0          |y|
SPA2102  |n|         0          |y|
SPA3102  |n|         0          |y|
SPA8000  |y|         0          |y|
SPA8800  |n|         0          |y|
======== =========== ========== =================

Cisco 7900 series (*SCCP* mode only):

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
7911G    |y|         0          |y|
7912G    |y|         0          |y|
7940G    |y|         0          |y|
7941G    |y|         0          |y|
7941G-GE |y|         0          |y|
7960G    |y|         0          |y|
7961G    |y|         0          |y|
======== =========== ========== =================


Gigaset
=======

Also known as Siemens.

=========== =========== ========== =================
Model       Tested [1]_ Fkeys [2]_ Backup proxy [3]_
=========== =========== ========== =================
C470 IP     |n|         0          |n|
C475 IP     |n|         0          |n|
C590 IP     |n|         0          |n|
C595 IP     |n|         0          |n|
C610 IP     |n|         0          |n|
C610A IP    |n|         0          |n|
S675 IP     |n|         0          |n|
S685 IP     |n|         0          |n|
N300 IP     |n|         0          |n|
N300A IP    |n|         0          |n|
N510 IP PRO |n|         0          |n|
=========== =========== ========== =================


Jitsi
=====

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
Jitsi    |y|         |u|        |n|
======== =========== ========== =================


Polycom
=======

SoundPoint IP:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
SPIP301  |y|         0          |y|
SPIP320  |n|         0          |y|
SPIP321  |n|         0          |y|
SPIP330  |n|         0          |y|
SPIP331  |n|         0          |y|
SPIP335  |y|         0          |y|
SPIP430  |n|         0          |y|
SPIP450  |y|         2          |y|
SPIP501  |y|         0          |y|
SPIP550  |y|         3          |y|
SPIP560  |n|         3          |y|
SPIP600  |n|         0          |y|
SPIP601  |n|         0          |y|
SPIP650  |n|         47         |y|
SPIP670  |n|         47         |y|
======== =========== ========== =================

SoundStation IP:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
SPIP4000 |n|         0          |y|
SPIP5000 |n|         0          |y|
SPIP6000 |y|         0          |y|
SPIP7000 |n|         0          |y|
======== =========== ========== =================

Others:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
VVX1500  |n|         0          |y|
======== =========== ========== =================


Snom
====

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
300      |n|         6          |n|
320      |y|         12         |n|
360      |n|         |u|        |n|
370      |n|         12         |n|
820      |y|         5          |n|
821      |n|         |u|        |n|
870      |y|         15         |n|
PA1      |n|         0          |n|
======== =========== ========== =================

.. note:: For some models, function keys are shared with line keys

There's a known issue with the provisioning of Snom phones in XiVO:

* After a factory reset of a phone, if no language and timezone are set for the
  "default config device" in :menuselection:`XiVO --> Configuration --> Provisioning --> Template device`,
  you will be forced to select a default language and timezone on the phone UI.


Technicolor
===========

Previously known as Thomson:

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
ST2022   |n|         |u|        |y|
ST2030   |y|         10         |y|
TB30     |n|         10         |y|
======== =========== ========== =================

.. note:: Function keys are shared with line keys

Yealink
=======

======== =========== ========== =================
Model    Tested [1]_ Fkeys [2]_ Backup proxy [3]_
======== =========== ========== =================
T12P     |n|         |u|        |n|
T20P     |n|         2          |n|
T22P     |n|         3          |n|
T26P     |n|         13         |n|
T28P     |y|         16         |n|
======== =========== ========== =================

.. note:: Some function keys are shared with line keys

For the plugins to work fully, you need to add the ``non-free`` repository
in :file:`/etc/apt/sources.list` and then::

   apt-get update
   apt-get install unrar


Zenitel
=======

========== =========== ========== =================
Model      Tested [1]_ Fkeys [2]_ Backup proxy [3]_
========== =========== ========== =================
IP station |y|         1          |n|
========== =========== ========== =================


Caption :

.. [1] ``Tested`` means the device has been tested by the XiVO development team and that
       the developers have access to this device.
.. [2] ``Fkeys`` is the number of programmable function keys that you can configure from the
       XiVO web interface. It is not necessarily the same as the number of physical function
       keys the device has (for example, a 6757i has 12 physical keys but you can configure 30
       function keys because of the page system).
.. [3] ``Backup proxy`` means the device supports a backup proxy and backup registrar.

.. |y| replace:: Yes
.. |n| replace:: No
.. |u| replace:: ---


