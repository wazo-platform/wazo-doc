***************
Server/Hardware
***************

This section describes how to configure the telephony hardware on a XiVO server.

.. note:: Currently XiVO support only Digium Telephony Interface cards

The configration process is the following :

#. Load the right DAHDI modules,
#. Configure the echo-canceller,
#. Configure your card and the associated span in asterisk.

At the end of this page you will also find some general notes and DAHDI.


.. _load_dahdi_modules:

Load the correct DAHDI modules
==============================

.. highlight:: none

* Know which card is in your server: 

You can see which cards are detected by issuing the ``dahdi_hardware`` command::

   dahdi_hardware
   pci:0000:05:0d.0     wcb4xxp+     d161:b410 Digium Wildcard B410P
   pci:0000:05:0e.0     wct4xxp+     d161:0205 Wildcard TE205P (4th Gen)

* Then you have to comment all the unused modules in :file:`/etc/dahdi/modules`.

For example, if you have one B410P and one TE205P you should comment every modules in :file:`/etc/dahdi/modules` except::

    wcb4xxp
    wct4xxp

* **If this is a TE13X card** (``wcte13xp`` module) you **MUST** create a configuration file to set the line mode
  as E1 (or T1).

Contrarily to other cards there is no jumper to change the line mode. The configuration below
sets the card in E1 mode::

    cat << EOF > /etc/modprobe.d/xivo-wcte13xp.conf
    # set wcte13xp cards in E1/T2 mode
    options wcte13xp default_linemode=e1
    EOF

* Then, restart dahdi::

   xivo-service restart


Hardware Echo-cancellation
==========================

It is *recommended* to use telephony cards with an hardware echo-canceller module.


Hardware Echo-cancellation Module
---------------------------------

If you have an hardware echo-canceller module you have to install its firmware.
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

   option <dahdi_module_name> vpmdtmfsupport=1

Thus, for a Digium card which uses the ``wct4xxp`` module, the content of the file will be::

   option wct4xxp vpmdtmfsupport=1

.. note:: You MUST restart dahdi for the new configuration to be enabled

.. warning:: Don't forget the extension ``.conf`` for the filename.
    Otherwise it won't be taken into account.


BRI card configuration
======================

Verifications
-------------

Verify that the ``wcb4xxp`` module is uncommented in :file:`/etc/dahdi/modules`.

If it wasn't, do again the step :ref:`load_dahdi_modules`.

Generate DAHDI configuration
----------------------------

Issue the command::
  
  dahdi_genconf

.. warning:: it will erase all existing configuration in :file:`/etc/dahdi/system.conf`
  and :file:`/etc/asterisk/dahdi-channels.conf` files !


Configure
---------

* Modify the :file:`/etc/dahdi/system.conf` file:

 * Check the span numbering,
 * If needed change the clock source,
 * Usually (at least in France) you should remove the ``crc4``,

 Following is **an example** :file:`/etc/dahdi/system.conf` file for a B410P 4 ports for French network
 (check the comments and see the :ref:`system_conf` section !)::

    # Span 1: B4/0/1 "B4XXP (PCI) Card 0 Span 1" (MASTER) RED 
    # span=1 (this is the first span), 
    #      1 (this is the primary clock source)
    #      0 (-)
    #      ccs (use ccs framing)
    #      ami (use ami coding )
    span=1,1,0,ccs,ami 
    # termtype: te
    bchan=1-2
    hardhdlc=3
    echocanceller=mg2,1-2
    
    # Span 2: B4/0/2 "B4XXP (PCI) Card 0 Span 2" RED 
    span=2,2,0,ccs,ami
    # termtype: te
    bchan=4-5
    hardhdlc=6
    echocanceller=mg2,4-5

    # Span 3: B4/0/3 "B4XXP (PCI) Card 0 Span 3" RED 
    span=3,3,0,ccs,ami
    # termtype: te
    bchan=7-8
    hardhdlc=9
    echocanceller=mg2,7-8

    # Span 4: B4/0/4 "B4XXP (PCI) Card 0 Span 4" RED 
    # span=4 (this is the fourth span), 
    #      0 (won't use this span as a sync source)
    #      0 (-)
    #      ccs (use ccs framing)
    #      ami (use ami coding )
    span=4,0,0,ccs,ami
    # termtype: nt
    bchan=10-11
    hardhdlc=12
    echocanceller=mg2,10-11


* Modify the :file:`/etc/asterisk/dahdi-channels.conf` file :

 * remove the unused lines like::
 
     context = default
     group = 63
  
 * Change the ``context`` lines if needed,
 * The ``signaling`` should be one of ``{bri_net,bri_cpe,bri_net_ptmp,bri_cpe_ptmp}``.

 Following is **an example** :file:`/etc/asterisk/dahdi-channels.conf` file for a B410P 4 ports for French network
 (check the comments and the :ref:`asterisk_dahdi_channel_conf` section !)::

    ; Span 1: B4/0/1 "B4XXP (PCI) Card 0 Span 1" (MASTER) RED
    group=0,11              ; belongs to group 0 and 11
    context=from-extern     ; incoming call to this span will be sent in 'from-extern' context
    switchtype = euroisdn
    signalling = bri_cpe    ; use 'bri_cpe' signaling
    channel => 1-2          ; the above configuration applies to channels 1 and 2
    
    ; Span 2: B4/0/2 "B4XXP (PCI) Card 0 Span 2" RED
    group=0,12
    context=from-extern
    switchtype = euroisdn
    signalling = bri_cpe
    channel => 4-5
    
    ; Span 3: B4/0/3 "B4XXP (PCI) Card 0 Span 3" RED
    group=0,13
    context=from-extern
    switchtype = euroisdn
    signalling = bri_cpe
    channel => 7-8
    
    ; Span 4: B4/0/4 "B4XXP (PCI) Card 0 Span 4" RED
    group=1,14              ; belongs to groups 1 and 14
    context=default         ; incoming call to this span will be sent in 'defaul' context
    switchtype = euroisdn
    signalling = bri_net    ; use 'bri_net' signaling
    channel => 10-11        ; the above configuration applies to channels 10 and 11


