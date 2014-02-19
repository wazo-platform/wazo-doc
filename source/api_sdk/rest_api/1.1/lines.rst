*****
Lines
*****

The resource ``/lines/`` only provides read operations. Modifications can only be done on
protocol-specific lines (see below).


Generic Lines
=============


Line Representation
-------------------

**Description**

+------------------------+-----------------------------+---------------------------------+
| Field                  | Values                      | Description                     |
+========================+=============================+=================================+
| id                     | int                         | Read-only                       |
+------------------------+-----------------------------+---------------------------------+
| context                | string                      | The name of an internal context |
+------------------------+-----------------------------+---------------------------------+
| name                   | string                      | The name of the line            |
+------------------------+-----------------------------+---------------------------------+
| protocol               | string, only value: ``sip`` | Read-only                       |
+------------------------+-----------------------------+---------------------------------+
| provisioning_extension | int                         | Code used to provision a device |
+------------------------+-----------------------------+---------------------------------+
| device_slot            | int                         | line's position on the device   |
+------------------------+-----------------------------+---------------------------------+
| links                  | list                        | The links to the resource       |
+------------------------+-----------------------------+---------------------------------+

**SIP example**

::

   {
       "id": 1,
       "context": "default",
       "name": "a1b2c4",
       "protocol": "sip",
       "provisioning_extension": 342395,
       "device_slot": 1,
       "links" : [
           {
               "rel": "lines_sip",
               "href": "https://xivoserver/1.1/lines_sip/1"
           }
       ]
   }

**Custom example**

.. warning:: Not yet implemented

::

   {
       "id": 2,
       "context": "default",
       "name": "custom",
       "protocol": "custom",
       "provisioning_extension": 438111,
       "device_slot": 2,
       "links" : [
           {
               "rel": "lines_custom",
               "href": "https://xivoserver/1.1/lines_custom/2"
           }
       ]
   }

**SCCP example**

.. warning:: Not yet implemented

::

   {
       "id": 3,
       "context": "default",
       "name": "SCCP/1234",
       "protocol": "sccp",
       "provisioning_extension": 382731,
       "device_slot": 1,
       "links" : [
           {
               "rel": "lines_sccp",
               "href": "https://xivoserver/1.1/lines_sccp/3"
           }
       ]
   }


List Lines
----------

**Query**::

   GET /1.1/lines

**Example request**::

   GET /1.1/lines HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 3,
       "items": [
           {
               "id": 1,
               "context": "default",
               "name": "a1b2c4",
               "protocol": "sip",
               "provisioning_extension": 342395,
               "device_slot": 1,
               "links" : [
                   {
                       "rel": "lines_sip",
                       "href": "https://xivoserver/1.1/lines_sip/1"
                   }
               ]
           },
           {
               "id": 2,
               "context": "default",
               "name": "custom",
               "protocol": "custom",
               "provisioning_extension": 438111,
               "device_slot": 2,
               "links" : [
                   {
                       "rel": "lines_custom",
                       "href": "https://xivoserver/1.1/lines_custom/2"
                   }
               ]
           },
           {
               "id": 3,
               "context": "default",
               "name": "SCCP/1234",
               "protocol": "sccp",
               "provisioning_extension": 382731,
               "device_slot": 1,
               "links" : [
                   {
                       "rel": "lines_sccp",
                       "href": "https://xivoserver/1.1/lines_sccp/3"
                   }
               ]
           }
       ]
   }


Get Line
--------

**Query**::

   GET /1.1/lines/<line_id>

**Example request**::

   GET /1.1/lines/42 HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": 42,
       "context": "default",
       "name": "a1b2c4",
       "protocol": "sip",
       "provisioning_extension": 342395,
       "device_slot": 1,
       "links" : [
           {
               "rel": "lines_sip",
               "href": "https://xivoserver/1.1/lines_sip/42"
           }
       ]
   }


SIP Lines
=========


SIP Line Representation
-----------------------

**Description**

+------------------------+--------+-----------------------------------------+
| Field                  | Value  | Description                             |
+========================+========+=========================================+
| id                     | int    | Read-only                               |
+------------------------+--------+-----------------------------------------+
| context                | string |                                         |
+------------------------+--------+-----------------------------------------+
| username               | string | Read-only                               |
+------------------------+--------+-----------------------------------------+
| secret                 | string | Read-only                               |
+------------------------+--------+-----------------------------------------+
| provisioning_extension | int    | Read-only                               |
+------------------------+--------+-----------------------------------------+
| device_slot            | int    | Line's position on the device           |
+------------------------+--------+-----------------------------------------+
| device_id              | string | ID of the device associated to the line |
+------------------------+--------+-----------------------------------------+
| callerid               | string | Read-only                               |
+------------------------+--------+-----------------------------------------+
| links                  | list   | The link to the resource                |
+------------------------+--------+-----------------------------------------+


List SIP Lines
--------------

