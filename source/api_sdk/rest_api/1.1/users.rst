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

+-----------+---------+------------------------------------------------------------------------+
| Field     | Values  | Description                                                            |
+===========+=========+========================================================================+
| id        | int     | Read-only                                                              |
+-----------+---------+------------------------------------------------------------------------+
| firstname | string  | If the user has no firstname, then this field is an empty string.      |
+-----------+---------+------------------------------------------------------------------------+
| lastname  | string  | If the user has no lastname, then this field is an empty string.       |
+-----------+---------+------------------------------------------------------------------------+
| userfield | boolean | A custom field which purpose is left to the client. If the user has no |
|           |         | userfield, then this field is an empty string.                         |
+-----------+---------+------------------------------------------------------------------------+

Example
-------

::

   {
       "id": 1,
       "firstname": "John",
       "lastname": "Doe",
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
               "userfield": ""
           },
           {
               "id": 2,
               "firstname": "Alice",
               "lastname": "Houet",
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
       "userfield": ""
   }


Create User
===========

Query
-----

::

   POST /1.1/users

Input
-----

+-----------+----------+--------+
| Field     | Required | Values |
+===========+==========+========+
| firstname | yes      | string |
+-----------+----------+--------+
| lastname  | no       | string |
+-----------+----------+--------+
| userfield | no       | string |
+-----------+----------+--------+

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
       "links" : [
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/1"
           }
       ]
   }


Update User
===========

The update does not need to set all the fields of the edited user. The update only needs to set the
modified fields.

If the firstname or the lastname is modified, the associated voicemail is also updated.

Query
-----

::

   PUT /1.1/users/<id>

Errors
------

+------------+-----------------------------------------+--------------------------------+
| Error code | Error message                           | Description                    |
+============+=========================================+================================+
| 400        | error while editing User: <explanation> | See explanation for more infos |
+------------+-----------------------------------------+--------------------------------+

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


Users-Voicemails Association
============================

See :ref:`user-voicemail-association`.
