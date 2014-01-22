.. _rest-api-1.1:

************
REST API 1.1
************

.. warning:: The 1.1 API is currently in beta version. Although it is rather stable, some minor
   changes could still happen and new resources will be added over time.

.. toctree::
   :maxdepth: 2

   call_logs
   cti_profile
   devices
   extensions
   func_keys
   lines
   line_extension
   users
   user_cti
   user_line
   voicemails
   voicemail_links
   xivo_main_config


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
