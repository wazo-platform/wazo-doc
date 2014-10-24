*************************
Analog card configuration
*************************

Verifications
=============

Verify that one of the ``{wctdm,wctdm24xxp}`` module is uncommented in :file:`/etc/dahdi/modules`
depending on the card you installed in your server.

If it wasn't, do again the step :ref:`load_dahdi_modules`

.. note:: Analog cards work with card module. You must add the appropriate card module
  to your analog card. Either:

    * an FXS module (for analog equipment - phones, ...),
    * an FXO module (for analog line)


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

See detailed explanations of this file in the :ref:`system_conf` section.

Below is **an example** for a typical FXS analog line span::

  # Span 2: WCTDM/4 "Wildcard TDM400P REV I Board 5"
  fxoks=32
  echocanceller=mg2,32


Asterisk dahdi-channels.conf configuration
------------------------------------------

Then you have to modify the :file:`/etc/asterisk/dahdi-channels.conf` file:

* remove the unused lines like::

    context = default
    group = 63

* change the ``context`` and ``callerid`` lines if needed,
* the ``signalling`` should be one of:

  * ``fxo_ks`` for **FXS** lines -yes it is the reverse
  * ``fxs_ks`` for **FXO** lines - yes it is the reverse

Below is **an example** for a typical french PRI line span::

  ; Span 2: WCTDM/4 "Wildcard TDM400P REV I Board 5"
  signalling=fxo_ks
  callerid="Channel 32" <4032>
  mailbox=4032
  group=5
  context=default
  channel => 32


Next step
=========

Now that you have configured your PRI card:

#. you must check if you need to follow one of the :ref:`analog_card_specific_conf` sections below,
#. then, if you have another type of card to configure, you can go back to the :ref:`configure your card <card_configuration>` section,
#. if you have configured all your card you have to configure the :ref:`interco_dahdi_conf` in the web interface.


.. _analog_card_specific_conf:

Specific configuration
======================

FXS modules
-----------

If you use **FXS** modules you should create the file :file:`/etc/modprobe.d/xivo-tdm` and insert the line::

   options DAHDI_MODULE_NAME fastringer=1 boostringer=1

Where DAHDI_MODULE_NAME is the DAHDI module name of your card (e.g. wctdm for a TDM400P).


FXO modules
-----------

If you use **FXO** modules you should create file :file:`/etc/modprobe.d/xivo-tdm`::

   options DAHDI_MODULE_NAME opermode=FRANCE

Where DAHDI_MODULE_NAME is the DAHDI module name of your card (e.g. wctdm for a TDM400P).

