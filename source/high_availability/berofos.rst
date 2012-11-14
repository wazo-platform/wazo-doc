*******************
Berofos Integration
*******************

XiVO offers the possibility to integrate a `berofos failover switch`_ within a HA cluster.

.. _berofos failover switch: http://www.beronet.com/product/failover-switch/

This is useful if you have one or more ISDN lines (i.e. T1/E1 or T2 lines) that you want to use
whatever the state of your XiVO HA cluster. To use a berofos within your XiVO HA
installation, you need to properly configure both your berofos and your XiVOs,
then the berofos will automatically switch your ISDN lines from your master node to
your slave node if your master goes down, and vice-versa when it comes back up.


You can also use a Berofos failover switch to secure the ISDN provider lines
when installing a XiVO in front of an existing PBX.
The goal of this configuration is to mitigate the consequences of an outage of the XiVO : with this
equipment the ISDN provider links could be switched to the PBX directly if the XiVO goes down.

XiVO **does not offer natively** the possibility to configure Berofos in this failover mode.
The `Berofos Integration with PBX`_ section describes a workaround.

.. _Berofos Integration with PBX: http://documentation.xivo.fr/production/introduction/introduction.html#berofos-integration-with-pbx


Installation and Configuration
==============================

Master Configuration
--------------------

There is nothing to be done on the master node.


Slave Configuration
-------------------

First, install the bntools package::

   apt-get install bntools

This will make the ``bnfos`` command available.

You can then connect your berofos to your network and power it on. By default, the berofos
will try to get an IP address via DHCP. If it is not able to get such address from a DHCP
server, it will take the 192.168.0.2/24 IP address.

.. note:: The DHCP server on XiVO does not offer IP addresses to berofos devices by default.

Next step is to create the :file:`/etc/bnfos.conf` file via the following command::

   bnfos --scan -x

If no berofos device is detected using this last command, you'll have to explicitly specify the IP
address of the berofos via the -h option::

   bnfos --scan -x -h <berofos ip>

At this stage, your :file:`/etc/bnfos.conf` file should contains something like this::

   [fos1]
   mac = 00:19:32:00:12:1D
   host = 10.34.1.50
   #login = <user>:<password>

It is advised to configure your berofos with a static IP address. You first need to
put your berofos into *flash mode* :

- press and hold the black button next to the power button,
- power on your berofos,
- release the black button when the red LEDs of port D start blinking.

Then, you can issue the following command, by first replacing the network configuration with
your one::

   bnfos --netconf -f fos1 -i 10.34.1.20 -n 255.255.255.0 -g 10.34.1.1 -d 0

.. note::

   * ``-i`` is the IP address
   * ``-n`` is the netmask
   * ``-g`` is the gateway
   * ``-d 0`` is to disable DHCP

You can then update your berofos firmware to version 1.53::

   wget http://www.beronet.com/downloads/berofos/bnfos_v153.bin
   bnfos --flash bnfos_v153.bin -f fos1

Once this is done, you'll have to reboot your berofos in operationnal mode (that is in normal mode).

Then you must rewrite the :file:`/etc/bnfos.conf` (mainly if you changed the IP address)::

   bnfos --scan -x -h <berofos ip>

Now that your berofos has proper network configuration and an up to date firmware, you
might want to set a password on your berofos::

   bnfos --set apwd=<password> -f fos1
   bnfos --set pwd=1 -f fos1

You must then edit the :file:`/etc/bnfos.conf` and replace the login line to something like::

   login = admin:<password>

Next, configure your berofos for it to work correctly with the XiVO HA::

   bnfos --set wdog=0 -f fos1
   bnfos --set wdogdef=0 -f fos1
   bnfos --set scenario=0 -f fos1
   bnfos --set mode=1 -f fos1
   bnfos --set modedef=1 -f fos1

This, among other things, disable the watchdog. The switching from one relay mode to the other will
be done by the XiVO slave node once it detects the master node is down, and vice-versa.

Finally, you can make sure everything works fine by running the xivo-berofos command::

   xivo-berofos master

