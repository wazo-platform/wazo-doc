***********
Supervision
***********

Introduction
============

Allows a contact center supervisor to monitor contact center activities

* Monitor real time information from call queues
* Agent activities per call queues
* Agent detailed activities


XiVO client as a Supervision Platform
=====================================

Configuration
-------------

A supervisor profile defined in :menuselection:`Service --> CTI Server -->
Profiles` menu, usually contains the following Xlets :

* Identity
* Queues
* Queue members
* Queues (entries detail)
* Agents (list)
* Agents (detail)


Supervision Panel
-----------------

.. figure:: images/cc_supervision.png
   :scale: 90%

* Click on queue name on queue list, display agent list for this queue in member
  of a queue, and updates calls waiting in xlet Calls of queue

* Click on an agent in agent list to display the details of this agent in Xlet
  Agent details

* Click on the `+` icon for an agent displays agent details.


Queue List
^^^^^^^^^^
**General information**

The queue list is a dashboard displaying queue statistics and real-time counters for each queue configured on the XiVO.

.. figure:: images/queue_list.png
   :scale: 90%


**Columns**

Queues
   queue name and number if configured to be displayed

Waiting calls
   The number of calls currently waiting for an agent in this queue, the background colored
   can change depending of the configured thresholds

EWT
   Estimated waiting time

Longest wait
   The maximum hold time for currently waiting calls, the background colored can change
   depending of the configured thresholds

Talking
   Shows the number of agents currently in conversation in the queue.
   This column is set to 0 when the queue has just been created and no members are already affected.

Logged
   Shows the number of logged agents in the queue.
   This column is set to N/A when the queue has just been created and no members are already affected.

Available
   Shows the number of available agents ready to take a call in the queue.
   This column is set to N/A when the queue has just been created and no members are already affected.

Received
   The number of received calls on this queue during the configured statistical window

Answered
   The number of answered calls on this queue during the configured statistical window

Abandoned
   The number of abandoned calls on this queue during the configured statistical window

Mean waiting time
   The mean  wait time in the statistical time window, in mm:ss
   If no calls are received - is displayed

Max waiting time
   The longest wait time in the statistical time window, in mm:ss
   If no calls are received - is displayed

Efficiency
   Answered calls over received calls during the configured statistical window
   (unanswered calls that are still waiting are not taken into account).
   If no calls are received - is displayed

QOS
   Percentage of calls taken within X seconds over answered calls during the configured
   If no calls are received - is displayed


**Counter availability**

When the XiVO client is initialized, na is diplayed for not initialized counters.
When the XiVO client is restarted the counters are always displayed and calculated as if
the application was not restarted. When the server is restarted, counters are reinitialized.

**Enabling the xlet**

The xlet can be added to any CTI profil from the web interface.

.. figure:: images/queue_list_enable.png
   :scale: 70%

**Configuration**

Some values can be configured for the xlet. The statistic fetch timer can be set in the CTI profile preferences.
This option is in seconds and the default is 30 seconds.

.. figure:: images/queue_list_fetch_time.png
   :scale: 70%

When logged to the XiVO client, one can modify his statistic parameters.

* Window is the period of statistical analysis to be displayed.

  On the server side, data that are used to compute statistics are only kept
  for around 3 hours, so there's a hard limit of 3 hours for this value.
* Qos is the wait time that is required for a call to be answered on time

These configurations can be done for each queue.

.. figure:: images/queue_list_fetch_param.png
   :scale: 90%

Display options can also be set on the client side.

* Queue display (longest wait) add the column showing the longest hold time for the currently waiting calls
* Queue display (number) shows the queue number
* The first pair of scroll box control the color switching threshold of the longest wait box
* The second pair of scroll box control the color switching threshold of the call waiting box

.. figure:: images/queue_list_config.png
   :scale: 90%

**Monitoring queues on high dimension screens**

You may want to display the queue list on one big screen, visible by multiple
people. However, the default font will not be large enough, so the information
will not be readable.

You can change the font size of this Xlet by giving a configuration file when
launching the XiVO Client::

   $ xivoclient -stylesheet big_fonts.qss

The :file:`big_fonts.qss` file should contain::

   QueuesView {font-size: 40px;}
   QueuesView QHeaderView {font-size: 40px;}

Units of size that can be used are described on the `Qt documentation`_.

.. _Qt documentation: http://doc.qt.nokia.com/latest/stylesheet-reference.html#length.


Agent List
^^^^^^^^^^

**General information**

The queue list is a dashboard displaying each agent configured on the XiVO.

.. figure:: images/agent_list.png
   :scale: 80%

**Columns**

Number
   The agent's number

First name & Last name
   The agent's first name and last name

Listen
   A *clickable cell* to listen to the agent's current call

Status since
   Shows the agent's status and the time spent in this status. An agent can have two statuses : *In use* or *Not in use*.

   An agent is *In use* when he cannot answer a call (in conversation, in wrapup or in pause).
   The agent is no longer *In use* when he becomes available to answer a call.

   .. note:: For now, the agent is not considered *In use* if he emits a call or receives a call directly through his phone, not through the queue.

Logged
   A *clickable cell* to log or unlog the agent

Joined queues
   The number of queues the agent will be receiving calls from

Paused
   A *clickable cell* to pause or unpause the agent

Paused queues
   The number of queues in which the agent is paused


Agent Details
^^^^^^^^^^^^^

**General information**

Display advanced informations of an agent and enable to login/logoff, add/remove to a queue, and pause/unpause.

.. figure:: images/agent_details.png

   Agent Details

1. This is the status information of agent
2. Button to login/logoff agent
3. Supervision button of the Xlet "Calls of a queue"
4. Pause/Unpause button for given queue
5. Add/Remove agent for given queue

You can't add/remove this agent to queue1/queue6 because there is hard linked in configuration (WEBI)


Queue members
^^^^^^^^^^^^^

The queue members lists which agents or phones will receive calls from the
selected queue and some of their attributes.

.. figure:: images/queue_members.png

**Columns**

Number
    The agent number or the phone number of the queue member.

Firstname and Lastname
    First name and last name of the agent or the user to which the phone belongs.

Logged
    Whether the agent is logged or not. Blank for a phone.

Paused
    Whether the agent is paused or not. Blank for a phone.

Answered calls
    Number of calls answered by the member since last restart or configuration reload.

Last call
    Hangup time of the last answered calls.

Penalty
    Penalty of the queue member.


Link XiVO Client presence to agent presence
===========================================

You can configure XiVO to have the following scenario:

* The agent person leaves temporarily his office (lunch, break, ...)
* He sets his presence in the XiVO Client to the according state
* The agent will be automatically set in pause and his phone will not ring from
  queues
* He comes back to his office and set his presence to 'Available'
* The pause will be automatically cancelled

You can :ref:`configure the presence states <presence-actions>` of CTI profiles
and attach ``Actions`` to them, such as `Set in pause` or `Enable DND`.

You can then attach an action `Set in pause` for multiple presence states and
attach an action `Cancel the pause` for the presence state `Available`.

For now, the actions attached to the mandatory presence `Disconnected` will not
be taken into account.
