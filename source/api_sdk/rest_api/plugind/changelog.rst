.. _plugind_changelog:

*********************************
wazo-plugind REST API changelog
*********************************

17.10
=====

* New endpoint for the plugin market

  * ``GET /market``

* Added the ``market`` install method to ``POST /plugins``


17.09
=====

* ``POST /plugins`` now accepts an ``options`` parameter for method specific arguments


17.08
=====

* ``POST /plugins`` and ``DELETE /plugins`` are now asynchronous


17.07
=====

* New endpoint for plugins

  * ``POST /plugins``
  * ``GET /plugins``
  * ``DELETE /plugins/<namespace>/<name>``


17.05
=====

* New endpoint to fetch the configuration:

  * ``GET /config``
