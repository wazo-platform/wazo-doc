**********
Statistics
**********

Introduction
============

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


