.. _plugind_changelog:

*********************************
wazo-plugind REST API changelog
*********************************

17.09
=====

* ``POST /plugins`` now accepts a branch parameter


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
