.. _debug-daemons:

*****************
Debugging Daemons
*****************

Here's how to run the various daemons present in XiVO in foreground and debug mode.

Note that it's usually a good idea to stop monit before running a daemon in foreground.


agentd
======

::

   xivo-agentd -f -v

* -f for foreground
* -v for verbose

Log file: ``/var/log/xivo-agentd.log``

::

    2013-10-29 11:03:55,799 [25830] (INFO): Starting xivo-agentd
    2013-10-29 11:03:58,632 [25830] (INFO): Executing statuses command


agid
====

::

   xivo-agid -f -d

* -f for foreground
* -d for debug

Log file: ``/var/log/xivo-agid.log``

::

   2014-06-18 11:01:02,816 [28779] (INFO) (xivo_agid.agid): xivo-agid starting...
   2014-06-18 11:01:04,479 [28779] (INFO) (xivo_agid.modules.callerid_forphones): executing update command 'update-config'
   2014-06-18 11:01:04,877 [28779] (INFO) (xivo_agid.modules.callerid_forphones): executing update command 'update-phonebook'


amid
====

::

   xivo-amid -f -v

* -f for foreground
* -v for verbose

Log file: ``/var/log/xivo-amid.log``

::

    2014-01-15 10:36:42,372 [5252] (INFO): Starting xivo-amid
    2014-01-15 10:36:42,372 [5252] (INFO): Connecting socket
    2014-01-15 10:36:42,372 [5252] (INFO): Connecting AMI client to localhost:5038


call-logd
=========

::

   xivo-call-logd -f -v

* -f for foreground
* -v for verbose

Log file: ``/var/log/xivo-call-logd.log``

::

    2014-02-12 14:58:05,051 [14650] (INFO): Starting xivo-call-logd
    2014-02-12 14:58:05,178 [14650] (INFO): Running...


confgend
========

::

   twistd -no --python=/usr/bin/xivo-confgend

No debug mode in confgend.

Log file: ``/var/log/xivo-confgend.log``

::

    2013-10-29 11:03:50-0400 [-] Starting factory <xivo_confgen.confgen.ConfgendFactory instance at 0x8ef970c>
    2013-10-29 11:03:55-0400 [Confgen,0,127.0.0.1] serving asterisk/features.conf
    2013-10-29 11:03:55-0400 [Confgen,1,127.0.0.1] serving asterisk/musiconhold.conf


ctid
====

::

   xivo-ctid -f -d

* -d for debug
* -f for foreground

Log file: ``/var/log/xivo-ctid.log``

::

    2013-10-29 11:03:58,789 xivo-ctid[25914] (INFO) (main): CTI Fully Booted in 0.660311 seconds
    2013-10-29 11:03:58,789 xivo-ctid[25914] (INFO) (interface_ami): Asterisk Call Manager/1.3
    2013-10-29 11:03:58,827 xivo-ctid[25914] (INFO) (AMI logger): Event received:Privilege=>system,all ModuleLoadStatus=>Done Event=>ModuleLoadReport ModuleCount=>169 ModuleSelection=>All


dxtora
======

::

   dxtora -f

* -f for foreground

Log file: ``/var/log/daemon.log``. Lines start with ``xivo-dxtora``.

::

    Oct 28 09:24:48 hostname xivo-dxtora[1399]: Received signal, exiting.
    Oct 28 09:24:58 hostname xivo-dxtora[8562]: Pulling DHCP info from unix socket


provd
=====

::

   twistd -no -r epoll xivo-provd -s -v

* -s for logging to stderr
* -v for verbose


Log file: ``/var/log/xivo-provd.log``

::

   2014-06-18 12:04:54,299 [8564] (INFO) (provd.main): Binding HTTP REST API service to "0.0.0.0:8666"
   2014-06-18 12:04:54,320 [8564] (INFO) (twisted): Site starting on 8666


restapi
=======

::

    xivo-restapid -f -d

* -f for foreground
* -d for debug messages

Log file: ``/var/log/xivo-restapid.log``

::

   2013-10-28 10:02:00,352 xivo-restapid[8905] (INFO) (xivo_restapi.flask_http_server): POST http://127.0.0.1:50050/1.1/devices with data {"mac":"00:00:00:00:00:00","template_id":"defaultconfigdevice","description":""}
   2013-10-28 10:04:35,815 xivo-restapid[8905] (INFO) (xivo_restapi.flask_http_server): GET http://127.0.0.1:50050/1.1/devices


sysconfd
========

::

   xivo-sysconfd -l debug -f

* -l debug for debug level logging
* -f for foreground

Log file: ``/var/log/xivo-sysconfd.log``

::

   2014-06-18 12:00:23,221 [8277] (INFO) (xivo-sysconfd): locking PID
   2014-06-18 12:00:23,233 [8277] (INFO) (xivo-sysconfd): pidfile ok
   2014-06-18 12:00:23,237 [8277] (INFO) (http_json_server): will now serve
