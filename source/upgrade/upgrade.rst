*********
Upgrading
*********

Upgrading a XiVO is done by executing commands through a terminal on the
server. You can connect to the server either through SSH or with a physical
console.

To upgrade your XiVO to the latest version, you **must** use the `xivo-upgrade`
script. You can start an upgrade with the command::

   xivo-upgrade

.. note::
   * You can't use xivo-upgrade if you have not run the wizard yet
   * Upgrading to XiVO 1.2 from a previous version (i.e. XiVO 1.1) is not
     supported right now.
   * When upgrading XiVO, you **must** also upgrade **all** associated XiVO
     Clients. There is currently no retro-compatibility on older XiVO Client
     versions.

This script will update XiVO and restart all daemons.

There are 2 options you can pass to xivo-upgrade:

* ``-d`` to only download packages without installing them. **This will still upgrade xivo-upgrade and xivo-service packages**.
* ``-f`` to force upgrade, without asking for user confirmation

.. warning::

   If xivo-upgrade fails or aborts in mid-process, the system might end up in a
   faulty condition. If in doubt, run the following command to check the current
   state of xivo's firewall rules::

      iptables -nvL

   If, among others, it displays something like the following line (notice the
   DROP and 5060) ::

      0     0 DROP       udp  --  *      *       0.0.0.0/0            0.0.0.0/0           udp dpt:5060

   Then your XiVO will not be able to register any SIP phones. In this case, you
   must delete the DROP rules with the following command::

      iptables -D INPUT -p udp --dport 5060 -j DROP

   Repeat this command until no more unwanted rules are left.


Typical Upgrade Process
=======================

* Read all `roadmaps <https://projects.xivo.io/projects/xivo/roadmap?tracker_ids%5B%5D=1&tracker_ids%5B%5D=2&completed=1>`_ starting from your current version to the current prod version.
* Read all existing Upgrade Notes (see below) starting from your current version to the current prod version.
* If in a specific configuration, follow the specific procedure described below (example : cluster).
* To download the packages beforehand, run ``xivo-upgrade -d`` (will upgrade xivo-upgrade, xivo-service and download all packages necessary, prior to stopping services for upgrade, making the upgrade faster).
* When ready (services will be stopped), run ``xivo-upgrade`` which will actually start the migration.
* When finished, check that the services are correctly running :

 * with ``xivo-service status`` command,
 * and with actual checks like SIP registration, ISDN links status, internal/incoming/outgoing calls, XiVO Client connections etc.


Specific procedure: XiVO 14.01, 14.02, 14.03, 14.04 installed from the ISO file
===============================================================================

In those versions, xivo-upgrade keeps XiVO on the same version. You must do the following, before
the normal upgrade::

   echo "deb http://mirror.xivo.io/debian/ xivo-five main" > /etc/apt/sources.list.d/xivo-upgrade.list \
   && apt-get update \
   && apt-get install xivo-fai \
   && rm /etc/apt/sources.list.d/xivo-upgrade.list \
   && apt-get update


Specific procedure: XiVO 13.03 and before
=========================================

When upgrading from XiVO 13.03 or earlier, you must do the following, before the normal upgrade::

   wget http://mirror.xivo.io/xivo_current.key -O - | apt-key add -


Specific procedure: XiVO 12.13 and before
=========================================

When upgrading from XiVO 12.13 or earlier, you must do the following, before the normal upgrade::

   apt-get update
   apt-get install debian-archive-keyring


Specific procedure: XiVO 1.2.1 and before
=========================================

Upgrading from 1.2.0 or 1.2.1 requires a special procedure before executing ``xivo-upgrade``::

   apt-get update
   apt-get install xivo-upgrade
   /usr/bin/xivo-upgrade

.. _upgrading-a-cluster:

Specific Procedure : Upgrading a Cluster
========================================

Here are the steps for upgrading a cluster:

#. On the master : deactivate the database replication by commenting the cron in
   :file:`/etc/cron.d/xivo-ha-master`
#. On the slave, deactivate the xivo-check-master-status script cronjob by commenting the line in
   :file:`/etc/cron.d/xivo-ha-slave`
#. On the slave, start the upgrade::

    xivo-slave:~$ xivo-upgrade

#. When the slave has finished, start the upgrade on the master::

    xivo-master:~$ xivo-upgrade

#. When done, launch the database replication manually::

    xivo-master:~$ xivo-master-slave-db-replication <slave ip>

#. Reactivate the cronjobs (see steps 1 and 2)


Upgrading to/from an archive version
====================================

.. toctree::
   :maxdepth: 1

   archives


Upgrade Notes
=============

15.04
-----

* Consult the `15.04 Roadmap <https://projects.xivo.io/versions/220>`_


15.03
-----

* Consult the `15.03 Roadmap <https://projects.xivo.io/versions/219>`_


15.02
-----

* Consult the `15.02 Roadmap <https://projects.xivo.io/versions/218>`_


15.01
-----

* Consult the `15.01 Roadmap <https://projects.xivo.io/versions/217>`_

* The :ref:`confd REST API <confd-api>` is now more restrictive on HTTP headers. Particularly, the
  headers Accept and Content-Type must be set to (typically) ``application/json``.
* The following configuration files have been created:

  * :file:`/etc/xivo-agid/config.yml`
  * :file:`/etc/xivo-call-logd/config.yml`
  * :file:`/etc/xivo-amid/config.yml`
  * :file:`/etc/xivo-agentd/config.yml`


Archives
--------

.. toctree::
   :maxdepth: 2

   old_upgrade_notes
