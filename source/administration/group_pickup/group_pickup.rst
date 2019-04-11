************
Group Pickup
************

Pickup groups allow users to intercept calls directed towards other users of the group. This
is done either by dialing a special extension or by pressing a function key.


Quick Summary
=============

In order to be able to use group pickup you have to:
 * Create a pickup group
 * Enable an extension to intercept calls
 * Add a function key to interceptors


Creating a Pickup Group
=======================

* ``POST /callpickups``
* ``POST /callpickups/{callpickup_id}/interceptors/groups``
* ``POST /callpickups/{callpickup_id}/interceptors/users``
* ``POST /callpickups/{callpickup_id}/targets/groups``
* ``POST /callpickups/{callpickup_id}/targets/users``


Enabling an Interception Extension
==================================

The pickup extension can be defined with:

* ``/extensions/features`` endpoint and ``features: pickup``

The default value for group pickup is *\*8*.

.. warning:: The extension must be enabled even if a function key is used.


Adding a Function Key to an Interceptor
=======================================

Assign a function to an interceptor of type ``pickup``