**Query**::

   GET /1.1/lines_sip

**Example request**::

   GET /1.1/lines_sip HTTP/1.1
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
               "username": "abcdef",
               "secret": "secret_password",
               "provisioning_extension": 123456,
               "device_slot": 1,
               "device_id": "2b63136208fb117335ce874e65eba2a3",
               "callerid": "\"John Doe\" <1002>",
               "links" : [
                   {
                       "rel": "lines_sip",
                       "href": "https://xivoserver/1.1/lines_sip/1"
                   }
               ]
           },
           {
               "id": 2,
               "context": "default",
               "username": "stuvwx",
               "secret": "super_secret_password",
               "provisioning_extension": 987456,
               "device_slot"; 1,
               "device_id": "b054de13b8b73d5683815929c20033ad",
               "callerid": "\"Mary Lin\" <1003>",
               "links" : [
                   {
                       "rel": "lines_sip",
                       "href": "https://xivoserver/1.1/lines_sip/2"
                   }
               ]
           }
       ]
   }

Get SIP Line
------------

**Query**::

   GET /1.1/lines_sip/<id>

**Example request**::

   GET /1.1/lines_sip/1 HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
        "id": 1,
        "context": "default",
        "username": "abcdef",
        "secret": "secret_password",
        "provisioning_extension": 123456,
        "device_slot": 1,
        "device_id": "b054de13b8b73d5683815929c20033ad",
        "callerid": "\"John Doe\" <1002>",
        "links": [
            {
                "rel": "lines_sip",
                "href": "https://xivoserver/1.1/lines_sip/1"
            }
        ]
   }


Create SIP Line
---------------

The username, secret and provisioning_extension are autogenerated.

**Query**::

   POST /1.1/lines_sip

**Input**

+-------------+----------+-------------------------+
| Field       | Required | Description             |
+-------------+----------+-------------------------+
| context     | yes      |                         |
+-------------+----------+-------------------------+
| device_slot | yes      | Line position on device |
+-------------+----------+-------------------------+

**Errors**

+------------+------------------------------------------------------+-------------------------------------------+
| Error code | Error message                                        | Description                               |
+============+======================================================+===========================================+
| 400        | error while creating Line: <explanation>             | See explanation for more details          |
+------------+------------------------------------------------------+-------------------------------------------+
| 400        | Invalid parameters: context <context> does not exist |                                           |
+------------+------------------------------------------------------+-------------------------------------------+
| 400        | Invalid parameters: device_slot must be numeric      | Use a positive number for the device slot |
+------------+------------------------------------------------------+-------------------------------------------+

**Example request**::

   POST /1.1/lines_sip HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
       "context": "default"
       "device_slot": 1
   }

**Example response**::

   HTTP/1.1 201 Created
   Location: /1.1/lines_sip/1
   Content-Type: application/json

    {
        "id": 1,
        "context": "default",
        "username": "abcdef",
        "secret": "secret_password",
        "provisioning_extension": 123456,
        "device_slot": 1,
        "device_id": null,
        "callerid": null,
        "links" : [
            {
                "rel": "lines_sip",
                "href": "https://xivoserver/1.1/lines_sip/1"
            }
        ]
    }


Update a SIP Line
-----------------

Only fields that need to be updated should be sent. All other fields will remain
unmodified during the update.

**Query**::

   PUT /1.1/lines_sip/<id>

**Errors**

Same as for creating a SIP line. Please see `Create SIP line`_


**Example request**::

   PUT /1.1/lines_sip/67 HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

   {
       "context": "my_context"
   }

**Example response**::

   HTTP/1.1 204 No Content


Delete SIP Line
---------------

A SIP line can not be deleted if it is still associated with a user, an extesion, or a device.
Any user, extension, or device attached to the line must be dissociated first.
Consult the documentation on :ref:`user-line-association`, :ref:`line-extension-association`
and :ref:`restapi-device` for further explanations.

**Query**::

   DELETE /1.1/lines_sip/<id>

**Errors**

+------------+--------------------------------------------------+----------------------------------------------------------------------------------+
| Error code | Error message                                    | Description                                                                      |
+============+==================================================+==================================================================================+
| 400        | error while deleting Line: <explanation>         | See error message for more details                                               |
+------------+--------------------------------------------------+----------------------------------------------------------------------------------+
| 400        | Error while deleting Line: line still has a link | Line is still associated to a user, extension, or device (see explanation above) |
+------------+--------------------------------------------------+----------------------------------------------------------------------------------+
| 404        | Not found                                        | The requested line was not found                                                 |
+------------+--------------------------------------------------+----------------------------------------------------------------------------------+


**Example request**::

   DELETE /1.1/lines_sip/1 HTTP/1.1
   Host: xivoserver

**Example response**::

   HTTP/1.1 204 No Content


User-Line Association
=====================

See :ref:`user-line-association`

Line-Extension Association
==========================

See :ref:`line-extension-association`.
