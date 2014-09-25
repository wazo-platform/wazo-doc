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

14.18
-----

* Consult the `14.18 Roadmap <https://projects.xivo.io/versions/209>`_
* xivo-fai packages were replaced with xivo-dist : a new tool to handle repositories sources.
  Uppon upgrade, xivo-dist is installed and run and all xivo-fai packages are purged.
  :ref:`Consult xivo-dist use cases <xivo_dist>`


14.17
-----

* Consult the `14.17 Roadmap <https://projects.xivo.io/versions/208>`_
* DAHDI configuration file :file:`/etc/dahdi/modules` is no more created by default and must now be
  maintained manually. No action is needed upon upgrade but be aware that the upstream sample file
  is now available in :file:`/usr/share/dahdi/modules.sample`. See
  :ref:`dahdi modules documentation <load_dahdi_modules>` for detailed info.
* The new :ref:`CCSS feature <ccss>` will not be enabled upon upgrade, you must explicitly enable it
  in the :menuselection:`IPBX --> IPBX Services --> Extensions` menu.


14.16
-----

* Consult the `14.16 Roadmap <https://projects.xivo.io/versions/207>`_
* See the :ref:`changelog <confd_changelog>` for xivo-confd's REST API
* DAHDI is upgraded to 2.10.0. If the upgrade process asks about :file:`/etc/dahdi/modules`, we
  recommend that you keep the old version of the file.
* Asterisk now inserts CEL and queue log entries via the ODBC asterisk modules instead of
  the pgsql modules.


14.15
-----

* Consult the `14.15 Roadmap <https://projects.xivo.io/versions/206>`_
* Duplicate function keys will be deleted uppon upgrade. If multiple function keys pointing to
  the same destination are detected for a given user, only the one with the lowest position will
  be kept. To see the list of deleted function keys, check the xivo-upgrade log file such as::

     grep MIGRATE_FK /var/log/xivo-upgrade.log

.. toctree::
   :maxdepth: 1

   14.15/dahdi_2.9.2


14.14
-----

* Consult the `14.14 Roadmap <https://projects.xivo.io/versions/205>`_
* See the :ref:`changelog <confd_changelog>` for REST API
* Upon an important freeze of Asterisk, Asterisk will be restarted. See the `associated ticket
  <https://projects.xivo.io/issues/5165>`_ for more information.


14.13
-----

* Consult the `14.13 Roadmap <https://projects.xivo.io/versions/204>`_
* See the :ref:`changelog <confd_changelog>` for REST API
* Skills-based routing: for an agent which doesn't have the skill X, the rule X < 10 was
  previously evaluated to true, since not having the skill X was equivalent to having it with a
  value of 0. This behaviour has changed, and the same expression is now evaluated to false. If you
  are using skills-based routing, you'll need to check that your rules are still doing what you
  expect. See :ref:`skill evaluation <skill-evaluation>` for more information.


14.12
-----

* Consult the `14.12 Roadmap <https://projects.xivo.io/versions/203>`_
* All provisioning plugins were modified. Although not mandatory, it is strongly advised to update
  all used plugins.
* The function key 'Activate voicemail' was removed as it was a duplicate of existing function key
  'Enable voicemail'. All users having the 'Activate voicemail' function key will have to be
  reconfigured with a 'Enable voicemail' function key in order to keep the equivalent feature.
* Log files have changed for the following daemons (previously in :file:`/var/log/daemon.log`):

  * xivo-provd: :file:`/var/log/xivo-provd.log`
  * xivo-agid: :file:`/var/log/xivo-agid.log`
  * xivo-sysconfd: :file:`/var/log/xivo-sysconfd.log`


14.11
-----

* Consult the `14.11 Roadmap <https://projects.xivo.io/versions/202>`_
* The API URL :ref:`/lines/\<id\>/extension <line-extension-association>` is now deprecated. Use
  :ref:`/lines/\<id\>/extensions <line-extension-associations>` instead.


