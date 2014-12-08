.. _xivo-dird:

===========
 XiVO dird
===========

xivo-dird is the directory server for XiVO. It offers a simple REST interface
to query all directories that are configured. xivo-dird is meant to be
extendable with plugins.

.. toctree::
   :maxdepth: 1

   configuration
   developer
   stock_plugins


.. _xivo-dird-usage:

Launching xivo-dird
===================

::

   usage: xivo-dird [-h] [-c CONFIG_FILE] [-d] [-f] [-l LOG_LEVEL] [-u USER]

   optional arguments:
     -h, --help            show this help message and exit
     -c CONFIG_FILE, --config-file CONFIG_FILE
                           The path where is the config file. Default: /etc/xivo-dird/config.yml
     -d, --debug           Log debug messages. Overrides log_level. Default:
                           False
     -f, --foreground      Foreground, don't daemonize. Default: False
     -l LOG_LEVEL, --log-level LOG_LEVEL
                           Logs messages with LOG_LEVEL details. Must be one of:
                           critical, error, warning, info, debug. Default: info
     -u USER, --user USER  The owner of the process.


Terminology
===========

Back-end
--------

A back-end is a plugin implementation to query a given directory.


Source
------

A source is an instance of a back-end. Given a csv back-end I can have many
configurations, each of these configurations is called a source. For example,
I could have the customer-csv and the employee-csv sources. All using the csv
back-end.


Plugins
-------

A plugin is an extension point in xivo-dird. It is a way to add or modify the
functionality of xivo-dird.


API
===

See :ref:`dird-api`.
