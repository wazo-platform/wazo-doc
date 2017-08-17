**********************
wazo-webhookd REST API
**********************

API reference
=============

API documentation is available on http://api.wazo.community.


Changelog
=========

17.12
-----

* New config option ``verify_certificate`` for subscriptions with service ``http``


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
