.. _purge_logs:

**********
Purge Logs
**********

Keeping records of personal communications for long periods may be subject to local legislation, to
avoid personal data retention. Also, keeping too many records may become resource intensive for the
server. To ease the removal of such records, ``xivo-purge-db`` is a process that removes old log
entries from the database. This allows keeping records for a maximum period and deleting older ones.

By default, xivo-purge-db removes all logs older than a year (365 days). xivo-purge-db is run
nightly.

.. note:: Please check the laws applicable to your country and modify ``days_to_keep`` (see below)
          in the configuration file accordingly.


Tables Purged
-------------

The following features are impacted by xivo-purge-db:

- :ref:`call_logs`
- :ref:`Call center statistics <call_center_stats>`

More technically, the tables purged by ``xivo-purge-db`` are:

-  ``call_logs``
-  ``cel``
-  ``queue_log``
-  ``stat_agent_periodic``
-  ``stat_call_on_queue``
-  ``stat_queue_periodic``


Configuration File
------------------

We recommend to override the setting ``days_to_keep`` from ``/etc/xivo-purge-db/config.yml`` in a
new file in ``/etc/xivo-purge-db/conf.d/``. Setting ``days_to_keep`` to 0 will NOT disable
``xivo-purge-db``, and will remove ALL logs from your system.

See :ref:`configuration-priority` and ``/etc/xivo-purge-db/config.yml`` for more details.


Manual Purge
------------

It is possible to purge logs manually. To do so, log on to the target XiVO server and run::

    xivo-purge-db

You can specify the number of days of logs to keep. For example, to purge entries older than 365
days::

    xivo-call-logs -d 365

Usage of ``xivo-purge-db``::

    usage: xivo-purge-db [-h] [-d DAYS_TO_KEEP]

    optional arguments:
      -h, --help            show this help message and exit
      -d DAYS_TO_KEEP, --days_to_keep DAYS_TO_KEEP
                            Number of days data will be kept in tables


Plugins
-------

A plugin is an extension point in xivo-purge-db. It is a way to add or modify the functionality of
xivo-purge-db. The only plugin available is `archives` to execute some codes before purging the database.


Archive Plugins (for Developpers)
---------------------------------

The only thing that plugin need to implement, is a ``days_to_keep`` as argument in its constructor. There
are no method that ``xivo-purge-db`` call after instantiation.

The following example can be found in `git repo`_

.. _git repo: https://github.com/xivo-pbx/xivo-purge-db/tree/master/contribs


Example
*******

Archive name: sample

Purpose: demonstrate how to create your own archive plugin.


Activate plugin
^^^^^^^^^^^^^^^

Example of file added in ``/etc/xivo-purge-db/conf.d/``:

.. code-block:: yaml
   :linenos:

    enabled_plugins:
        archives:
            - sample


sample.py
^^^^^^^^^

The following example will be save a file in ``/tmp/xivo_purge_db.sample`` with ``Save tables
before purge. 365 days to keep!`` as content by default.

.. code-block:: python
   :linenos:

    sample_file = '/tmp/xivo_purge_db.sample'


    class SamplePlugin(object):

        def __init__(self, days_to_keep):
            with open(sample_file, 'w') as output:
                output.write('Save tables before purge. {0} days to keep!'.format(days_to_keep))


Install sample plugin
^^^^^^^^^^^^^^^^^^^^^

The following setup.py shows an example of a python library that add a plugin:

.. code-block:: python
   :linenos:
   :emphasize-lines: 15-17

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    from setuptools import setup
    from setuptools import find_packages


    setup(
        name='xivo-purge-db-sample-plugin',
        version='0.0.1',

        description='An example program',
        packages=find_packages(),
        entry_points={
            'xivo_purge_db.archives': [
                'sample = xivo_purge_db_sample.sample:SamplePlugin',
            ],
        }
    )
