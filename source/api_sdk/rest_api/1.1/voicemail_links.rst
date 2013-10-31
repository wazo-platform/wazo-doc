.. _voicemail-links-association-api:

*********************
Voicemail Association
*********************

Service for associating a user with a voicemail.


Association Representation
==========================

Description
-----------

+--------------+-------+----------------+
| Field        | Value | Description    |
+==============+=======+================+
| voicemail_id | int   | Voicemail's ID |
+--------------+-------+----------------+


Get the Voicemail associated to a User
======================================

Query
-----

::

    GET /1.1/users/<user_id>/voicemail

Errors
------

+------------+----------------+-------------------------------------------------+
| Error code | Error message  | Description                                     |
+============+================+=================================================+
| 404        |                | The user does not have any voicemail associated |
+------------+----------------+-------------------------------------------------+

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

Errors
------

+------------+--------------------------------------------------------------------+------------------------------------------------------------+
| Error code | Error message                                                      | Description                                                |
+============+====================================================================+============================================================+
| 400        | Nonexistent parameters: voicemail_id <voicemail_id> does not exist |                                                            |
+------------+--------------------------------------------------------------------+------------------------------------------------------------+
| 400        | Invalid parameters: user <user_id> has no line                     | A user needs to have a line to assocaite a voicemail       |
+------------+--------------------------------------------------------------------+------------------------------------------------------------+
| 400        | Invalid parameters: user <user_id> already has a voicemail         | A user can only have a maximum of one voicemail associated |
+------------+--------------------------------------------------------------------+------------------------------------------------------------+

Example request
---------------

::

    POST /1.1/users/59/voicemail
    Host: xivoserver
    Content-Type: application/json

    {
        "voicemail_id": 432
    }

Example response
----------------

::

    HTTP/1.1 201
    Location: /1.1/users/59/voicemail

    {
        "voicemail_id": 432,
        "user_id": 59,
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
