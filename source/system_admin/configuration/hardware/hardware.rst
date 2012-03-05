***************
Server/Hardware
***************

Load the correct DAHDI modules
==============================

You can see which cards are detected by launching ''dahdi_hardware'':: 

 dahdi_hardware 
 pci:0000:05:0d.0     wcb4xxp+     d161:b410 Digium Wildcard B410P
 pci:0000:05:0e.0     wct4xxp+     d161:0205 Wildcard TE205P (4th Gen)

Comment out all the unused modules in ''/etc/dahdi/modules'' 

Then, restart dahdi (you need to stop asterisk if you want to stop dahdi)::

 /etc/init.d/monit stop
 /etc/init.d/asterisk stop
 /etc/init.d/dahdi stop
 /etc/init.d/dahdi start


BRI card configuration
======================

Verifications
-------------

Verify that the ''wcb4xxp'' module is uncommented in ''/etc/dahdi/modules''.

If it wasn't, do again the step #Load the correct DAHDI modules

Generate DAHDI configuration
----------------------------

`dahdi_genconf`

.. warning:: it will erase all existing configuration !

Configure
---------

Modify the ''/etc/asterisk/dahdi-channels.conf'' file :

* by removing the lines like::

   context = default
   group = 63

* Change the context lines if needed,
* The ''signaling'' should be one of ''{bri_net,bri_cpe,bri_net_ptmp,bri_cpe_ptmp}''.


PRI card configuration
======================

Verifications
-------------

Verify that one of the ''{wct1xxp,wcte11xp,wcte12xp,wct4xxp}'' module is uncommented in 
''/etc/dahdi/modules'' depending on the card you installed in your server.

If it wasn't, do again the step #Load the correct DAHDI modules


Generate DAHDI configuration
----------------------------

`dahdi_genconf`

.. warning:: it will erase all existing configuration !


Configure
---------
* Modify the ''/etc/dahdi/system.conf'' :

 * Check the span numbering,
 * If needed change the clock source,
 * Usually (at least in France) you should remove the ''crc4'',

* Modify the ''/etc/asterisk/dahdi-channels.conf'' file :

 * by removing the unused lines like::
 
     context = default
     group = 63
  
 * Change the context lines if needed,
 * The ''signaling'' should be one of ''{pri_net,pri_cpe}''.


Echo-canceller Module
^^^^^^^^^^^^^^^^^^^^^

If your card has an echo canceller module you need to install the firmware. 
This can be achieved via the ''xivo-fetchfw'' tool : 

'''Know which firmware you need :'''

The simplest way is to restart dahdi and then to lookup in the dmesg which 
firmware does DAHDI request at startup : 
 
.. code-block:: none

   dmesg |grep firmware
   [    7.781192] wct4xxp 0000:05:0e.0: firmware: requesting dahdi-fw-oct6114-064.bin


Otherwise you can also issue (with DAHDI >= 2.5.0) the ''cat /proc/dahdi/1'' command 
(assuming that the span 1 is a PRI port) and you should see lines containing ''EC: VPMOCT64'' : 
 

.. code-block:: none

   cat /proc/dahdi/1 
   Span 1: TE2/0/1 "T2XXP (PCI) Card 0 Span 1" HDB3/CCS ClockSource 
   
   1 TE2/0/1/1 Clear (In use) (EC: VPMOCT064 - INACTIVE)
   .....................................................


'''Use ''xivo-fetchfw'' : '''

You can search for ''digium'' occurences in the available packages :
 xivo-fetchfw -Ss digium

You can install the package named ''digium-oct6114-064'' :
 xivo-fetchfw -S digium-oct6114-064

Get help :
 xivo-fetchfw -h

Get help on a specific operation :
 xivo-fetchfw -h -S


Sync cable
^^^^^^^^^^

You can link several PRI Digium card between themselves with a sync cable to 
have the share the exact same clock.

If you do this, you need to load the DAHDI module with the ''timingcable=1'' option.

Create '''/etc/modprobe.d/xivo-timingcable''' file and insert line :
 options <module> timingcable=1

