**********
Extensions
**********

Extension Representation
========================

**Description**

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

**Example**::

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
       "commented": false
   }


Create Extension
================

**Errors**

+------------+-----------------------------------------------+--------------------------------+
| Error code | Error message                                 | Description                    |
+============+===============================================+================================+
| 400        | error while creating Extension: <explanation> | See explanation for more infos |
+------------+-----------------------------------------------+--------------------------------+

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

.. warning:: The values of ``exten`` and ``context`` are not yet checked for validity. No errors
   will be returned if the ``context`` is inexistant or if the ``exten`` is outside of all extension
   ranges of the context.

**Example request**::

   POST /1.1/extensions HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
       "exten": "1234",
       "context": "default",
       "commented": false
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

**Errors**

+------------+----------------------------------------------+--------------------------------+
| Error code | Error message                                | Description                    |
+============+==============================================+================================+
| 400        | error while editing Extension: <explanation> | See explanation for more infos |
+------------+----------------------------------------------+--------------------------------+

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

**Errors**

+------------+-----------------------------------------------+------------------------------------------------------------------+
| Error code | Error message                                 | Description                                                      |
+============+===============================================+==================================================================+
| 400        | error while deleting Extension: <explanation> | The requested extension is probably associated to other objects. |
|            |                                               | See explanation for more infos                                   |
+------------+-----------------------------------------------+------------------------------------------------------------------+
| 404        | Not found                                     | The requested extension was not found                            |
+------------+-----------------------------------------------+------------------------------------------------------------------+

::

   DELETE /1.1/extensions/<id>

**Example request**::

   DELETE /1.1/extensions/1 HTTP/1.1
   Host: xivoserver

**Example response**::

   HTTP/1.1 204 No Content
