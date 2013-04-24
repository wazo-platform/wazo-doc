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

The xlet is *read-only* and presents a list of queues. For each queue, the xlet displays a status box for each logged agents. Each status box gives the following information:

* Agent name
* Agent status: Shows the agent’s status. An agent can have three statuses:

  * *Not in use* when he is ready to answer an ACD call
  * *Out of queue* when he called or answered a call not from the queue
  * *In use* when he is either on call from a queue, on pause or on wrapup

* Agent status since: Shows the time spent in the current status
* Background color:

  * green if *Not in use*
  * purple if *Out of queue*
  * orange if *In use*


Changing the disposition
========================

The disposition of the Xlet can be changed in two ways:

* Placement of queues
* Which queues are displayed

The disposition is saved whenever the XiVO Client is closed and restored when it is opened again.


Changing the placement of queues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The little windows containing each queue can be resized and moved around. That way, any layout can be achieved, according to the size and importance of each queue.


Choosing which queues are displayed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is a little contextual menu when right-clicking on the title bar of every queue window. Checking/unchecking the lines of this menu shows/hides the associated queue.

.. figure:: ./images/dashboard_choosing_queues.png

.. _dashboard-xlet-issues:


Known issues
============

* There is no profile containing this xlet. Profile must be created manually.
* There is no sorting on agents in a queue.
* An emtpy queue will display an empty box with no message specifying the queue has no logged agents.


Configuration
=============

No special configuration necessary other than creating a CTI profile in which the Agent Status Dashboard is added.
