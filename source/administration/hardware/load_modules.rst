.. _load_dahdi_modules:

Load the correct DAHDI modules
==============================

.. highlight:: none

* Know which card is in your server:

You can see which cards are detected by issuing the ``dahdi_hardware`` command::

   dahdi_hardware
   pci:0000:05:0d.0     wcb4xxp+     d161:b410 Digium Wildcard B410P
   pci:0000:05:0e.0     wct4xxp+     d161:0205 Wildcard TE205P (4th Gen)

* Then you have to create the file :file:`/etc/dahdi/modules` according to your hardware. You can
  copy and edit the sample file from :file:`/usr/share/dahdi/modules.sample`, leaving only the
  needed modules.

For example, if you have one B410P and one TE205P, your :file:`/etc/dahdi/modules` file should
contain the following lines::

    wcb4xxp
    wct4xxp

* **If this is a TE13X card** (``wcte13xp`` module) you **MUST** create a configuration file to set
  the line mode as E1 (or T1).

Contrarily to other cards there is no jumper to change the line mode. The configuration below
sets the card in E1 mode::

    cat << EOF > /etc/modprobe.d/xivo-wcte13xp.conf
    # set wcte13xp cards in E1/T2 mode
    options wcte13xp default_linemode=e1
    EOF

* Then, restart dahdi::

   xivo-service restart
