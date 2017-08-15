.. _plugind_changelog:

*******************************
wazo-plugind REST API changelog
*******************************


.. _plugind_changelog_v02:

17.12
=====

* New resource added ``GET /plugins/<namespace>/<name>``


17.11
=====

* REST API Version ``0.1`` has been deprecated and will be removed in Wazo ``18.02``
* REST API Version ``0.2`` has been added with the following changes

  * ``POST /plugins`` does not have a ``url`` parameter has top level argument in its body
  * ``POST /plugins`` now requires an ``url`` parameter in its options field when using the ``git`` method
  * ``POST /plugins`` now accepts an ``url`` parameter in its options fields when using the ``market`` method


Example:

.. code-block:: sh

   # Version 0.1
   curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ \
     "url": "https://git.example.com/repo.git", \
     "method": "git", \
     "options": {"ref": "v1"} \
   }' 'https://wazo.example.com:9503/0.1/plugins'

   # Version 0.2
   curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ \
     "method": "git", \
     "options": {"ref": "v1", "url": "https://git.example.com/repo.git"} \
   }' 'https://wazo.example.com:9503/0.2/plugins'


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
