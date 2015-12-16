.. _migrate_i386_to_amd64:

===========================================================
Migrate XiVO from ``i386`` (32 bits) to ``amd64`` (64 bits)
===========================================================

There is no fully automated method to migrate XiVO from ``i386`` to ``amd64``.

The procedure is:

#. :ref:`Upgrade <upgrade>` your ``i386`` machine to XiVO >= 15.13
#. :ref:`Install <install>` a XiVO ``amd64`` **using the same version as the upgraded XiVO i386**
#. Make a backup of your XiVO ``i386`` by following the :ref:`backup procedure <manual_backup>`
#. Copy the backup tarballs to the XiVO ``amd64``
#. Restore the backup by following the :ref:`restore procedure <restore>`

Before starting the services after restoring the backup on the XiVO ``amd64``, you should ensure
that there won't be a conflict between the two machines, e.g. two DHCP servers on the same broadcast
domain, or both XiVO fighting over the same SIP trunk register. You can disable the XiVO ``i386`` by
running::

  xivo-service stop

But be aware the XiVO ``i386`` will be enabled again after you reboot it.
