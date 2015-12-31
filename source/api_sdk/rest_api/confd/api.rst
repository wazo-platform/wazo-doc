.. _confd-api:

**************
XiVO confd API
**************

.. note:: REST API 1.1 for confd is currently evolving. New features and small fixes are regularly being added
    over time. We invite the reader to periodically check the :ref:`changelog <confd_changelog>`
    for an update on new features and changes.

.. toctree::
   :maxdepth: 1

   changelog
   examples

.. warning:: Some services are still being developped and can be changed without prior warning. Use
    at your own risk. Here is a list of services in BETA stage:

        * Function Keys


API reference
=============

API documentation is available on http://api.xivo.io. This section
contains extended documentation for certain aspects of the API.

.. toctree::
   :maxdepth: 2

   func_keys
   user_import


Migration from 1.0
==================

The API version 1.0 is no longer supported and has been removed. In most cases, code that used the old API can be 
migrated to version 1.1 without much hassle by updating the URL. For example, in 1.0, the URL to list users was::

     /1.0/users/

  In 1.1, it is::

     /1.1/users

Please note that there are no trailing slashes in URLs for version 1.1.

For further details consult the documentation at http://api.xivo.io
