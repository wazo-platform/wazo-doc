Analog card configuration
=========================

Verifications
-------------

Verify that one of the ``{wctdm,wctdm24xxp}`` module is uncommented in :file:`/etc/dahdi/modules`
depending on the card you installed in your server.

If it wasn't, do again the step :ref:`load_dahdi_modules`


Generate DAHDI configuration
----------------------------

Issue the command::

  dahdi_genconf

.. warning:: it will erase all existing configuration in :file:`/etc/dahdi/system.conf`
  and :file:`/etc/asterisk/dahdi-channels.conf` files !


Configure
---------

* With **FXS** modules :

Create file :file:`/etc/modprobe.d/xivo-tdm`::

   options <module> fastringer=1 boostringer=1

Where <module> is the DAHDI module name of your card (e.g. wctdm for a TDM400P).

* With **FXO** modules:

Create file :file:`/etc/modprobe.d/xivo-tdm`::

   options <module> opermode=FRANCE

Where <module> is the DAHDI module name of your card (e.g. wctdm for a TDM400P).

#. Modify the :file:`/etc/dahdi/system.conf` :
#. Check the span numbering,
#. Modify the :file:`/etc/asterisk/dahdi-channels.conf` file :

  * remove the unused lines like::

     context = default
     group = 63

  * Change the ``context`` lines if needed
