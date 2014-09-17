.. _hwec_configuration:

Hardware Echo-cancellation
==========================

It is *recommended* to use telephony cards with an hardware echo-canceller module.

.. warning:: with **TE13X** cards, you **MUST** install the echo-canceller firmware.
    Otherwise the card won't work properly.


Hardware Echo-cancellation Module
---------------------------------

If you have an hardware echo-canceller module you **HAVE TO** install its firmware.
This can be achieved via the ``xivo-fetchfw`` tool :

* Know which firmware you need :

The simplest way is to restart dahdi and then to lookup in the dmesg which
firmware does DAHDI request at startup::

   dmesg |grep firmware
   [    7.781192] wct4xxp 0000:05:0e.0: firmware: requesting dahdi-fw-oct6114-064.bin

Otherwise you can also issue (with DAHDI >= 2.5.0) the ``cat /proc/dahdi/1`` command
(assuming that the span 1 is a PRI port) and you should see lines containing something like
``EC: VPMOCT64`` which tells you the echo-canceller module you have::

   cat /proc/dahdi/1
   Span 1: TE2/0/1 "T2XXP (PCI) Card 0 Span 1" HDB3/CCS ClockSource

   1 TE2/0/1/1 Clear (In use) (EC: VPMOCT064 - INACTIVE)
   .....................................................

* Use xivo-fetchfw to find the name of the package :

You can search for ``digium`` occurences in the available packages::

   xivo-fetchfw search digium

* Install the package :

In our example, we install the package named ``digium-oct6114-064``::

   xivo-fetchfw install digium-oct6114-064


Get help on xivo-fetchfw::

   xivo-fetchfw -h


Activate the Hardware Echo-cancellation
---------------------------------------

To use the hardware echo-canceller of the card you must activate it in
:file:`/etc/asterisk/chan_dahdi.conf` file::

    echocancel = 1


Use the Hardware Echo-canceller for DTMF detection
--------------------------------------------------

If you have an hardware echo-canceller it can be used to detect the DTMF.

Create the file :file:`/etc/modprobe.d/xivo-hwec-dtmf.conf` with the following content (replace the
``<dahdi_module_name>`` word by the DAHDI module name)::

   options <dahdi_module_name> vpmdtmfsupport=1

Thus, for a Digium card which uses the ``wct4xxp`` module, the content of the file will be::

   options wct4xxp vpmdtmfsupport=1

.. note:: You MUST restart dahdi for the new configuration to be enabled

.. warning:: Don't forget the extension ``.conf`` for the filename.
    Otherwise it won't be taken into account.
