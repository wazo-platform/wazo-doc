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
| 13.25 to 14.17 | xivo-fai-14.06              |
+----------------+-----------------------------+


Upgrade from an archive to current version
==========================================

Archive version < 13.25::

   apt-get update
   apt-get install -t squeeze-xivo-skaro-$(cat /usr/share/xivo/XIVO-VERSION) xivo-fai xivo-fai-skaro
   xivo-upgrade

.. We need the old xivo-fai (squeeze), because the new xivo-fai (xivo-five) conflicts with
   xivo-fai-skaro. We need xivo-fai-skaro at least to download postgresql-9.1.

Archive version >= 13.25 and < 14.18::

   apt-get update
   apt-get install xivo-fai
   xivo-upgrade

Archive version >= 14.18::

  xivo-dist xivo-five
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

Current version after 14.18::

   xivo-dist xivo-15.12
   xivo-upgrade

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
   echo "deb http://mirror.xivo.io/archive xivo-13.25 main" > /etc/apt/sources.list.d/xivo-13.25.list
   apt-get update
   apt-get install xivo-fai-13.25
   rm /etc/apt/sources.list.d/xivo-13.25.list
   apt-get purge xivo-fai-skaro-13.02
   apt-get update
   xivo-upgrade

Source and destination archive version after 14.18::

   xivo-dist xivo-15.12
   xivo-upgrade
