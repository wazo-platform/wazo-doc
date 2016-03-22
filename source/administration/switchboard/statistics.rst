.. _switchboard_stats:

**********************
Switchboard Statistics
**********************

Limitations
===========

.. note::

   Statistics are produced by `xivo-ctid`. If a call is received when `xivo-ctid` is
   stopped, no statistics will be produced for that call.

.. note::

   Statistics are only generated for calls answered in XiVO ≥ 16.03.

.. note::

   Statistics are only available for existing switchboard queues, i.e. deleting a queue will also
   delete the associated statistics.


Daily Statistics
================

Switchboard statistics can be retrieved in CSV format via the web interface in
:menuselection:`Services --> Statistics --> Switchboard --> Statistics`.

.. image:: images/statistics.png

* Start date: when empty, the result will contain statistics from the beginning
* End date: when empty, the result will contain statistics until the current time

.. note:: Switchboard statistics older than a year are automatically removed. See :ref:`purge_logs`
          for more details.


Report
------

The generated CSV report includes the following columns:

* date: The date at which the calls were received
* entered: The number of calls to the switchboard for the given date excluding calls when the switchboard was closed (e.g. with a :ref:`schedule <schedules>`)
* answered: The number of calls that have been answered by the operator and then transferred or completed by the operator
* transferred: The number of calls that have been transferred by the switchboard operator to another destination
* abandoned: The number of calls that have been abandoned in the switchboard queue or while waiting in the hold queue
* forwarded: The number of calls that have been forwarded to another destination:

  * a call reaching a full queue
  * a call waiting until the max ring time is reached
  * a call forwarded because of a diversion rule
  * a call forwarded because of a leave empty condition

* waiting_time_average: The average time spent in the switchboard and hold queue for all calls that entered the switchboard


Events
======

Switchboard statistic events are published on the bus to be consumed by collectd.

Configuration
-------------

In order to process these events, you need:

* collectd installed on your XiVO: ``apt-get install collectd``
* In :file:`/etc/collectd/collectd.conf.d/amqp.conf`, configure collectd to read events from the
  bus (RabbitMQ)::

   LoadPlugin amqp

   <Plugin "amqp">
     <Subscribe "xivo">
       Host "127.0.0.1"
       Port "5672"
       VHost "/"
       User "guest"
       Password "guest"
       Exchange "collectd"
       ExchangeType "topic"
       RoutingKey "collectd.#"
     </Subscribe>
   </Plugin>

* another service receiving events from collectd, e.g. logstash, graphite, another collectd.


Event description
-----------------

The collectd events have the following attributes:

* host: the UUID of the XiVO.
* plugin: ``switchboard``
* plugin_instance: the name (not the display name) of the queue for incoming calls of the switchboard.
* type: ``counter`` or ``gauge``.
* type_instance: the following values.

entered
   This event is produced when a call enters the switchboard on an open schedule. Calls that did not
   enter the queue, if the queue was full for example, will also generate an entered event.


abandoned
   This event is produced when the called hangs up while waiting in the incoming queue or in the
   hold queue.


transferred
   This event is produced when a call is transferred from the switchboard by the operator. For
   attended transfers, the event is sent when the transfer is completed.


forwarded
   This event is produced when a call is redirected to another destination under certain conditions.
   This include:

   * When the queue is full
   * When the queue timeout is reached
   * When no agent are logged with a join empty configuration
   * When a divertion occured


completed
   This event is produced when a call was answered by the operator without being transferred to
   another destination.


wait_time
   This event is produced when a call is completed, its value is the sum of all times spent in the
   hold queue and the time spent in the incoming queue before being answered.
