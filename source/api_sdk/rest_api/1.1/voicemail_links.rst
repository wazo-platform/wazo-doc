.. _voicemail-links-association-api:

***************************
Voicemail Links Association
***************************


Association Representation
==========================

Description
-----------

+--------------+-------+-------------+
| Field        | Value | Description |
+==============+=======+=============+
| voicemail_id | int   |             |
+--------------+-------+-------------+


Get a Voicemail from an User
============================

Query
-----

::

    GET /1.1/users/<user_id>/voicemails

Example request
---------------

::

    GET /1.1/users/20/voicemails
    Host: xivoserver

Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "voicemail_id": 432,
        "links": [
           {
               "rel": "voicemails",
               "href": "https://xivoserver/1.1/voicemails/432"
           },
    }



Associate a User to a Voicemail
===============================

Query
-----

::

    POST /1.1/users/<user_id>/voicemails

Input
-----

+--------------+----------+--------+------------------------+
| Field        | Required | Values | Description            |
+==============+==========+========+========================+
| voicemail_id | yes      | int    | Must be an existing id |
+--------------+----------+--------+------------------------+

Example request
---------------

::

    POST /1.1/users/59/voicemails
    Host: xivoserver
    Content-Type: application/json

    {
        "voicemail_id": 432,
    }

Example response
----------------

::

    HTTP/1.1 204 No Content



Remove a user from a voicemail
==============================


Query
-----

::

    DELETE /1.1/users/<user_id>/voicemails

Example request
---------------

::

    DELETE /1.1/users/20/voicemails
    Host: xivoserver

Example response
----------------

::

    HTTP/1.1 204 No Content
