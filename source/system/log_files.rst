*********
Log Files
*********

Every XiVO service has its own log file, placed in :file:`/var/log`.

agid
----

* File location: :file:`/var/log/xivo-agid.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-agid`
* Number of archived files: 15
* Rotation frequence: Daily


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


provd
-----

* File location: :file:`/var/log/xivo-provd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-provd`
* Number of archived files: 15
* Rotation frequence: Daily


sysconfd
--------

* File location: :file:`/var/log/xivo-sysconfd.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-sysconfd`
* Number of archived files: 15
* Rotation frequence: Daily


web-interface
-------------

* File location: :file:`/var/log/xivo-web-interface/\*.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-web-interface`
* Number of archived files: 21
* Rotation frequence: Daily


xivo-confgend
-------------

The xivo-confgend daemon output is sent to the file specified with the ``--logfile`` parameter when
launched with twistd.

The file location can be changed in :file:`/etc/init.d/xivo-confgend`. Search the line begining with
``logfile=/var/log/xivo-confgend.log`` and change it to your liking.

* File location: :file:`/var/log/xivo-confgend.log`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-confgend`
* Number of archived files: 15
* Rotation frequence: Daily


xivo-ctid
---------

* File location: :file:`/var/log/xivo-ctid.pid`
* Rotate configuration: :file:`/etc/logrotate.d/xivo-ctid`
* Number of archived log files: 15
* Rotation frequence: Daily
