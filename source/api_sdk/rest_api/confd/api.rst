.. _confd-api:

**************
XiVO confd API
**************

.. note:: REST API 1.1 for confd is currently evolving. New features and small fixes are regularly being added
    over time. We invite the reader to periodically check the :ref:`changelog <restapi_changelog>`
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

.. toctree::
   :maxdepth: 2

   call_logs
   cti_profile
   devices
   extensions
   func_keys
   lines
   line_extensions
   Line Extension Association ***DEPRECATED*** <line_extension>
   users
   user_cti
   user_line
   voicemails
   voicemail_links
   configuration
   agent_queue


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
