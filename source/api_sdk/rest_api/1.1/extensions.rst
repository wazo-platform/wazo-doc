**********
Extensions
**********

Extension Representation
========================

**Description**

+-----------+---------+------------------------------------+
| Field     | Values  | Description                        |
+===========+=========+====================================+
| id        | int     | Read-only                          |
+-----------+---------+------------------------------------+
| exten     | string  |                                    |
+-----------+---------+------------------------------------+
| context   | string  |                                    |
+-----------+---------+------------------------------------+
| commented | boolean | If True the extension is disabled. |
+-----------+---------+------------------------------------+
| links     | list    | The link to the resource.          |
+-----------+---------+------------------------------------+

**Example**::

   {
       "id": 1,
       "context": "default",
       "exten": "1234",
       "commented": 0,
       "links" : [
           {
               "rel": "extensions",
               "href": "https://xivoserver/1.1/extensions/1"
           }
       ]
   }


List Extension
==============

::

   GET /1.1/extensions

**Example request**::

   GET /1.1/extensions HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items": [
           {
               "id": 1,
               "context": "default",
               "exten": "1234",
               "commented": 0,
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
               "commented": 1,
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

::

   GET /1.1/extensions/<id>

**Example request**::

   GET /1.1/extensions/1 HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": 1,
       "context": "default",
       "exten": "1234",
       "commented": 0
   }


Create Extension
================

::

   POST /1.1/extensions

**Input**

+-----------+----------+---------+------------------------------------+
| Field     | Required | Values  | Description                        |
+===========+==========+=========+====================================+
| exten     | yes      | string  |                                    |
+-----------+----------+---------+------------------------------------+
| context   | yes      | string  |                                    |
+-----------+----------+---------+------------------------------------+
| commented | no       | boolean | If True the extension is disabled. |
+-----------+----------+---------+------------------------------------+

**Example request**::

   POST /1.1/extensions HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
       "exten": "1234"
       "context": "default"
       "commented": 0
   }

**Example response**::

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
the modified fields.

::

   PUT /1.1/extensions/<id>

**Example request**::

   PUT /1.1/extensions/42 HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

   {
       "context": "my_context"
   }

**Example response**::

   HTTP/1.1 204 No Content


Delete Extension
================

::

   DELETE /1.1/extensions/<id>

**Example request**::

   DELETE /1.1/extensions/1 HTTP/1.1
   Host: xivoserver

**Example response**::

   HTTP/1.1 204 No Content
