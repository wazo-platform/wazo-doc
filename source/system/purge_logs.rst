.. _purge_logs:

**********
Purge Logs
**********

xivo-purge-db is a process that removes old log entries from the database. This allows
keeping records for a maximum period and deleting older ones.

xivo-purge-db is run nightly.


.. note:: Keeping records for long periods maybe subject to local legislation.
          Please verify your laws and modify `days_to_keep` in the configuration file.


Tables Purged
-------------

These tables are purged by `xivo-purge-db`

-  `call_logs`
-  `cel`
-  `queue_log`
-  `stat_agent_periodic`
-  `stat_call_on_queue`
-  `stat_queue_periodic`


Configuration File
------------------

It suggested to overload variable `days_to_keep` in a new file in ``/etc/xivo-purge-db/conf.d/``

See :ref:`configuration-priority` for more details.


Manual Purge
------------

It is possible to purge logs manually. To do so, log on to the target XiVO server and run::

    xivo-purge-db

You can specify the number of days of logs to keep.
For example, to purge entries older than 365 days::

    xivo-call-logs -d 365

Usage of `xivo-purge-db`::

    usage: xivo-purge-db [-h] [-d DAYS_TO_KEEP]

    optional arguments:
      -h, --help            show this help message and exit
      -d DAYS_TO_KEEP, --days_to_keep DAYS_TO_KEEP
                            Number of days data will be kept in tables
