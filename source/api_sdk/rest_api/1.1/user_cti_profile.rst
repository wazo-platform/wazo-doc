.. _user-cti-profile-association:

******************************
User - CTI Profile Association
******************************


Association Representation
==========================

Description
-----------

+----------------+-------+-----------------------+
| Field          | Value | Description           |
+================+=======+=======================+
| user_id        | int   | User's ID. Read-only. |
+----------------+-------+-----------------------+
| cti_profile_id | int   | CTI Profile's ID.     |
+----------------+-------+-----------------------+

Get the CTI profile associated to a User
========================================

Query
-----

::

    GET /users/<user_id>/cti_profile

Errors
------

+------------+----------------------------------------------------+-------------+
| Error code | Error message                                      | Description |
+============+====================================================+=============+
| 404        | User with id=<user_id> does not exist              |             |
+------------+----------------------------------------------------+-------------+
| 404        | User with id=<user_id> does not have a CTI profile |             |
+------------+----------------------------------------------------+-------------+


Example Request
---------------

::

    GET /users/34/cti_profile
    Host: xivoserver
    Accept: application/json


Example Response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "user_id": 34,
        "cti_profile_id": 2,
        "links": [
            {
                "rel": "users",
                "href": "https://xivoserver/1.1/users/34"
            },
            {
                "rel": "cti_profiles",
                "href": "https://xivoserver/1.1/cti_profiles/2"
            }
        ]
    }


Associate a CTI Profile to a User
=================================

Query
-----

::

    POST /users/<user_id>/cti_profile


Input
-----

+----------------+----------+--------+------------------------+
| Field          | Required | Values | Description            |
+================+==========+========+========================+
| cti_profile_id | yes      | int    | Must be an existing id |
+----------------+----------+--------+------------------------+


Errors
------

+------------+------------------------------------------------------------------------+--------------------------------------------+
| Error code | Error message                                                          | Description                                |
+============+========================================================================+============================================+
| 404        | User with id=<user_id> does not exist                                  |                                            |
+------------+------------------------------------------------------------------------+--------------------------------------------+
| 400        | Nonexistent parameters: cti_profile_id <cti_profile_id> does not exist |                                            |
+------------+------------------------------------------------------------------------+--------------------------------------------+
| 400        | Invalid parameters: user with id <user_id> already has a CTI profile   | Please use a PUT to update the association |
+------------+------------------------------------------------------------------------+--------------------------------------------+


Example request
---------------

::

    POST /1.1/users/75/cti_profile
    Host: xivoserver
    Content-Type: application/json

    {
        "cti_profile_id": 3
    }


Example response
----------------

::

    HTTP/1.1 201
    Location: /1.1/users/75/cti_profile

    {
        "user_id": 75,
        "cti_profile_id": 3,
        "links": [
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/75"
           },
           {
               "rel": "cti_profiles",
               "href": "https://xivoserver/1.1/cti_profiles/3"
           }
        ]
    }


Dissociate a CTI Profile from a User
====================================


Query
-----

::

    DELETE /1.1/users/<user_id>/cti_profile


Errors
------

+------------+----------------------------------------------------+-------------+
| Error code | Error message                                      | Description |
+============+====================================================+=============+
| 404        | User with id=<user_id> does not exist              |             |
+------------+----------------------------------------------------+-------------+
| 404        | User with id=<user_id> does not have a CTI profile |             |
+------------+----------------------------------------------------+-------------+


Example request
---------------

::

    DELETE /1.1/users/<user_id>/cti_profile
    Host: xivoserver


Example response
----------------

::

    HTTP/1.1 204 No Content

Change the CTI Profile associated to a User
===========================================

Query
-----

::

    PUT /users/<user_id>/cti_profile


Input
-----

+----------------+----------+--------+------------------------+
| Field          | Required | Values | Description            |
+================+==========+========+========================+
| cti_profile_id | yes      | int    | Must be an existing id |
+----------------+----------+--------+------------------------+


Errors
------

+------------+------------------------------------------------------------------------+-------------+
| Error code | Error message                                                          | Description |
+============+========================================================================+=============+
| 404        | User with id=<user_id> does not exist                                  |             |
+------------+------------------------------------------------------------------------+-------------+
| 404        | User with id=<user_id> does not have a CTI profile                     |             |
+------------+------------------------------------------------------------------------+-------------+
| 400        | Nonexistent parameters: cti_profile_id <cti_profile_id> does not exist |             |
+------------+------------------------------------------------------------------------+-------------+


Example request
---------------

::

    PUT /1.1/users/75/cti_profile
    Host: xivoserver
    Content-Type: application/json

    {
        "cti_profile_id": 3
    }


Example response
----------------

::

    HTTP/1.1 200
    Location: /1.1/users/75/cti_profile

    {
        "user_id": 75,
        "cti_profile_id": 3,
        "links": [
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/75"
           },
           {
               "rel": "cti_profiles",
               "href": "https://xivoserver/1.1/cti_profiles/3"
           }
        ]
    }
