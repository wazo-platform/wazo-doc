*********
Upgrading
*********

To upgrade your XiVO to the latest version, you **must** use xivo-upgrade::

   xivo-upgrade

.. note:: 
   * You can't use xivo-upgrade if you have not run the wizard
   * Upgrading to XiVO 1.2 from a previous version (i.e. XiVO 1.1) is not supported right now.

This script will update XiVO and restart all daemons.

There are 2 options for xivo-upgrade:

* ``-d`` to only download packages, no package will be installed
* ``-f`` to force upgrade, do not ask for user confirmation


.. warning::

   If xivo-upgrade fails or aborts in mid-process, system might end up in a faulty condition. If in doubt, run the following command to check the current state of xivo's firewall rules::

      iptables -nvL

   If, among others, it displays something like the following line (notice the DROP and 5060) ::

      0     0 DROP       udp  --  *      *       0.0.0.0/0            0.0.0.0/0           udp dpt:5060

   Then your XiVO will not be able to register any SIP phones. In this case, you must delete the DROP rules with the following command::

      iptables -D INPUT -p udp --dport 5060 -j DROP

   Untill no more unwanted rules are left behind.


Cluster Upgrade
===============

If upgrading a cluster you should follow these steps :

#. On the master : deactivate the database replication by commenting the cron in :file:`/etc/cron.d/xivo-ha-master`
#. On the slave, start the upgrade::

    xivo-2:~$ xivo-upgrade

#. On the master, when done with the slave, start the upgrade::

    xivo-1:~$ xivo-upgrade

#. When done, launch the database replication manually::

    xivo-1:~$ /usr/sbin/xivo-master-slave-db-replication <slave ip>

#. If it is ok, reactivate the database replication


Upgrade Notes on Older Versions
===============================


* Before upgrading from XiVO 1.2.3 or earlier, you must do the following::

   wget http://mirror.xivo.fr/xivo_current.key -O - | apt-key add -


* Upgrading from 1.2.0 or 1.2.1 require a special procedure before executing xivo-upgrade::

   apt-get update
   apt-get install xivo-upgrade
   /usr/bin/xivo-upgrade

