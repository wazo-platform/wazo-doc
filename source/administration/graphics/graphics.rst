********
Graphics
********

The Services/Graphics section gives a historical overview of a Wazo system's
activity based on snapshots recorded every 5 minutes.
Graphics are available for the following resources :

* CPU
* Entropy
* Interruptions
* IRQ Stats
* System Load
* Memory Usage
* Open Files
* Open Inodes
* Swap Usage

Each section is presented as a series of 4 graphics : daily, weekly, monthly
and yearly history. Each graphic can be clicked on to zoom. All information presented is read only.

.. figure:: graphics_overview.png
   :scale: 85%


Troubleshooting
===============

Missing graphs
--------------

Symptoms:

* daily graphs are missing
* weekly/monthly/yearly graphs stop updating
* a mail is sent from cron every 5 minutes about a "bad magic number"

Cause:

* the machine was forcefully stopped, while munin (responsible for the graphs) was running,
  resulting in a file corruption

Resolution:

* Run the following command::

   rm /var/lib/munin/htmlconf.storable /var/lib/munin/limits.storable

* The graphs will be restored on the next run of munin, in the next 5 minutes.
