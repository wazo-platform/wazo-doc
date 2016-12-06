.. _ccss:

***************
Call Completion
***************

The call completion feature (or CCSS, for Call Completion Supplementary Services) in Wazo allows for
a caller to be automatically called back when a called party has become available.

#. To illustrate, let's say Alice attempts to call Bob.
#. Bob is currently on a phone call with Carol, though, so Bob rejects the call from Alice
#. Alice then dials \*40 to request call completion.
#. Once Bob has finished his phone call, Alice will be automatically called back by the system.
#. When she answers, Bob will be called on her behalf.

This feature has been introduced in XiVO in version 14.17.


Description
===========

Call completion can be used in two scenarios:

* when the called party is busy (Call Completion on Busy Subscriber)
* when the called party doesn't answer (Call Completion on No Response)

We have already discussed the busy scenario in the introduction section.

Let's now illustrate the no answer scenario:

#. Alice attempts to call Bob.
#. Bob doesn't answer the phone. Alternatively, Alice hangs up before Bob has the time to answer the
   call.
#. Alice then dial \*40 to request call completion.
#. When Bob's phone becomes busy and then is no longer busy, Alice is automatically called back.
#. When she answers, Bob will be called on her behalf.

The important thing to note here is step #4. Bob's phone needs to become busy and then no longer
busy for Alice to be called back. This means that if Bob was away when Alice called him, but when he
came back he did not received nor placed any call, then Alice will not be called back.

In fact, in all scenarios, after call completion has been requested by the caller, the called phone
needs to transition from busy to no longer busy for the caller to be called back.  This means that
in the following scenario:

#. Alice attempts to call Bob.
#. Bob is currently on a phone call, so he doesn't answer the call from Alice.
#. Bob finish his call a few seconds later.
#. Alice then dials \*40 to request call completion (Bob is not busy anymore).

Then, for Alice to be called back, Bob needs to become busy and then not busy.

If Alice is busy when Bob becomes not busy, then the call completion callback will only happen
after both Alice and Bob are not busy.

When call completion is active, it can be cancelled by dialing the \*40 extension.

Some timers governs the use of call completion. These are:

* offer timer: the time the caller has to request call completion. Defaults to 30 (seconds).
* busy available timer: when call completion on busy subscriber is requested, if this timer expires
  before the called party becomes available, then the call completion attempt will be cancelled.
  Defaults to 900 (seconds).
* no response available timer: similar to the "busy available timer", but when call completion on no
  response is requested. Defaults to 900 (seconds).
* recall timer: when the caller who requested call completion is called back, how long the original
  caller's phone rings before giving up. Defaults to 30 (seconds).

It's currently impossible to modify the value of these timers in Wazo.


Special Scenarios
-----------------

There are four special scenarios:

* the call completion will not activate
* the call completion will activate and call back for the original called party
* the call completion will activate and call back for the rerouted called party
* the call completion will activate and call back for the original called party but fail to join him

Call completion will not activate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is not possible to activate call completion in the following two scenarios.

First scenario: Alice tries to call Bob, but Bob has currently reached its "simultaneous calls"
limit. When activating call completion, Alice hears that the call completion can not be activated.

.. note:: The "simultaneous calls" option is configured per user via the Wazo web interface.

Second scenario: Alice tries to call Bob, but the call is redirected to Charlie.

This occurs when Bob redirects/rejects the call with any of the following:

* Unconditional call forwarding towards Charlie
* Closed schedule towards Charlie
* Call permission forbidding Alice to call Bob
* Preprocess subroutine forwarding the call towards Charlie

Call completion will activate and call back for the original called party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Alice tries to call Bob, but the call is redirected to Charlie. When activating call
completion, Alice hears that the call completion is activated and eventually Alice is called back to
speak with Bob.

This occurs when Bob redirects/rejects the call with any of the following:

* No-answer call forwarding towards Charlie
* Busy call forwarding towards Charlie

Call completion will activate and call back for the rerouted called party
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Alice tries to call Bob, but the call is redirected to Charlie. When activating call
completion, Alice hears that the call completion is activated and eventually Alice is called back to
speak with Charlie.

This occurs when Bob redirects the call with any of the following:

* Boss-Secretary filter to the secretary Charlie

Call completion will activate and call back for the original called party but fail to join him
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scenario: Alice tries to call Bob, but the call is redirected to Charlie. When activating call
completion, Alice hears that the call completion is activated and eventually Alice is called back to
speak with Bob. But when Alice answers, Bob is not called. If Alice activates call completion again,
she will hear that the call completion was cancelled.

This occurs when Bob redirects/rejects the call with any of the following:

* Do Not Disturb mode
* a new call forwarding rule that was applied after Alice activated call completion:

  * Unconditional call forwarding towards Charlie
  * Closed schedule towards Charlie
  * Call permission forbidding Alice to call Bob
  * Preprocess subroutine forwarding the call towards Charlie

Limitations
-----------

* Call completion can only be used with SIP lines. It can't be used with SCCP lines.
* It can't be used with outgoing calls and incoming calls, except if these calls are passing through
  a customized trunk of type Local.
* It can't be used with groups or queues.
* The call completion feature can't be enabled only for a few users; either all users have access to
  it, or none.


Configuration
=============

The call completion extension is enabled via the :menuselection:`Services --> IPBX --> IPBX
services --> Extensions` page, in the :guilabel:`General` tab.

.. figure:: images/cc_extension.png

   Call Completion Extension

If your Wazo has been installed in version 14.16 or earlier, then this extension is by default
disabled. Otherwise, this extension is by default enabled.
