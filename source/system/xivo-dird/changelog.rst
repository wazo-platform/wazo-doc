.. _dird_changelog:

*******************
xivo-dird changelog
*******************

15.13
=====

* Added private contacts endpoints in REST API:

  * GET ``/privates``
  * POST ``/privates``
  * DELETE ``/privates/<contact_id>``

* Signature of backend method ``list()`` has a new argument ``args``
* Argument ``args`` for backend methods ``list()`` and ``search()`` has a new key ``token_infos``
* Methods ``__call__()`` and ``lookup()`` of service plugin ``lookup`` take a new ``token_infos``
  argument


15.12
=====

* Added authentication on all REST API endpoints
* Service plugins receive the whole configuration, rather than only their own section
