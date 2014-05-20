********
Entities
********

.. warning:: This feature is currently under development.

Purpose
=======

In some cases, as the telephony provider, you want different independent organisation to have their
telephony served by your XiVO, e.g. different departments using the same telephony infrastructure,
but you do not want each organisation to see or edit the configuration of other organisations.

Configuration
=============

In :menuselection:`Configuration --> Entities`, you can create entities, one for each independant
organisation.

In :menuselection:`Configuration --> Users`, you can select an entity for each administrator.

.. note:: Once an entity is linked with an administrator, it can not be deleted. You have to unlink the entity
          from all administrator to be able to delete it.

There are some unique fields.

* Login CTI
* Agent Number
* Queue name
* Context name

It is possible that an error message appears when creating.