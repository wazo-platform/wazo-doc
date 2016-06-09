.. _debug-daemons:

*****************
Debugging Daemons
*****************

To activate debug mode, add ``debug: true`` in the daemon :ref:`configuration file
<configuration-files>`). The output will be available in the daemon's :ref:`log file <log-files>`.

It is also possible to run the XiVO daemon, in command line. This will allow to run in foreground
and debug mode. To see how to use it, type::

   xivo-{name} -h

Note that it's usually a good idea to stop monit before running a daemon in foreground::

   systemctl stop monit.service


xivo-confgend
=============

::

   twistd -no --python=/usr/bin/xivo-confgend

No debug mode in confgend.


xivo-provd
==========

::

   twistd -no -u xivo-provd -g xivo-provd -r epoll xivo-provd -s -v

* -s for logging to stderr
* -v for verbose


consul
======

::

   sudo -u consul /usr/bin/consul agent -config-dir /etc/consul/xivo -pid-file /var/run/consul/consul.pid

There is no log file, but you can consult the output of consul with::

  consul monitor

::

   2015/08/03 09:48:25 [INFO] consul: cluster leadership acquired
   2015/08/03 09:48:25 [INFO] consul: New leader elected: this-xivo
   2015/08/03 09:48:26 [INFO] raft: Disabling EnableSingleNode (bootstrap)
   2015/08/03 11:04:08 [INFO] agent.rpc: Accepted client: 127.0.0.1:41545
