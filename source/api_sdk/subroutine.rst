**********
Subroutine
**********

What is it ?
============

The preprocess subroutine allows you to enhance XiVO features through the Asterisk dialplan. Features that can be enhanced are :

* User
* Group
* Queue
* Meetme
* Incoming call
* Outcall

There are three possible categories :

* Subroutine for one feature
* Subroutine for global forwarding
* Subroutine for global incoming call to an object


Adding new subroutine
=====================

If you want to add a new subroutine, we propose to edit a new configuration file in the directory : :file:`/etc/asterisk/extensions_extra.d`.
You can also add this file by the web interface.

An example :

::

 [myexemple]
 exten = s,1,NoOp(This is an example)
 same  =   n,Return()

Don't forget to finish your subroutine by a Return().


Global subroutine
=================

There is predefined subroutine for this feature, you can find the name and the activation in the :file:`/etc/pf-xivo/asterisk/xivo_globals.conf`.
The variables are :

::

 ; Global Preprocess subroutine
 XIVO_PRESUBR_GLOBAL_ENABLE = 1
 XIVO_PRESUBR_GLOBAL_USER = xivo-subrgbl-user
 XIVO_PRESUBR_GLOBAL_GROUP = xivo-subrgbl-group
 XIVO_PRESUBR_GLOBAL_QUEUE = xivo-subrgbl-queue
 XIVO_PRESUBR_GLOBAL_MEETME = xivo-subrgbl-meetme
 XIVO_PRESUBR_GLOBAL_INCOMING = xivo-subrgbl-incoming
 XIVO_PRESUBR_GLOBAL_OUTGOING = xivo-subrgbl-outgoing

So if you want to add a subroutine for all of your XiVO users you can do this :

::

 [xivo-subrgbl-user]
 exten = s,1,NoOp(This is an example for all f my users)
 same  =   n,Return()

Forward subroutine
==================

You can also use a global subroutine for call forward.

::

 ; Preprocess subroutine for forwards
 XIVO_PRESUBR_FWD_ENABLE = 1
 XIVO_PRESUBR_FWD_USER = xivo-subrfwd-user
 XIVO_PRESUBR_FWD_GROUP = xivo-subrfwd-group
 XIVO_PRESUBR_FWD_QUEUE = xivo-subrfwd-queue
 XIVO_PRESUBR_FWD_MEETME = xivo-subrfwd-meetme
 XIVO_PRESUBR_FWD_VOICEMAIL = xivo-subrfwd-voicemail
 XIVO_PRESUBR_FWD_SCHEDULE = xivo-subrfwd-schedule
 XIVO_PRESUBR_FWD_VOICEMENU = xivo-subrfwd-voicemenu
 XIVO_PRESUBR_FWD_SOUND = xivo-subrfwd-sound
 XIVO_PRESUBR_FWD_CUSTOM = xivo-subrfwd-custom
 XIVO_PRESUBR_FWD_EXTENSION = xivo-subrfwd-extension


Dialplan variables
==================

Some of the XiVO variables can be used in subroutines.

::

  XIVO_CALLORIGIN ; intern for internal calls, extern for external calls

