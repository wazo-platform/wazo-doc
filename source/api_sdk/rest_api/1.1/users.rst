*****
Users
*****

.. TODO should either document the user-line association model (i.e. a line's main
   user vs secondary user and related constraint) or add a link to where this is
   documented

User Representation
===================

Description
-----------

+-----------------------+--------+------------------------------------------------------------------------+
| Field                 | Values | Description                                                            |
+=======================+========+========================================================================+
| id                    | int    | Read-only                                                              |
+-----------------------+--------+------------------------------------------------------------------------+
| firstname             | string | User's first name                                                      |
+-----------------------+--------+------------------------------------------------------------------------+
| lastname              | string | User's last name                                                       |
+-----------------------+--------+------------------------------------------------------------------------+
| timezone              | string | User's timezone                                                        |
+-----------------------+--------+------------------------------------------------------------------------+
| language              | string | User's language                                                        |
+-----------------------+--------+------------------------------------------------------------------------+
| description           | string | Additional information about the user                                  |
+-----------------------+--------+------------------------------------------------------------------------+
| caller_id             | string | Name that appears on the phone when calling                            |
+-----------------------+--------+------------------------------------------------------------------------+
| outgoing_caller_id    | string | Caller id to use when calling through a trunk                          |
+-----------------------+--------+------------------------------------------------------------------------+
| mobile_phone_number   | string | Phone number for the user's mobile device                              |
+-----------------------+--------+------------------------------------------------------------------------+
| username              | string | username for connecting to the CTI                                     |
+-----------------------+--------+------------------------------------------------------------------------+
| password              | string | password for connecting to the CTI                                     |
+-----------------------+--------+------------------------------------------------------------------------+
| music_on_hold         | string | Name of the MOH category to use for music on hold                      |
+-----------------------+--------+------------------------------------------------------------------------+
| preprocess_subroutine | string | Name of the subroutine to execute in asterisk before receiving a call  |
+-----------------------+--------+------------------------------------------------------------------------+
| userfield             | string | A custom field which purpose is left to the client. If the user has no |
|                       |        | userfield, then this field is an empty string.                         |
+-----------------------+--------+------------------------------------------------------------------------+



Example
-------

::

   {
       "id": 1,
       "firstname": "John",
       "lastname": "Doe",
       "timezone": "America/Montreal",
       "language": "fr_FR",
       "description": "The most common name in America",
       "caller_id": "Johnny",
       "outgoing_caller_id": "default",
       "mobile_phone_number": "5554151234",
       "username": "john",
       "password": "supersecretpassword",
       "music_on_hold": "waiting",
       "preprocess_subroutine": "ivr",
       "userfield": ""
   }


List Users
==========

The users are listed in ascending order on lastname, then firstname.

Query
-----

::

   GET /1.1/users

Parameters
----------

.. warning:: filtering on the line number is not implemented yet

q
   List only users matching this filter.
   The filter is done on the firstname, lastname and firstname + lastname and is case insensitive.


Example requests
----------------

Listing all available users::

   GET /1.1/users HTTP/1.1
   Host: xivoserver
   Accept: application/json

Searching for a user called "john"::

   GET /1.1/users?q=john HTTP/1.1
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
                "firstname": "John",
                "lastname": "Doe",
                "timezone": "",
                "language": "en_US",
                "description": "",
                "caller_id": "\"John Doe\"",
                "outgoing_caller_id": "default",
                "mobile_phone_number": "",
                "username": "",
                "password": "",
                "music_on_hold": "default",
                "preprocess_subroutine": "",
                "userfield": ""
           },
           {
                "id": 2,
                "firstname": "Mary",
                "lastname": "Sue",
                "timezone": "",
                "language": "fr_FR",
                "description": "",
                "caller_id": "\"Mary Sue\"",
                "outgoing_caller_id": "default",
                "mobile_phone_number": "",
                "username": "",
                "password": "",
                "music_on_hold": "default",
                "preprocess_subroutine": "",
                "userfield": ""
           }
       ]
   }


Get User
--------

::

   GET /1.1/users/<id>

Parameters
----------

include
   See `List Users`_.

Example request
---------------

