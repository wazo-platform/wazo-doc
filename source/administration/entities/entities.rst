********
Entities
********

Purpose
=======

In some cases, as the telephony provider, you want different independent organisations to have their
telephony served by your XiVO, e.g. different departments using the same telephony infrastructure,
but you do not want each organisation to see or edit the configuration of other organisations.

Configuration
=============

In :menuselection:`Configuration --> Entities`, you can create entities, one for each independant
organisation.

In :menuselection:`Configuration --> Users`, you can select an entity for each administrator.

.. note:: Once an entity is linked with an administrator, it can not be deleted. You have to unlink the entity
          from all administrator to be able to delete it.

For the new entity to be useful, you need to create contexts in this entity. You may need:

* an Internal context for users, groups, queues, etc.
* an Incall context for incoming calls
* an Outcall context for outgoing calls, which should be included in the Internal context for the
  users to be able to call external numbers


Limitations
===========

Global Fields
^^^^^^^^^^^^^

Some fields are globally unique and will collide when the same value is used in different entities:

* User CTI login
* Agent number
* Queue name
* Context name

An error message will appear when creating resources with colliding parameters, saying the resource
already exists, even if the entity-linked administrator can not see them.

Affected Lists
^^^^^^^^^^^^^^

Only the following lists may be filtered by entity:

* Lines
* Users
* Devices
* Groups
* Voicemails
* Conference Rooms
* Incoming calls
* Call filters
* Call pickups
* Schedules
* Agents
* Queues

For the devices:

* The filtering only applies to the devices associated with a line.
* The devices in autoprov mode or not configured mode are visible by every administrator.

REST API
^^^^^^^^

The REST API does not have the notion of entity. When creating a resource without context via REST
API, the resource will be associated to an arbitrary entity. Affected resources are:

* Contexts
* Call filters
* Group pickups
* Schedules
* Users
