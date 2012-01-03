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

Log Files
========= 

agid
----
Default configuration

* File location: '/var/log/daemon.log'

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
Default configuration

* File location: '/var/log/daemon.log'

sysconfd
--------
Default configuration

* File location: '/var/log/daemon.log'

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

