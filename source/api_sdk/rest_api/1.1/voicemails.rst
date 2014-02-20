**********
Voicemails
**********


Voicemail Representation
========================

Description
-----------

+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| Field           | Values  | Description                                                                                                           |
+=================+=========+=======================================================================================================================+
| id              | integer | (Read-only)                                                                                                           |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| name            | string  | Voicemail name.                                                                                                       |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| number          | string  | Voicemail number.                                                                                                     |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| context         | string  | Voicemail's context.                                                                                                  |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| password        | string  | Numeric password used to access the mailbox                                                                           |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| email           | string  | Email address where messages will be sent.                                                                            |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| language        | string  | Language used for the voicemail menu prompt. See `Voicemail languages`_ for a list of available languages.            |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| timezone        | string  | Timezone used for announcing at what time a message was recorded. See `Voicemail timezones`_ for a list of timezones. |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| max_messages    | integer | Maximum number of messages to store.                                                                                  |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| attach_audio    | boolean | Attach an audio file of the recorded message when sending an email.                                                   |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| delete_messages | boolean | Delete messages once they have been listened to.                                                                      |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+
| ask_password    | boolean | Ask for password when accessing the voicemail menu.                                                                   |
+-----------------+---------+-----------------------------------------------------------------------------------------------------------------------+


Example
-------

::

   {
       "id": "1",
       "name": "John Doe",
       "number": "1000",
       "context": "default",
       "password": "1234",
       "email": "john.doe@example.com",
       "language": "en_US",
       "timezone": "eu-fr",
       "max_messages": 10,
       "attach_audio: false,
       "delete_messages": false,
       "ask_password": true,
       "links": [
            {
                "rel": "voicemails",
                "href: "https://xivoserver/1.1/voicemails/1"
            }
        ]
    }


Voicemail list
==============

Query
-----

::

    GET /1.1/voicemails


Parameters
----------


order
   Sort the list using a column (e.g. "number"). Columns allowed: name, number, context, email, language, timezone.

direction
    'asc' or 'desc'. Sort list in ascending (asc) or descending (desc) order

limit
    total number of voicemails to show in the list. Must be a positive integer

skip
    number of voicemails to skip over before starting the list. Must be a positive integer

search
    Search voicemails. Only voicemails with a field containing the search term
    will be listed.

Errors
------

+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| Error code | Error message                                                        | Description                                                              |
+============+======================================================================+==========================================================================+
| 400        | Invalid parameters: limit must be a positive number                  | the 'limit' parameter must be a number                                   |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: skip must be a positive number                   | the 'skip' parameter must be a number                                    |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: ordering parameter '<field>' does not exist      | you must use one of the fields available in a device when sorting a list |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: direction parameter '<direction>' does not exist | use either 'asc' or 'desc' as a direction when sorting a list            |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+


Example requests
----------------

List all available voicemails::

    GET /1.1/voicemails HTTP/1.1
    Host: xivoserver
    Accept: application/json

List voicemails, sort by descending number::

    GET /1.1/voicemails?order=number&direction=desc
    Host: xivoserver
    Accept: application/json

List only the first 10 voicemails containing the word "john"::

    GET /1.1/voicemails?search=john&limit=10
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items": [
            {
                "id": "1",
                "name": "John Doe",
                "number": "1000",
                "context": "default",
                "password": null,
                "email": "john.doe@example.com",
                "language": "en_US",
                "timezone": "eu-fr",
                "max_messages": null,
                "attach_audio: false,
                "delete_messages": false,
                "ask_password": false,
                "links": [
                    {
                        "rel": "voicemails",
                        "href: "https://xivoserver/1.1/voicemails/1"
                    }
                ]
            },
            {
                "id": "2",
                "name": "Roger Smith",
                "number": "1001",
                "context": "default",
                "password": null,
                "email": null,
                "language": "en_US",
                "timezone": "eu-fr",
                "max_messages": 20,
                "attach_audio: false,
                "delete_messages": false,
                "ask_password": false,
                "links": [
                    {
                        "rel": "voicemails",
                        "href: "https://xivoserver/1.1/voicemails/2"
                    }
                ]
            }
        ]
    }


Get Voicemail
=============

Query
-----

::

    GET /1.1/voicemails/<id>

Example request
---------------

::

    GET /1.1/voicemails/1 HTTP/1.1
    Host: xivoserver
    Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

    {
        "id": "1",
        "name": "John Doe",
        "number": "1000",
        "context": "default",
        "password": null,
        "email": "john.doe@example.com",
        "language": "en_US",
        "timezone": "eu-fr",
        "max_messages": null,
        "attach_audio: false,
        "delete_messages": false,
        "ask_password": false,
        "links": [
            {
                "rel": "voicemails",
                "href: "https://xivoserver/1.1/voicemails/2"
            }
        ]
    }


Create a Voicemail
==================

Query
-----

::

    POST /1.1/voicemails

Input
-----

