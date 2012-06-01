******
Backup
******


What is actually backuped ?
===========================

Data
^^^^

Here is the list of the folder and files backuped::

    /etc/asterisk /etc/dahdi /etc/dhcp /etc/pf-xivo /etc/wanpipe 
    /etc/network/interfaces /etc/resolv.conf /etc/hosts /etc/hostname
    /var/lib/asterisk/ /var/lib/pf-xivo/ /var/spool/asterisk/ /var/log/asterisk/ /var/lib/pf-xivo-provd

The following files/folders are excluded from this backup :

- folders : ``/var/spool/asterisk/monitor /var/spool/asterisk/meetme``
- log files, coredump files,
- audio recordings,
- and, files greater than 10Mo or folders containing more than 100 files
  if they belong to one of these folders : ``/var/lib/pf-xivo/sounds``, ``/var/lib/asterisk/sounds/custom``, ``/var/lib/asterisk/moh``, ``/var/spool/asterisk/voicemail``, ``/var/spool/asterisk/monitor``


Database
^^^^^^^^

All XiVO database is backuped (xivo and asterisk).


Periodic backup
===============

A backup of the database and the data are launched each day with a logrotate task.
Note that you can retrieve the backup from the web-interface in
:menuselection:`Services ---> IPBX ---> IPBX Configuration ---> Backup Files` page.

Logrotate task::

    /etc/logrotate.d/pf-xivo-backup

Logrotate cron::

    /etc/cron.daily/logrotate

Backup script::

    /usr/sbin/pf-xivo-backup

Backup location::
    
    /var/backups/pf-xivo/


Creating a databases backup file manually
=========================================

You can manually create a database backup file named `db-manual.tgz` by issuing the following commands:

::

   pf-xivo-backup db db-manual.tgz


Creating a data backup file manually
====================================

You can manually create a data backup file named `data-manual.tgz` by issuing the following commands:

::

   pf-xivo-backup data data-manual.tgz


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

   /etc/init.d/monit stop
   /etc/init.d/xivo-ctid stop
   /etc/init.d/asterisk stop
   /etc/init.d/xivo-confgend stop
   /etc/init.d/pf-xivo-agid stop
   /etc/init.d/pf-xivo-sysconfd stop
   /etc/init.d/pf-xivo-provd stop

Restoring System Files
======================

System files are stored in the data.tgz file located in the `/var/backups/pf-xivo` directory.

This file contains for example, voicemail files, musics, voice guides, phone sets firmwares, provisioning server configuration database.

To restore the file :

::
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


Drop the asterisk database and restore it with the one from the backup:

::

   sudo -u postgres dropdb asterisk
   sudo -u postgres pg_restore -C -d postgres asterisk.dump


Do the same thing for the xivo database:

::

   sudo -u postgres dropdb xivo
   sudo -u postgres pg_restore -C -d postgres xivo.dump

After Restoring The System
==========================

Restart the services you stopped at the first step:

::

   /etc/init.d/pf-xivo-provd start
   /etc/init.d/pf-xivo-sysconfd start
   /etc/init.d/pf-xivo-agid start
   /etc/init.d/xivo-confgend start
   /etc/init.d/asterisk start
   /etc/init.d/xivo-ctid start
   /etc/init.d/monit start

You may also reboot the system.