Special cases
-------------

Here are some special cases where you might need to modify the default options : 

* if your telecom operator brings layer 1 down when the line is idle, you should add the following 
  option in :file:`/etc/asterisk/chan_dahdi.conf` and restart asterisk (works with XiVO 12.20 and 
  above)::

     layer2_persistence=keep_up


PRI card configuration
======================

Verifications
-------------

Verify that one of the ``{wct1xxp,wcte11xp,wcte12xp,wcte13xp,wct4xxp}`` module is uncommented in
:file:`/etc/dahdi/modules` depending on the card you installed in your server.

If it wasn't, do again the step :ref:`load_dahdi_modules`

.. warning:: Be aware that TE3XP cards' dahdi module need a specific configuration.
    See :ref:`load_dahdi_modules` paragraph.

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


Voice Compression Card configuration
====================================

Here's how to install a Digium TC400M card (used for G.729a and/or G.723.1 codecs) :

* Verify that the ``wctc4xxp`` module is uncommented in :file:`/etc/dahdi/modules`.
  If it wasn't, do again the step :ref:`load_dahdi_modules`.

* install the card firmware::

    xivo-fetchfw install digium-tc400m

* comment out the following line in :file:`/etc/asterisk/modules.conf`::

    noload = codec_dahdi.so

* restart asterisk::

    /etc/init.d/asterisk restart

* depending on the codec you want to transcode, you can modify the ``mode`` parameter of the module by
  creating a file in :file:`/etc/modprobe.d/`. This parameter can take the following value :

 * mode = mixed : this the default value which activates transcoding for 92 channels
   in G.729a or G.723.1 (5.3 Kbit and 6.3 Kbit)
 * mode = g729 : this option activates transcoding for 120 channels in G.729a
 * mode = g723 : this option activates transcoding for 92 channels in G.723.1 (5.3 Kbit et 6.3 Kbit)

Example::

   cat << EOF > /etc/modprobe.d/xivo-transcode.conf
   options wctc4xxp mode=g729
   EOF
   
After having applied the configuration (see `Apply configuration`_ section) you can verify that the
card is correctly seen by asterisk with the ``transcoder show`` CLI command - this command should show
the encoders/decoders registered by the TC400 card::

   *CLI> transcoder show
   0/0 encoders/decoders of 120 channels are in use.


Apply configuration
===================

When done, you have to restart asterisk and dahdi::

   /etc/init.d/monit stop
   /etc/init.d/asterisk stop
   /etc/init.d/dahdi stop
   /etc/init.d/dahdi start
   /etc/init.d/asterisk start
   /etc/init.d/monit start


Check IRQ misses
================

It's always useful to verify if there isn't any *missed IRQ* problem with the cards.

Check::

   cat /proc/dahdi/<span number>

If the *IRQ misses* counter increments, it's not good::

   cat /proc/dahdi/1
   Span 1: WCTDM/0 "Wildcard TDM800P Board 1" (MASTER)
   IRQ misses: 1762187
     1 WCTDM/0/0 FXOKS (In use) 
     2 WCTDM/0/1 FXOKS (In use) 
     3 WCTDM/0/2 FXOKS (In use) 
     4 WCTDM/0/3 FXOKS (In use)

Digium gives some hints in their *Knowledge Base* here : http://kb.digium.com/entry/1/63/

PRI Digium cards needs 1000 interuption per seconds. If the systeme cannot supply them,
it increment the IRQ missed counter.

As indicated in Digium *KB* you should avoid shared IRQ with other equipments (like HD or NIC interfaces).


Notes on configuration files
============================


.. _system_conf:

/etc/dahdi/system.conf
----------------------

A *span* is created for each card port. Below is an example of a standard E1 port::

   span=1,1,0,ccs,hdb3
   dchan=16
   bchan=1-15,17-31
   echocanceller=mg2,1-15,17-31

Each span has to be declared with the following information::

   span=<spannum>,<timing>,<LBO>,<framing>,<coding>[,crc4]

* ``spannum`` : corresponds to the span number. It starts to 1 and has to be incremented by 1 at each new span.
  This number MUST be unique.
* ``timing`` : describes the how this span will be considered regarding the synchronisation :

  * 0 : do not use this span as a synchronisation source,
  * 1 : use this span as the primary synchronisation source,
  * 2 : use this span as the secondary synchronisation source etc.

* ``LBO`` : 0 (not used)
* ``framing`` : correct values are ``ccs`` or ``cas``.
  For ISDN lines, ``ccs`` is used.
* ``coding`` : correct valus are ``hdb3`` or ``ami``.
  For example, ``hdb3`` is used for an E1 (PRI) link, whereas ``ami`` is used for T0 (french BRI) link.
* ``crc4`` : this is a framing option for PRI lines.
  For example it is rarely use in France.

Note that the ``dahdi_genconf`` command should usually give you the correct parameters (if you correctly set the cards
jumper). All these information should be checked with your operator.


/etc/asterisk/chan_dahdi.conf
-----------------------------

This file contains the general parameters of the DAHDI channel.
It is not generated via the ``dahdi_genconf`` command.


.. _asterisk_dahdi_channel_conf:

/etc/asterisk/dahdi-channels.conf
---------------------------------

This file contains the parameters of each channel.
It is generated via the ``dahdi_genconf`` command.
