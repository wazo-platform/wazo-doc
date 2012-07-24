**********
Statistics
**********

Configuration
=============

In order to be able to display call center statistics you have first to create one or more configuration.

.. figure:: images/Statistic_configuration.png
   :scale: 90%
   :alt: Statistics Configuration

   Statistics Configuration

This configuration is used to generate statistic cache and to allow user to display statistic with XiVO web interface

General Architecture
--------------------

.. figure:: images/Statistic_archi.png
   :scale: 90%
   :alt: Statistics Architecture

   Statistics Architecture


Configuration
-------------

+------------------+---------------------------------+---------------------------------------------------------------------------+
| Field            | Values                          | Description                                                               |
|                  |                                 |                                                                           |
+==================+=================================+===========================================================================+
|                  |                                 |                                                                           |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| name             | string                          | Any name usefull to remember what the configuration is used to            |
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
| start            | hh:nmm                          | beginning of work, data of of working hours will not be in cache          |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| end              | hh:nmm                          | End of working hours                                                      |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| **Periods**      |                                 |                                                                           |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| Period 1         | Ex : 0-20 ( seconds )           | Used for period statistics, as call answered within Period X etc ...      |
+------------------+---------------------------------+---------------------------------------------------------------------------+
| Period n         | Ex : 0-20 ( seconds )           | Used for period statistics, as call answered within Period X etc ...      |
+------------------+---------------------------------+---------------------------------------------------------------------------+


When a configuration created, cache has to be generated for each object type

.. figure:: images/Statistic_cache.png
   :scale: 90%
   :alt: Statistics Cache

   Statistics Cache


How to generate the cache
-------------------------

To get the reporting to work, the cache must be generated. The script to generate the cache is *xivo-stat fill_db*.
When *xivo-stat fill_db* is run, all stats are computed from the last fill_db to the end of the previous hour.

.. warning:: *xivo-stat fill_db* can be a long operation when used for the first time or after a *xivo-stat clean_db*.


Cleaning the cache
------------------

If for some reason the cache generation fails and the cache becomes unusable, the administrator can clean the cache
using *xivo_stat clean_db*.


Queue statistics
================

Queue statistics can be viewed in :menuselection:`Services --> Statistics --> Queue`.

.. figure:: images/statistic_queue.png
   :scale: 85%
   :alt: Queue statistic


Counters
--------

* Total: Number of received calls
* Answered: Calls answered by an agent
* Abandonned: The caller hanged up while waiting for an answer
* Close: Calls received when the queue was closed
* No answer (NA): The call reached the ringtimeout delay
* Busy: The queue was already full when the call was received
* Join empty (JE): There was no agent available when the call was received
* Leave empty (LE): There is no agent to take the call anymore
* Average waiting time (AWT): The average wait time of call that have waited
* Home rated (HR): The ratio of answered calls over received calls
* Quality of service (QoS): Percentage of calls answered in less than x seconds over the number of answered calls, where x is defined in the configuration
