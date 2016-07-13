.. _subroutine:

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
* Outgoing call

There are three possible categories :

* Subroutine for one feature
* Subroutine for global forwarding
* Subroutine for global incoming call to an object


Adding new subroutine
=====================

If you want to add a new subroutine, we propose to edit a new configuration file in the directory :file:`/etc/asterisk/extensions_extra.d`.
You can also add this file by the web interface.

An example::

   [myexemple]
   exten = s,1,NoOp(This is an example)
   same  =   n,Return()

Don't forget to finish your subroutine by a Return().


Global subroutine
=================

There is predefined subroutine for this feature, you can find the name and the activation in the :file:`/etc/xivo/asterisk/xivo_globals.conf`.
The variables are::

   ; Global Preprocess subroutine
   XIVO_PRESUBR_GLOBAL_ENABLE = 1
   XIVO_PRESUBR_GLOBAL_USER = xivo-subrgbl-user
   XIVO_PRESUBR_GLOBAL_AGENT = xivo-subrgbl-agent
   XIVO_PRESUBR_GLOBAL_GROUP = xivo-subrgbl-group
   XIVO_PRESUBR_GLOBAL_QUEUE = xivo-subrgbl-queue
   XIVO_PRESUBR_GLOBAL_MEETME = xivo-subrgbl-meetme
   XIVO_PRESUBR_GLOBAL_DID = xivo-subrgbl-did
   XIVO_PRESUBR_GLOBAL_OUTCALL = xivo-subrgbl-outcall
   XIVO_PRESUBR_GLOBAL_PAGING = xivo-subrgbl-paging

So if you want to add a subroutine for all of your XiVO users you can do this::

   [xivo-subrgbl-user]
   exten = s,1,NoOp(This is an example for all my users)
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

Some of the XiVO variables can be used and modified in subroutines.

* ``XIVO_CALLOPTIONS``: the value is a list of options to be passed to the Dial application, e.g.
  ``hHtT``. This variable is available in agent, user and outgoing call subroutines. Please note
  that it may not be set earlier, because it will be overwritten.

* ``XIVO_CALLORIGIN``: the value is:

  * ``extern`` for calls coming from a DID
  * ``intern`` for all other calls

  This variable is used by xivo-agid when :ref:`selecting the ringtone <xivo_ring.conf>` for ringing
  a user. This variable is available only in user subroutines.

* ``XIVO_DSTNUM``: the value is the extension dialed, as received by XiVO (e.g. an internal
  extension, a DID, or an outgoing extension including the local prefix). This
  variable is available in all subroutines.

* ``XIVO_MOBILEPHONENUMBER``: the value is the phone number of a user, as set in the web interface.
  This variable is only available in user subroutines.

* ``XIVO_SRCNUM``: the value is the callerid number of the originator of the call: the internal
  extension of a user (outgoing callerid is ignored), or the public extension of an external
  incoming call. This variable is available in all subroutines.
