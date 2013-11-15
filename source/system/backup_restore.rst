******
Backup
******

Periodic backup
===============

A backup of the databases and the data are launched every day with a logrotate task.
It is run at 06:25 a.m. and backups are kept for 7 days.

Logrotate task:

    :file:`/etc/logrotate.d/xivo-backup`

Logrotate cron:

    :file:`/etc/cron.daily/logrotate`


Retrieve the backup
===================

You can retrieve the backup from the web-interface in
:menuselection:`Services --> IPBX --> IPBX Configuration --> Backup Files` page.

Otherwise with a shell access you can retrieve them in :file:`/var/backups/xivo/`.
In this directory you will find :file:`db.tgz` and :file:`data.tgz` files for the databases and data
backup.

Backup script:

    :file:`/usr/sbin/xivo-backup`

Backup location:

    :file:`/var/backups/xivo/`


What is actually backuped ?
===========================

Data
----

Here is the list of the folder and files backuped:

* :file:`/etc/asterisk`
* :file:`/etc/dahdi`
* :file:`/etc/dhcp`
* :file:`/etc/pf-xivo`
* :file:`/etc/wanpipe`
* :file:`/etc/network/interfaces`
* :file:`/etc/resolv.conf`
* :file:`/etc/hosts`
* :file:`/etc/hostname`
* :file:`/var/lib/asterisk/`
* :file:`/var/lib/pf-xivo/`
* :file:`/var/lib/xivo-provd`
* :file:`/var/log/asterisk/`
* :file:`/var/spool/asterisk/`

The following files/folders are excluded from this backup:

* folders:

  * :file:`/var/spool/asterisk/monitor`
  * :file:`/var/spool/asterisk/meetme`

* log files, coredump files,
* audio recordings,
* and, files greater than 10Mo or folders containing more than 100 files
  if they belong to one of these folders:

  * :file:`/var/lib/pf-xivo/sounds`
  * :file:`/var/lib/asterisk/sounds/custom`
  * :file:`/var/lib/asterisk/moh`
  * :file:`/var/spool/asterisk/voicemail`
  * :file:`/var/spool/asterisk/monitor`


Database
--------

All XiVO databases are backuped (xivo and asterisk).


Creating a database backup file manually
========================================

.. warning::
    
    A backup file may take a lot of space on the disk.
    You should check the free space on the partition before doing it.

You can manually create a *database* backup file named :file:`db-manual.tgz` in :file:`/var/tmp` by issuing the following commands::

   xivo-backup db /var/tmp/db-manual


Creating a data backup file manually
====================================

.. warning:: 
    
    A backup file may take a lot of space on the disk.
    You should check the free space on the partition before doing it.

You can manually create a *data* backup file named :file:`data-manual.tgz` in :file:`/var/tmp` by issuing the following commands::

   xivo-backup data /var/tmp/data-manual


*******
Restore
*******

Introduction
============

A backup of both the configuration files and the databases used by a XiVO installation is done
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

   tar zxvfp /var/backups/xivo/data.tgz -C /


Restoring the databases
=======================

.. warning::

    * This will destroy all the current data in your databases.
    * You have to check the free space on your system partition before extracting the backups.


Databases backups are created as :file:`db.tgz` files in the :file:`/var/backups/xivo` directory.
These tarballs contains a dump of the two databases used in XiVO.

In this example, we'll restore the databases from a backup file named :file:`db.tgz`
placed in the home directory of root.

Then, extract the content of the :file:`db.tgz` file into the :file:`/var/tmp` directory and go inside
the newly created directory::

   tar xvf db.tgz -C /var/tmp
   cd /var/tmp/pg-backup

Drop the asterisk database and restore it with the one from the backup::

   sudo -u postgres dropdb asterisk
   sudo -u postgres pg_restore -C -d postgres asterisk-*.dump

Do the same thing for the xivo database::

   sudo -u postgres dropdb xivo
   sudo -u postgres pg_restore -C -d postgres xivo-*.dump


Restoring and Keeping System Configuration
==========================================

System configuration as network interfaces is stored in xivo database. If you
want to keep this configuration and only restore xivo data you may omit to
restore xivo database provided you restore the following tables :

* entity
* stats_conf
* stats_conf_agent
* stats_conf_group
* stats_conf_incall
* stats_conf_queue
* stats_conf_user

::

   sudo -u postgres pg_restore -d xivo -t entity -t entity_id_seq -c xivo-*.dump
   sudo -u postgres pg_restore -d xivo -t ldapserver -t ldapserver_id_seq -c xivo-*.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf -t stats_conf_id_seq -c xivo-*.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_agent -c xivo-*.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_group -c xivo-*.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_incall -c xivo-*.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_queue -c xivo-*.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_user -c xivo-*.dump

Restore the rights on these tables ::

   su postgres -c 'psql xivo -c "GRANT ALL ON ALL TABLES IN SCHEMA public TO xivo"'
   su postgres -c 'psql xivo -c "GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO xivo"'

.. warning:: Restoring the data.tgz file restore also system files as host
   hostname network interfaces etc... You will need to reapply network
   configuration if you restore the data.tgz file


After Restoring The System
==========================

Restart the services you stopped at the first step::

   xivo-service start

You may also reboot the system.
