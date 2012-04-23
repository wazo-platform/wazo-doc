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
* Queues (detail)
* Queues (entries detail)
* Agents (list)
* Agents (detail)

Supervision Panel
-----------------


.. figure:: images/cc_supervision.png
   :scale: 70%

* Click on queue name on queue list, display agent list for this queue in member
  of a queue, and updates calls waiting in xlet Calls of queue

* Click on the `+` icon for an agent displays agent details.

Queue List
^^^^^^^^^^
**General information**

The queue list is a gathering of information and statistics for each queues configured on the XiVO.

.. figure:: images/queue_list.png
   :scale: 90%


**Columns**

Queues
   queue name and number if configured to be displayed

Waiting calls
   The number of calls currently waiting for an agent in this queue, the background colored can change depending of the configured thresholds

Longest wait
   The maximum hold time for currently waiting calls, the background colored can change depending of the configured thresholds

Received
   The number of received calls on this queue during the configured statistical window

Answered
   The number of answered calls on this queue during the configured statistical window

Abandoned
   The number of abandoned calls on this queue during the configured statistical window

Max waiting time
   The longest wait time in the statistical time window, in mm:ss

Efficiency
   Answered calls over received calls during the configured statistical window (unanswered calls that are still waiting are not taken into account). If no calls are received the displayed value is empty

QOS
   Percentage of calls taken within X seconds over answered calls during the configured statistical window , X can be configured on queue basis

**Counter availability**

When the XiVO client is initialized, na is diplayed for not initialized counters. When the XiVO client is restarted the counters are always displayed and calculated as if the application was not restarted. When the server is restarted, counters are reinitialized.

**Enabling the xlet**

The xlet can be added to any CTI profil from the web interface.

.. figure:: images/queue_list_enable.png
   :scale: 70%

**Configuration**

Some values can be configured for the xlet. The statistic fetch timer can be set in the CTI profile preferences. This option is in seconds and the default is 30 seconds.

.. figure:: images/queue_list_fetch_time.png
   :scale: 70%

When logged to the XiVO client, one can modify his statistic parameters.

* Window is the period of statistical analysis to be displayed
* qos is the wait time that is required for a call to be answered on time

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
