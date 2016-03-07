**********************
Switchboard Statistics
**********************

Limitations
===========

.. note::

   Statistics are produced by `xivo-ctid`. If a call is received when `xivo-ctid` is
   stopped, no statistics will be produced for that call.

.. note::

   Statistics are not generated for call already completed.

.. note::

   Statistics are only available for existing switchboard queues, i.e. deleting a queue will also
   deleted the associated statistics.


Daily Statistics
================

Switchboard statistics can be retrieved in CSV format via the web interface in
:menuselection:`Services --> Statistics --> Switchboard --> Statistics`.

.. image:: images/statistics.png


Events
======

Switchboard statistic events are published on the bus to be consumed by collectd.


entered
-------

This event is produced when a call enters the switchboard on an open schedule.
Calls that did not enter the queue, if the queue was full for example, will also
generate an entered event.


abandoned
---------

This event is produced when the called hangs up while waiting in the incoming
queue or in the hold queue.


transferred
-----------

This event is produced when a call is transferred from the switchboard by the
operator. For attended transfers, the event is sent when the transfer is
completed.


forwarded
---------

This event is produced when a call is redirected to another destination under
certain conditions. This include:

* When the queue is full
* When the queue timeout is reached
* When no agent are logged with a join empty configuration
* When a divertion occured


completed
---------

This event is produced when a call was answered by the operator without being
transferred to another destination.


wait_time
---------

This event is produced when a call is completed, its value is the sum of all
times spent in the hold queue and the time spent in the incoming queue before
being answered.
