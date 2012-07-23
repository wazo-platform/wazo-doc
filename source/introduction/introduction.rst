************
Introduction
************

XiVO History
============

XiVO has been created in 2005 by Proformatique.

`XiVO 1.2 was released <https://projects.xivo.fr/news/49>`_ on February 3, 2012.


Known Bugs and Limitations
==========================

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

XiVO **does not currently support Fax detection**. The following describe a workaround to use this feature.

.. note:: This workaround works only :
        
    * on incoming calls towards an User (and an User only),
    * if the incoming trunk is a DAHDI trunk,
    * if the user has a voicemail which is activated and with the email field filled

    Be aware that this workaround will probably not survive any upgrade.

#. Activate fax detection in DAHDI configuration by editing :file:`/etc/asterisk/chan_dahdi.conf` and 
   adding the following line before the include statement::

    ;; Workaround Fax detection
    faxdetect = yes

#. Under :menuselection:`Services --> IPBX --> IPBX configuration --> Configuration files` add a new file
   containing the following dialplan::
    
    ;; Fax Detection
    [pre-user-global-faxdetection]
    exten = s,1,NoOp(Answer call to be able to detect fax if call is external AND user has an email configured)
    same  =   n,GotoIf($["${XIVO_CALLORIGIN}" = "extern"]?:return)
    same  =   n,GotoIf(${XIVO_USEREMAIL}?:return)
    same  =   n,Answer()
    same  =   n,Wait(4)
    same  =   n(return),Return()

    exten = fax,1,NoOp(Fax detected from ${CALLERID(num)} towards ${XIVO_DSTNUM} - will be sent upon reception to ${XIVO_USEREMAIL})
    same  =     n,Gosub(faxtomail,s,1(${XIVO_USEREMAIL}))

#. In :file:`/etc/pf-xivo/asterisk/xivo_globals.conf` activate the global user subroutine to ``pre-user-global-forfax``::
    
    XIVO_PRESUBR_GLOBAL_USER = pre-user-global-faxdetection

#. Reload asterisk configuration (both for dialplan and dahdi)::
    
    asterisk -rx 'core reload'

