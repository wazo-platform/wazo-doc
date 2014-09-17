PRI card configuration
======================

Verifications
-------------

Verify that one of the ``{wct1xxp,wcte11xp,wcte12xp,wcte13xp,wct4xxp}`` module is uncommented in
:file:`/etc/dahdi/modules` depending on the card you installed in your server.

If it wasn't, do again the step :ref:`load_dahdi_modules`

.. warning:: **TE13XP** cards :

    * these cards need a specific dahdi module configuration. See :ref:`load_dahdi_modules` paragraph,
    * you **MUST** install the correct echo-canceller firmware to be able to use these cards. See :ref:`hwec_configuration` paragraph.

Generate DAHDI configuration
----------------------------

Issue the command::

  dahdi_genconf

.. warning:: it will erase all existing configuration in :file:`/etc/dahdi/system.conf`
  and :file:`/etc/asterisk/dahdi-channels.conf` files !


Configure
---------

* Modify the :file:`/etc/dahdi/system.conf` :

 * Check the span numbering,
 * If needed change the clock source,
 * Usually (at least in France) you should remove the ``crc4``,

* Modify the :file:`/etc/asterisk/dahdi-channels.conf` file :

 * remove the unused lines like::

     context = default
     group = 63

 * Change the ``context`` lines if needed,
 * The ``signaling`` should be one of ``{pri_net,pri_cpe}``.


.. _sync_cable:

Sync cable
^^^^^^^^^^

You can link several PRI Digium card between themselves with a sync cable to
share the exact same clock.

If you do this, you need to:

* use the coding wheel on the Digium cards to give them an order of recognition in DAHDI/Asterisk (see Digium_telephony_cards_support_),
* daisy-chain the cards with a sync cable (see Digium_telephony_cards_support_),
* load the DAHDI module with the ``timingcable=1`` option.

Create :file:`/etc/modprobe.d/xivo-timingcable.conf` file and insert the line::

   options <module> timingcable=1

Where <module> is the DAHDI module name of your card (e.g. wct4xxp for a TE205P).


.. _Digium_telephony_cards_support: http://www.digium.com/en/support/telephony-cards

