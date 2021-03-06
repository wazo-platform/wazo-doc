.. _log-files:

*********
Log Files
*********

Every Wazo service has its own log file, placed in :file:`/var/log`.


asterisk
--------

The Asterisk log files are managed by logrotate.

It's configuration files :file:`/etc/logrotate.d/asterisk` and :file:`/etc/asterisk/logger.conf`

The message log level is enabled by default in :file:`logger.conf` and contains notices, warnings
and errors. The full log entry is commented in :file:`logger.conf` and should only be enabled when
verbose debugging is required. Using this option in production would produce VERY large log files.

* Files location: :file:`/var/log/asterisk/\*`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-auth
---------

* File location: :file:`/var/log/wazo-auth.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-auth`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-agid
---------

* File location: :file:`/var/log/wazo-agid.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-agid`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-calld
------------

* File location: :file:`/var/log/wazo-calld.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-calld`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-dird
---------

* File location: :file:`/var/log/wazo-dird.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-dird`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-upgrade
------------

* File location: :file:`/var/log/wazo-upgrade.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-upgrade`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-agentd
-----------

* File location: :file:`/var/log/wazo-agentd.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-agentd`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-amid
---------

* File location: :file:`/var/log/wazo-amid.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-amid`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-call-logd
--------------

* File location: :file:`/var/log/wazo-call-logd.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-call-logd`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-confd
----------

* File location: :file:`/var/log/wazo-confd.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-confd`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-confgend
-------------

The wazo-confgend daemon output is sent to the file specified with the ``--logfile`` parameter when
launched with twistd.

The file location can be changed by customizing the wazo-confgend.service unit file.

* File location: :file:`/var/log/wazo-confgend.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-confgend`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-phoned
-----------

* File location: :file:`/var/log/wazo-phoned.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-phoned`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-dxtora
-----------

* File location: :file:`/var/log/wazo-dxtora.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-dxtora`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-provd
----------

* File location: :file:`/var/log/wazo-provd.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-provd`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-purge-db
-------------

* File location: :file:`/var/log/wazo-purge-db.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-purge-db`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-stat
---------

* File location: :file:`/var/log/xivo-stat.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-stat`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-sysconfd
-------------

* File location: :file:`/var/log/xivo-sysconfd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-sysconfd`
* Number of archived files: 15
* Rotation frequence: Daily


wazo-websocketd
---------------

* File location: :file:`/var/log/wazo-websocketd.log`
* Rotate configuration: :file:`/etc/logrotate.d/wazo-websocketd`
* Number of archived files: 15
* Rotation frequence: Daily
