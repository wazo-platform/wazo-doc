.. _hwec_configuration:

**************************
Hardware Echo-cancellation
**************************

It is *recommended* to use telephony cards with an hardware echo-canceller module.

.. warning:: with **TE13x, TE23x and TE43x** cards, you **MUST** install the echo-canceller firmware.
    Otherwise the card won't work properly.


Know which firmware you need
============================

If you have an hardware echo-canceller module you **HAVE TO** install its firmware.

You first need to know which firmware you need.
The simplest way is to restart dahdi and then to lookup in the dmesg which
firmware does DAHDI request at startup::

   dmesg |grep firmware
   [    7.781192] wct4xxp 0000:05:0e.0: firmware: requesting dahdi-fw-oct6114-064.bin

In the example above you can see that the module ``wct4xxp`` requested the ``dahdi-fw-oct6114-064.bin``
firmware file.


Install the firmware
====================

You can install the firmware via the ``xivo-fetchfw`` utility.

#. Use xivo-fetchfw to find the name of the package. You can search for ``digium`` 
   occurences in the available packages::

    xivo-fetchfw search digium

#. Install the package. In our example, we install the package 
   named ``digium-oct6114-064``::

    xivo-fetchfw install digium-oct6114-064


Activate the Hardware Echo-cancellation
=======================================

To use the hardware echo-canceller of the card you must activate it in
:file:`/etc/asterisk/chan_dahdi.conf` file::

    echocancel = 1


Apply the configuration
=======================

To apply the configuration, restart the services::

  xivo-service restart


Next step
=========

The next step is to :ref:`configure your card <card_configuration>` according to the operator links.


Specific configuration
======================

This section describes some specific configuration. You should not follow them
unless you have a specific need.


Use the Hardware Echo-canceller for DTMF detection
--------------------------------------------------

If you have an hardware echo-canceller it can be used to detect the DTMF.

Create the file :file:`/etc/modprobe.d/xivo-hwec-dtmf.conf` with the following content (replace the
``DAHDI_MODULE_NAME`` word by the DAHDI module name)::

   options DAHDI_MODULE_NAME vpmdtmfsupport=1

Thus, for a Digium card which uses the ``wct4xxp`` module, the content of the file will be::

   options wct4xxp vpmdtmfsupport=1

.. note:: You MUST restart dahdi for the new configuration to be enabled

.. warning:: Don't forget the extension ``.conf`` for the filename.
    Otherwise it won't be taken into account.
