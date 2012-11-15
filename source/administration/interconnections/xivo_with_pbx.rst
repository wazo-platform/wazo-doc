.. index:: interconnections

*********************************************
Interconnect a XiVO to a PBX via an ISDN link
*********************************************

XiVO will play the role of gateway for the PBX. It will bring new features to the PBX like voicemail, conference, etc.
Interconnect a XiVO to a PBX allows to migrate slowly users and features.

.. figure:: images/xivo-pbx.png
   :align: center
   :scale: 65%

   Interconnect a XiVO to a PBX


Context choice
--------------

Use to the maximum a couple of contexts from / to by interconnection

* ISDN Provider = "to-extern" and "from-extern"
* ISDN link with PBX = "to-pbx" and "from-pbx"


Hardware
--------

General uses
============

You must have an ISDN card able to support both the ISDN provider and ISDN links with PBX.


.. note::

    If you have two ISDN provider links to PBX, XiVO should have a card with 4 spans : two to the provider, and two to the PBX.

If you use two cards
====================

If you have to use two cards, you have to :

* Use a cable for clock synchronization between the cards
* Configure the "wheel" to define the cards order in the system. The ISDN links used by XiVO to synchronize have to be pluged on the card number one!

Please refer to the section :ref:`Sync cable <sync_cable>`

Configuration
-------------

You have now to configure two files :

1. :file:`/etc/dahdi/system.conf`

2. :file:`/etc/asterisk/dahdi-channels.conf`

system.conf
===========

Horloge
^^^^^^^

.. warning:: Consider the configuration of the clock!

    * Provider side : ISDN links recover sync clock provider
    * PBX side : ISDN links provide sync PBX


* 1 span te provider side (to receive clock)
* 0 span nt PBX side (to provide clock)

To configure :file:`/etc/dahdi/system.conf` please refer to the section :ref:`system.conf <system_conf>`


Exemple
^^^^^^^

Below an example for interconnection with two ISDN provider::

    # Span 1: TE4/0/1 "TE4XXP (PCI) Card 0 Span 1" (MASTER)
    span=1,1,0,ccs,hdb3
    # termtype: te
    bchan=1-15,17-31
    dchan=16
    echocanceller=mg2,1-15,17-31

    # Span 2: TE4/0/2 "TE4XXP (PCI) Card 0 Span 2" 
    span=2,2,0,ccs,hdb3
    # termtype: te
    bchan=32-46,48-62
    dchan=47
    echocanceller=mg2,32-46,48-62

    # Span 3: TE4/0/3 "TE4XXP (PCI) Card 0 Span 3" 
    span=3,0,0,ccs,hdb3
    # termtype: nt
    bchan=63-77,79-93
    dchan=78
    echocanceller=mg2,63-77,79-93

    # Span 4: TE4/0/4 "TE4XXP (PCI) Card 0 Span 4" 
    span=4,0,0,ccs,hdb3
    # termtype: nt
    bchan=94-108,110-124
    dchan=109
    echocanceller=mg2,94-108,110-124


dahdi-channels.conf
===================

Configuraton
^^^^^^^^^^^^

Modify the file :file:`/etc/asterisk/dahdi-channels.conf` ::

    group : g0 provider side, g2 PBX side
    context : from-extern or from-pabx
    signalling : pri_cpe provider side, pri_net PBX side


.. warning:: On certains destinations, some PBX use an overlapdialing (digits sent one by one). In this case, we have to activate a parameter on the spans concerned :

    overlapdial = incoming

This can be see with "pri intense debug" 

Below an example to dahdi-channels.conf. Be careful to three parameters :

* group
* context
* signalling

Example
^^^^^^^
::
 
    ; Span 1: TE4/0/1 "TE4XXP (PCI) Card 0 Span 1" (MASTER) 
    group=0,11
    context=from-extern
    switchtype = euroisdn
    signalling = pri_cpe
    channel => 1-15,17-31

    ; Span 2: TE4/0/2 "TE4XXP (PCI) Card 0 Span 2" 
    group=0,12
    context=from-extern
    switchtype = euroisdn
    signalling = pri_cpe
    channel => 32-46,48-62

    ; Span 3: TE4/0/3 "TE2XXP (PCI) Card 0 Span 3" 
    group=2,13
    context=from-pabx
    overlapdial=incoming
    switchtype = euroisdn
    signalling = pri_net
    channel => 63-77,79-93

    ; Span 4: TE4/0/4 "T4XXP (PCI) Card 0 Span 4" 
    group=2,14
    context=from-pabx
    overlapdial=incoming
    switchtype = euroisdn
    signalling = pri_net
    channel => 94-108,110-124


Passthru function
====================

Create the "from-pabx" context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Create a file named xxxxx.conf (where xxxxx is the customer name) in the directory :file:`/etc/asterisk/extensions_extra.d/`. 
* Add the following lines in the file::

    [from-pabx]
    exten = _X.,1,NoOp(« Appel depuis Pabx »)
    exten = _X.,n,goto(default,${EXTEN},1) 

This dialplan allows to route incoming calls from the PBX in the default context of XiVO.
Then, calls are routed :

* Or to a SIP phone (in default context)
* Or to the outgoing (to-extern context included in default context)

Create the "to-extern" context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the webi, create a context named "to-pabx" : ::

    Name : to-pabx
    Display Name : to-pabx
    Context type : Outcall
    Include sub-contexts : No context inclusion

This context allows to route incoming calls from the XiVO to the PBX.

.. figure:: images/context-to-extern.png
   :align: center
   :scale: 85%

   to-extern context


Create incoming calls
^^^^^^^^^^^^^^^^^^^^^

In our example, incoming calls on spans 1 and 3 (spans pluged to the provider) are routed by from-extern context.
We are going to create a default route to redirect incoming calls to the PBX.

Create an incoming call as below : ::

    DID : XXXX (according to the number of digits sent by the provider)
    Context : Incoming calls
    Destination : Customized
    Command : Goto(to-pabx,${XIVO_DSTNUM},1)

.. figure:: images/incoming_call.png
   :align: center
   :scale: 85%

   Incoming call XXXX


Create the interconnections
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You have to create two interconnections :

* provider side : dahdi/g0
* PBX side : dahdi/g1

In the menu :menuselection:`Services --> IPBX --> Trunk management --> Customized` page ::

    Name : t2-operateur
    Interface : dahdi/g0
    Contexte : to-extern

.. figure:: images/interco1.png
   :align: center
   :scale: 85%

   Customized interconnection


The second interconnection ::

    Name : t2-pabx
    Interface : dahdi/g2
    Context : to-pabx

.. figure:: images/interco2.png
   :align: center
   :scale: 85%

   Customized interconnection


Create outgoing calls
^^^^^^^^^^^^^^^^^^^^^

You must create two rules of outgoing calls in the menu :menuselection:`Services --> IPBX --> Call management --> Outgoing calls` page

1. Redirect calls to the PBX ::

    Name : fsc-pabx
    Context : to-pabx
    Trunks : choose the "t2-pabx" interconnection

.. figure:: images/outgoing_call_general.png
   :align: center
   :scale: 80%

   Outgoing call


In the extensions tab ::

    exten : XXXX

.. figure:: images/outgoing_call_exten.png
   :align: center
   :scale: 75%

   Outgoing call

2. Rename the rule "default" in "fsc-operateur"::

    Name : fsc-operateur
    Context : to-extern
    Trunks : choose the "t2-operateur" interconnection

In the extensions tab::

    exten = X.
