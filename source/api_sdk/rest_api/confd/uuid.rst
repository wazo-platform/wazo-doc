****
UUID
****

A XiVO UUID

UUID Representation
===================

Description
-----------

+-------+--------+-------------+
| Field | Values | Description |
+=======+========+=============+
| uuid  | string | XiVO's UUID |
+-------+--------+-------------+

Example
-------

::

   {
       "uuid": "6fa459ea-ee8a-3ca4-894e-db77e160355e"
   }


Get UUID
========

Query
-----

::

   GET /1.1/uuid

Example request
---------------

::

   GET /1.1/uuid HTTP/1.1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "uuid": "6fa459ea-ee8a-3ca4-894e-db77e160355e"
   }