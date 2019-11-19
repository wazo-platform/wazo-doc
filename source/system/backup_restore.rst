.. _backup:

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

With shell access, you can retrieve them in :file:`/var/backups/xivo`.
In this directory you will find :file:`db.tgz` and :file:`data.tgz` files for the database and data
backups.

Backup scripts:

    :file:`/usr/sbin/xivo-backup`

Backup location:

    :file:`/var/backups/xivo`


What is actually backed-up?
===========================

Data
----

Here is the list of folders and files that are backed-up:

* :file:`/etc/asterisk/`
* :file:`/etc/consul/`
* :file:`/etc/crontab`
* :file:`/etc/dahdi/`
* :file:`/etc/dhcp/`
* :file:`/etc/hostname`
* :file:`/etc/hosts`
* :file:`/etc/ldap/`
* :file:`/etc/network/if-up.d/xivo-routes`
* :file:`/etc/network/interfaces`
* :file:`/etc/ntp.conf`
* :file:`/etc/profile.d/xivo_uuid.sh`
* :file:`/etc/resolv.conf`
* :file:`/etc/ssl/`
* :file:`/etc/systemd/`
* :file:`/etc/wanpipe/`
* :file:`/etc/wazo-agentd/`
* :file:`/etc/wazo-agid/`
* :file:`/etc/wazo-amid/`
* :file:`/etc/wazo-auth/`
* :file:`/etc/wazo-call-logd/`
* :file:`/etc/wazo-calld/`
* :file:`/etc/wazo-chatd/`
* :file:`/etc/wazo-confd/`
* :file:`/etc/wazo-confgend-client/`
* :file:`/etc/wazo-phoned/`
* :file:`/etc/wazo-dird/`
* :file:`/etc/wazo-plugind/`
* :file:`/etc/wazo-purge-db/`
* :file:`/etc/wazo-webhookd/`
* :file:`/etc/wazo-websocketd/`
* :file:`/etc/wazo-dxtora/`
* :file:`/etc/xivo/`
* :file:`/root/.config/wazo-auth-cli/`
* :file:`/usr/local/bin/`
* :file:`/usr/local/sbin/`
* :file:`/usr/local/share/`
* :file:`/usr/share/wazo/WAZO-VERSION`
* :file:`/var/lib/asterisk/`
* :file:`/var/lib/consul/`
* :file:`/var/lib/wazo/`
* :file:`/var/lib/wazo-auth-keys/`
* :file:`/var/lib/wazo-provd/`
* :file:`/var/log/asterisk/`
* :file:`/var/spool/asterisk/`
* :file:`/var/spool/cron/crontabs/`

The following files/folders are excluded from this backup:

* folders:

  * :file:`/var/lib/consul/checks`
  * :file:`/var/lib/consul/raft`
  * :file:`/var/lib/consul/serf`
  * :file:`/var/lib/consul/services`
  * :file:`/var/lib/wazo-provd/plugins/*/var/cache/*`
  * :file:`/var/spool/asterisk/monitor/`
  * :file:`/var/spool/asterisk/meetme/`

* files

  * :file:`/var/lib/wazo-provd/plugins/xivo-polycom*/var/tftpboot/*.ld`

* log files, coredump files
* audio recordings
* and, files greater than 10 MiB or folders containing more than 100 files if they belong to one of
  these folders:

  * :file:`/var/lib/wazo/sounds/`
  * :file:`/var/lib/asterisk/sounds/custom/`
  * :file:`/var/lib/asterisk/moh/`
  * :file:`/var/spool/asterisk/voicemail/`
  * :file:`/var/spool/asterisk/monitor/`


Database
--------

The following databases from PostgreSQL are backed up:

* ``asterisk``: all the configuration done via the web interface (exceptions: High Availability,
  Provisioning, Certificates)


.. _manual_backup:

Creating backup files manually
==============================

.. warning::

    A backup file may take a lot of space on the disk.
    You should check the free space on the partition before creating one.


Database
--------

You can manually create a *database* backup file named :file:`db-manual.tgz` in :file:`/var/tmp` by
issuing the following commands::

   xivo-backup db /var/tmp/db-manual


Files
-----

You can manually create a *data* backup file named :file:`data-manual.tgz` in :file:`/var/tmp` by
issuing the following commands::

   xivo-backup data /var/tmp/data-manual


.. _restore:

*******
Restore
*******

Introduction
============

A backup of both the configuration files and the database used by a Wazo installation is done
automatically every day. These backups are created in the :file:`/var/backups/xivo` directory and
are kept for 7 days.


Limitations
===========

* You must restore a backup on the **same version** of Wazo that was backed up (though the
  architecture -- ``i386`` or ``amd64`` -- may differ)
* You must restore a backup on a machine with the **same hostname and IP address**


Before Restoring the System
===========================

.. warning::

    Before restoring a Wazo on a fresh install you have to setup Wazo using the wizard.

Stop monit and all the Wazo services::

   wazo-service stop


Restoring System Files
======================

System files are stored in the data.tgz file located in the :file:`/var/backups/xivo` directory.

This file contains for example, voicemail files, musics, voice guides, phone sets firmwares,
provisioning server configuration database.

To restore the file ::

   tar xvfp /var/backups/xivo/data.tgz -C /

Once the database and files have been restored, you can :ref:`finalize the restore <after_restore>`


Restoring the Database
======================

.. warning::

    * This will destroy all the current data in your database.
    * You have to check the free space on your system partition before extracting the backups.
    * If restoring Wazo >= 18.01 on a different machine, you should not restore the system
      configuration, because of network interface names that would change. See
      :ref:`restore_keep_system_config`.

Database backups are created as :file:`db.tgz` files in the :file:`/var/backups/xivo` directory.
These tarballs contains a dump of the database used in Wazo.

In this example, we'll restore the database from a backup file named :file:`db.tgz`
placed in the home directory of root.

First, extract the content of the :file:`db.tgz` file into the :file:`/var/tmp` directory and go
inside the newly created directory::

   tar xvf db.tgz -C /var/tmp
   cd /var/tmp/pg-backup

Drop the asterisk database and restore it with the one from the backup::

   sudo -u postgres dropdb asterisk
   sudo -u postgres pg_restore -C -d postgres asterisk-*.dump

Once the database and files have been restored, you can :ref:`finalize the restore <after_restore>`


Troubleshooting
---------------

When restoring the database, if you encounter problems related to the system locale, see
:ref:`postgresql_localization_errors`.


.. _restore_keep_system_config:

Alternative: Restoring and Keeping System Configuration
=======================================================

System configuration like network interfaces is stored in the database. It is
possible to keep this configuration and only restore Wazo data.

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

Once the database and files have been restored, you can :ref:`finalize the restore <after_restore>`


.. _after_restore:

After Restoring The System
==========================


.. If you modify this procedure, please update wazo-acceptance/wazo_acceptance/assets/xivo-backup-manager
   accordingly

#. Restore the server UUID::

    XIVO_UUID=$(sudo -u postgres psql -d asterisk -tA -c 'select uuid from infos')
    echo "export XIVO_UUID=$XIVO_UUID" > /etc/profile.d/xivo_uuid.sh

   Then edit :file:`/etc/systemd/system.conf` to update ``XIVO_UUID`` in ``DefaultEnvironment``


#. You may reboot the system, or execute the following steps.
#. Update systemd runtime configuration::

    source /etc/profile.d/xivo_uuid.sh
    systemctl set-environment XIVO_UUID=$XIVO_UUID
    systemctl daemon-reload

#. Restart the services you stopped in the first step::

    wazo-service start
