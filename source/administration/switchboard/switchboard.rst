***********
Switchboard
***********

This page describes the configuration needed to have a switchboard on your XiVO.


Overview
========

The switchboard functionnality is available in XiVO through the XiVO client. The goal of this page is to
describe how to configure your switchboard and how to use it.

The switchboard xlet and profile allow an operator to view incoming calls and answer them.
Put calls on hold, view the call on hold and pick the call on hold back.


Configuration
=============


Quick Summary
-------------

In order to configure a switchboard on your XiVO, you need to:

* Create a queue for your switchboard
* Create a queue for your switchboard's call on hold
* Create the users that will be operators
* Assign the switchboard plugin to your user
* Create an agent for your user
* Assign the incoming calls to the switchboard queue
* For each operator, add a function key for logging in or logging out from the switchboard queue.
* Set "no answer" destinations on the switchboard queue


Supported Devices
-----------------

The supported phones for the switchboard are:

* Aastra 6755i
* Aastra 6757i


Create a Queue for Your Switchboard
-----------------------------------

All calls to the switchboard will first be distributed to a queue.

To create this queue, go to :menuselection:`Services --> Call center --> Queues` and click the add button.

.. figure:: images/queue_general.png

The Following configuration is mandatory

* The :menuselection:`General --> Name` field has to be *__switchboard*
* The :menuselection:`Application --> Allow caller to hang up call` option has to be *enabled*
* The :menuselection:`Application --> Allow callee to transfer the call` option has to be *enabled*
* The :menuselection:`Advanced --> Member reachability timeout` option has to be *disabled*
* The :menuselection:`Advanced --> Time before retrying a call to a member` option has to be *1 second*
* The :menuselection:`Advanced --> Delay before reassigning a call` option has to be *disabled*

Other important fields

* The :menuselection:`General --> Display name` field is the name displayed in the XiVO client xlets and in the statistics
* The :menuselection:`General --> Number` field is the number that will be used to reach the switchboard internally typically *9*

Create a Queue for Your Switchboard on Hold
-------------------------------------------

The switchboard uses a queue to track it's calls on hold.

To create this queue, go to :menuselection:`Services --> Call center --> Queues` and click the add button.

The Following configuration is mandatory

* The :menuselection:`General --> Name` field has to be *__switchboard_hold*
* The :menuselection:`General --> Number` field has to be a valid number in a context reachable by the switchboard

Other important fields

* The :menuselection:`General --> Display name` field is the name displayed in the XiVO client xlets and in the statistics


Create the Users that Will be Operators
---------------------------------------

Each operator needs to have a user configured with a line. The XiVO client profile has to be set to *Switchboard*.

The following configuration is mandatory for switchboard users

* The :menuselection:`General --> First name` field has to be set
* The :menuselection:`General --> Simultaneous calls` option has to be set to *1*
* The :menuselection:`General --> Enable XiVO Client` option has to be set *enabled*
* The :menuselection:`General --> Login` field has to be set
* The :menuselection:`General --> Password` field has to be set
* The :menuselection:`General --> Profile` field has to be  *Switchboard*
* The :menuselection:`Lines --> Number` field has to be *empty*
* The :menuselection:`Lines --> Device` field has to be a supported device
* The :menuselection:`Services --> Enable call transfer` option has to be *enabled*

.. figure:: images/user_general.png


Set the Switchboard Plugin on your Phone
----------------------------------------

The provisioning plugin for the switchboard must be *xivo-aastra-switchboard*.

See :ref:`provd-plugins-mgmt` for more details.

This *xivo-aastra-switchboard* plugin must be set on the user's phone

* Edit device associated to your user in :menuselection:`Services --> Devices`
* Select a *xivo-aastra-switchboard* plugin and save
* Synchronize you phone to apply the changes

.. figure:: images/device_plugin_switchboard.png


Create an Agent for the Operator
--------------------------------

Each operator needs to have an associated agent.

To create an agent:

* Go to :menuselection:`Services --> Call center --> Agents`
* Click on the group `default`
* Click on the `Add` button

.. figure:: images/agent_add.png

* Associate the user to the agent in the `Users` tab

.. figure:: images/agent_user.png

* Assign the Agent to the *Switchboard* Queue

.. figure:: images/agent_queue.png


Send Incoming Calls to the *Switchboard* Queue
----------------------------------------------

Incoming calls should be sent to the *Switchboard* queue to be distributed to
the operators. To do this, we have to change the destination of our incoming
call to the queue.

In this example, we associate our incoming call (DID *444*) to our *Switchboard* queue:

.. figure:: images/incall_general.png


Set "No Answer" Destinations on the *Switchboard* Queue
-------------------------------------------------------

When there are no operators available to answer a call, "No Answer" destinations
should be used to redirect calls towards another destination.

In this example we redirect "No Answer", "Busy" and "Congestion" calls to the
*everyone* group and "Fail" calls to the *guardian* user.

You can also choose to redirect all the calls to another user or a voice mail.

.. figure:: images/queue_no_answer.png


Usage
=====


The XiVO Client Switchboard Profile
-----------------------------------

When the user connects with his XiVO Client, he gets the Switchboard profile.

.. figure:: images/xivoclient-switchboard.png
   :scale: 50%

.. note:: If you don't see the Switchboard Xlet, right-click on the grey
          bar at the right of the *Help* menu and check the line *Switchboard*:

.. figure:: images/enable-switchboard.png

The two main Xlets of this profile are the Switchboard Xlet and the Contacts Xlet.

1. The Switchboard Xlet lists the incoming calls waiting to be answered, calls on hold and
the current call.

2. The Contacts Xlet lists and searches among the users of the company. See the
page about the :ref:`contact-xlet` on how to transfer calls.

The user can login it's agent using a function key or an extension to start
receiving calls.


The Switchboard Xlet
--------------------

The switchboard xlet is made of three parts. The current call at the top, the list of incoming
calls on the left and the list of waiting calls.


Answering an incoming call
^^^^^^^^^^^^^^^^^^^^^^^^^^

When the switchboard receives a call, the new call is added to the incoming call
list on the left. The user can answer this call by clicking on the first call in the
list or by pressing the *Enter* key.

.. note:: The focus must be on the XiVO client for the keyboard shortcuts to be handled

Once the call is answered, it is removed from the incoming calls list and displayed
in the *Current Call* frame.


Distributing a call
^^^^^^^^^^^^^^^^^^^

Once the call has been answered and placed in the current call frame, the user
can distribute the call to another user using the :ref:`contact-xlet`, put the call on hold
using the *Hold* button or the *F7* key or end the call using the *Hangup* button or
the *F8* key.

If the user place the call on hold, it will be removed from the currents call frame and
displayed in the call on hold list.


Retrieving a call on hold
^^^^^^^^^^^^^^^^^^^^^^^^^

Once a call has been placed on hold, the user will most certainly want to retrieve
that call later to distribute it to another destination.

Any call on hold can be retrieved by clicking the desired call in the *Waiting call* list.
The focus can also be moved to the *Waiting Call* list and the call picked from the list
using the *Enter* key.

Once a call has been retrieved from the *Waiting Call* list, it is placed back into
the *Current Call* frame, ready to be distributed.

.. warning::

  Calls that have been placed on hold and retrieved must be hung up using
  the *Hangup* button. Hanging up using the phone will put the call back on hold.
