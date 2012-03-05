*****************
High Availability
*****************

The :abbr:`HA (High Availability)` solution in XiVO makes it possible to maintain basic
telephony function whatever your main XiVO server is running or not. When running a XiVO
HA cluster, users are guaranteed to never experience a downtime of more than 5 minutes of
their basic telephony service.

.. note:: Information on this page applies only to XiVO 1.2 and later.

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

The HA solution is guaranteed to work correctly with the following devices:

* Aastra 6700i series, 3.2.2 firmware


Configuration
=============

First thing to do is to :ref:`install 2 XiVO <installation>`. Note that every setting in the
"Configuration" menu are not automatically copied from the master node to the slave.

.. FIXME this is just a description of what is done on a xivo without HA to make it "HA-wise".
   To be replaced with real information when available.

Then:

* Activate the DHCP server on master
* Set ``readonly-idpwd`` to ``false`` in :file:`/etc/pf-xivo/web-interface/ipbx.ini` on slave.
* Change SIP expiry value on master and slave:

  * min: 20 seconds
  * max: 2 minutes
  * default: 40 seconds

* Create 2 users on master and recreate the exact same user on slave

.. important:: When you upgrade a node of your cluster, you should also upgrade the other so that
   they both are running the same version of XiVO.

.. TODO rajouter comment on configure un trunk distant si on n'utilise pas de register


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

* DND, call forwards, call filtering, ..., statuses are lost.
* If you are statically connected as an agent (i.e. you use "agent callback login"), then
  you'll need to reconnect as a static agent when the master goes down. Since it's hard to
  know when the master goes down, if you CTI client disconnect and you can't reconnect it,
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

Plumbing
========

3 scripts are used to manage services and data replication.

* xivo-master-slave-db-replication <slave_ip> is used on the master to replicate the master's data on the slave server.
* xivo-manage-slave-services {start,stop} is used on the slave to start, stop monit and asterisk. The services won't be restarted after an upgrade or restart.
* xivo-check-master-status <master_ip> is used to check the status of the master and enable or disable services accordingly.

