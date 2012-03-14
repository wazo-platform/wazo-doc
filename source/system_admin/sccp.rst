***********************************
Skinny Call Control Protocol (SCCP)
***********************************

Introduction
------------

::

   SCCP (or skinny) is a stimulus protocol used to fully interact with Cisco phones.
   What is libsccp ? It's a channel driver written for Asterisk by Avencall based on the channel skinny.

   At the present moment, we are strictly focusing our effort on the Asterisk 1.8 branch which is a Long-Term-Support (LTS) release.

Contact
-------

::

   libsccp is actually developed and maintained by Nicolas Bouliane (nbouliane@avencall.com)
   If you need any help, have questions or want to give some help by providing patch or by testing code you can write me an email.

   For a more interactive chat, you can find me on irc.freenode.net on #xivo, my alias is acidfu.

Installation
------------

::

   git clone git://git.xivo.fr/official/xivo-libsccp.git
   cd xivo-libsccp/xivo-libsccp/
   autoreconf -fvi
   ./configure
   make
   cp ./src/.libs/libsccp.so /usr/lib/asterisk/modules/chan_sccp.so

Configuration
-------------

| example /etc/asterisk/sccp.conf:

::
 
   [general]
   bindaddr=10.97.8.5
   dateformat=D.M.Y

   keepalive=10
   authtimeout=10
   dialtimeout=3
   context=default

   [lines]

   [100]
   cid_num=100
   cid_name=Bob

   [devices]

   [SEP00164766A428]
   device=SEP00164766A428
   line=100
   voicemail=200

| **WARNING** ! The option 'context' is very important. If you get it wrong, you won't be able to call or receive call.
| If you are unsure in what context your extension is configured, you can do:

::

   nibskaro*CLI> dialplan show 107@
   [ Context 'xivo-callme' created by 'pbx_config' ]
     '_X.' =>          1. Gosub(xivo-pickup,0,1)                     [pbx_config]
                       2. While(1)                                   [pbx_config]
                       3. Playback(hello-world)                      [pbx_config]
                       4. Wait(2)                                    [pbx_config]
                       5. EndWhile()                                 [pbx_config]

   [ Context 'default' created by 'pbx_config' ]
     '107' =>          1. Dial(SCCP/107)                             [pbx_config]

   -= 2 extensions (6 priorities) in 2 contexts. =-


We see that the extention 107 is effectively configured in the context 'default'.

Features
--------

+-----------------------------+-----------+
| Receive call                | Supported |
+=============================+===========+
| Initiate call               | Yes       |
+-----------------------------+-----------+
| Hangup call                 | Yes       |
+-----------------------------+-----------+
| Transfer call               | Yes       |
+-----------------------------+-----------+
| Busy signal                 | Yes       |
+-----------------------------+-----------+
| Congestion Signal           | Yes       |
+-----------------------------+-----------+
| Autoanswer (Paging)         | Yes       |
+-----------------------------+-----------+
| Call forward                | Yes       |
+-----------------------------+-----------+
| Group pickup                | Not yet   |
+-----------------------------+-----------+
| Hotline (auto-provisioning) | Not yet   |
+-----------------------------+-----------+
| Multi-instance per line     | Not yet   |
+-----------------------------+-----------+
| Speed dial                  | Not yet   |
+-----------------------------+-----------+
| Multi line                  | Not yet   |
+-----------------------------+-----------+
| Direct RTP                  | Not yet   |
+-----------------------------+-----------+

Telephone
---------

+-------------+-----------+
| Device type | Supported |
+=============+===========+
| 7905        | Not Yet   |
+-------------+-----------+
| 7906        | Yes       |
+-------------+-----------+
| 7911        | Yes       |
+-------------+-----------+
| 7912        | Yes       |
+-------------+-----------+
| 7940        | Yes       |
+-------------+-----------+
| 7941        | Yes       |
+-------------+-----------+
| 7941GE      | Yes       |
+-------------+-----------+
| 7960        | Yes       |
+-------------+-----------+
| 7961        | Yes       |
+-------------+-----------+

CLI
---

The command line interface provide a way to interact with the different Asterisk modules, and in our case with the sccp channel driver (libsccp).

::

 nibskaro*CLI> sccp show version
 SCCP library 0.93alpha <nbouliane@avencall.com>
 nibskaro*CLI>

::

 nibskaro*CLI> sccp show config

 bindaddr = 10.97.8.5
 dateformat = D.M.Y
 keepalive = 10
 authtimeout = 10
 context = default
 
 Device: [SEP001122AABBCC]
 Line extension: <110> instance: (1)
 
 Device: [SEP001AA27ABBFC]
 Line extension: <109> instance: (1)
 
 Device: [SEP00175A4AA36D]
 Line extension: <108> instance: (1)
 
 Device: [SEP0023EBC64F92]
 Line extension: <107> instance: (1)
 
 Device: [SEP001AA289341B]
 Line extension: <106> instance: (1)
 
 Device: [SEP001AA289341A]
 Line extension: <105> instance: (1)
 
 Device: [SEP001AA289343B]
 Line extension: <101> instance: (2)
 Line extension: <103> instance: (1)
 
 Device: [SEPACA016FDF235]
 Line extension: <203> instance: (2)
 Line extension: <200> instance: (1)
 
 Device: [SEP00164766A428]
 Line extension: <102> instance: (1)
 
::
 
 nibskaro*CLI> sccp show devices 
 Device            Type     Reg.state
 ===============   ======   ==========
 SEP001122AABBCC   unknown  Unregistered
 SEP001AA27ABBFC   7912     Registered
 SEP00175A4AA36D   7941GE   Registered
 SEP0023EBC64F92   7961     Registered
 SEP001AA289341B   unknown  Unregistered
 SEP001AA289341A   7906     Unregistered
 SEP001AA289343B   unknown  Unregistered
 SEPACA016FDF235   7940     Registered
 SEP00164766A428   unknown  Unregistered

::

 nibskaro*CLI> sccp reset <device> [restart]
 Cause a SCCP device to reset itself, optionally with a full restart

FAQ
---

| Q. When is this *feature X* will be available ?
| A. The order in which we implement features is based on our client needs. Write us an email that clearly explain
|  your setup and what you would like to do and we will see what we can do. We don't provide any timeline.

| Q. I want to use the Page() application to call many phones at the same time.
| A. Here a Page() example for a one way call (half-duplex):

::

   exten => 1000,1,Verbose(2, Paging to external cisco phone)
    same => n,Page(sccp/100/autoanswer&sccp/101/autoanswer,i,120 )

| ... for a two-way call (full-duplex):

::

   exten => 1000,1,Verbose(2, Paging to external cisco phone)
    same => n,Page(sccp/100/autoanswer&sccp/101/autoanswer,di,120 )