The green LEDs on your berofos should be lighted on ports A and B.


Connection
----------

Two XiVOs
^^^^^^^^^

Here's how to connect the ISDN lines between your berofos with:

* two XiVOs in high availability

In this configuration you can protect **up two 4** ISDN lines. If more than 4 ISDN lines to protect,
you must set up a `Multiple berofos`_ configuration.

Here's an example with 4 ISDN lines coming from your telephony provider::

   ISDN lines (provider)
     | | | |
     | | | |
   +---------------------------------------------+
   |    A           B           C           D    |
   | 1|2|3|4     1|2|3|4     1|2|3|4     1|2|3|4 |
   +---------------------------------------------+
                 | | | |                 | | | |
                 | | | |                 | | | |
               +--------+              +--------+
               | xivo-1 |              | xivo-2 |
               +--------+              +--------+


Two XiVOs  and one PBX
^^^^^^^^^^^^^^^^^^^^^^

Here's how to connect your berofos with:

* two XiVOs in high availability,
* one PBX.

In this configuration you can protect **up two 2** ISDN lines. If more than 2 ISDN lines to protect,
you must set up a `Multiple berofos`_ configuration. 

Logical view::

                   +--------+                            +-----+
   -- Provider ----| xivo-1 | -- ISDN Interconnection  --| PBX | -- Phones
                   +--------+                            +-----+
                     | xivo-2 |
                     +--------+

This example shows the case where there are 2 ISDN lines coming from your telephony provider::

   ISDN lines (provider)
     | |
     | |
   +------------------------------------------------------+
   |    A               B            C           D        |
   | 1|2|3|4         1|2   3|4      1|2|3|4     1|2   3|4 |
   +------------------------------------------------------+
         | |     CPE | |   | | NET          CPE | |   | | NET
         | |   spans | |   | | spans      spans | |   | | spans
         | |       +----------+              +------------+
         | |       |  xivo-1  |              |   xivo-2   |
         | |       +----------+              +------------+
         | |
         | |
       +------+
       | PBX  |
       +------+


One XiVO and one PBX
^^^^^^^^^^^^^^^^^^^^

This case is not currently supported. You'll find a workaround in the `known bugs and limitation`_ section.

.. _known bugs and limitation: http://documentation.xivo.fr/production/introduction/introduction.html#berofos-integration-with-pbx


Multiple berofos
----------------

It's possible to use more than 1 berofos with XiVO.

For each supplementary berofos you want to use, you must first configure it properly
like you did for the first one. The only difference is that you need to add a berofos
declaration to the :file:`/etc/bnfos.conf` file instead of creating/overwriting the
file. Here's an example of a valid config file for 2 berofos::

    [fos1]
    mac = 00:19:32:00:12:1D
    host = 10.100.0.201
    login = admin:foobar

    [fos2]
    mac = 00:11:22:33:44:55
    host = 10.100.0.202
    login = admin:barfoo

.. warning::
   berofos name must follow the pattern ``fosX`` where X is a number starting with 1,
   then 2, etc. The ``bnfos`` tool won't work properly if it's not the case.


Operation
=========

When your XiVO switch the relay mode of your berofos, it logs the event in the
:file:`/var/log/syslog` file.


Default mode
============

Note that when the berofos is off, the A and D ports are connected together. This
behavior is not customizable.


Uninstallation
==============

It is important to remove the :file:`/etc/bnfos.conf` file on the slave node when you don't
want to use anymore your berofos with your XiVOs.


Reset the Berofos
=================

You can reset the berofos configuration :

#. Power on the berofos,
#. When red and green LEDs are still lit, press & hold the black button,
#. Release it when the red LEDs of the D port start blinking fast
#. Reboot the beronet, it should have lost its configuration.

External links
==============

* `Install BeroFos (in French) <https://wiki.xivo.fr/index.php/XiVO_1.1-Gallifrey/Install_BeroFos>`_
* `berofos user manual <http://www.beronet.com/downloads/docs/berofos/berofos_user_manual.pdf>`_
