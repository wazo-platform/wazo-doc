************
Debug Daemon
************


Here's how to run the various daemon present in XiVO in foreground and debug mode.

Note that it's usually a good idea to stop monit `/etc/init.d/monit stop` before running a daemon in foreground.

agid
----

 agid -f -d

* -f for foreground
* -d for debug

confgend
--------

 twistd -no --python=/usr/bin/xivo-confgend

No debug mode in confgend.

dxtora
------

 dxtora -f

* -f for foreground

provd
-----

 twistd -no provd -s -v

* -s for logging to stderr
* -v for verbose

sysconfd
--------

 sysconfd -l debug -f

* -l debug for debug level logging
* -f for foreground

xivo-ctid
---------

 xivo-ctid -d

* -d for foreground and debug
