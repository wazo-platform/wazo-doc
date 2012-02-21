***********
Subroutine
***********

What is it ?
============

The preprocess subroutine is for enhanced the xivo functionnalities with the Asterisk dialplan. You can enhanced this fonctionnality :

* User
* Group
* Queue
* Meetme
* Incoming call
* Outcall

There is tree possible categories :

* Subroutine for one fonctionnality
* Subroutine for global forwarding
* Subroutine for global incoming call to an object

Adding new subroutine
=====================

If you want to adding a new subroutine, we propose to edit a new configuration file in the directory : /etc/asterisk/extensions_extra.d
You can also add this file by the web interface.

An example :

.. code-block:: python

 [myexemple]
 exten = s,1,NoOp(This is an example)
 same  =   n,Return()

Don't forget to finish your subroutine by a Return().


Global subroutine
=================

There is predefined subroutine for this feature, you can find the name and the activation in the /etc/pf-xivo/asterisk/xivo_globals.conf.
The variables are :

.. code-block:: python

 ; Global Preprocess subroutine
 XIVO_PRESUBR_GLOBAL_ENABLE = 1
 XIVO_PRESUBR_GLOBAL_USER = xivo-subrgbl-user
 XIVO_PRESUBR_GLOBAL_GROUP = xivo-subrgbl-group
 XIVO_PRESUBR_GLOBAL_QUEUE = xivo-subrgbl-queue
 XIVO_PRESUBR_GLOBAL_MEETME = xivo-subrgbl-meetme
 XIVO_PRESUBR_GLOBAL_INCOMING = xivo-subrgbl-incoming
 XIVO_PRESUBR_GLOBAL_OUTGOING = xivo-subrgbl-outgoing

So if you want to adding a subroutine for all of your xivo users you can do this :

.. code-block:: python

 [xivo-subrgbl-user]
 exten = s,1,NoOp(This is an example for all f my users)
 same  =   n,Return()

Forward subroutine
==================

You can also using a global subroutine for the forward.

.. code-block:: python

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

Features subroutine
===================

.. code-block:: python

 ; Preprocess subroutine for features
 XIVO_GROUP_MEMBER_SUBROUTINE = xivo-subrfeatures-groupmember
