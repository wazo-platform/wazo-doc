***************************
Wazo Package File Structure
***************************

Package naming
==============

Let's assume we want to organise the files for xivo-confd.

* Git repo name: ``xivo-confd``
* Binary file name: ``xivo-confd``
* Python package name: ``xivo_confd``

::

   xivo-confd
   |-- bin
   |   `-- xivo-confd
   |-- contribs
   |   `-- docker
   |       |-- ...
   |       `-- prod
   |           `-- ...
   |-- debian
   |   `-- ...
   |-- Dockerfile
   |-- docs
   |   `-- ...
   |-- etc
   |   `-- ...
   |-- integration-tests
   |   `-- ...
   |-- LICENSE
   |-- README.md
   |-- requirements.txt
   |-- setup.cfg
   |-- setup.py
   |-- test-requirements.txt
   |-- .travis.yml
   `-- xivo_confd
       `-- ...

Sources
-------

``etc/``
   Contains default configuration files.

``docs/``
   Contains technical documentation for this package: API doc, architecture doc, diagrams, ...
   Should be in RST format using Sphinx.

``bin/``
   Contains the binaries. Not applicable for pure libraries.

``integration_tests/``
   Contains the tests bigger than unit-tests. Tests should be runnable simply, e.g.
   ``nosetests integration_tests``.

``README.md``
   Read me in markdown (Github flavor).

``LICENSE``
   License (GPLv3)

``.travis.yml``
   Travis CI configuration file


Python
------

Standard files:

* setup.py
* setup.cfg
* requirements.txt
* test-requirements.txt
* xivo_confd/ (the main sources)


Debian
------

``debian/``
   Contains the Debian packaging files (``control``, ``rules``, ...)


Docker
------

``Dockerfile``
   Used to build a docker image for a working production version

``contribs/docker/prod/``
   Contains the files necessary for running xivo-confd inside a production Docker image

``contribs/docker/other/``
   Contains the Dockerfile and other files to run xivo-confd inside Docker with specific configuration


File naming
===========

* PID file: ``/var/run/xivo-confd/xivo-confd.pid``
* WSGI socket file: ``/var/run/xivo-confd/xivo-confd.sock``
* Config file: ``/etc/xivo-confd/config.yml``
* Log file: ``/var/log/xivo-confd.log``
* Static data files: ``/usr/share/xivo-confd``
* Storage data files: ``/var/lib/xivo-confd``
