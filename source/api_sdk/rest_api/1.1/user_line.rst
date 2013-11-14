.. _user-line-association:

*********************
User Line Association
*********************

Service for associating a user with a line.


Association Representation
==========================

Description
-----------

+-----------+---------+-------------------------------------------------------------------------+
| Field     | Value   | Description                                                             |
+===========+=========+=========================================================================+
| line_id   | bool    | Line's ID                                                               |
+-----------+---------+-------------------------------------------------------------------------+
| main_user | boolean | Read-only. True if the user is the first to have been associated to the |
|           |         | line.                                                                   |
+-----------+---------+-------------------------------------------------------------------------+
| main_line | boolean | Read-only. To be implemented later. Always true.                        |
+-----------+---------+-------------------------------------------------------------------------+
| links     | list    | The links to the related resources                                      |
+-----------+---------+-------------------------------------------------------------------------+


Get the Lines associated to a User
==================================

Query
-----

::

    GET /1.1/users/<user_id>/lines

Errors
------

+------------+------------------------------------------------------------------+-------------+
| Error code | Error message                                                    | Description |
+============+==================================================================+=============+
| 404        | Invalid parameters: user with id=<user_id> does not have a lines |             |
+------------+------------------------------------------------------------------+-------------+
| 404        | User with id=<user_id> does not exist                            |             |
+------------+------------------------------------------------------------------+-------------+


Example request
---------------

::

    GET /1.1/users/20/lines
    Host: xivoserver
    Accept: application/json

Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

   [
      {
           "line_id": 132,
           "main_user": true,
           "main_line": true,
           "links": [
              {
                  "rel": "lines",
                  "href": "https://xivoserver/1.1/lines/132"
              }
           ]
       }
    ]



Associate a Line to a User
==========================

Query
-----

::

    POST /1.1/users/<user_id>/lines

Input
-----

+-----------+----------+---------+-------------------------------------------------------------------------------+
| Field     | Required | Values  | Description                                                                   |
+===========+==========+=========+===============================================================================+
| line_id   | yes      | int     | Must be an existing id                                                        |
+-----------+----------+---------+-------------------------------------------------------------------------------+
| main_user | no       | boolean | Read-only. True if the user is the first to have been associated to the line. |
+-----------+----------+---------+-------------------------------------------------------------------------------+
| main_line | no       | boolean | Read-only. To be implemented later. Always true.                              |
+-----------+----------+---------+-------------------------------------------------------------------------------+


Errors
------

+------------+----------------------------------------------------------+-------------+
| Error code | Error message                                            | Description |
+============+==========================================================+=============+
| 400        | Nonexistent parameters: line_id <line_id> does not exist |             |
+------------+----------------------------------------------------------+-------------+

Example request
---------------

::

    POST /1.1/users/59/lines
    Host: xivoserver
    Content-Type: application/json

    {
        "line_id": 432
    }

Example response
----------------

::

    HTTP/1.1 201
    Location: /1.1/users/59/lines

    {
        "line_id": 432,
        "main_user": true,
        "main_line": true,
        "links": [
           {
               "rel": "lines",
               "href": "https://xivoserver/1.1/lines/432"
           }
        ]
    }


Deassociate a User from a Line
==============================


Query
-----

::

    DELETE /1.1/users/<user_id>/lines/<line_id>


Errors
------

+------------+-------------------------------------------------------------------------+-------------+
| Error code | Error message                                                           | Description |
+============+=========================================================================+=============+
| 400        | Nonexistent parameters: line_id <line_id> does not exist                |             |
+------------+-------------------------------------------------------------------------+-------------+
| 400        | Nonexistent parameters: line_id <line_id> does not associated to a user |             |
+------------+-------------------------------------------------------------------------+-------------+


Example request
---------------

::

    DELETE /1.1/users/59/lines/598
    Host: xivoserver
    Content-Type: application/json

Example response
----------------

::

    HTTP/1.1 204 No Content
