******************
xivo-dird REST API
******************

API reference
=============

API documentation is available on http://api.xivo.io.


Changelog
=========

16.14
-----

* The `exclude` query parameter has been added to the following routes to exclude
  directory sources from searches.

    * GET ``/0.1/directories/lookup/<profile>``
    * GET ``/0.1/directories/reverse/<profile>/<xivo_user_uuid>``