Where <module> is the DAHDI module name of your card (e.g. wct4xxp for a TE205P).


Analog card configuration
=========================

Verifications
-------------
Verify that one of the ''{wctdm,wctdm24xxp}'' module is uncommented in ''/etc/dahdi/modules'' 
depending on the card you installed in your server.

If it wasn't, do again the step #Load the correct DAHDI modules


Generate DAHDI configuration
----------------------------

`dahdi_genconf`

.. warning:: it will erase all existing configuration !


Configure
---------

With FXS modules :

Create file '''/etc/modprobe.d/xivo-tdm''' : 
 options '''<module>''' fastringer=1 boostringer=1
 
Where <module> is the DAHDI module name of your card (e.g. wctdm for a TDM400P).

With FXO modules:

Create file '''/etc/modprobe.d/xivo-tdm''' :
 options '''<module>''' opermode=FRANCE
 
Where <module> is the DAHDI module name of your card (e.g. wctdm for a TDM400P).

1. Modify the ''/etc/dahdi/system.conf'' :
2. Check the span numbering,
3. Modify the ''/etc/asterisk/dahdi-channels.conf'' file :

  * by removing the unused lines like::
  
     context = default
     group = 63 
  * Change the context lines if needed,


Apply configuration
===================

When done, you have to restart asterisk and dahdi ::

   /etc/init.d/monit stop
   /etc/init.d/asterisk stop
   /etc/init.d/dahdi stop
   /etc/init.d/dahdi start
   /etc/init.d/asterisk start
   /etc/init.d/monit start


Check IRQ misses
================

It's always useful to verify if there isn't any ''missed IRQ'' problem with the cards.

Check :
 cat /proc/dahdi/<numero de span>

If the ''IRQ misses'' counter increments, it's not good::

   cat /proc/dahdi/1
   Span 1: WCTDM/0 "Wildcard TDM800P Board 1" (MASTER)
   IRQ misses: 1762187
     1 WCTDM/0/0 FXOKS (In use) 
     2 WCTDM/0/1 FXOKS (In use) 
     3 WCTDM/0/2 FXOKS (In use) 
     4 WCTDM/0/3 FXOKS (In use)

Digium gives some hints in their ''Knowledge Base'' here : http://kb.digium.com/entry/1/63/

PRI Digium cards needs 1000 interuption per seconds. If the système cannot supply them, 
it increment the IRQ missed counter.

As indicated in Digium ''KB'' you should avoid shared IRQ with other equipments (like HD or NIC interfaces).


Voice Compression Card configuration
====================================

Here's how to install a Digium TC400M card (used for G.729a and/or G.723.1 codecs) :

* install the card firmware : <pre> xivo-fetchfw -S digium-tc400m </pre>
* comment out the line below in ''/etc/asterisk/modules.conf'' : <pre>noload = codec_dahdi.so </pre>
* restart asterisk : <pre>/etc/init.d/asterisk restart</pre>
* depending on the codec you want to transcode, you modify the ''mode'' parameter of the module by creating 
  a file in ''/etc/modprobe.d/''. This parameter can take the following value :
  
 * mode = mixed : this the default value which activates transcoding for 92 channels 
   in G.729a or G.723.1 (5.3 Kbit and 6.3 Kbit)
 * mode = g729 : this option activates transcoding for 120 channels in G.729a
 * mode = g723 : this option activates transcoding for 92 channels in G.723.1 (5.3 Kbit et 6.3 Kbit)
 
Example :

.. code-block:: none

   cat << EOF > /etc/modprobe.d/xivo-transcode
   options wctc4xxp mode=g729
   EOF
   
restart asterisk::
   
   /etc/init.d/monit stop
   /etc/init.d/asterisk stop
   /etc/init.d/dahdi stop
   /etc/init.d/dahdi start
   /etc/init.d/asterisk start
   /etc/init.d/monit start

'''you can verify''' that the card is correctly seen by asterisk with the ''transcoder show'' CLI command - this command should show the encoders/decoders registered by the TC400 card :
   

.. code-block:: none

   *CLI> transcoder show
   0/0 encoders/decoders of 120 channels are in use.

