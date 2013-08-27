***********************************
Adding support for a new SCCP phone
***********************************


Introduction
------------

This page describes the requirements to considered that a SCCP phone is working
with XiVO libsccp.


Checklist
---------


Basic functionnality
^^^^^^^^^^^^^^^^^^^^

* Register on Asterisk
* SCCP reset [restart]
* Call history
* Date time display


Telephony
^^^^^^^^^

These test should be done with and without direct media enabled

* Emit a call
* Receive a call
* Receive and transfer a call
* Emit a call and transfer the call
* Hold and resume a call
* Features (\*0 and others)
* Receive 2 calls simultaneously
* Emit 2 calls simultaneously
* DTMF on an external IVR


Function keys
^^^^^^^^^^^^^

* Redial
* DnD
* Hold
* Resume
* New call
* End call
* Call forward (Enable)
* Call forward (Disable)
* Try each button in each mode (on hook, in progress, etc)


Optionnal options to test and document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Phone book
* Caller ID and other display i18n
* MWI
* Speeddial/BLF
