*********
Upgrading
*********


Upgrading to 1.2 from a previous version is not supported right now.

To upgrade from a prior 1.2 version, you need to use xivo-upgrade :

::

 xivo-upgrade

This script will be update xivo and restart all daemons

For version before rc-1, you need to use aptitude/apt-get:

::

 apt-get update && apt-get dist-upgrade

Since RC 1
==========

You can use xivo-upgrade


To Beta 2
=========

* confgen package was not correctly generated in Beta 1

::

 apt-get install xivo-confgen=1:1.2~beta-2.3-1
 apt-get install xivo-confgend=1:1.2~beta-2.3-1
 apt-get install xivo-libconfgend=1:1.2~beta-2.3-1

Alpha 5 to Alpha 6
==================

::

 aptitude update
 aptitude full-upgrade
