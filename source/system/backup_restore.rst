******
Backup
******

What is actually backuped ?
===========================

Data
----

Here is the list of the folder and files backuped::

    /etc/asterisk /etc/dahdi /etc/dhcp /etc/pf-xivo /etc/wanpipe 
    /etc/network/interfaces /etc/resolv.conf /etc/hosts /etc/hostname
    /var/lib/asterisk/ /var/lib/pf-xivo/ /var/spool/asterisk/ /var/log/asterisk/ /var/lib/pf-xivo-provd

The following files/folders are excluded from this backup :

* folders : ``/var/spool/asterisk/monitor /var/spool/asterisk/meetme``
* log files, coredump files,
* audio recordings,
* and, files greater than 10Mo or folders containing more than 100 files
  if they belong to one of these folders : ``/var/lib/pf-xivo/sounds``, ``/var/lib/asterisk/sounds/custom``, ``/var/lib/asterisk/moh``, ``/var/spool/asterisk/voicemail``, ``/var/spool/asterisk/monitor``


Database
--------

All XiVO databases are backuped (xivo and asterisk).


Periodic backup
===============

A backup of the databases and the data are launched each day with a logrotate task.
Note that you can retrieve the backup from the web-interface in
:menuselection:`Services --> IPBX --> IPBX Configuration --> Backup Files` page.

Logrotate task::

    /etc/logrotate.d/pf-xivo-backup

Logrotate cron::

    /etc/cron.daily/logrotate

Backup script::

    /usr/sbin/pf-xivo-backup

Backup location::
    
    /var/backups/pf-xivo/


Creating a database backup file manually
=========================================

You can manually create a database backup file named `db-manual.tgz` by issuing the following commands::

   pf-xivo-backup db db-manual


Creating a data backup file manually
====================================

You can manually create a data backup file named `data-manual.tgz` by issuing the following commands::

   pf-xivo-backup data data-manual


*******
Restore
*******

Introduction
============

A backup of both the configuration files and the databases used by a XiVO installation is done
automatically every day.
These backups are created in the `/var/backups/pf-xivo` directory and are kept for 7 days.


Before Restoring the System
===========================

Before restoring a XiVO on a fresh install you have to setup XiVO using the installation wizard.

Stop monit and all the xivo services.

::

   xivo-service stop


Restoring System Files
======================

System files are stored in the data.tgz file located in the `/var/backups/pf-xivo` directory.

This file contains for example, voicemail files, musics, voice guides, phone sets firmwares, provisioning server configuration database.

To restore the file ::

   tar zxvfp /var/backups/pf-xivo/data.tgz -C /


Restoring the databases
=======================

.. warning::

   This will destroy all the current data in your databases

Databases backups are created as `db.tgz` files in the `/var/backups/pf-xivo` directory.
These tarballs contains a dump of the two databases used in XiVO 1.2.

In this example, we'll restore the databases from a backup file named `db.tgz`
placed in the home directory of root.

Then, extract the content of the `db.tgz` file into the /tmp directory and go inside
the newly created directory.

::

   tar xvf db.tgz -C /tmp
   cd /tmp/pg-backup

Drop the asterisk database and restore it with the one from the backup::

   sudo -u postgres dropdb asterisk
   sudo -u postgres pg_restore -C -d postgres asterisk.dump

Do the same thing for the xivo database::

   sudo -u postgres dropdb xivo
   sudo -u postgres pg_restore -C -d postgres xivo.dump


Restoring and Keeping System Configuration
==========================================

System configuration as network interfaces is stored in xivo database. If you want to keep this configuration and only restore xivo data
you may omit to restore xivo database provided you restore the following tables :

* entity
* stats_conf
* stats_conf_agent
* stats_conf_group
* stats_conf_incall
* stats_conf_queue
* stats_conf_user

::

   sudo -u postgres pg_restore -d xivo -t entity -c xivo.dump
   sudo -u postgres pg_restore -d xivo -t ldapserver -c xivo.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf -c xivo.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_agent -c xivo.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_group -c xivo.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_incall -c xivo.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_queue -c xivo.dump
   sudo -u postgres pg_restore -d xivo -t stats_conf_user -c xivo.dump

Restore the rights on these tables ::
  
   su postgres
   psql xivo
   SELECT execute('GRANT ALL ON '||schemaname||'.'||tablename||' TO xivo;') FROM pg_tables WHERE schemaname = 'public';
   SELECT execute('GRANT ALL ON SEQUENCE '||relname||' TO xivo;') FROM pg_class WHERE relkind = 'S';


.. warning::
   Restoring the data.tgz file restore also system files as host hostname network interfaces etc... You will need to reapply 
   network configuration if you restore the data.tgz file

After Restoring The System
==========================

Restart the services you stopped at the first step::

   xivo-service start

You may also reboot the system.
