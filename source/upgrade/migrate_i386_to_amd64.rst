.. _migrate_i386_to_amd64:

===========================================================
Migrate Wazo from ``i386`` (32 bits) to ``amd64`` (64 bits)
===========================================================

There is no fully automated method to migrate Wazo from ``i386`` to ``amd64``.

The procedure is:

#. :ref:`Upgrade <upgrade>` your ``i386`` machine to XiVO/Wazo >= 15.13
#. :ref:`Install <install>` a Wazo ``amd64`` **using the same version as the upgraded Wazo i386**
#. Make a backup of your Wazo ``i386`` by following the :ref:`backup procedure <manual_backup>`
#. Copy the backup tarballs to the Wazo ``amd64``
#. Restore the backup by following the :ref:`restore procedure <restore>`

Before starting the services after restoring the backup on the Wazo ``amd64``, you should ensure
that there won't be a conflict between the two machines, e.g. two DHCP servers on the same broadcast
domain, or both Wazo fighting over the same SIP trunk register. You can disable the Wazo ``i386`` by
running::

  wazo-service stop

But be aware the Wazo ``i386`` will be enabled again after you reboot it.
