********
Database
********

Adding a Migration Script
=========================

Strating with XiVO 14.08, the database migration is handled by
`alembic <http://alembic.readthedocs.org>`_.

The XiVO migration scripts can be found in the
`xivo-manage-db <https://github.com/xivo-pbx/xivo-manage-db>`_ repository.

On a XiVO, they are located in the :file:`/usr/share/xivo-manage-db` directory.

To add a new migration script from your developer machine, go into the root
directory of the xivo-manage-db repository. There should be an :file:`alembic.ini`
file in this directory. You can then use the following command to create a new
migration script::

   alembic revision -m "<description>"

This will create a file in the :file:`alembic/versions` directory, which you'll have to edit.
