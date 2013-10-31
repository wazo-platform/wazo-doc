.. _user-line-extension-association:

*******************************
User-Line-Extension Association
*******************************


Association Representation
==========================

Description
-----------

+--------------+---------+-------------------------------------------------------------------------+
| Field        | Value   | Description                                                             |
+==============+=========+=========================================================================+
| id           | int     | Read-only                                                               |
+--------------+---------+-------------------------------------------------------------------------+
| user_id      | int     |                                                                         |
+--------------+---------+-------------------------------------------------------------------------+
| line_id      | int     |                                                                         |
+--------------+---------+-------------------------------------------------------------------------+
| extension_id | int     |                                                                         |
+--------------+---------+-------------------------------------------------------------------------+
| main_user    | boolean | Read-only. True if the user is the first to have been associated to the |
|              |         | line.                                                                   |
+--------------+---------+-------------------------------------------------------------------------+
| main_line    | boolean | Read-only. To be implemented later. Always true.                        |
+--------------+---------+-------------------------------------------------------------------------+
| links        | list    | The links to the related resources                                      |
+--------------+---------+-------------------------------------------------------------------------+

Example
-------

::

   {
       "id": 83
       "user_id": 42,
       "line_id": 42324,
       "extension_id": 2132,
       "main_user": true,
       "main_line": true,
       "links" : [
           {
               "rel": "user_links",
               "href": "https://xivoserver/1.1/user_links/83"
           },
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/42"
           },
           {
               "rel": "lines",
               "href": "https://xivoserver/1.1/lines_sip/42324"
           },
           {
               "rel": "extensions",
               "href": "https://xivoserver/1.1/extensions/2132"
           }
       ]
   }


List the Lines Associated to a User
===================================

Query
-----

::

   GET /1.1/users/<user_id>/user_links

Example request
---------------

::

   GET /1.1/users/42/user_links
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 1,
       "items": [
           {
               "id": 83,
               "user_id": 42,
               "line_id": 42324,
               "extension_id": 2132,
               "main_user": true,
               "main_line": true,
               "links" : [
                   {
                       "rel": "user_links",
                       "href": "https://xivoserver/1.1/user_links/83"
                   },
                   {
                       "rel": "users",
                       "href": "https://xivoserver/1.1/users/42"
                   },
                   {
                       "rel": "lines",
                       "href": "https://xivoserver/1.1/lines_sip/42324"
                   },
                   {
                       "rel": "extensions",
                       "href": "https://xivoserver/1.1/extensions/2132"
                   }
               ]
           }
       ]
   }


List the Users Using a Line
===========================

Query
-----

::

   GET /1.1/lines/<line_id>/user_links

Example request
---------------

::

   GET /1.1/lines/42/user_links
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 1,
       "items": [
           {
               "id": 83,
               "user_id": 63,
               "line_id": 42,
               "extension_id": 68,
               "main_user": true,
               "main_line": true,
               "links" : [
                   {
                       "rel": "user_links",
                       "href": "https://xivoserver/1.1/user_links/83"
                   },
                   {
                       "rel": "users",
                       "href": "https://xivoserver/1.1/users/63"
                   },
                   {
                     "rel": "lines",
                       "href": "https://xivoserver/1.1/lines_sip/42"
                   },
                   {
                       "rel": "extensions",
                       "href": "https://xivoserver/1.1/extensions/68"
                   }
               ]
           }
       ]
   }


List the Users Using an Extension
=================================

Query
-----

::

   GET /1.1/extensions/<extension_id>/user_links

Example request
---------------

::

   GET /1.1/extensions/42/user_links
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 1,
       "items": [
           {
               "id": 83,
               "user_id": 63,
               "line_id": 89,
               "extension_id": 42,
               "main_user": true,
               "main_line": true,
               "links" : [
                   {
                       "rel": "user_links",
                       "href": "https://xivoserver/1.1/user_links/83"
                   },
                   {
                       "rel": "users",
                       "href": "https://xivoserver/1.1/users/63"
                   },
                   {
                     "rel": "lines",
                       "href": "https://xivoserver/1.1/lines_sip/89"
                   },
                   {
                       "rel": "extensions",
                       "href": "https://xivoserver/1.1/extensions/42"
                   }
               ]
           }
       ]
   }


