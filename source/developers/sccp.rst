***********************************
Skinny Call Control Protocol (SCCP)
***********************************

Introduction
------------

SCCP (or skinny) is a stimulus protocol used to fully interact with Cisco phones.
What is libsccp ? It's a channel driver written for Asterisk by Avencall based on the channel skinny.


Installation
------------

The following packages are required to compile libsccp on a XiVO.

* build-essential
* autoconf
* automake
* libtool
* asterisk-dev

::

    apt-get update && apt-get install build-essential autoconf automake libtool asterisk-dev

::

   git clone git://gitorious.org/xivo/xivo-libsccp.git
   cd xivo-libsccp/xivo-libsccp/
   autoreconf -fvi
   ./configure
   make
   cp ./src/.libs/libsccp.so /usr/lib/asterisk/modules/chan_sccp.so


Configuration
-------------

example /etc/asterisk/sccp.conf:

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

.. warning::
    The option 'context' is very important. If you get it wrong, you won't be
    able to call or receive call. If you are unsure in what context your
    extension is configured, you can do:

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


CLI
---

The command line interface provide a way to interact with the different Asterisk modules, and in our case with the sccp channel driver (libsccp).

::

 nibskaro*CLI> sccp show version
 xivo-libsccp 1.3
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

::

 nibskaro*CLI> sccp update config
 Parse the configuration and add new lines and devices


FAQ
---

::

    Q. When is this *feature X* will be available?
    A. The order in which we implement features is based on our client needs. Write
       us an email that clearly explain your setup and what you would like to do and we
       will see what we can do. We don't provide any timeline.

::

    Q. I want to use the Page() application to call many phones at the same time.
    A. Here a Page() example for a one way call (half-duplex):

    exten => 1000,1,Verbose(2, Paging to external cisco phone)
     same => n,Page(sccp/100/autoanswer&sccp/101/autoanswer,i,120 )

    ...for a two-way call (full-duplex):

    exten => 1000,1,Verbose(2, Paging to external cisco phone)
     same => n,Page(sccp/100/autoanswer&sccp/101/autoanswer,di,120 )

