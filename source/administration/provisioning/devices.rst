.. _devices:

*****************
Supported Devices
*****************

Aastra
======

6700i and 9000i series:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
6730i    |n|         8          |y|
6731i    |y|         8          |y|
6735i    |y|         26         |y|
6737i    |y|         30         |y|
6739i    |y|         55         |y|
6751i    |n|         |u|        |y|
6753i    |y|         6          |y|
6755i    |y|         26         |y|
6757i    |y|         30         |y|
6757i CT |n|         30         |y|
9143i    |y|         7          |y|
9480i    |n|         6          |y|
9480i CT |n|         6          |y|
======== =========== ========== ============

The M670i and M675i expansion modules are supported.


Alcatel-Lucent
==============

IP Touch series:

====================== =========== ========== ============
Model                  Tested [1]_ Fkeys [2]_ XiVO HA [3]_
====================== =========== ========== ============
4008 Extended Edition  |y|         4          |n|
4018 Extended Edition  |y|         4          |n|
====================== =========== ========== ============

Note that you *must not* download the firmware for these phones unless you
agree to the fact it comes from a non-official source.

For the plugin to work fully, you need these additional packages::

   apt-get install p7zip python-pexpect telnet


Avaya
=====

1200 series IP Deskphones (previously known as Nortel IP Phones):

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
1220 IP  |y|         0          |n|
1230 IP  |n|         0          |n|
======== =========== ========== ============



Cisco
=====


Cisco Small Business SPA300 series:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
SPA301   |n|         1          |n|
SPA303   |n|         3          |n|
======== =========== ========== ============

.. note:: Function keys are shared with line keys for all SPA phones

Cisco Small Business SPA500 series:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
SPA501G  |y|         8          |n|
SPA502G  |n|         1          |n|
SPA504G  |y|         4          |n|
SPA508G  |y|         8          |n|
SPA509G  |n|         12         |n|
SPA525G  |y|         5          |n|
SPA525G2 |n|         5          |n|
======== =========== ========== ============

The SPA500 expansion module is supported.

Cisco Small Business IP Phones (previously known as Linksys IP Phones)

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
SPA901   |n|         1          |n|
SPA921   |n|         1          |n|
SPA922   |n|         1          |n|
SPA941   |n|         4          |n|
SPA942   |y|         4          |n|
SPA962   |y|         6          |n|
======== =========== ========== ============

.. note::
   You must install the firmware of each SPA9xx phones you are using since they
   reboot in loop when they can't find their firmware.

The SPA932 expansion module is supported.

ATAs:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
PAP2T    |n|         0          |n|
SPA2102  |n|         0          |n|
SPA3102  |n|         0          |n|
SPA8000  |y|         0          |n|
SPA8800  |n|         0          |n|
======== =========== ========== ============

.. note::
   These devices can be used to connect Faxes. For better success with faxes some parameters 
   must be changed. You can read the :ref:`fax-analog-gateway` section.

Cisco 7900 series (*SCCP* mode only):

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
7911G    |y|         0          |n|
7912G    |y|         0          |n|
7940G    |y|         0          |n|
7941G    |y|         0          |n|
7941G-GE |y|         0          |n|
7960G    |y|         0          |n|
7961G    |y|         0          |n|
======== =========== ========== ============

.. _cisco-provisioning:

To install firmware for xivo-cisco-sccp plugins, you need to manually download
the firmware files from the Cisco website and save them in the
:file:`/var/lib/xivo-provd/plugins/$plugin-name/var/cache` directory.

For example, if you have installed the ``xivo-cisco-sccp-legacy`` plugin and you want
to install the ``7940-7960-fw``, ``networklocale`` and ``userlocale_fr_FR`` package, you
must:

* Go to http://www.cisco.com
* Click on "Log In" in the top right corner of the page, and then log in
* Click on the "Support" menu
* Click on the "Downloads" tab, then on "Voice & Unified Communications"
* Select "IP Telephony", then "Unified Communications Endpoints", then the model
  of your phone (in this example, the 7940G)
* Click on "Skinny Client Control Protocol (SCCP) software"
* Choose the same version as the one shown in the plugin
* Download the file with an extension ending in ".zip", which is usually the last
  file in the list
* In the XiVO web interface, you'll then be able to click on the "install" button
  for the firmware

The procedure is similar for the network locale and the user locale package, but:

* Instead of clicking on "Skinny Client Control Protocol (SCCP) software", click on
  "Unified Communications Manager Endpoints Locale Installer"
* Click on "Linux"
* Choose the same version of the one shown in the plugin
* For the network locale, download the file named "po-locale-combined-network.cop.sgn"
* For the user locale, download the file named "po-locale-$locale-name.cop.sgn, for example
  "po-locale-fr_FR.cop.sgn" for the "fr_FR" locale
