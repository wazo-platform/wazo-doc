.. _restapi-cti-profile:

************
CTI Profiles
************

CTI Profiles representation
===========================

Description
-----------

+-------+---------+-------------------------+
| Field | Values  | Description             |
+=======+=========+=========================+
| id    | integer | Read-only               |
+-------+---------+-------------------------+
| name  | string  | Display name            |
+-------+---------+-------------------------+


Example
-------

::

   {
       "id": 1,
       "name": "Client"
   }


CTI Profiles list
=================

Query
-----

::

   GET /1.1/cti_profiles

Example requests
----------------

Listing all available CTI profiles:

::

   GET /1.1/cti_profiles HTTP/1.1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items":
       [
           {
                "id": 1,
                "name": "Client"
           },
           {
                "id": 2,
                "name": "Agent"
           }
       ]
   }


Get CTI Profile
===============

Query
-----

::

   GET /1.1/cti_profiles/<id>

Example request
---------------

::

   GET /1.1/cti_profiles/1 HTTP/1.1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
        "id": 1,
        "name": "Client"
   }
