*****************************
Databases Merge Upgrade Notes
*****************************

The ``xivo`` database has been merged into the ``asterisk`` database in XiVO 14.08.
This has an impact on:

* The :ref:`restore <restore>` procedure. There's only one database to restore now.
  Also, the procedure to restore the data while keeping the system configuration
  has been updated.
* The data that is replicated between the master and the slave in a
  :ref:`high availability <high-availability>` cluster.

Previously, all the configuration that was under the "Configuration" menu
of the web interface was not replicated between the master and slave. This
is now replicated, except for:

* HA settings
* All the network configuration (i.e. everything under the
  :menuselection:`Configuration --> Network` section)
* All the support configuration (i.e. everything under the
  :menuselection:`Configuration --> Support` section)

The call center statistics have also been excluded from the replication.

The way the replication is done has also been updated, which makes it
faster.


Optional Upgrade Procedure
==========================

When upgrading to XiVO 14.08, the database schema will be altered.

This will result in a longer upgrade time if you have a lots of rows in the queue_log table.

You can see the number of rows in your queue_log table with::

   sudo -u postgres psql -c "SELECT count(*) FROM queue_log" asterisk

On ordinary hardware, you can expect that it will take ~10 minutes for every
2.5 million of rows. So if you have 5 million of rows in your queue_log table,
you can expect that the upgrade will take an extra 20 minutes.

It is possible to reduce the amount of additional time the upgrade will take by
either removing rows from the table or altering the table before the upgrade.

Both these commands can be run while the XiVO services are up.

For example, if you want to remove all the rows before march 2014, you can
use::

   sudo -u postgres psql -c "DELETE FROM queue_log WHERE \"time\" < '2014-03-01'" asterisk

If you want to alter the table before the upgrade, you can use::

   sudo -u postgres psql -c "ALTER TABLE queue_log ADD COLUMN id SERIAL PRIMARY KEY; GRANT ALL ON SEQUENCE queue_log_id_seq TO asterisk" asterisk

.. note:: It is recommended to execute this command when there's no activity
   on the system.


More Technical Information
==========================

The way the database is initially provisioned and the way it is altered during an
upgrade has also been changed.

In XiVO 14.07 and earlier, the database was provisioned by executing
the :file:`/usr/share/xivo-manage-db/datastorage/asterisk.sql` SQL script.
Starting with XiVO 14.08, the ``xivo-init-db`` is responsible for provisioning
the database. This script should not be used by an administrator in normal
circumstance.

Starting with XiVO 14.08, database migration are done with the help of
`alembic <http://alembic.readthedocs.org>`_ instead
of the asterisk-XXX.sql and xivo-XXX.sql scripts. The alembic migration
scripts can be found inside the :file:`/usr/share/xivo-manage-db` directory.

Otherwise, the ``xivo-check-db`` and ``xivo-update-db`` commands have been
updated to work with both the old and the new systems and are still the official
way to check the database state and update the database respectively.
