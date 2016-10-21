.. _dird_changelog:

*******************
xivo-dird changelog
*******************

16.14
=====

* The ``phonebook`` backend has been removed in favor of the ``dird_phonebook`` backend.


16.12
=====

* Added phonebook imports

  * POST ``0.1/tenants/<tenant>/phonebooks/<phonebook_id>/contacts/import``


16.11
=====

* Added a new internal phonebook with a CRUD interface
* Added a new backend to do lookups in the new phonebook


15.20
=====

* The ldap plugins `ldap_network_timeout` default value has been incremented from 0.1 to 0.3 seconds


15.19
=====

* Added the ``voicemail`` type in :ref:`dird-integration-views` configuration
* Removed reverse endpoints in REST API:

  * GET ``/0.1/directories/reverse/<profile>/me``


15.18
=====

* Added reverse endpoints in REST API:

  * GET ``/0.1/directories/reverse/<profile>/<xivo_user_uuid>``
  * GET ``/0.1/directories/reverse/<profile>/me``


15.17
=====

* Added directories endpoints in REST API:

  * GET ``/0.1/directories/input/<profile>/aastra``
  * GET ``/0.1/directories/lookup/<profile>/aastra``
  * GET ``/0.1/directories/input/<profile>/polycom``
  * GET ``/0.1/directories/lookup/<profile>/polycom``
  * GET ``/0.1/directories/input/<profile>/snom``
  * GET ``/0.1/directories/lookup/<profile>/snom``
  * GET ``/0.1/directories/lookup/<profile>/thomson``
  * GET ``/0.1/directories/lookup/<profile>/yealink``


15.16
=====

* Added more cisco endpoints in REST API:

  * GET ``/0.1/directories/input/<profile>/cisco``
* Endpoint ``/0.1/directories/lookup/<profile>/cisco`` accepts a new ``limit`` and ``offset`` query string arguments.


15.15
=====

* Added cisco endpoints in REST API:

  * GET ``/0.1/directories/menu/<profile>/cisco``
  * GET ``/0.1/directories/lookup/<profile>/cisco``


15.14
=====

* Added more personal contacts endpoints in REST API:

  * GET ``/0.1/personal/<contact_id>``
  * PUT ``/0.1/personal/<contact_id>``
  * POST ``/0.1/personal/import``
  * DELETE ``/0.1/personal``

* Endpoint ``/0.1/personal`` accepts a new ``format`` query string argument.


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
