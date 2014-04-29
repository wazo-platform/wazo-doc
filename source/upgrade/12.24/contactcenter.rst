*************************
Contact Center XiVO 12.24
*************************

In order to fix problems related to Asterisk freezing through the chan_agent module,
XiVO 12.24 implements a new way of managing agents.


Warning
=======

The contact center XiVO 12.24 does not implement all the features available in 12.22.
Therefore, you must not upgrade your XiVO if you depend on these features.
These features will be reimplemented in the future starting with version 13.01.


Missing Features
================

* Skill-based routing
* Penalities
* Call listening


Live reload via the web interface
=================================

Agents must be logged out for the following operations:

 * Adding or removing agents from the queues
 * When changing the name of a queue (only the name, not the displayed name)

You can logoff all the agents with the following command::

   xivo-agentctl -c "logoff all"


Preprocess subroutines
======================

Subroutines on users are currently no longer executed when an agent receives a call from the queue


High availability (HA)
======================

HA for the contact center is not supported for the moment.
When switching from a master to a slave, you must relog all your agents.


SCCP Devices
============

The "Available" / "In use" statuses for agents that are logged in do not work for the moment.


Changes in behavior
===================

"In use" indicator in the XiVO client
-------------------------------------

In XiVO 12.22, an agent is seen as "In use" when:

* The agent's phone is ringing or has answered a call coming only from a queue

In XiVO 12.24:

* The agent's phone is "In use" no matter where the call comes from


"Available" indicator in the XiVO client
----------------------------------------

In XiVO 12.22, an agent is seen as "Available" when:

* The agent is not in pause/wrapup and his phone isn't ringing/in conversation
  for a call coming from a queue

In XiVO 12.24:

* The agent is not in pause/wrapup and his phone is in the "idle" state


"Agent linked" / "Agent unlinked" Events
----------------------------------------

The "Agent linked" event no longer exists in XiVO 12.24. xivo-upgrade will
automatically migrate "Agent linked" / "Agent unlinked" sheets to the "linked" /
"unlinked" event.


"Static" Agent VS "Dynamic" agent in the XiVO client
----------------------------------------------------

There is no longer a difference between a "static" or "dynamic" membership.
All agent memberships are now considered "static". Membership changes between
the web interface and the XiVO client are now synchronized.


Updates
=======

Please note that when upgrading, the following actions will take place automatically:

* All agents will be logged off before migrating
* All agents with a "dynamic" membership will be removed from their queues


Useful links
============

:ref:`rabbitmq-var-full`
