.. _dird_changelog:

*****************************
xivo-dird REST API changelog
*****************************

15.13
=====

* Added private contacts endpoints in REST API:

  * GET ``/privates``
  * POST ``/privates``
  * DELETE ``/privates/<contact_id>``

* Methods ``search()`` and ``list()`` signature for backends has changed:

  * new argument ``args``

* Service plugin ``lookup`` takes a new ``token_infos`` argument

15.12
=====

* Added authentication on all REST API endpoints
* Service plugins receive the whole configuration, rather than only their own section
