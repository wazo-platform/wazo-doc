********
Graphics
********

There are graphics, locate to :file:`/var/cache/munin/www/localdomain/localhost.localdomain/`, that
give a historical overview of a Wazo system's activity based on snapshots recorded every 5 minutes.
Graphics are available for the following resources :

* :file:`cpu-*.png`
* :file:`entropy-*.png`
* :file:`interrupts-*.png`
* :file:`irqstats-*.png`
* :file:`load-*.png`
* :file:`memory-*.png`
* :file:`open_files-*.png`
* :file:`open_inodes-*.png`
* :file:`swap-*.png`

Each graphic is available with different time range: ``day``, ``week``, ``month``, ``year``


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
