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
