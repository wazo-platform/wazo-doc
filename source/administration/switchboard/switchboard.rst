***********
Switchboard
***********

This page describes the configuration needed to have a switchboard on your XiVO.


Overview
========

Switchboard functionality is available in the XiVO client. The goal of this page is to explain how to
configure your switchboard and how to use it.

The switchboard xlet and profile allow an operator to view incoming calls, answer them,
put calls on hold, view the calls on hold and pick up the calls on hold.


Limitations
===========

.. note::

  It is impossible to cancel a transfer to an invalid number in the dialplan.
  The operator will have to wait until the prompt is over before trying to
  transfer again.

.. note::

  The shortcut keys of the switchboard do not work on the Mac version of the
  XiVO client.

.. note::

  The enter shortcut to answer a call will not work if the focus is currently
  on a widget that will consume the key press. ie: a text field, a drop down
  list or a button.


Configuration
=============

Quick Summary
-------------

In order to configure a switchboard on your XiVO, you need to:

* Create a queue for your switchboard
* Create a queue for your switchboard's calls on hold
* Create the users that will be operators
* Assign the switchboard plugin to your user
* Create an agent for your user
* Assign the incoming calls to the switchboard queue
* For each operator, add a function key for logging in or logging out from the switchboard queue.
* Set "no answer" destinations on the switchboard queue


.. _switchboard_supported_devices:

Supported Devices
-----------------

The supported phones for the switchboard are:

* Aastra 6755i
* Aastra 6757i
* Snom 720


Create a Queue for Your Switchboard
-----------------------------------

All calls to the switchboard will first be distributed to a switchboard queue.

To create this queue, go to :menuselection:`Services --> Call center --> Queues` and click the add button.

.. figure:: images/queue_general.png

The Following configuration is mandatory

* The :menuselection:`General --> Name` field has to be *__switchboard*
* The :menuselection:`General --> Preprocess subroutine` field has to be *xivo_subr_switchboard*
* The :menuselection:`Application --> Allow caller to hang up call` option has to be *enabled*
* The :menuselection:`Application --> Allow callee to transfer the call` option has to be *enabled*
* The :menuselection:`Advanced --> Member reachability timeout` option has to be *disabled*
* The :menuselection:`Advanced --> Time before retrying a call to a member` option has to be *1 second*
* The :menuselection:`Advanced --> Delay before reassigning a call` option has to be *disabled*
* The :menuselection:`Advanced --> Call a member already on` option has to be *disabled*
* The :menuselection:`Advanced --> Autopause agents` option has to be *disabled*

Other important fields

* The :menuselection:`General --> Display name` field is the name displayed in the XiVO client xlets and in the statistics
* The :menuselection:`General --> Number` field is the number that will be used to reach the switchboard internally (typically *9*)


Create a Queue for Your Switchboard on Hold
-------------------------------------------

The switchboard uses a queue to track its calls on hold.

To create this queue, go to :menuselection:`Services --> Call center --> Queues` and click the add button.

The Following configuration is mandatory

* The :menuselection:`General --> Name` field has to be *__switchboard_hold*
* The :menuselection:`General --> Number` field has to be a valid number in a context reachable by the switchboard

Other important fields

* The :menuselection:`General --> Display name` field is the name displayed in the XiVO client xlets and in the statistics

.. warning:: This queue MUST have **NO** members


Create the Users that Will be Operators
---------------------------------------

Each operator needs to have a user configured with a line. The XiVO client profile has to be set to *Switchboard*.

The following configuration is mandatory for switchboard users

* The :menuselection:`General --> First name` field has to be set
* The :menuselection:`General --> Enable XiVO Client` option has to be *enabled*
* The :menuselection:`General --> Login` field has to be set
* The :menuselection:`General --> Password` field has to be set
* The :menuselection:`General --> Profile` field has to be set to *Switchboard*
* The :menuselection:`Lines --> Number` field has to have a valid extension
* The :menuselection:`Lines --> Device` field has to be a :ref:`supported device <switchboard_supported_devices>`
* The :menuselection:`Services --> Enable call transfer` option has to be *enabled*

