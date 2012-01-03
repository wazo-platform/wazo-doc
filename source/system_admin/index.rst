.. _system_admin:


*************************
System And Administration
*************************


High Availability
=================

Security
========

Hardware
========

Backup And Restore
==================

Internal Services
=================

sysconfd
--------

confgen
-------

ctid
----

.. _log-files:

Log Files
========= 
Many XiVO services use the syslog's '/var/log/daemon.log' file to log events.

This log file's configuration is located at '/etc/logrotate.d/rsyslog'

The default configuration for all services using this file is the following

* File location: '/var/log/daemon.log'
* Rotation frequence: Weekly
* Number of archived files: 4

agid
----
The agid log files are sent to the system's syslog.

See :ref:`log-files` above for global configuration info.

asterisk
--------
The Asterisk log files are managed by logrotate.

It's configuration files '/etc/logrotate.d/asterisk' and '/etc/asterisk/logger.conf'

The message log level is enabled by default in logger.conf and contains notices, warnings and errors.
The full log entry is commented in logger.conf and should only be enabled when verbose debugging is required. Using this option in production would VERY large log files.

Default configuration

* Files location: '/var/log/asterisk/\*'
* Number of archived files: 15
* Rotation frequence: Daily

provd
-----
Provd logs are send to the system's syslog.

See :ref:`log-files` above for global configuration info.

sysconfd
--------
Sysconfd logs are send to the system's syslog.

See :ref:`log-files` above for global configuration info.

web-interface
-------------

xivo-confgend
-------------
Default configuration

* File location: '/var/log/xivo-confgend.log'

xivo-ctid
---------
The xivo-ctid log file is managed by logrotate.

It's configuration file is '/etc/logrotate.d/xivo-ctid'.

Default configuration

* Max log file size: 100M
* Number of archived log files: 15
* Rotation frequence: Daily
* File location: '/var/log/xivo-ctid.pid'

