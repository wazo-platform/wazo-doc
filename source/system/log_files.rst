.. _log-files:

*********
Log Files
*********

Every XiVO service has its own log file, placed in :file:`/var/log`.


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


xivo-agentd
-----------

* File location: :file:`/var/log/xivo-agentd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-agentd`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-agid
---------

* File location: :file:`/var/log/xivo-agid.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-agid`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-amid
---------

* File location: :file:`/var/log/xivo-amid.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-amid`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-auth
---------

* File location: :file:`/var/log/xivo-auth.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-auth`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-call-logd
--------------

* File location: :file:`/var/log/xivo-call-logd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-call-logd`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-confd
----------

* File location: :file:`/var/log/xivo-confd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-confd`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-confgend
-------------

The xivo-confgend daemon output is sent to the file specified with the ``--logfile`` parameter when
launched with twistd.

The file location can be changed by customizing the xivo-confgend.service unit file.

* File location: :file:`/var/log/xivo-confgend.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-confgend`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-ctid
---------

* File location: :file:`/var/log/xivo-ctid.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-ctid`
* Number of archived log files: 15
* Rotation frequence: Daily


xivo-ctid-ng
------------

* File location: :file:`/var/log/xivo-ctid-ng.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-ctid-ng`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-dird
---------

* File location: :file:`/var/log/xivo-dird.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-dird`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-dird-phoned
----------------

* File location: :file:`/var/log/xivo-dird-phoned.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-dird-phoned`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-dxtora
-----------

* File location: :file:`/var/log/xivo-dxtora.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-dxtora`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-provd
----------

* File location: :file:`/var/log/xivo-provd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-provd`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-purge-db
-------------

* File location: :file:`/var/log/xivo-purge-db.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-purge-db`
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


xivo-upgrade
------------

* File location: :file:`/var/log/xivo-upgrade.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-upgrade`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-web-interface
------------------

* File location: :file:`/var/log/xivo-web-interface/\*.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-web-interface`
* Number of archived files: 21
* Rotation frequence: Daily


xivo-websocketd
---------------

* File location: :file:`/var/log/xivo-websocketd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-websocketd`
* Number of archived files: 15
* Rotation frequence: Daily
