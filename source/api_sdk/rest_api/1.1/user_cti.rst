.. _user-cti-configuration:

**********************
User CTI configuration
**********************


CTI Configuration Representation
================================

Description
-----------

+----------------+-------+---------------------------------+
| Field          | Value | Description                     |
+================+=======+=================================+
| user_id        | int   | User's ID. Read-only.           |
+----------------+-------+---------------------------------+
| cti_profile_id | int   | CTI Profile's ID.               |
+----------------+-------+---------------------------------+
| enabled        | bool  | Status of the CTI configuration |
+----------------+-------+---------------------------------+

Get the CTI Configuration for a User
====================================

Query
-----

::

    GET /users/<user_id>/cti

Errors
------

+------------+---------------------------------------+-------------+
| Error code | Error message                         | Description |
+============+=======================================+=============+
| 404        | User with id=<user_id> does not exist |             |
+------------+---------------------------------------+-------------+


Example Request
---------------

::

    GET /users/34/cti
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


Edit the CTI configuration of a user
====================================

Query
-----

::

    PUT /users/<user_id>/cti


Input
-----

+----------------+----------+--------+--------------------------+
| Field          | Required | Values | Description              |
+================+==========+========+==========================+
| cti_profile_id | yes      | int    | Must be an existing id   |
+----------------+----------+--------+--------------------------+
| enabled        | yes      | bool   | Enable / disable the CTI |
+----------------+----------+--------+--------------------------+


Errors
------

+------------+------------------------------------------------------------------------+-------------------------------------------+
| Error code | Error message                                                          | Description                               |
+============+========================================================================+===========================================+
| 404        | User with id=<user_id> does not exist                                  |                                           |
+------------+------------------------------------------------------------------------+-------------------------------------------+
| 400        | Nonexistent parameters: cti_profile_id <cti_profile_id> does not exist |                                           |
+------------+------------------------------------------------------------------------+-------------------------------------------+
| 400        | The user must have a username and password to enable the CTI           | Add a username and a password to the user |
+------------+------------------------------------------------------------------------+-------------------------------------------+


Example request
---------------

::

    PUT /1.1/users/75/cti
    Host: xivoserver
    Content-Type: application/json

    {
        "cti_profile_id": 3,
        "enabled": true
    }


Example response
----------------

::

    HTTP/1.1 204 No Content
