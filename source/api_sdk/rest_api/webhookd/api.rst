**********************
wazo-webhookd REST API
**********************

API reference
=============

API documentation is available on http://api.wazo.community.

More specific documentation:

.. toctree::
   :maxdepth: 2

   templates


Changelog
=========

17.12
-----

* New config options for subscriptions with service ``http``:

  * ``verify_certificate``
  * ``content_type``

* The config option ``body`` for subscriptions with service ``http`` now accept template values. See
  :ref:`webhookd_templates` for more details.
* A new API for checking the status of the daemon:

  * GET ``/1.0/status``

17.11
-----

* New resources to manage webhook subscriptions

  * GET ``/1.0/subscriptions``
  * POST ``/1.0/subscriptions``
  * GET ``/1.0/subscriptions/<uuid>``
  * PUT ``/1.0/subscriptions/<uuid>``
  * DELETE ``/1.0/subscriptions/<uuid>``


17.09
-----

* A new resource has been added to fetch the current configuration of wazo-webhookd

    * GET ``/1.0/config``