+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Field           | Required | Values  | Notes                                                                                                                                   |
+=================+==========+=========+=========================================================================================================================================+
| name            | yes      | string  |                                                                                                                                         |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| number          | yes      | string  | Must be a string of positive numbers                                                                                                    |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| context         | yes      | string  |                                                                                                                                         |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| password        | no       | string  | Must be a string of positive numbers                                                                                                    |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| email           | no       | string  |                                                                                                                                         |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| language        | no       | string  | Consult `Voicemail Languages`_ for a list of valid languages. The system default will be used if none is specified.                     |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| timezone        | no       | string  | Consult `Voicemail Timezones`_ for a list of valid timezones. The system default will be used if none is specified.                     |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| max_messages    | no       | integer | Valid values are: 1,10,15,20,25,50,75,100,125,150,175,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,9999 |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| attach_audio    | no       | boolean | Default value is `false`                                                                                                                |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| delete_messages | no       | boolean | Default value is `false`                                                                                                                |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ask_password    | no       | boolean | Default value is `false`                                                                                                                |
+-----------------+----------+---------+-----------------------------------------------------------------------------------------------------------------------------------------+

Errors
------

+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Error code | Error message                                                              | Description                                                                          |
+============+============================================================================+======================================================================================+
| 500        | Error while creating Voicemail: <explanation>                              | See explanation for more details.                                                    |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Error while creating Voicemail: number <number> already exists             | A voicemail with the same number already exists. Use another number.                 |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Invalid parameters: password                                               | Only numeric passwords are supported.                                                |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Invalid parameters: number <number> must be a sequence of positive numbers | The string must only have positive numbers                                           |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Invalid parameters: max_messages must be greater than 0                    | Only positive integers are accepted.                                                 |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Nonexistent parameters: context <context> does not exist                   | The context used by the voicemail does not exist. You must create the context first. |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Nonexistent parameters: language <language> does not exist                 | Consult `Voicemail Languages`_ for a list of available languages.                    |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Nonexistent parameters: timezone <timezone> does not exist                 | Consult `Voicemail Timezones`_ for a list of available timezones.                    |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| 400        | Missing parameters: <list of missing fields>                               |                                                                                      |
+------------+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------+

Example request
---------------

::

   POST /1.1/voicemails HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
        "name": "John Doe",
        "number": "1000",
        "context": "default"
   }

Example response
----------------

::

   HTTP/1.1 201 Created
   Location: /1.1/voicemails/1
   Content-Type: application/json

   {
        "id": "1",
        "name": "John Doe",
        "number": "1000",
        "context": "default",
        "password": null,
        "email": null,
        "language": null,
        "timezone": "eu-fr"
        "max_messages": null,
        "attach_audio: false,
        "delete_messages": false,
        "ask_password": false,
        "links": [
            {
                "rel": "voicemails",
                "href: "https://xivoserver/1.1/voicemails/2"
            }
        ]
   }

Update a Voicemail
==================

Only the fields that need to be updated must be sent during an update. A voicemail
can only be updated if it isn't associated to a user.

Query
-----

::

   PUT /1.1/voicemails/<id>

Parameters
----------

id
    Voicemail's id

Input
-----

Same as for creating a voicemail. Please see `Create a Voicemail`_

Errors
------

Same as creating a voicemail (See `Create a Voicemail`_) with the following additions:


+------------+-----------------------------------------------------------------------------+-------------+
| Error code | Error message                                                               | Description |
+============+=============================================================================+=============+
| 400        | Error while editing Voicemail: cannot edit a voicemail associated to a user |             |
+------------+-----------------------------------------------------------------------------+-------------+


Example request
---------------

::

   PUT /1.1/voicemails/1 HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

   {
       "number": "2000",
       "attach_audio": true
   }

Example response
----------------

::

   HTTP/1.1 204 No Content


Delete a Voicemail
==================

A voicemail can not be deleted if it is still attached to a user.
The user must be dissociated first.
Consult the documentation on :ref:`user-voicemail-association` for futher details.

.. warning::
    Any extension that redirects to the voicemail (e.g. an Incoming call) will be disabled after deletion.

Errors
------

+------------+--------------------------------------------------------------------------------+-------------------------------------------------------------------+
| Error code | Error message                                                                  | Description                                                       |
+============+================================================================================+===================================================================+
| 400        | error while deleting Voicemail <explanation>                                   | See error message for more details                                |
+------------+--------------------------------------------------------------------------------+-------------------------------------------------------------------+
| 400        | error while deleting Voicemail: Cannot delete a voicemail associated to a user | You must unassociate a user from his voicemail before deleting it |
+------------+--------------------------------------------------------------------------------+-------------------------------------------------------------------+
| 404        | Not found                                                                      | The requested voicemail was not found or does not exist           |
+------------+--------------------------------------------------------------------------------+-------------------------------------------------------------------+

Query
-----

::

   DELETE /1.1/voicemails/<id>

Example request
---------------

::

   DELETE /1.1/voicemails/1 HTTP/1.1
   Host: xivoserver

Example response
----------------

::

   HTTP/1.1 204 No Content


Voicemail Languages
===================

.. warning:: Not yet implemented.

Returns a list of languages that can be used when creating or updating a voicemail.

Query
-----

::

    GET /1.1/voicemails/languages

Example request
---------------

::

   GET /1.1/voicemails/languages HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 7,
       "items": [
            "de_DE",
            "en_US",
            "es_ES",
            "fr_FR",
            "fr_CA",
            "it_IT",
            "nl_NL"
        ]
    }


Voicemail Timezones
===================

.. warning:: Not yet implemented.

Returns a list of timezones that can be used when creating or updating a voicemail.

Query
-----

::

    GET /1.1/voicemails/timezones

Example request
---------------

::

   GET /1.1/voicemails/timezones HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 1,
       "items": [
            "eu-fr"
        ]
   }
