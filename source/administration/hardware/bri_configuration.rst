**********************
BRI card configuration
**********************

Verifications
=============

Verify that the ``wcb4xxp`` module is uncommented in :file:`/etc/dahdi/modules`.

If it wasn't, do again the step :ref:`load_dahdi_modules`.

Generate DAHDI configuration
============================

Issue the command::

  dahdi_genconf

.. warning:: it will erase all existing configuration in :file:`/etc/dahdi/system.conf`
  and :file:`/etc/asterisk/dahdi-channels.conf` files !


Configure
=========

DAHDI system.conf configuration
-------------------------------

First step is to check :file:`/etc/dahdi/system.conf` file:

* check the span numbering,
* if needed change the clock source,

See detailed explanations of this file in the :ref:`system_conf` section.


Below is **an example** for a typical french BRI line span::

    # Span 1: B4/0/1 "B4XXP (PCI) Card 0 Span 1" (MASTER) RED
    span=1,1,0,ccs,ami
    # termtype: te
    bchan=1-2
    hardhdlc=3
    echocanceller=mg2,1-2


Asterisk dahdi-channels.conf configuration
------------------------------------------

Then you have to modify the :file:`/etc/asterisk/dahdi-channels.conf` file:

* remove the unused lines like::

     context = default
     group = 63

* change the ``context`` lines if needed,
* the ``signalling`` should be one of:

  * ``bri_net``
  * ``bri_cpe``
  * ``bri_net_ptmp``
  * ``bri_cpe_ptmp``

See some explanations of this file in the :ref:`asterisk_dahdi_channel_conf` section.


Below is **an example** for a typical french BRI line span::

    ; Span 1: B4/0/1 "B4XXP (PCI) Card 0 Span 1" (MASTER) RED
    group = 0,11              ; belongs to group 0 and 11
    context = from-extern     ; incoming call to this span will be sent in 'from-extern' context
    switchtype = euroisdn
    signalling = bri_cpe    ; use 'bri_cpe' signalling
    channel => 1-2          ; the above configuration applies to channels 1 and 2


Next step
=========

Now that you have configured your BRI card:

#. you must check if you need to follow one of the :ref:`bri_card_specific_conf` sections below,
#. then, if you have another type of card to configure, you can go back to the :ref:`configure your card <card_configuration>` section,
#. if you have configured all your card you have to configure the :ref:`interco_dahdi_conf` in the web interface.


.. _bri_card_specific_conf:

Specific configuration
======================

You will find below 3 configurations that we recommend for BRI lines.
These configurations were tested on different type of french BRI lines with success.

.. note:: The pre-requisites are:

  * XiVO >= 14.12,
  * Use per-port dahdi interconnection (see the :ref:`interco_dahdi_conf` section)


If you don't know which one to configure we recommend that you try each one after the other in this order:

#. :ref:`bri_card_ptmp_wol1l2`
#. :ref:`bri_card_ptmp_wl1l2`
#. :ref:`bri_card_ptp_wl1l2`


.. _bri_card_ptmp_wol1l2:

PTMP without layer1/layer2 persistence
--------------------------------------

In this mode we will configure asterisk and DAHDI:

* to use Point-to-Multipoint (PTMP) signalling,
* and to leave Layer1 and Layer2 DOWN

Follow theses steps to configure:

#. **Before** the line ``#include dahdi-channels.conf`` add, in file :file:`/etc/asterisk/chan_dahdi.conf`,
   the following lines::

     layer1_presence = ignore
     layer2_persistence = leave_down

#. In the file :file:`/etc/asterisk/dahdi-channels.conf` use ``bri_cpe_ptmp`` signalling::

     signalling = bri_cpe_ptmp

#. Create the file :file:`/etc/modprobe.d/xivo-wcb4xxp.conf` to deactivate the layer1 persistence::

    touch /etc/modprobe.d/xivo-wcb4xxp.conf

#. Fill it with the following content::

    options wcb4xxp persistentlayer1=0

#. Then, apply the configuration by restarting the services::

    xivo-service restart


.. note:: Expected behavior:

  * The `dahdi show status` command should show the BRI spans in *RED* status if there is no call,
  * For outgoing calls the layer1/layer2 should be brought back up by the XiVO (i.e. asterisk/chan_dahdi),
  * For incoming calls the layer1/layer2 should be brought back up by the operator,
  * You can consider that there is *a problem* only if incoming or outgoing calls are rejected.


.. _bri_card_ptmp_wl1l2:

PTMP with layer1/layer2 persistence
-----------------------------------

In this mode we will configure asterisk and DAHDI:

* to use Point-to-Multipoint (PTMP) signalling,
* and to keep Layer1 and Layer2 UP

Follow theses steps to configure:

#. **Before** the line ``#include dahdi-channels.conf`` add, in file :file:`/etc/asterisk/chan_dahdi.conf`,
   the following lines::

    layer1_presence = required
    layer2_persistence = keep_up

#. In the file :file:`/etc/asterisk/dahdi-channels.conf` use ``bri_cpe_ptmp`` signalling::

    signalling = bri_cpe_ptmp

#. If it exists, delete the file :file:`/etc/modprobe.d/xivo-wcb4xxp.conf`::

    rm /etc/modprobe.d/xivo-wcb4xxp.conf

#. Then, apply the configuration by restarting the services::

    xivo-service restart


.. note:: Expected behavior:

  * The `dahdi show status` command should show the BRI spans in **OK** status even if there is no call,
  * In asterisk CLI you may see the spans going Up/Down/Up : it is *a problem* only if incoming or
    outgoing calls are rejected.


.. _bri_card_ptp_wl1l2:

PTP with layer1/layer2 persistence
----------------------------------

In this mode we will configure asterisk and DAHDI:

* to use Point-to-Point (PTP) signalling,
* and use default behavior for Layer1 and Layer2.

Follow theses steps to configure:

#. In file :file:`/etc/asterisk/chan_dahdi.conf` remove all occurrences of
   ``layer1_presence`` and ``layer2_persistence`` options.

#. In the file :file:`/etc/asterisk/dahdi-channels.conf` use ``bri_cpe`` signalling::

    signalling = bri_cpe

#. If it exists, delete the file :file:`/etc/modprobe.d/xivo-wcb4xxp.conf`::

    rm /etc/modprobe.d/xivo-wcb4xxp.conf

#. Then, apply the configuration by restarting the services::

    xivo-service restart


.. note:: Expected behavior:

  * The `dahdi show status` command should show the BRI spans in **OK** status even if there is no call,
  * In asterisk CLI you should not see the spans going Up and Down : if it happens, it is *a problem* only if incoming or
    outgoing calls are rejected.

