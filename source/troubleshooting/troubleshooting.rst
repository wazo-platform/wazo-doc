Troubleshooting
===============

The list of current bugs can be found on
`the official XiVO issue tracker <https://projects.xivo.fr/issues?set_filter=1&tracker_id=1>`_.


Transfers using DTMF
--------------------

When transfering a call using DTMF (\*1) you get an *invalid extension* error when dialing the
extension.

The workaround to this problem is to create a preprocess subroutine and assign it to the destinations
where you have the problem.

Under :menuselection:`Services --> IPBX --> IPBX configuration --> Configuration files` add a new file
containing the following dialplan::

    [allow-transfer]
    exten = s,1,NoOp(## Setting transfer context ##)
    same = n,Set(__TRANSFER_CONTEXT=<internal-context>)
    same = n,Return()

Do not forget to substitute <internal-context> with your internal context.

Some places where you might want to add this preprocess subroutine is on queues and outgoing calls
to be able to transfer the called person to another extension.


Boss-Secretary Filter
---------------------

In some cases, the function key and BLF will not work.
The work around consists in deleting affected users and re-create them.

Associated ticket : #3595


Fax detection
-------------

XiVO **does not currently support Fax detection**. The following describe a workaround to use this
feature. The behavior is to answer all incoming (external) call, wait for a number of seconds (4 in
this example) : if a fax is detected, receive it otherwise route the call normally.

.. note:: This workaround works only :
        
    * on incoming calls towards an User (and an User only),
    * if the incoming trunk is a DAHDI trunk,
    * if the user has a voicemail which is activated and with the email field filled

    Be aware that this workaround will probably not survive any upgrade.

#. Activate fax detection in DAHDI configuration by editing :file:`/etc/asterisk/chan_dahdi.conf` and
   adding the following lines **before** the line ``#include dahdi-channels.conf``::

    ;; Workaround Fax detection
    faxdetect = yes

#. In the Web Interface and under :menuselection:`Services --> IPBX --> IPBX configuration -->
   Configuration files` add a new file named *fax-detection.conf* containing the following
   dialplan::
    
    ;; Fax Detection
    [pre-user-global-faxdetection]
    exten = s,1,NoOp(Answer call to be able to detect fax if call is external AND user has an email configured)
    same  =   n,GotoIf($["${XIVO_CALLORIGIN}" = "extern"]?:return)
    same  =   n,GotoIf(${XIVO_USEREMAIL}?:return)
    same  =   n,Answer()
    same  =   n,Wait(4) ; You can change the number of seconds that it'll wait for Fax
    same  =   n(return),Return()

    exten = fax,1,NoOp(Fax detected from ${CALLERID(num)} towards ${XIVO_DSTNUM} - will be sent upon reception to ${XIVO_USEREMAIL})
    same  =     n,GotoIf($["${CHANNEL(channeltype)}" = "DAHDI"]?changeechocan:continue))
    same  =     n(changeechocan),Set(CHANNEL(echocan_mode)=fax) ; if chan type is dahdi set echo canceller in fax mode
    same  =     n(continue),Gosub(faxtomail,s,1(${XIVO_USEREMAIL}))

#. In the file :file:`/etc/pf-xivo/asterisk/xivo_globals.conf` set the global user subroutine to
   ``pre-user-global-faxdetection`` : this subroutine will be executed each time a user is called::
    
    XIVO_PRESUBR_GLOBAL_USER = pre-user-global-faxdetection

#. Reload asterisk configuration (both for dialplan and dahdi)::
    
    asterisk -rx 'core reload'


Berofos Integration with PBX
----------------------------

You can use a Berofos failover switch to secure the ISDN provider lines 
when installing a XiVO in front of an existing PBX.
The goal of this configuration is to mitigate the consequences of an outage of the XiVO : with this
equipment the ISDN provider links could be switched to the PBX directly if the XiVO goes down.

XiVO **does not offer natively** the possibility to configure Berofos in this failover mode.
This section describes a workaround.

Logical view::

                   +------+                            +-----+
   -- Provider ----| XiVO | -- ISDN Interconnection  --| PBX | -- Phones
                   +------+                            +-----+

Connection::

       +-------------Bero*fos---------------+
       | A        B        C        D       |
       | o o o o  o o o o  o o o o  o o o o |
       +-+-+------+-+------+-+------+-+-----+
         | |      | |      | |      | |
        / /       | |      | |      | | 
       / /    +--------+   / /   +---------+	
     2 T2     |  XiVO  |  / /    |   PBX   |	
              +--------+ / /     +---------+
                  | |   / /	
                  \ \__/ /
                   \____/


The following describes how to configure your XiVO and your Berofos.

#. Follow the Berofos general configuration (firmware, IP, login/password) described 
   on the the berofos_ page.

#. When done, apply these specific parameters to the berofos::

    bnfos --set scenario=1   -h 10.105.2.26 -u admin:berofos
    bnfos --set mode=1       -h 10.105.2.26 -u admin:berofos
    bnfos --set modedef=1    -h 10.105.2.26 -u admin:berofos
    bnfos --set wdog=1       -h 10.105.2.26 -u admin:berofos
    bnfos --set wdogdef=1    -h 10.105.2.26 -u admin:berofos
    bnfos --set wdogitime=60 -h 10.105.2.26 -u admin:berofos	

#. Add the following script :file:`/usr/local/sbin/berofos-workaround`::

    #!/bin/bash
    # Script workAround for berofos integration with a XiVO in front of PABX
    
    /etc/init.d/asterisk status
    if [ $? -eq 0 ]; then
       # If asterisk is running, we (re)enable wdog and (re)set the mode
       /usr/bin/bnfos --set mode=1 -f fos1
       /usr/bin/bnfos --set modedef=1 -f fos1
       /usr/bin/bnfos --set wdog=1 -f fos1
    else
       /usr/bin/logger "$0 - Asterisk is not running"
    fi
    
    # Now 'kick' berofos ten times each 5 seconds
    for ((i == 1; i <= 10; i += 1)); do
        /usr/bin/bnfos --kick -f fos1
    	/bin/sleep 5
    done

#. Add execution rights to script::
   
    chmod +x /usr/local/sbin/berofos-workaround

#. Create a cron to launch the script every minutes :file:`/etc/cron.d/berofos-cron-workaround`::

	# Workaround to berofos integration

	*/1 * * * * root /usr/local/sbin/berofos-workaround 2>&1 > /dev/null


.. _berofos: http://documentation.xivo.fr/production/high_availability/berofos.html#slave-configuration

Upgrading from Skaro-1.2.3
--------------------------

#. There is an issue with ``xivo-libsccp`` and ``pf-xivo-base-config`` during an upgrade from 1.2.3::

    dpkg: error processing /var/cache/apt/archives/pf-xivo-base-config_13%3a1.2.4-1_all.deb (--unpack):
    trying to overwrite '/etc/asterisk/sccp.conf', which is also in package xivo-libsccp 1.2.3.1-1
    ...
    Errors were encountered while processing:
    /var/cache/apt/archives/pf-xivo-base-config_13%3a1.2.4-1_all.deb
    E: Sub-process /usr/bin/dpkg returned an error code (1)


#. You have to remove :file:`/var/lib/dpkg/info/xivo-libsccp.conffiles`::

    rm /var/lib/dpkg/info/xivo-libsccp.conffiles

#. You have to edit :file:`/var/lib/dpkg/info/xivo-libsccp.list` and remove the following line::

    /etc/asterisk/sccp.conf

#. and remove :file:`/etc/asterisk/sccp.conf`::

    rm /etc/asterisk/sccp.conf

#. Now, you can launch ``xivo-upgrade`` to finish the upgrade process
