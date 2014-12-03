.. _devices:

*******
Devices
*******

In XiVO, there is two kind of devices:

.. toctree::
   :maxdepth: 1

   official_devices
   community_devices

The officially supported devices will be supported across upgrades and phone features are guaranteed
to be supported on the latest version.

The community supported devices are only supported by the community. In other words, maintenance,
bug, corrections and features are developed by members of the XiVO community. XiVO does not
officially endorse support for these devices.

The next topics lists the officially and community supported devices. For each vendor, a table shows
the various features supported by XiVO. Here's an example:

+--------------------------------------------+---------+---------+--------------+
|                                            | Model X | Model Y | Model Z      |
+============================================+=========+=========+==============+
| Provisioning                               | Y       | Y       | Y            |
+--------------------------------------------+---------+---------+--------------+
| H-A                                        | Y       | Y       | Y            |
+--------------------------------------------+---------+---------+--------------+
| Directory XIVO                             | N       | Y       | Y            |
+--------------------------------------------+---------+---------+--------------+
| Funckeys                                   | 0       | 2       | 8            |
+--------------------------------------------+---------+---------+--------------+
|                                            | **Supported programmable keys**  |
+--------------------------------------------+---------+---------+--------------+
| User with supervision function             | Y       | Y       | Y            |
+--------------------------------------------+---------+---------+--------------+

The rows have the following meaning:

Provisioning
   Is the device supported by the :ref:`auto-provisioning <provisioning>` system ?

H-A
   Is the device supported by the :ref:`high availability <high-availability>` system ?

Directory XiVO
   Is the device supported by the :ref:`remote directory <remote-directory>` ? In other word, is it
   possible to consult the XiVO's remote directory from the device ?

Funckeys
   How many function keys can be configured on the device from the XiVO web interface ?

   The number of function keys that can be configured on a device is not necessarily the same as
   the number of physical function keys the device has. For example, an Aastra 6757i has 12 physical
   keys but you can configure 30 function keys because of the page system.

Inside a table, the following legend is used:

* Y = Yes / Supported
* N = No / Not supported
* NT = Not tested
* NYT = Not yet tested

Each table also contains a section about the supported function keys. In that section, the following
legend can also be used:

* FK = Funckey
* SK = SoftKey
* HK = HardKey
* MN = Menu

Function keys work using the extensions in :menuselection:`Services --> Extensions`. It is important
to enable the function keys you want to use.  Also, the enable transfer option in the user
configuration services tab must be enabled to use transfer function keys.
