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

asterisk
--------

web-interface
-------------

xivo-confgend
-------------

xivo-ctid
---------
The log file of xivo-ctid is managed by logrotate.

It's configuration file is '/etc/logrotate.d/xivo-ctid'.

Defaults configuration

* Max log file size: 100M
* Number of archived log files: 15
* Log date: daily
* File location: '/var/log/xivo-ctid.pid'