14.10
-----

* Consult the `14.10 Roadmap <https://projects.xivo.io/versions/201>`_
* Custom MOH have been `fixed`_, but can not be used for playing uploaded files anymore. See
  :ref:`moh`.

.. _fixed: https://projects.xivo.io/issues/5038


14.09
-----

* Consult the `14.09 Roadmap <https://projects.xivo.io/versions/200>`_
* REST API 1.0 is no more. All code, tests and documentation was removed from XiVO.
  All code developped for REST API 1.0 must now be adapted to use REST API 1.1.


14.08
-----

* Consult the `14.08 Roadmap <https://projects.xivo.io/versions/199>`_
* The ``xivo`` database has been merged into the ``asterisk`` database. The database
  schema has also been altered in a way that it might make the upgrade longer than
  usual.

Please consult the following detailed updated notes for more information:

.. toctree::
   :maxdepth: 1

   14.08/database_merge


14.07
-----

* Consult the `14.07 Roadmap <https://projects.xivo.io/versions/198>`_
* Configuration for phones used for the switchboard has changed.

Please consult the following detailed updated notes for more information:

.. toctree::
   :maxdepth: 1

   14.07/switchboard_plugin


14.06
-----

* Consult the `14.06 Roadmap <https://projects.xivo.io/versions/197>`_
* The XiVO client now uses Qt 5 instead of Qt 4. There is nothing to be aware of unless you
  are :ref:`building your own version <build_xivoclient>` of it.


14.05
-----

* Consult the `14.05 Roadmap <https://projects.xivo.io/versions/196>`_
* The :ref:`cti-protocol` has been updated.
* The specification of the 'answered-rate' queue statistic has changed to
  exclude calls on a closed queue
* The switchboard can now choose which incoming call to answer
* The package versions do not necessarily contain the current XiVO version, it may contain older
  versions. Only the package ``xivo`` is guaranteed to have the current XiVO version.

Please consult the following detailed updated notes for more information:

.. toctree::
   :maxdepth: 1

   14.05/dahdi_2.9.0
   14.05/sccp_next


14.04
-----

* Consult the `14.04 Roadmap <https://projects.xivo.io/versions/195>`_
* Live reload of the configuration can be enabled and disabled using the REST API
* The generation of call logs for unanswered calls from the XiVO client have
  been improved.


14.03
-----

* Consult the `14.03 Roadmap <https://projects.xivo.io/versions/194>`_
* A migration script adds an index on the linkedid field in the cel table.
  Tests have shown that this operation can last up to 11.5 minutes on a XiVO
  Corporate with 18 millions CELs. xivo-upgrade will thus be slightly longer.
* Two new daemons are now operationnal, xivo-amid and xivo-call-logd:

  * xivo-amid constantly reads the AMI and sends AMI events to the RabbitMQ bus
  * xivo-call-logd generates call-logs in real time based on AMI LINKEDID_END
    events read on the bus
* An increase in load average is expected with the addition of these two new
  daemons.
* The cron job calling xivo-call-logs now runs once a day at 4:25 instead of
  every 5 minutes.


14.02
-----

* Consult the `14.02 Roadmap <https://projects.xivo.io/versions/193>`_
* PHP Web services has been removed from documentation
* REST API 1.0 Web services has been removed from documentation
* REST API 1.1 User-Line-Extension service is replaced by User-Line and Line-Extension services


14.01
-----

* Consult the `14.01 Roadmap <https://projects.xivo.io/versions/192>`_
* The following paths have been renamed:

  * :file:`/etc/pf-xivo` to :file:`/etc/xivo`
  * :file:`/var/lib/pf-xivo` to :file:`/var/lib/xivo`
  * :file:`/usr/share/pf-xivo` to :file:`/usr/share/xivo`

You must update any dialplan or configuration file using these paths


Archives
--------

.. toctree::
   :maxdepth: 2

   old_upgrade_notes
