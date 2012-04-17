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
