.. _dashboard-xlet:

**********************
Agent Status Dashboard
**********************

Overview
========

The goal of the agent status dashboard xlet is to give contact center supervisors a better overview of agent status evolution in active queues.

.. figure:: ./images/xlet_dashboard.png


Usage
=====

The xlet is *read-only* and presents a list of queues aligned vertically. For each queue, the xlet displays a status box for each logged agents. Each status box gives the following information :

* Agent name
* Agent status : Shows the agent’s status. An agent can have two statuses: *In use* or *Not in use*.
* Agent status since : Shows the time spent in the current status
* Border color : orange if *In use*, green if *Not in use*
  

An agent is *In use* when he cannot receive a call from a queue (in conversation, in wrapup or in pause).

Known issues
============

* There is no profile containing this xlet. Profile must be created  manually.
* Xlet *Agent Status Dashboard* must be inserted in cti profile using dock mode. Otherwise, it will be impossible to scroll among queues.
* Modification and deletion of queues are not handled in display until the XiVO client is reconnected.
* As of now, there is no way to configure the displayed queues. Xlet displays all queues.
* There is no sorting on agents in a queue or in list of queues.
* An emtpy queue will display an empty box with no message specifying the queue has no logged agents.
* Layout is very basic at the moment: all queues are vertically aligned one queue per line. If there are more agents logged than space available to display them, a scrollbar will be available.

Configuration
=============

No special configuration necessary other than creating a cti profile in which the Agent Status Dashboard is added.


