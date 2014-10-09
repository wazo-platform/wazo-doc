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
* the ``signaling`` should be one of:

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
    signalling = bri_cpe    ; use 'bri_cpe' signaling
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

*Work In Progress*