* Both files must be placed in :file:`/var/lib/xivo-provd/plugins/$plugin-name/var/cache` directory. Then install them in the XiVO Web Interface.

.. note:: Currently user and network locale 9.0.2 should be used for plugins xivo-sccp-legacy and xivo-cisco-sccp-9.0.3

Digium
======

Digium phones:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
D40      |y|         2          |n|
D50      |n|         14         |n|
D70      |y|         106        |n|
======== =========== ========== ============

.. note:: Some function keys are shared with line keys

Particularities:

* For best results, activate :ref:`dhcp-integration` on your XiVO.
* English is the only language supported, other languages (e.g. french) are not supported.
* Impossible to do directed pickup using a BLF function key.
* Only supports DTMF in RFC2833 mode.
* Does not work reliably with Cisco ESW520 PoE switch. When connected to such a switch, the D40
  tends to reboot randomly, and the D70 does not boot at all.
* It's important to not edit the phone configuration via the phones' web interface
  when using these phones with XiVO.
* Paging doesn't work.


Gigaset
=======

Also known as Siemens.

=========== =========== ========== ============
Model       Tested [1]_ Fkeys [2]_ XiVO HA [3]_
=========== =========== ========== ============
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
=========== =========== ========== ============


Jitsi
=====

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
Jitsi    |y|         |u|        |n|
======== =========== ========== ============

Panasonic
=========


Panasonic KX-HTXXX series:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
KX-HT113   |n|         |u|         |n|
KX-HT123   |n|         |u|         |n|
KX-HT133   |n|         |u|         |n|
KX-HT136   |n|         |u|         |n|
======== =========== ========== ============

.. note:: This phone is for testing for the moment


Polycom
=======

SoundPoint IP:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
SPIP301  |y|         0          |n|
SPIP320  |n|         0          |n|
SPIP321  |n|         0          |n|
SPIP330  |n|         0          |n|
SPIP331  |n|         0          |n|
SPIP335  |y|         0          |n|
SPIP430  |n|         0          |n|
SPIP450  |y|         2          |n|
SPIP501  |y|         0          |n|
SPIP550  |y|         3          |n|
SPIP560  |n|         3          |n|
SPIP600  |n|         0          |n|
SPIP601  |n|         0          |n|
SPIP650  |n|         47         |n|
SPIP670  |n|         47         |n|
======== =========== ========== ============

SoundStation IP:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
SPIP4000 |n|         0          |n|
SPIP5000 |n|         0          |n|
SPIP6000 |y|         0          |n|
SPIP7000 |n|         0          |n|
======== =========== ========== ============

Others:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
VVX1500  |n|         0          |n|
======== =========== ========== ============


Snom
====

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
300      |n|         6          |n|
320      |y|         12         |n|
360      |n|         |u|        |n|
370      |n|         12         |n|
710      |n|         5          |n|
720      |n|         18         |n|
760      |n|         12         |n|
820      |y|         4          |n|
821      |n|         |u|        |n|
870      |y|         15         |n|
MP       |n|         |u|        |n|
PA1      |n|         0          |n|
======== =========== ========== ============

.. note:: For some models, function keys are shared with line keys

There's a known issue with the provisioning of Snom phones in XiVO:

* After a factory reset of a phone, if no language and timezone are set for the
  "default config device" in :menuselection:`XiVO --> Configuration --> Provisioning --> Template device`,
  you will be forced to select a default language and timezone on the phone UI.


Technicolor
===========

Previously known as Thomson:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
ST2022   |n|         |u|        |n|
ST2030   |y|         10         |n|
======== =========== ========== ============

.. note:: Function keys are shared with line keys


Yealink
=======

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
T20P     |n|         2          |n|
T22P     |n|         3          |n|
T26P     |n|         13         |n|
T28P     |y|         16         |n|
======== =========== ========== ============

.. note:: Some function keys are shared with line keys

For the plugins to work fully, you need to add the ``non-free`` repository
in :file:`/etc/apt/sources.list` and then::

   apt-get update
   apt-get install unrar


Zenitel
=======

========== =========== ========== ============
Model      Tested [1]_ Fkeys [2]_ XiVO HA [3]_
========== =========== ========== ============
IP station |y|         1          |n|
========== =========== ========== ============

Caption :

.. [1] ``Tested`` means the device has been tested by the XiVO development team and that
       the developers have access to this device.
.. [2] ``Fkeys`` is the number of programmable function keys that you can configure from the
       XiVO web interface. It is not necessarily the same as the number of physical function
       keys the device has (for example, a 6757i has 12 physical keys but you can configure 30
       function keys because of the page system).
.. [3] ``XiVO HA`` means the device is confirmed to work with :ref:`XiVO HA <high-availability>`.

.. |y| replace:: Yes
.. |n| replace:: No
.. |u| replace:: ---