::

   GET /1.1/users/1 HTTP/1.1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
                "id": 1,
                "firstname": "John",
                "lastname": "Doe",
                "timezone": "",
                "language": "en_US",
                "description": "",
                "caller_id": "\"John Doe\"",
                "outgoing_caller_id": "default",
                "mobile_phone_number": "",
                "username": "",
                "password": "",
                "music_on_hold": "default",
                "preprocess_subroutine": "",
                "userfield": ""
   }


Create a User
=============

Query
-----

::

   POST /1.1/users

Input
-----

+-----------------------+----------+--------------------------------------+
| Field                 | Required | Values                               |
+=======================+==========+======================================+
| firstname             | yes      | string                               |
+-----------------------+----------+--------------------------------------+
| lastname              | no       | string                               |
+-----------------------+----------+--------------------------------------+
| timezone              | no       | string. Must be a valid timezone     |
+-----------------------+----------+--------------------------------------+
| language              | no       | string. Must be a valid language     |
+-----------------------+----------+--------------------------------------+
| description           | no       | string                               |
+-----------------------+----------+--------------------------------------+
| caller_id             | no       | string                               |
+-----------------------+----------+--------------------------------------+
| outgoing_caller_id    | no       | string: default, anonymous or custom |
+-----------------------+----------+--------------------------------------+
| mobile_phone_number   | no       | string of digits                     |
+-----------------------+----------+--------------------------------------+
| username              | no       | string                               |
+-----------------------+----------+--------------------------------------+
| password              | no       | string. Minimum of 4 characters      |
+-----------------------+----------+--------------------------------------+
| music_on_hold         | no       | string. Must be a valid category     |
+-----------------------+----------+--------------------------------------+
| preprocess_subroutine | no       | string                               |
+-----------------------+----------+--------------------------------------+
| userfield             | no       | string                               |
+-----------------------+----------+--------------------------------------+

Errors
------


+------------+------------------------------------------+--------------------------------+
| Error code | Error message                            | Description                    |
+============+==========================================+================================+
| 400        | error while creating User: <explanation> | See explanation for more infos |
+------------+------------------------------------------+--------------------------------+

Example request
---------------

::

   POST /1.1/users HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
       "firstname": "John",
       "lastname": "Doe",
       "userfield": ""
   }

Example response
----------------

::

   HTTP/1.1 201 Created
   Location: /1.1/users/1
   Content-Type: application/json

   {
       "id": 1,
       "firstname": "John",
       "lastname": "Doe",
       "timezone": "",
       "language": "en_US",
       "description": "",
       "caller_id": "\"John Doe\"",
       "outgoing_caller_id": "default",
       "mobile_phone_number": "",
       "username": "",
       "password": "",
       "music_on_hold": "default",
       "preprocess_subroutine": "",
       "userfield": ""
       "links" : [
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/1"
           }
       ]
   }


Update a User
=============

Only the fields that need to be modified can be set.

If the firstname or the lastname is modified, the name of associated voicemail is also updated.

Query
-----

::

   PUT /1.1/users/<id>

Input
-----

Same as for creating a User. Please see `Create a User`_


Errors
------

Same as for creating a User. Please see `Create a User`_


Example request
---------------

::

   PUT /1.1/users/67 HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

   {
       "firstname": "Jonathan"
   }


Example response
----------------

::

   HTTP/1.1 204 No Content


Delete User
===========

The user will not be removed if he is associated to a line and an extension. You must delete the
association first.

The user will also be removed from all queues, groups or other XiVO entities whom he is member.


Query
-----

::

   DELETE /1.1/users/<id>

Errors
------

+------------+------------------------------------------+-------------------------------------------------------------+
| Error code | Error message                            | Description                                                 |
+============+==========================================+=============================================================+
| 400        | error while deleting User: <explanation> | The requested user is probably associated to other objects. |
|            |                                          | See explanation for more infos                              |
+------------+------------------------------------------+-------------------------------------------------------------+
| 404        | Empty                                    | The requested user was not found                            |
+------------+------------------------------------------+-------------------------------------------------------------+

Example request
---------------

::

   DELETE /1.1/users/67 HTTP/1.1
   Host: xivoserver

Example response
----------------

::

   HTTP/1.1 204 No Content


User-Line-Extension Association
===============================

See :ref:`user-line-extension-association`.


User-Line Association
=====================

See :ref:`user-line-association`.


Users-Voicemails Association
============================

See :ref:`user-voicemail-association`.
