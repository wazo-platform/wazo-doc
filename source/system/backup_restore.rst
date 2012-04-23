******
Backup
******

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


*******
Restore
*******

Restoring the configuration files
=================================

A backup of both the configuration files and the databases used by a XiVO installation is done 
automatically every day. 
These backups are created in the `/var/backups/pf-xivo` directory and are kept for 7 days.


Restoring the databases
=======================

.. warning::

   This will destroy all the current data in your databases

Databases backups are created as `db.tgz` files in the `/var/backups/pf-xivo` directory. 
These tarballs contains a dump of the two databases used in XiVO 1.2.

In this example, we'll restore the databases from a backup file named `db.tgz` 
placed in the home directory of root.

First, stop monit plus all the services that are connected to the databases.

::

   /etc/init.d/monit stop
   /etc/init.d/xivo-ctid stop
   /etc/init.d/asterisk stop
   /etc/init.d/xivo-confgend stop
   /etc/init.d/pf-xivo-agid stop
   /etc/init.d/pf-xivo-sysconfd stop


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


Finally, restart the services you stopped at the first step:

::

   /etc/init.d/pf-xivo-sysconfd start
   /etc/init.d/pf-xivo-agid start
   /etc/init.d/xivo-confgend start
   /etc/init.d/asterisk start
   /etc/init.d/xivo-ctid start
   /etc/init.d/monit start


