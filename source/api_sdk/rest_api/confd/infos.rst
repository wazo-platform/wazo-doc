*****
Infos
*****

A XiVO server infos


Infos Representation
====================

Description
-----------

+-------+--------+-------------+
| Field | Values | Description |
+=======+========+=============+
| uuid  | string | XiVO's UUID |
+-------+--------+-------------+


Example
-------

.. code-block:: javascript

   {
       "uuid": "6fa459ea-ee8a-3ca4-894e-db77e160355e"
   }


Get Infos
=========

Query
-----

.. code-block:: http

   GET /1.1/infos


Example request
---------------

.. code-block:: http

   GET /1.1/infos HTTP/1.1
   Host: xivoserver
   Accept: application/json


Example response
----------------

.. code-block:: http

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "uuid": "6fa459ea-ee8a-3ca4-894e-db77e160355e"
   }
