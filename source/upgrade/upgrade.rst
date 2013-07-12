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

* Read all `roadmaps <https://projects.xivo.fr/projects/xivo/roadmap?tracker_ids%5B%5D=1&tracker_ids%5B%5D=2&completed=1>`_ starting from your current version to the current prod version.
* Read all existing Upgrade Notes (see below) starting from your current version to the current prod version.
* If in a specific configuration, follow the specific procedure described below (example : cluster).
* To download the packages beforehand, run ``xivo-upgrade -d`` (will upgrade xivo-upgrade, xivo-service and download all packages necessary, prior to stopping services for upgrade, making the upgrade faster).
* When ready (services will be stopped), run ``xivo-upgrade`` which will actually start the migration.
* When finished, check that the services are correctly running :

 * with ``xivo-service status`` command,
 * and with actual checks like SIP registration, ISDN links status, internal/incoming/outgoing calls, XiVO Client connections etc.


Specific procedure: XiVO 13.03 and before
=========================================

When upgrading from XiVO 13.03 or earlier, you must do the following, before the normal upgrade::

   wget http://mirror.xivo.fr/xivo_current.key -O - | apt-key add -


Specific procedure: XiVO 1.2.1 and before
=========================================

Upgrading from 1.2.0 or 1.2.1 requires a special procedure before executing ``xivo-upgrade``::

   apt-get update
   apt-get install xivo-upgrade
   /usr/bin/xivo-upgrade


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

    xivo-master:~$ /usr/sbin/xivo-master-slave-db-replication <slave ip>

#. Reactivate the cronjobs (see steps 1 and 2)


Upgrade Notes
=============

13.14
-----

* Consult the `13.13 Roadmap <https://projects.xivo.fr/versions/180>`_
* Recording campaigns are now in the xivo-recording-campaigns package. Consult :ref:`Recording Campaigns <recording-campaigns>` if you are using the recording campaign feature to install the package after the upgrade.
* The latest Polycom plugin enables the phone lock feature with a default user password of '123'. All Polycom phones used with XiVO also have a default admin password. In order for the phone lock feature to be secure, one should change every phone's admin AND user passwords.
* WebServices for SIP trunks/lines: field "nat": value "yes" changed to "force_rport,comedia"

13.13
-----

* Consult the `13.13 Roadmap <https://projects.xivo.fr/versions/179>`_


13.12
-----

* Consult the `13.12 Roadmap <https://projects.xivo.fr/versions/178>`_
* CTI protocol: Modified values of agent ``availability``. Read :ref:`CTI Protocol changelog <cti-protocol>`
* Clean-up was made related to the minimization of the XiVO Client. Some visual differences have been observed on Mac OS X that do not affect the XiVO Client in a functional way.


13.11
-----

* Consult the `13.11 Roadmap <https://projects.xivo.fr/versions/177>`_
* Asterisk has been upgraded from version 11.3.0 to 11.4.0

API changes:

* Dialplan variable XIVO_INTERFACE_0 is now XIVO_INTERFACE
* Dialplan variable XIVO_INTERFACE_NB and XIVO_INTERFACE_COUNT have been removed
* The following fields have been removed from the lines and users web services

  * line_num
  * roles_group
  * rules_order
  * rules_time
  * rules_type


13.10
-----

* Consult the `13.10 Roadmap <https://projects.xivo.fr/versions/176>`_

API changes:

* CTI protocol: for messages of class ``getlist`` and function ``updateconfig``, the ``config`` object/dictionary
  does not have a ``rules_order`` key anymore.


13.09
-----

* Consult the `13.09 Roadmap <https://projects.xivo.fr/versions/175>`_
* The *Restart CTI server* link has been moved from :menuselection:`Services --> CTI Server --> Control`
  to :menuselection:`Services --> IPBX --> Control`.
* The Agent Status Dashboard has been optimized.
* The Directory xlet can now be used to place call.


13.08
-----

* Consult the `13.08 Roadmap <https://projects.xivo.fr/versions/174>`_
* asterisk has been upgraded from version 1.8.21.0 to 11.3.0, which is a major asterisk upgrade.
* The switchboard's queue now requires the *xivo_subr_switchboard* preprocess subroutine.
* A fix to bug `#4296 <https://projects.xivo.fr/issues/4296>`_ introduced functional changes due to the order in which sub-contexts are included. Please refer to `ticket <https://projects.xivo.fr/issues/4296>`_ for details.

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   asterisk_11
   xivo_subr_switchboard


13.07
-----

* Consult the `13.07 Roadmap <https://projects.xivo.fr/versions/173>`_
* Agent Status Dashboard has more features and less limitations. See related :ref:`dashboard xlet documentation <dashboard-xlet>`
* XiVO call centers have no more notion of 'disabled agents'. All previously disabled agents in web interface will become active agents after upgrading.
* asterisk has been upgraded from version 1.8.20.1 to 1.8.21.0. Please note that in XiVO 13.08, asterisk will be upgraded to version 11.
* DAHDI has been upgraded from version 2.6.1 to 2.6.2.
* libpri has been upgraded from version 1.4.13 to 1.4.14.
* PostgreSQL upgraded from version 9.0.4 to 9.0.13


13.06
-----

* Consult the `13.06 Roadmap <https://projects.xivo.fr/versions/172>`_
* The new Agent Status Dashboard has a few known limitations. See related :ref:`dashboard xlet known issues section <dashboard-xlet-issues>`
* Status Since counter in xlet list of agents has changed behavior to better reflect states of agents in queues as seen by asterisk. See `Ticket #4254 <https://projects.xivo.fr/issues/4254>`_ for more details.


13.05
-----

* Consult the `13.05 Roadmap <https://projects.xivo.fr/versions/171>`_
* The bug `#4228 <https://projects.xivo.fr/issues/4228>`_ concerning BS filter only applies to 13.04 servers installed from scratch. Please upgrade to 13.05.
* The order of softkeys on SCCP phones has changed, e.g. the *Bis* button is now at the left.


13.04
-----

* Consult the `13.04 Roadmap <https://projects.xivo.fr/versions/170>`_
* Upgrade procedure for HA Cluster has changed. Refer to `Specific Procedure : Upgrading a Cluster`_.
* Configuration of switchboards has changed. Since the directory xlet can now display any column from the lookup source, a display filter has to be configured and assigned to the __switchboard_directory context. Refer to :ref:`Directory xlet documenttion <directory-xlet>`.
* There is no more context field directly associated with a call filter. Boss and secretary users associated with a call filter must necessarily be in the same context.


12.24
-----

* Consult the `12.24 Roadmap <https://projects.xivo.fr/versions/165>`_
* XiVO 12.24 has some limitations mainly affecting the contact center features due to the rewriting of the code handling agents.

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   contactcenter_12.24

Another change is in effect beginning with XiVO 12.24: the field
``profileclient`` in the CSV user import sees its values change.

+-------------+-------------+
| Old value   | New value   |
+=============+=============+
| client      | Client      |
+-------------+-------------+
| agent       | Agent       |
+-------------+-------------+
| switchboard | Switchboard |
+-------------+-------------+
| agentsup    | Supervisor  |
+-------------+-------------+
| oper        | *removed*   |
+-------------+-------------+
| clock       | *removed*   |
+-------------+-------------+
