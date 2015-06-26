******
Backup
******

Periodic backup
===============

A backup of the database and the data are launched every day with a logrotate task.
It is run at 06:25 a.m. and backups are kept for 7 days.

Logrotate task:

    :file:`/etc/logrotate.d/xivo-backup`

Logrotate cron:

    :file:`/etc/cron.daily/logrotate`


Retrieve the backup
===================

You can retrieve the backup from the web-interface in
:menuselection:`Services --> IPBX --> IPBX Configuration --> Backup Files` page.

Otherwise, with shell access, you can retrieve them in :file:`/var/backups/xivo`.
In this directory you will find :file:`db.tgz` and :file:`data.tgz` files for the database and data
backups.

Backup script:

    :file:`/usr/sbin/xivo-backup`

Backup location:

    :file:`/var/backups/xivo`


What is actually backed-up?
===========================

Data
----

Here is the list of folders and files that are backed-up:

* :file:`/etc/asterisk`
* :file:`/etc/dahdi`
* :file:`/etc/dhcp`
* :file:`/etc/hostname`
* :file:`/etc/hosts`
* :file:`/etc/ldap`
* :file:`/etc/network/if-up.d/xivo-routes`
* :file:`/etc/network/interfaces`
* :file:`/etc/ntp.conf`
* :file:`/etc/xivo`
* :file:`/etc/resolv.conf`
* :file:`/etc/ssl`
* :file:`/etc/wanpipe`
* :file:`/var/lib/asterisk`
* :file:`/var/lib/consul`
* :file:`/var/lib/xivo`
* :file:`/var/lib/xivo-provd`
* :file:`/var/log/asterisk`
* :file:`/var/spool/asterisk`
* :file:`/usr/local/sbin`

The following files/folders are excluded from this backup:

* folders:

  * :file:`/var/lib/xivo-provd/plugins/*/var/cache/*`
  * :file:`/var/spool/asterisk/monitor`
  * :file:`/var/spool/asterisk/meetme`

* log files, coredump files
* audio recordings
* and, files greater than 10 MiB or folders containing more than 100 files if they belong to one of
  these folders:

  * :file:`/var/lib/xivo/sounds`
  * :file:`/var/lib/asterisk/sounds/custom`
  * :file:`/var/lib/asterisk/moh`
  * :file:`/var/spool/asterisk/voicemail`
  * :file:`/var/spool/asterisk/monitor`


Database
--------

Creating a database backup file manually
========================================

.. warning::

    A backup file may take a lot of space on the disk.
    You should check the free space on the partition before creating one.

You can manually create a *database* backup file named :file:`db-manual.tgz` in :file:`/var/tmp` by issuing the following commands::

   xivo-backup db /var/tmp/db-manual


Creating a data backup file manually
====================================

.. warning::

    A backup file may take a lot of space on the disk.
    You should check the free space on the partition before creating one.

You can manually create a *data* backup file named :file:`data-manual.tgz` in :file:`/var/tmp` by issuing the following commands::

   xivo-backup data /var/tmp/data-manual


.. _restore:

*******
Restore
*******

Introduction
============

A backup of both the configuration files and the database used by a XiVO installation is done
automatically every day.
These backups are created in the :file:`/var/backups/xivo` directory and are kept for 7 days.


Before Restoring the System
===========================

.. warning::

    Before restoring a XiVO on a fresh install you have to setup XiVO using the wizard (see :ref:`configuration_wizard` section).

Stop monit and all the xivo services::

   xivo-service stop


Restoring System Files
======================

System files are stored in the data.tgz file located in the :file:`/var/backups/xivo` directory.

This file contains for example, voicemail files, musics, voice guides, phone sets firmwares, provisioning server configuration database.

To restore the file ::

   tar xvfp /var/backups/xivo/data.tgz -C /


Restoring the Database
======================

.. warning::

    * This will destroy all the current data in your database.
    * You have to check the free space on your system partition before extracting the backups.
    * Be aware that this procedure applies **only to XiVO >= 14.08** (see the relevant upgrade notes).

Database backups are created as :file:`db.tgz` files in the :file:`/var/backups/xivo` directory.
These tarballs contains a dump of the database used in XiVO.

In this example, we'll restore the database from a backup file named :file:`db.tgz`
placed in the home directory of root.

First, extract the content of the :file:`db.tgz` file into the :file:`/var/tmp` directory and go inside
the newly created directory::

   tar xvf db.tgz -C /var/tmp
   cd /var/tmp/pg-backup

Drop the asterisk database and restore it with the one from the backup::

   sudo -u postgres dropdb asterisk
   sudo -u postgres pg_restore -C -d postgres asterisk-*.dump


Restoring and Keeping System Configuration
==========================================

System configuration like network interfaces is stored in the database. It is
possible to keep this configuration and only restore xivo data.

Rename the asterisk database to asterisk_previous::

   sudo -u postgres psql -c 'ALTER DATABASE asterisk RENAME TO asterisk_previous'

Restore the asterisk database from the backup::

   sudo -u postgres pg_restore -C -d postgres asterisk-*.dump

Restore the system configuration tables from the asterisk_previous database::

   sudo -u postgres pg_dump -c -t dhcp -t netiface -t resolvconf asterisk_previous | sudo -u postgres psql asterisk

Drop the asterisk_previous database::

   sudo -u postgres dropdb asterisk_previous

.. warning:: Restoring the data.tgz file also restores system files such as host
   hostname, network interfaces, etc. You will need to reapply the network
   configuration if you restore the data.tgz file.


After Restoring The System
==========================

Restart the services you stopped in the first step::

   xivo-service start

You may also reboot the system.
