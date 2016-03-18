.. _compatible-devices:

Community Supported Devices
===========================

The community supported devices are only supported by the community. In other words, maintenance,
bug, corrections and features are developed by members of the XiVO community. XiVO does not
officially endorse support for these devices.

``xivo-provd`` plugins for these devices can be installed from the
:ref:`"community supported devices" repository <alternative-plugins-repo>`.

Aastra
------

6700i and 9000i series:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
6730i    |n|         8          |y|
6753i    |y|         6          |y|
6757i    |y|         30         |y|
9143i    |y|         7          |y|
9480i    |n|         6          |y|
9480CT   |n|         6          |y|
======== =========== ========== ============


Alcatel-Lucent
--------------

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
-----

1200 series IP Deskphones (previously known as Nortel IP Phones):

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
1220 IP  |y|         0          |n|
1230 IP  |n|         0          |n|
======== =========== ========== ============


Cisco
-----

Cisco Small Business SPA300 series:

=========== =========== ========== ============
Model       Tested [1]_ Fkeys [2]_ XiVO HA [3]_
=========== =========== ========== ============
SPA301      |n|         1          |n|
SPA303      |n|         3          |n|
=========== =========== ========== ============

.. note:: Function keys are shared with line keys for all SPA phones

Cisco Small Business SPA500 series:

=========== =========== ========== ============
Model       Tested [1]_ Fkeys [2]_ XiVO HA [3]_
=========== =========== ========== ============
SPA501G     |y|         8          |n|
SPA502G     |n|         1          |n|
SPA504G     |y|         4          |n|
SPA508G     |y|         8          |n|
SPA509G     |n|         12         |n|
SPA512G     |n|         1          |n|
SPA514G     |n|         4          |n|
SPA525G     |y|         5          |n|
SPA525G2    |n|         5          |n|
=========== =========== ========== ============

The SPA500 expansion module is supported.

Cisco Small Business IP Phones (previously known as Linksys IP Phones)

=========== =========== ========== ============
Model       Tested [1]_ Fkeys [2]_ XiVO HA [3]_
=========== =========== ========== ============
SPA901      |n|         1          |n|
SPA921      |n|         1          |n|
SPA922      |n|         1          |n|
SPA941      |n|         4          |n|
SPA942      |y|         4          |n|
SPA962      |y|         6          |n|
=========== =========== ========== ============

.. note:: You must install the firmware of each SPA9xx phones you are using since they reboot in
          loop when they can’t find their firmware.

The SPA932 expansion module is supported.

ATAs:

=========== =========== ========== ============
Model       Tested [1]_ Fkeys [2]_ XiVO HA [3]_
=========== =========== ========== ============
PAP2        |n|         0          |n|
SPA2102     |n|         0          |n|
SPA8800     |n|         0          |n|
SPA112      |n|         0          |n|
=========== =========== ========== ============

   For best results, activate :ref:`dhcp-integration` on your XiVO.

.. note::
   These devices can be used to connect Faxes. For better success with faxes some parameters
   must be changed. You can read the :ref:`fax-analog-gateway` section.

.. note::
   If you want to manually resynchronize the configuration from the ATA device
   you should use the following url::

     http://ATA_IP/admin/resync?http://XIVO_IP:8667/CONF_FILE

   where :

      * *ATA_IP*    is the IP address of the ATA,
      * *XIVO_IP*   is the IP address of your XiVO,
      * *CONF_FILE* is one of ``spa2102.cfg``, ``spa8000.cfg``


Fanvil
------

=========== =========== ========== ============
Model       Tested [1]_ Fkeys [2]_ XiVO HA [3]_
=========== =========== ========== ============
C62P        |y|         5          |y|
=========== =========== ========== ============


Gigaset
-------

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
-----

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
Jitsi    |y|         |u|        |n|
======== =========== ========== ============


Panasonic
---------

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
-------

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
SPIP320  |n|         0          |n|
SPIP321  |n|         0          |n|
SPIP330  |n|         0          |n|
SPIP430  |n|         0          |n|
SPIP501  |y|         0          |n|
SPIP600  |n|         0          |n|
SPIP601  |n|         0          |n|
SPIP670  |n|         47         |n|
======== =========== ========== ============

SoundStation IP:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
SPIP4000 |n|         0          |n|
======== =========== ========== ============

Others:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
VVX1500  |n|         0          |n|
======== =========== ========== ============


Snom
----

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
300      |n|         6          |y|
320      |y|         12         |y|
360      |n|         |u|        |y|
820      |y|         4          |y|
MP       |n|         |u|        |y|
PA1      |n|         0          |y|
======== =========== ========== ============

.. note:: For some models, function keys are shared with line keys

.. warning:: If you are using Snom phones with HA, you should not assign multiple lines to the same device.

There's a known issue with the provisioning of Snom phones in XiVO:

* After a factory reset of a phone, if no language and timezone are set for the "default config device" in :menuselection:`XiVO --> Configuration --> Provisioning --> Template device`, you will be forced to select a default language and timezone on the phone UI.


Technicolor
-----------

Previously known as Thomson:

======== =========== ========== ============
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_
======== =========== ========== ============
ST2022   |n|         |u|        |u|
ST2030   |y|         10         |y|
======== =========== ========== ============

.. note:: Function keys are shared with line keys


.. _yealink-community-devices:

Yealink
-------

======== =========== ========== ============ ================
Model    Tested [1]_ Fkeys [2]_ XiVO HA [3]_ Plugin
======== =========== ========== ============ ================
CP860    |n|         0          |u|          xivo-yealink-v72
T23P     |n|         3          |u|          xivo-yealink-v80
T23G     |y|         3          |y|          xivo-yealink-v80
T27P     |y|         21         |y|          xivo-yealink-v80
T29G     |n|         27         |u|          xivo-yealink-v80
T49G     |y|         29         |y|          xivo-yealink-v80
======== =========== ========== ============ ================

.. note:: Some function keys are shared with line keys


Zenitel
-------

========== =========== ========== ============
Model      Tested [1]_ Fkeys [2]_ XiVO HA [3]_
========== =========== ========== ============
IP station |y|         1          |n|
========== =========== ========== ============

.. [1] ``Tested`` means the device has been tested by the XiVO development team and that
       the developers have access to this device.
.. [2] ``Fkeys`` is the number of programmable function keys that you can configure from the
       XiVO web interface. It is not necessarily the same as the number of physical function
       keys the device has (for example, a 6757i has 12 physical keys but you can configure 30
       function keys because of the page system).
.. [3] ``XiVO HA`` means the device is confirmed to work with :ref:`XiVO HA <high-availability>`.
.. [4] These devices are marked as ``Not Tested`` because other similar models using the same firmware have been tested instead.
       If these devices ever present any bugs, they will be troubleshooted by the XiVO support team.

.. |y| replace:: Yes
.. |n| replace:: No
.. |ny| replace:: Not Yet
.. |u| replace:: ---
