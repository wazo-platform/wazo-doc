.. _rest-api-1.1:

************
REST API 1.1
************

.. warning:: The 1.1 API is currently under heavy discussion and development. It cannot be used on a
   production system as it is not yet implemented. Moreover anything currently documented about the
   1.1 API is subject to change.

   See :ref:`rest-api-1.0` for the current production version.

.. toctree::

   call_logs
   extensions
   lines
   users
   user_links
   devices


Migration from 1.0
==================


URL
---

* Occurences of ``1.0`` have been replaced for ``1.1``
* Trailing slashes have been removed.

  For example, in 1.0, the URL to list users is::

     /1.0/users/

  In 1.1, it is::

     /1.1/users

