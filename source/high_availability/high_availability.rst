**********************
High Availability (HA)
**********************

The :abbr:`HA (High Availability)` solution in XiVO makes it possible to maintain basic
telephony function whatever your main XiVO server is running or not. When running a XiVO
HA cluster, users are guaranteed to never experience a downtime of more than 5 minutes of
their basic telephony service.

The HA solution in XiVO is based on a 2-nodes "master and slave" architecture. In the normal situation,
both the master and slave nodes are running in parallel, the slave acting as an "hot standby", and all
the telephony services are provided by the master node. If the master fails or must be shutdown for
maintenance, then the telephony devices automatically communicate with the slave node instead
of the master one. Once the master is up again, the telephony devices failback to the
master node. Both the failover and the failback operation are done automatically, i.e. without
any user intervention, although an administrator might want to run some manual operations after
failback as to, for example, make sure any voicemail messages that were left on the slave are
copied back to the master.


Prerequisites
=============

The HA in XiVO only works with telephony devices (i.e. phones) that support
the notion of a primary and backup telephony server.

* The master and the slave must be in the same subnet
* If firewalling, the master must be allowed to join the slave on port 5232

The HA solution is guaranteed to work correctly with the following devices:

* Aastra 6700i series, 3.2.2 firmware


Quick Summary
=============

* You need two configured XiVO (wizard passed)
* Configure one XiVO as a master -> setup the slave address
* Restart cti server on master
* Configure the other XiVO as a slave -> setup the master address
* Start configuration synchronization by running the script ``xivo-master-slave-db-replication <slave_ip>``
* Resynchronize all your devices

That's it you now have a HA configuration, and every hour all the configuration done on the master will be reported to the slave.


Configuration Details
=====================

First thing to do is to :ref:`install 2 XiVO <installation>`. Note that every setting in the
"Configuration" menu are not automatically copied from the master node to the slave.

.. important:: When you upgrade a node of your cluster, you should also upgrade the other so that
   they both are running the same version of XiVO.

You must configure the :abbr:`HA (High Availability)` in the Web interface
(:menuselection:`Configuration --> Management --> High Availability` page).

You can configure the master and slave in whatever order you want.

.. warning:: When the HA is configured, some changes will be automatically
   made to the configuration of XiVO.

SIP expiry value on master and slave will be automatically updated:

* min: 20 seconds
* max: 2 minutes
* default: 40 seconds

.. figure:: images/general_settings_sip_expiry.png

   :menuselection:`Services --> IPBX --> General Settings --> SIP Protocol`

The provisioning server configuration will be automatically updated in order to allow
phones to switch from XiVO power failure.

.. figure:: images/provd_config_registrar.png

   :menuselection:`Configuration --> Provisioning --> Template Line --> Edit default`


.. warning:: Especially not change these values when the HA is configured, this could cause problems.
   These values will be reset to blank when the HA is disabled.

.. important:: For the telephony devices to take the new proxy/registrar settings
   into account, you must :ref:`resynchronize the devices <synchronize-device>`
   or restart them manually.


Disable node
------------

Default status of :abbr:`High Availability (HA)` is disabled:

.. note:: You can reset at any time by choosing a server mode (disabled)

.. figure:: images/ha_dashboard_disabled.png

   HA Dashboard Disabled (default state)


Master node
-----------

In choosing the method ``Master`` you must enter the IP address of the slave node.

.. figure:: images/ha_dashboard_master.png

   HA Dashboard Master

.. important:: You have to restart the cti server once the master node is configured.


Slave node
----------

In choosing the method ``Slave`` you must enter the IP address of master node.

.. figure:: images/ha_dashboard_slave.png

   HA Dashboard Slave

Configuration Replication
-------------------------

Once master slave configuration is completed, XiVO configuration is replicated from the master node
to the salve every hour (:00).
Replication can be started manually by running the replication script :

::

   xivo-master-slave-db-replication <slave_ip>
   
   Slave replication completed succesfully


Internals
=========

3 scripts are used to manage services and data replication.

* xivo-master-slave-db-replication <slave_ip> is used on the master to replicate the master's
  data on the slave server.
* xivo-manage-slave-services {start,stop} is used on the slave to start, stop monit and asterisk.
  The services won't be restarted after an upgrade or restart.
* xivo-check-master-status <master_ip> is used to check the status of the master and enable or
  disable services accordingly.


Limitations
===========

When the master node is down, some features are not available and some behave a bit
differently. This includes:

* CTI client is not available.
* Call history / call records are not recorded.
* Voicemail messages saved on the master node are not available.
* Custom voicemail greetings recorded on the master node are not available.
* More generally, custom sounds are not available. This includes music on hold and recordings.
* Custom dialplan (i.e. dialplan found in the :file:`/etc/asterisk/extensions_extra.d` directory
  or in the :menuselection:`Services --> IPBX --> IPBX configuration --> Configuration files` page)
  is not available.

Note that, on failover and on failback:

* DND, call forwards, call filtering, ..., statuses may be lost if changed recently.
* If you are statically connected as an agent (i.e. you use "agent callback login"), then
  you'll need to reconnect as a static agent when the master goes down. Since it's hard to
  know when the master goes down, if your CTI client disconnect and you can't reconnect it,
  then it's a sign the master might be down.

Additionally, only on failback:

* Voicemail messages are not copied from the slave to the master, i.e. if someone
  left a message on your voicemail when the master was down, you won't be able to
  consult it once the master is up again.
* More generally, custom sounds are not copied back. This includes recordings.

Here's the list of limitations that are more relevant on an administrator standpoint:

* In the case a DHCP server is running on the master node, then when the master is down,
  phones won't be able to get a new DHCP lease, so it is advised not to restart the phones.
* The master status is up or down, there's no middle status. This mean that if Asterisk is crashed
  the XiVO is still up and the failover will NOT happen.


Berofos Integration
===================

.. toctree::
   :maxdepth: 2

   berofos
