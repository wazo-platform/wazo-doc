**********
Statistics
**********


Overview
========

The statistics page is used to monitor queues and agents efficiency. Statistics
are generated automatically every night but it can also be done manually.


Configuration
=============

In order to be able to display call center statistics you have first to create one or more configuration.

.. figure:: images/Statistic_configuration.png
   :scale: 90%
   :alt: Statistics Configuration

   Statistics Configuration

The configuration is used to generate reports from the cache. The cache is generated independently
from the configuration so adding a new configuration does not require a new cache generation.


+------------------+---------------------------------+---------------------------------------------------------------------------+
| Field            | Values                          | Description                                                               |
|                  |                                 |                                                                           |
+==================+=================================+===========================================================================+
|                  |                                 |                                                                           |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| name             | string                          | Any name useful to remember what the configuration is used to             |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| interval         | enum [0-999] [day, week, month] | This parameter is used as a default when you display statistics.          |
|                  |                                 | If -1 day, default view displays yesterday statistics                     |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| show on page     |                                 | Display on the summary page                                               |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| timezone         | America/Montreal                | Time difference to apply when users are not in the same time zone as XIVO |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| **Period cache** |                                 |                                                                           |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| start            | YYYY-MM                         | Cache start date                                                          |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| Cache start date | hh:mm                           | Cache end date if left to 0 the end of cache is the server current date   |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| **Working Hour** |                                 |                                                                           |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| start            | hh:mm                           | beginning of work, data of of working hours will not be in cache          |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| end              | hh:mm                           | End of working hours                                                      |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| **Periods**      |                                 |                                                                           |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| Period 1         | Ex : 0-20 ( seconds )           | Used for period statistics, as call answered within Period X etc ...      |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| Period n         | Ex : 0-20 ( seconds )           | Used for period statistics, as call answered within Period X etc ...      |
+------------------+---------------------------------+---------------------------------------------------------------------------+

.. note:: Statistics are computed on full hours only. If work hours are from 8h30 to 16h15,
    working hours should be set from 8h to 17h.


How to generate the cache
-------------------------

To get the reporting to work, the cache must be generated. The cache is
generated automatically and periodically. By default, it is re-generated every
day.

However, you can do it manually safely. The script to generate the cache is
*xivo-stat fill_db*.  When this script is run, all stats are computed from the
last fill_db to the end of the previous hour.

.. note:: *xivo-stat fill_db* can be a long operation when used for the first time or after a *xivo-stat clean_db*.

.. note:: *xivo-stat fill_db* will only compute the statistics up to the last complete hour.
    ie. at 12h47, statistics will be computed from the last *xivo-stat fill_db* to 11h59 59s


Cleaning the cache
------------------

If for some reason the cache generation fails and the cache becomes unusable,
the administrator can safely clean the cache using *xivo_stat clean_db* and then
re-generate it. This does *not* erase any data.


Queue statistics
================

Queue statistics can be viewed in :menuselection:`Services --> Statistics --> Queue`.

.. figure:: images/statistic_queue.png
   :scale: 85%
   :alt: Queue statistic


Counters
--------

* Received: Number of received calls
* Answered: Calls answered by an agent
* Abandoned: The caller hanged up while waiting for an answer
* Dissuaded or Overflowed:

  * Closed: Calls received when the queue was closed
  * No answer (NA): The call reached the ring timeout delay
  * Satured: The queue was already full when the call was received or one of the diversion parameter was reached
  * Blocking : There was no agent available when the call was received or there is no agent to take the call anymore

* Average waiting time (AWT): The average wait time of call that have waited
* Answered rate (HR): The ratio of answered calls over received calls
* Quality of service (QoS): Percentage of calls answered in less than x seconds
  over the number of answered calls, where x is defined in the configuration


Agent performance
=================

Agent performance statistics can be viewed in :menuselection:`Services --> Statistics --> Agent`.

.. figure:: images/statistic_agent.png
    :scale: 85%
    :alt: Queue statistic


Counters
--------

* Answered: The number of answered calls for this agent.
* Conversation: Time spent in conversation for calls answered during a given period.
