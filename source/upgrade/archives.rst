*****************************************
Upgrade involving archive version of XiVO
*****************************************

Introduction
============

What is an archive version?
---------------------------

An archive version refers to a XiVO installation whose version is frozen: you can't upgrade it until
you manually change the upgrade server.

What is the point?
------------------

Using archive versions enable you to upgrade your XiVO to a specific version, in case you don't want
to upgrade to the latest (which is not recommended, but sometimes necessary). You will then be able
to upgrade your newer archive version to the latest version or to an even newer archive version.

Prerequisites
=============

.. warning:: These procedures are *complementary* to the upgrade procedure listed in
             :ref:`version_specific_upgrade`. You must follow the version-specific procedure
             *before* running the following procedures.

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
| 14.18+         | *packages removed*          |
+----------------+-----------------------------+


Upgrade from an archive to the latest version
=============================================

Archive version < 13.25::

   apt-get update
   apt-get install {xivo-fai,xivo-fai-skaro}/squeeze-xivo-skaro-$(cat /usr/share/pf-xivo/XIVO-VERSION)
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

As a result, xivo-upgrade will upgrade XiVO to the latest stable version.

Upgrade from an older non-archive version to a newer archive version
====================================================================

Non-archive version means any "normal" way of installing XiVO (ISO install, script install over
pre-installed Debian, xivo-upgrade).

Downgrades are not supported: you can only upgrade to a greater version.

We only support upgrades to archive versions >= 13.25, e.g. you can upgrade a 12.16 to 14.16, but
not 12.16 to 13.16

Current version before 14.18 (here 13.25)
-----------------------------------------

::

   apt-get install xivo-fai-13.25

You are now considered in an archived version, see the section `Upgrade from an older archive
version to a newer archive version`_ below.

Current version after 14.18
---------------------------

::

   xivo-dist xivo-15.12
   apt-get update
   apt-get install xivo-upgrade/xivo-15.12
   xivo-upgrade


Upgrade from an older archive version to a newer archive version
================================================================

Downgrades are not supported: you can only upgrade to a greater version.

We only support upgrades to archive versions >= 13.25, e.g. you can upgrade a 12.16 to 14.16, but
not 12.16 to 13.16

1.2 - 13.24 to 13.25 - 14.17 (here 1.2.3 to 14.16)
--------------------------------------------------

::

   cat > /etc/apt/preferences.d/50-xivo-14.16.pref <<EOF
   Package: *
   Pin: release a=xivo-14.16
   Pin-Priority: 700
   EOF

   cat > /etc/apt/sources.list.d/squeeze-archive.list <<EOF
   deb http://archive.debian.org/debian/ squeeze main
   EOF

   apt-get update
   apt-get install {xivo-fai,xivo-fai-skaro}/squeeze-xivo-skaro-1.2.3
   apt-get update
   apt-get install xivo-fai-14.16
   apt-get update
   apt-get install xivo-upgrade/xivo-14.16
   xivo-upgrade
   rm /etc/apt/preferences.d/50-xivo-14.16.pref
   rm /etc/apt/sources.list.d/squeeze-archive.list
   apt-get update

.. We need the old xivo-fai (squeeze), because the new xivo-fai (xivo-five) conflicts with
   xivo-fai-skaro. We need xivo-fai-skaro at least to download postgresql-9.1.
.. We need to explicitly install xivo-upgrade before running it, in case the admin has already run
   xivo-upgrade, but cancelled the upgrade.

13.25 - 14.16 to 13.25 - 14.17 (here 13.25 to 14.16)
----------------------------------------------------

::

   cat > /etc/apt/preferences.d/50-xivo-14.16.pref <<EOF
   Package: *
   Pin: release a=xivo-14.16
   Pin-Priority: 700
   EOF

   apt-get update
   apt-get install xivo-fai
   apt-get purge xivo-fai-13.25
   apt-get update
   apt-get install xivo-fai-14.16
   apt-get update
   apt-get install xivo-upgrade/xivo-14.16
   xivo-upgrade
   rm /etc/apt/preferences.d/50-xivo-14.16.pref

.. We need to explicitly install xivo-upgrade before running it, in case the admin has already run
   xivo-upgrade, but cancelled the upgrade.

13.25 - 14.17 to 14.18+ (here 14.05 to 15.11)
---------------------------------------------

::

   apt-get update
   apt-get install xivo-fai
   apt-get update
   apt-get install xivo-dist
   xivo-dist xivo-15.11
   apt-get purge 'xivo-fai*'
   apt-get update
   apt-get install xivo-upgrade/xivo-15.11
   xivo-upgrade

.. We need to explicitly install xivo-upgrade before running it, in case the admin has already run
   xivo-upgrade, but cancelled the upgrade.

14.18+ to 14.19+ (here 14.18 to 15.12)
--------------------------------------

::

   xivo-dist xivo-15.12
   apt-get update
   apt-get install xivo-upgrade/xivo-15.12
   xivo-upgrade

.. We need to explicitly install xivo-upgrade before running it, in case the admin has already run
   xivo-upgrade, but cancelled the upgrade.
