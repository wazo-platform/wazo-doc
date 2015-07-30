.. _dird_changelog:

*******************
xivo-dird changelog
*******************

15.14
=====

* Added more personal contacts endpoints in REST API:

  * GET ``/0.1/personal/<contact_id>``
  * PUT ``/0.1/personal/<contact_id>``


15.13
=====

* Added personal contacts endpoints in REST API:

  * GET ``/0.1/directories/personal/<profile>``
  * GET ``/0.1/personal``
  * POST ``/0.1/personal``
  * DELETE ``/0.1/personal/<contact_id>``

* Signature of backend method ``list()`` has a new argument ``args``
* Argument ``args`` for backend methods ``list()`` and ``search()`` has a new key ``token_infos``
* Argument ``args`` for backend method ``load()`` has a new key ``main_config``
* Methods ``__call__()`` and ``lookup()`` of service plugin ``lookup`` take a new ``token_infos``
  argument


15.12
=====

* Added authentication on all REST API endpoints
* Service plugins receive the whole configuration, rather than only their own section
