.. _voicemail-links-association-api:

***************************
Voicemail Links Association
***************************


Get a Voicemail from an User
============================

**Parameters**

voicemail_id
    Voicemail's id

::

    GET /1.1/users/<user_id>/voicemail

**Example request**::

    GET /1.1/users/20/voicemail
    Host: xivoserver

**Example response**::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "voicemail_id": 432,
    }



Associate a User to a Voicemail
===============================

**Parameters**

voicemail_id
    Voicemail's id

::

    POST /1.1/users/<user_id>/voicemail

**Input**

+--------------+----------+--------+----------------------------------+
| Field        | Required | Values | Description                      |
+==============+==========+========+==================================+
| voicemail_id | yes      | Int    | Must be an existing voicemail id |
+--------------+----------+--------+----------------------------------+

**Example request**::

    POST /1.1/users/59/voicemail
    Host: xivoserver
    Content-Type: application/json

    {
        "voicemail_id": 432,
    }

**Example response**::

    HTTP/1.1 204 No Content



Remove a user from a voicemail
==============================

**Parameters**

voicemail_id
    Voicemail's id

::

    DELETE /1.1/users/<user_id>/voicemail

**Example request**::

    DELETE /1.1/users/20/voicemail
    Host: xivoserver

**Example response**::

    HTTP/1.1 204 No Content