.. figure:: images/user_general.png


Set the Switchboard Plugin on your Phone
----------------------------------------

The provisioning plugin for the switchboard must be *xivo-aastra-switchboard* or *xivo-snom-switchboard*.

See :ref:`provd-plugins-mgmt` for more details.

The switchboard plugin must be set on the user's device.

* Edit device associated to your user in :menuselection:`Services --> Devices`
* Select the appropriate switchboard plugin and save
* Synchronize you phone to apply the changes

.. figure:: images/device_plugin_switchboard.png

.. warning::
  To be able to use a Snom phone for the switchboard, you have to be able to do
  the appropriate HTTP request from the XiVO to the device's web service.
  The following command should work from your XiVO's bash command line
  `wget http://guest:guest@<phone IP address>/command.htm?key=SPEAKER`. If this
  command does not activate the phone's speaker, your network configuration will
  have to be *fixed* before you can be able to use the Snom switchboard.

.. warning:: When using a Snom switchboard you should not use the first function key.


Create an Agent for the Operator
--------------------------------

Each operator needs to have an associated agent.

.. warning:: Each agent MUST ONLY be a member of the Switchboard queue

To create an agent:

* Go to :menuselection:`Services --> Call center --> Agents`
* Click on the group `default`
* Click on the `Add` button

.. figure:: images/agent_add.png

* Associate the user to the agent in the `Users` tab

.. figure:: images/agent_user.png

* Assign the Agent to the *Switchboard* Queue (**and ONLY to the Switchboard queue**)

.. figure:: images/agent_queue.png


Send Incoming Calls to the *Switchboard* Queue
----------------------------------------------

Incoming calls must be sent to the *Switchboard* queue to be distributed to
the operators. To do this, we have to change the destination of our incoming
call for the switchboard queue.

In this example, we associate our incoming call (DID *444*) to our *Switchboard* queue:

.. figure:: images/incall_general.png


Set "No Answer" Destinations on the *Switchboard* Queue
-------------------------------------------------------

When there are no operators available to answer a call, "No Answer" destinations
should be used to redirect calls towards another destination.

You also need to set the timeout of the Switchboard queue to know when calls will be
redirected.

.. figure:: images/queue_application.png

The reachability timeout must not be disabled nor be too short.

The time before retrying a call to a member should be as low as possible (1 second).

.. figure:: images/queue_advanced.png

In this example we redirect "No Answer", "Busy" and "Congestion" calls to the
*everyone* group and "Fail" calls to the *guardian* user.

You can also choose to redirect all the calls to another user or a voice mail.

.. figure:: images/queue_no_answer.png


XiVO Client configuration
=========================

Directory xlet
--------------

The transfer destination is chosen in the Directory xlet. You **must** follow the :ref:`directory-xlet` section to be able to use it.


Configuration for multiple switchboards
---------------------------------------

The above documentation can be used for multiple switchboards on the same
XiVO by replacing the *__switchboard* and *__switchboard_hold* queues name
and configuring the operators XiVO client accordingly in the
:menuselection:`XiVO Client --> Configure --> Functions --> Switchboard` window.

.. figure:: images/multi_switchboard.png


Usage
=====

.. warning::

  The switchboard configuration must be completed before using the switchboard. This includes :

    * Device, User, Agent and Queues configuration (see above),
    * Directory xlet configuration (see :ref:`directory-xlet`)

  If it's not the case, the user must disconnect his XiVO client and reconnect.


The XiVO Client Switchboard Profile
-----------------------------------

When the user connects with his XiVO Client, he gets the Switchboard profile.

.. figure:: images/xivoclient-answering.png

