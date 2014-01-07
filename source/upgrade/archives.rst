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
   apt-get install xivo-fai/squeeze-xivo-skaro-$(cat /usr/share/pf-xivo/XIVO-VERSION) xivo-fai-skaro
   apt-get update
   xivo-upgrade

As a result, xivo-upgrade will always upgrade XiVO to the latest stable version.

From the current version, use an archive version
================================================

Downgrades are not supported: you can only upgrade to a greater version.

Current version between 1.2 and 13.24::

   apt-get update
   apt-get install xivo-fai-skaro-13.23
   apt-get purge xivo-fai-skaro
   apt-get update

Current version after 13.25::

   apt-get update
   apt-get install xivo-fai-13.25
   apt-get purge xivo-fai
   apt-get update

As a result, xivo-upgrade will not upgrade XiVO to a greater version than the archive you chose.


Upgrade from an archive version to another archive version
==========================================================

Downgrades are not supported: you can only upgrade to a greater version.

Source and destination archive version between 1.2 to 13.24::

   apt-get update
   apt-get install xivo-fai-skaro-13.24
   apt-get purge xivo-fai-skaro-13.02
   apt-get update
   xivo-upgrade

Source or destination archive version after 13.25::

   apt-get update
   echo "deb http://mirror.xivo.fr/archive xivo-13.25 main" > /etc/apt/sources.list.d/xivo-13.25.list
   apt-get update
   apt-get install xivo-fai-13.25
   rm /etc/apt/sources.list.d/xivo-13.25.list
   apt-get purge xivo-fai-skaro-13.02
   apt-get update
   xivo-upgrade
