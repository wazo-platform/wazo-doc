*********
Upgrading
*********

Upgrading a XiVO is done by executing commands through a terminal on the server. You can connect to the server either through SSH or with a physical console.

To upgrade your XiVO to the latest version, you **must** use the `xivo-upgrade` script. You can start an upgrade with the command::

   xivo-upgrade

.. note:: 
   * You can't use xivo-upgrade if you have not run the wizard yet
   * Upgrading to XiVO 1.2 from a previous version (i.e. XiVO 1.1) is not supported right now.
   * When upgrading Xivo, you **must** also upgrade **all** associated XiVO Clients. There is currently no retro-compatibility on older XiVO Client versions.

This script will update XiVO and restart all daemons.

There are 2 options you can pass to xivo-upgrade:

* ``-d`` to only download packages without installing them
* ``-f`` to force upgrade, without asking for user confirmation

.. warning::

   If xivo-upgrade fails or aborts in mid-process, the system might end up in a faulty condition. If in doubt, run the following command to check the current state of xivo's firewall rules::

      iptables -nvL

   If, among others, it displays something like the following line (notice the DROP and 5060) ::

      0     0 DROP       udp  --  *      *       0.0.0.0/0            0.0.0.0/0           udp dpt:5060

   Then your XiVO will not be able to register any SIP phones. In this case, you must delete the DROP rules with the following command::

      iptables -D INPUT -p udp --dport 5060 -j DROP

   Repeat this command until no more unwanted rules are left.


Upgrading a cluster
===================

Here are the steps for upgrading a cluster:

#. On the master : deactivate the database replication by commenting the cron in :file:`/etc/cron.d/xivo-ha-master`
#. On the slave, start the upgrade::

    xivo-2:~$ xivo-upgrade

#. When the slave has finished, start the upgrade on the slave::

    xivo-1:~$ xivo-upgrade

#. When done, launch the database replication manually::

    xivo-1:~$ /usr/sbin/xivo-master-slave-db-replication <slave ip>

#. Reactivate the database replication (see first step)


Upgrade Notes for older Versions of XiVO
========================================

* When upgrading from XiVO 1.2.3 or earlier, you must do the following::

   wget http://mirror.xivo.fr/xivo_current.key -O - | apt-key add -

* Upgrading from 1.2.0 or 1.2.1 requires a special procedure before executing xivo-upgrade::

   apt-get update
   apt-get install xivo-upgrade
   /usr/bin/xivo-upgrade

