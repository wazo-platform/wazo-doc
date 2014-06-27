**********
Extensions
**********

An extension represents a number that can be dialed on a phone. Once an
extension is created, it can be associated with different kinds of resources.
These associations determine where a call will be routed when the extension is
dialed.

An extension is composed of an "exten" (the number to dial) and a "context" (
from where are we allowed to dial). The context restrains what source a call
will come in from. (e.g. DID calls will come from the context "from-extern")

Extension Representation
========================

Description
-----------

+-----------+---------+-----------------------------------+
| Field     | Values  | Description                       |
+===========+=========+===================================+
| id        | int     | Read-only                         |
+-----------+---------+-----------------------------------+
| exten     | string  |                                   |
+-----------+---------+-----------------------------------+
| context   | string  |                                   |
+-----------+---------+-----------------------------------+
| commented | boolean | If True the extension is disabled |
+-----------+---------+-----------------------------------+
| links     | list    | The link to the resource          |
+-----------+---------+-----------------------------------+

Example
-------

::

   {
       "id": 1,
       "context": "default",
       "exten": "1234",
       "commented": false,
       "links" : [
           {
               "rel": "extensions",
               "href": "https://xivoserver/1.1/extensions/1"
           }
       ]
   }


Extension list
==============

Query
-----

::

   GET /1.1/extensions


Parameters
----------


order
   Sort the list using a column (e.g. "exten"). Columns allowed: exten, context.

direction
    'asc' or 'desc'. Sort list in ascending (asc) or descending (desc) order.

limit
    maximum number of items to return in the list. Must be a positive integer.

skip
    number of extensions to skip over before starting the list. Must be a positive integer.

search
    Search term. Only extensions with a field containing the search term
    will be listed.

type
    Only show extensions of a certain type. Types allowed: internal, incall


Example requests
----------------

List all available extensions::

   GET /1.1/extensions HTTP/1.1
   Host: xivoserver
   Accept: application/json

List extensions sorted by exten in descending order::

   GET /1.1/extensions?order=exten&direction=desc HTTP/1.1
   Host: xivoserver
   Accept: application/json

List only the first 10 extensions having the number "17" in the exten::

   GET /1.1/extensions?limit=10&search=17 HTTP/1.1
   Host: xivoserver
   Accept: application/json

List extensions of type incall::

   GET /1.1/extensions?type=incall HTTP/1.1
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
               "id": 1,
               "context": "default",
               "exten": "1234",
               "commented": false,
               "links" : [
                   {
                       "rel": "extensions",
                       "href": "https://xivoserver/1.1/extensions/1"
                   }
               ]
           },
           {
               "id": 2,
               "context": "default",
               "exten": "6789",
               "commented": true,
               "links" : [
                   {
                       "rel": "extensions",
                       "href": "https://xivoserver/1.1/extensions/2"
                   }
               ]
           }
       ]
   }


Get Extension
=============

Query
-----

::

   GET /1.1/extensions/<id>

Example request
---------------

::

   GET /1.1/extensions/1 HTTP/1.1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": 1,
       "context": "default",
       "exten": "1234",
       "commented": false
   }


Create Extension
================

The extension number must be included in one of the extension ranges for the given context.

Query
-----

::

   POST /1.1/extensions

Input
-----

+-----------+----------+---------+------------------------------------+
| Field     | Required | Values  | Description                        |
+===========+==========+=========+====================================+
| exten     | yes      | string  |                                    |
+-----------+----------+---------+------------------------------------+
| context   | yes      | string  |                                    |
+-----------+----------+---------+------------------------------------+
| commented | no       | boolean | If True the extension is disabled. |
+-----------+----------+---------+------------------------------------+

Errors
------

+------------+------------------------------------------------------+------------------------------------+
| Error code | Error message                                        | Description                        |
+============+======================================================+====================================+
| 400        | exten <number> not inside range of context <context> |                                    |
+------------+------------------------------------------------------+------------------------------------+
| 400        | error while creating Extension: <explanation>        | See error message for more details |
+------------+------------------------------------------------------+------------------------------------+

Example request
---------------

::

   POST /1.1/extensions HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
       "exten": "1234",
       "context": "default",
       "commented": false
   }

Example response
----------------

::

   HTTP/1.1 201 Created
   Location: /1.1/extensions/1
   Content-Type: application/json

   {
       "id": 1,
       "links" : [
           {
               "rel": "extensions",
               "href": "https://xivoserver/1.1/extensions/1"
           }
       ]
   }


Update an Extension
===================

The update does not need to set all the fields of the edited extension. The update only needs to set
the modified fields. The new extension number must be included in one of the extension ranges for
the new context.


Query
-----

::

   PUT /1.1/extensions/<id>

Errors
------

+------------+----------------------------------------------+---------------------------------------+
| Error code | Error message                                | Description                           |
+============+==============================================+=======================================+
| 400        | error while editing Extension: <explanation> | See error message for more details    |
+------------+----------------------------------------------+---------------------------------------+
| 400        | exten <number> not inside range of <context> |                                       |
+------------+----------------------------------------------+---------------------------------------+
| 404        | Not found                                    | The requested extension was not found |
+------------+----------------------------------------------+---------------------------------------+

Example request
---------------

::

   PUT /1.1/extensions/42 HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

   {
       "context": "my_context"
   }

Example response
----------------

::

   HTTP/1.1 204 No Content


Delete Extension
================

An extension can not be deleted if it is associated to a line.
You must delete the association first. Consult the documentation on :ref:`line-extension-associations`
for further details.

Query
-----

::

   DELETE /1.1/extensions/<id>

Errors
------

+------------+------------------------------------------------------------+---------------------------------------+
| Error code | Error message                                              | Description                           |
+============+============================================================+=======================================+
| 400        | error while deleting Extension: <explanation>              | See error message for more details    |
+------------+------------------------------------------------------------+---------------------------------------+
| 400        | Error while deleting Extension: extension still has a link | See explanation above                 |
+------------+------------------------------------------------------------+---------------------------------------+
| 404        | Not found                                                  | The requested extension was not found |
+------------+------------------------------------------------------------+---------------------------------------+

Example request
---------------

::

   DELETE /1.1/extensions/1 HTTP/1.1
   Host: xivoserver

Example response
----------------

::

   HTTP/1.1 204 No Content


Line-Extension Association
==========================

See :ref:`line-extension-associations`.
