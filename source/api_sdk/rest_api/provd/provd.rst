****************
Provd Management
****************

.. _provd-api-provd-mgr:

Get the Provd Manager
=====================

The provd manager resource represents the main entry point to the xivo-provd REST API.

It links to the following resources:

* The ``dev`` relation links to a :ref:`device manager <provd-api-dev-mgr>`.
* The ``cfg`` relation links to a :ref:`config manager <provd-api-cfg-mgr>`.
* The ``pg`` relation links to a :ref:`plugin manager <provd-api-pg-mgr>`.
* The ``srv.configure`` relation links to the provd manager :ref:`configuration service <provd-api-configure>`.


Query
-----

.. code-block:: http

   GET /provd


Example request
---------------

.. code-block:: http

   GET /provd HTTP/1.1
   Host: xivoserver
   Accept: application/vnd.proformatique.provd+json


Example response
----------------

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/vnd.proformatique.provd+json

   {
       "links": [
           {
               "href": "/provd/dev_mgr",
               "rel": "dev"
           },
           {
               "href": "/provd/cfg_mgr",
               "rel": "cfg"
           },
           {
               "href": "/provd/pg_mgr",
               "rel": "pg"
           },
           {
               "href": "/provd/configure",
               "rel": "srv.configure"
           }
       ]
   }
