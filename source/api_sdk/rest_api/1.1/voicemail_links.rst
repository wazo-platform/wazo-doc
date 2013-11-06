.. _voicemail-links-association-api:

*********************
Voicemail Association
*********************

Service for associating a user with a voicemail.


Association Representation
==========================

Description
-----------

+--------------+-------+---------------------------+
| Field        | Value | Description               |
+==============+=======+===========================+
| voicemail_id | int   | Voicemail's ID            |
+--------------+-------+---------------------------+
| enabled      | bool  | Enable voicemail for user |
+--------------+-------+---------------------------+


Get the Voicemail associated to a User
======================================

Query
-----

::

    GET /1.1/users/<user_id>/voicemail

Errors
------

+------------+----------------------------------------------------------------------+-------------+
| Error code | Error message                                                        | Description |
+============+======================================================================+=============+
| 404        | Invalid parameters: user with id=<user_id> does not have a voicemail |             |
+------------+----------------------------------------------------------------------+-------------+
| 404        | User with id=<user_id> does not exist                                |             |
+------------+----------------------------------------------------------------------+-------------+


Example request
---------------

::

    GET /1.1/users/20/voicemail
    Host: xivoserver
    Accept: application/json

Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "voicemail_id": 132,
        "user_id": 20,
        "enabled": true,
        "links": [
           {
               "rel": "voicemails",
               "href": "https://xivoserver/1.1/voicemails/132"
           },
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/20"
           }
        ]
    }



Associate a User to a Voicemail
===============================

Query
-----

::

    POST /1.1/users/<user_id>/voicemail

Input
-----

+--------------+----------+--------+------------------------+
| Field        | Required | Values | Description            |
+==============+==========+========+========================+
| voicemail_id | yes      | int    | Must be an existing id |
+--------------+----------+--------+------------------------+
| enabled      | no       | bool   | Default value : true   |
+--------------+----------+--------+------------------------+


Errors
------

+------------+--------------------------------------------------------------------+---------------------------------------------------------------------------+
| Error code | Error message                                                      | Description                                                               |
+============+====================================================================+===========================================================================+
| 400        | Nonexistent parameters: voicemail_id <voicemail_id> does not exist |                                                                           |
+------------+--------------------------------------------------------------------+---------------------------------------------------------------------------+
| 400        | Invalid parameters: user with id <user_id>  does not have any line | A user needs to have a line to associate a voicemail                      |
+------------+--------------------------------------------------------------------+---------------------------------------------------------------------------+
| 400        | Invalid parameters: user with id <user_id> already has a voicemail | You must unassociate the current voicemail before reassociating a new one |
+------------+--------------------------------------------------------------------+---------------------------------------------------------------------------+

Example request
---------------

::

    POST /1.1/users/59/voicemail
    Host: xivoserver
    Content-Type: application/json

    {
        "voicemail_id": 432,
        "enabled": false,
    }

Example response
----------------

::

    HTTP/1.1 201
    Location: /1.1/users/59/voicemail

    {
        "voicemail_id": 432,
        "user_id": 59,
        "enabled": false,
        "links": [
           {
               "rel": "voicemails",
               "href": "https://xivoserver/1.1/voicemails/432"
           },
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/59"
           }
        ]
    }


Deassociate a User from a Voicemail
===================================


Query
-----

::

    DELETE /1.1/users/<user_id>/voicemail


Example request
---------------

::

    DELETE /1.1/users/20/voicemail
    Host: xivoserver

Example response
----------------

::

    HTTP/1.1 204 No Content
