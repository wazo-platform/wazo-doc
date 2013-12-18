*****************************************
Upgrade involving archive version of XiVO
*****************************************

Archive package names
=====================

Archive packages are named as follow:

+----------------+-----------------------------+
| XiVO version   | Archive package name        |
+================+=============================+
| 1.2 to 1.2.12  | pf-fai-xivo-1.2-skaro-1.2.1 |
+----------------+-----------------------------+
| 12.14 to 13.24 | xivo-fai-skaro-13.04        |
+----------------+-----------------------------+
| from 13.25     | xivo-fai-13.25              |
+----------------+-----------------------------+


Upgrade to current version from an archive
==========================================

::

   apt-get update
   apt-get install xivo-fai
   apt-get update
   apt-get install xivo-fai
   apt-get update
   xivo-upgrade

As a result, xivo-upgrade will always upgrade XiVO to the latest stable version.

From the current version, use an archive version
================================================

::

   apt-get update
   apt-get install xivo-fai-13.25
   apt-get purge xivo-fai xivo-fai-skaro
   apt-get update

As a result, xivo-upgrade will not upgrade XiVO to a greater version than the archive you chose.


Upgrade from an archive version to another archive version
==========================================================

Downgrades are not supported: you can only upgrade to a greater version.

From 1.2 to 13.24::

   apt-get update
   echo "deb http://mirror.xivo.fr/archive squeeze-xivo-skaro-13.24 main" > /etc/apt/sources.list.d/xivo-13.24.list
   apt-get update
   apt-get install xivo-fai-skaro-13.24
   rm /etc/apt/sources.list.d/xivo-13.24.list
   apt-get purge xivo-fai-skaro-13.02
   apt-get update
   xivo-upgrade

From 13.25::

   apt-get update
   echo "deb http://mirror.xivo.fr/archive xivo-13.25 main" > /etc/apt/sources.list.d/xivo-13.25.list
   apt-get update
   apt-get install xivo-fai-13.25
   rm /etc/apt/sources.list.d/xivo-13.25.list
   apt-get purge xivo-fai-skaro-13.02
   apt-get update
   xivo-upgrade