1. *Current Call* frame
2. *Answer* button
3. *Call* button
4. *Blind transfer* button
5. *Attended transfer* button
6. *Hold* button
7. *Hangup* button
8. *Incoming Calls* list
9. *Waiting Calls* list
10. *Directory* Xlet
11. *Dial* Xlet

.. note:: If you don't see the Switchboard Xlet, right-click on the grey
          bar at the right of the *Help* menu and check *Switchboard*:

.. figure:: images/enable-switchboard.png

The operator can login his agent using a function key or an extension to start
receiving calls.


Call flow
---------

Answering an incoming call
^^^^^^^^^^^^^^^^^^^^^^^^^^

When the switchboard receives a call, the new call is added to the *Incoming Calls* list on the left
and the phone starts ringing. The user can answer this call **only when his phone is ringing**, by:

* clicking on any call in the list
* clicking the *Answer* button
* pressing the *Enter* key

.. note:: The XiVO Client must be the active window for the keyboard shortcuts
          to be handled

The operator can select which call to answer by:

* clicking directly on the incoming call
* pressing *F10* to select the incoming calls frame and pressing the up and down arrow keys

Once the call has been answered, it is removed from the incoming calls list and
displayed in the *Current Call* frame.


Making a Call
^^^^^^^^^^^^^

The switchboard operator can do the following operations:

* Press the *Call* button or press *F3*
* Search for the call destination in the directory xlet
* Press to confirm the selection and start the call


Distributing a call
^^^^^^^^^^^^^^^^^^^

Once the call has been answered and placed in the current call frame, the operator has 3 choices:

* transfer the call to another user

  * using the *Blind transfer* button or the *F4* key.
  * using the *Attended transfer* button or the *F5* key

* put the call on hold using the *Hold* button or the *F7* key
* end the call using the *Hangup* button or the *F8* key.


Transferring a call
^^^^^^^^^^^^^^^^^^^

Transfer buttons allow the operator to select towards which destination he wishes to transfer the call. This is made through the *Directory* xlet. For defails about the xlet *Directory* usage and configuration see :ref:`directory-xlet`.

Once the destination name has been entered, press *Enter*. If multiple destinations are displayed, you can choose by:

* double-clicking on the destination
* using *Up*/*Down* arrows then:

  * pressing *Enter*
  * pressing the transfer button again

Blind transfers are straightforward: once the call is transferred, the operator is free to manage other calls.

Attended transfers are a bit more complicated: the operator needs to wait for the transfer destination to answer before completing the transfer.

In this example, the operator is currently asking *Bernard Marx* if he can transfer *Alice Wonderland* to him.

.. figure:: images/xivoclient-transferring.png

1. *Complete transfer* button
2. *Cancel transfer* button
3. Transfer destination filtering field (xlet *Directory*)
4. Transfer destination list (xlet *Directory*)

Once the destination has answered, you can:

* cancel the transfer with *F8* key
* complete the transfer with *F5* key

.. note:: The operator can not complete an attended transfer while the transfer destination is ringing. In this case, the operator must cancel the attended transfer and use the *Blind transfer* action.


Putting a call on hold
^^^^^^^^^^^^^^^^^^^^^^

If the user places the call on hold, it will be removed from the *Current call*
frame and displayed in the *Waiting calls* list. The time counter shows how long
the call has been waiting, thus it will be reset each time the call returns in
the *Waiting calls* list. The calls are ordered from the oldest to the newest.


Retrieving a call on hold
^^^^^^^^^^^^^^^^^^^^^^^^^

Once a call has been placed on hold, the operator will most certainly want to
retrieve that call later to distribute it to another destination.

To retrieve a call on hold:

* click the desired call in the *Waiting calls* list
* with the keyboard:

  * move the focus to the *Waiting calls* list (*F9* key)
  * choose the desired call with the arrow keys
  * press the *Enter* key.

Once a call has been retrieved from the *Waiting calls* list, it is moved back
into the *Current Call* frame, ready to be distributed.
