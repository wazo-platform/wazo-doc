********************
XiVO Daemon Skeleton
********************

Description
===========

Example for xivo-testd

- /etc/xivo/xivo-testd/testd.yml
- /var/log/xivo-testd.log
- /var/run/xivo-testd/xivo-testd.pid
- /tmp/xivo-testd/rest-api.sock

- bin/
- bin/xivo-test

- debian/
- debian/xivo-testd.dirs
- debian/xivo-testd.init
- debian/xivo-testd.install
- debian/xivo-testd.links
- debian/xivo-testd.logrotate
- debian/xivo-testd.postinst

- etc/
- etc/nginx/site-available/xivo-testd
- etc/xivo/xivo-testd/xivo-testd.yml

- xivo_test/
- xivo_test/bin/
- xivo_test/bin/xivo_test.py
- xivo_test/config.py

bin/ directory
==============

bin/xivo-test
-------------

.. literalinclude:: skeleton/bin/xivo-test
   :language: python



debian/ directory
=================

debian/xivo-testd.dirs
----------------------

.. literalinclude:: skeleton/debian/xivo-testd.dirs
   :language: bash


debian/xivo-testd.init
----------------------

.. literalinclude:: skeleton/debian/xivo-testd.init
   :language: bash


debian/xivo-testd.install
-------------------------

.. literalinclude:: skeleton/debian/xivo-testd.install
   :language: bash


debian/xivo-testd.links
-----------------------

.. literalinclude:: skeleton/debian/xivo-testd.links
   :language: bash


debian/xivo-testd.logrotate
---------------------------

.. literalinclude:: skeleton/debian/xivo-testd.logrotate
   :language: bash


debian/xivo-testd.postinst
--------------------------

.. literalinclude:: skeleton/debian/xivo-testd.postinst
   :language: bash


debian/xivo-libtest.install
---------------------------

.. literalinclude:: skeleton/debian/xivo-testd.install
   :language: bash



/ directory
===========

/etc/nginx/site-available/xivo-testd
------------------------------------

.. literalinclude:: skeleton/etc/nginx/site-available/xivo-testd
   :language: bash

/etc/xivo/xivo-testd/xivo-testd.yml
-----------------------------------

Example of configuration file depending on the daemon...

.. literalinclude:: skeleton/etc/xivo/xivo-testd/xivo-testd.yml
   :language: yaml



xivo_test/ directory
====================

xivo_test/bin/xivo_testd.py
---------------------------

.. literalinclude:: skeleton/xivo_test/bin/xivo_testd.py
   :language: python


xivo_test/config.py
-------------------

.. literalinclude:: skeleton/xivo_test/config.py
   :language: python