Get a User-Line Association
===========================

Query
-----

::

   GET /1.1/user_links/<user_link_id>

Example request
---------------

::

   GET /1.1/user_links/1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": 83,
       "user_id": 42,
       "line_id": 42324,
       "extension_id": 2132,
       "main_user": true,
       "main_line": true,
       "links" : [
           {
               "rel": "users",
               "href": "https://xivoserver/1.1/users/42"
           },
           {
               "rel": "lines",
               "href": "https://xivoserver/1.1/lines_sip/42324"
           },
           {
               "rel": "extensions",
               "href": "https://xivoserver/1.1/extensions/2132"
           }
       ]
   }

.. _associate_line_to_user:

Associate Line to User
======================

.. warning:: Deleting a user from the Web interface will always remove his associated lines, whether he be a main
             user or not. As a result, any other user associated to the given line will also have his line deleted.

Query
-----

::

   POST /1.1/user_links

Input
-----

+--------------+----------+---------+-------------------------------------------------------------+
| Field        | Required | Values  | Description                                                 |
+==============+==========+=========+=============================================================+
| user_id      | yes      | int     | Must be an existing id                                      |
+--------------+----------+---------+-------------------------------------------------------------+
| line_id      | yes      | int     | Must be an existing id                                      |
+--------------+----------+---------+-------------------------------------------------------------+
| extension_id | yes      | int     | Must be an existing id                                      |
+--------------+----------+---------+-------------------------------------------------------------+

Errors
------

+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| Error code | Error message                                                            | Description                                      |
+============+==========================================================================+==================================================+
| 400        | Error while creating UserLineExtension : <explanation>                   | See explanation for details                      |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Missing parameters : <parameters>                                        |                                                  |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Invalid parameters : <parameters>                                        | ids must be integers                             |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Invalid parameters : user is already associated to this line             |                                                  |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Invalid parameters : extension is already associated to a line           |                                                  |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Invalid parameters : extension is already associated to another resource |                                                  |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Invalid Parameters : Exten <number> not inside user range of <context>   | Please check the ranges defined for your context |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Nonexistent parameters : extension_id <extension_id> does not exist      |                                                  |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Nonexistent parameters : line_id <line_id> does not exist                |                                                  |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+
| 400        | Nonexistent parameters : user_id <user_id> does not exist                |                                                  |
+------------+--------------------------------------------------------------------------+--------------------------------------------------+

Example request
---------------

::

   POST /1.1/user_links
   Host: xivoserver
   Content-Type: application/json

   {
       "user_id": 42,
       "line_id": 42324,
       "extension_id": 2132
   }

Example response
----------------

::

   HTTP/1.1 201 Created
   Location: /1.1/user_links/63
   Content-Type: application/json

   {
       "id": 63,
       "links" : [
           {
               "rel": "user_links",
               "href": "https://xivoserver/1.1/user_links/63"
           }
       ]
   }


Deassociate Line From User
==========================

If the user is the main user of the line and there is at least 1 secondary user associated to this
line, an error is returned.

Query
-----

::

   DELETE /1.1/user_links/<user_link_id>

Errors
------

+------------+-----------------------------------------------+----------------------------------------------------+
| Error code | Error message                                 | Description                                        |
+============+===============================================+====================================================+
| 400        | There are other users associated to this line | The requested user_link is associated to main_user |
+------------+-----------------------------------------------+----------------------------------------------------+
| 404        | Not found                                     | The requested user_link was not found              |
+------------+-----------------------------------------------+----------------------------------------------------+

Example request
---------------

::

   DELETE /1.1/user_links/42 HTTP/1.1
   Host: xivoserver

Example response
----------------

::

   HTTP/1.1 204 No Content
