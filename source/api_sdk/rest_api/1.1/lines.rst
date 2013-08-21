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

+-----------+-----------------------------+---------------------------------+
| Field     | Values                      | Description                     |
+===========+=============================+=================================+
| id        | int                         | Read-only                       |
+-----------+-----------------------------+---------------------------------+
| context   | string                      | The name of an internal context |
+-----------+-----------------------------+---------------------------------+
| protocol  | string, only value: ``sip`` | Read-only                       |
+-----------+-----------------------------+---------------------------------+
| interface | string                      |                                 |
+-----------+-----------------------------+---------------------------------+
| links     | list                        | The links to the resource       |
+-----------+-----------------------------+---------------------------------+

**SIP example**

::

   {
       "id": 1,
       "context": "default",
       "protocol": "sip",
       "interface": "sip/abcdef",
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
       "protocol": "custom",
       "interface": "Local/123@default",
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
       "protocol": "sccp",
       "interface": "sccp/1234",
       "links" : [
           {
               "rel": "lines_sccp",
               "href": "https://xivoserver/1.1/lines_sccp/3"
           }
       ]
   }


List Lines
----------

::

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
               "protocol": "sip",
               "interface": "sip/abcdef",
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
               "protocol": "custom",
               "interface": "Local/123@default",
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
               "protocol": "sccp",
               "interface": "sccp/1234",
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

::

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
       "protocol": "sip",
       "interface": "sip/abcdef",
       "links" : [
           {
               "rel": "lines_sip",
               "href": "https://xivoserver/1.1/lines_sip/42"
           }
       ]
   }


SIP Lines
=========


Restrictions
------------


* Lines created via the REST API can not be used to provision devices automatically.
* Lines created via the REST API will have an empty Caller ID.


SIP Line Representation
-----------------------

**Description**

+------------------------+---------+-----------------------------------+
| Field                  | Value   | Description                       |
+========================+=========+===================================+
| id                     | int     | Read-only                         |
+------------------------+---------+-----------------------------------+
| context                | string  |                                   |
+------------------------+---------+-----------------------------------+
| interface              | string  | Read-only                         |
+------------------------+---------+-----------------------------------+
| username               | string  | Read-only                         |
+------------------------+---------+-----------------------------------+
| secret                 | string  | Read-only                         |
+------------------------+---------+-----------------------------------+
| provisioning_extension | string  | Read-only                         |
+------------------------+---------+-----------------------------------+
| commented              | boolean | If True the extension is disabled |
+------------------------+---------+-----------------------------------+
| description            | string  |                                   |
+------------------------+---------+-----------------------------------+
| links                  | list    | The link to the resource          |
+------------------------+---------+-----------------------------------+


List SIP Lines
--------------

::

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
               "interface": "sip/abcdef",
               "username": "abcdef",
               "secret": "password",
               "provisioning_extension": "123456",
               "commented": false,
               "description": "line blue",
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
               "interface": "sip/stuvwx",
               "username": "stuvwx",
               "secret": "password",
               "provisioning_extension": "987456",
               "commented": false,
               "description": "line red",
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

::

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
       "interface": "sip/abcdef",
       "username": "abcdef",
       "secret": "password",
       "provisioning_extension": "123456",
       "commented": false,
       "description": "line blue"
   }


Create SIP Line
---------------

The SIP username and secret and the provisioning_extension are autogenerated.

**Errors**

+------------+------------------------------------------+--------------------------------+
| Error code | Error message                            | Description                    |
+============+==========================================+================================+
| 400        | error while creating Line: <explanation> | See explanation for more infos |
+------------+------------------------------------------+--------------------------------+

::

   POST /1.1/lines_sip

**Input**

+-------------+----------+-------------------------+
| Field       | Required | Description             |
+-------------+----------+-------------------------+
| context     | yes      |                         |
+-------------+----------+-------------------------+
| device_slot | yes      | Line position on device |
+-------------+----------+-------------------------+

.. warning:: The values of ``context`` are not yet checked for validity. No errors will be returned
   if the ``context`` is inexistant.

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
        "links" : [
            {
                "rel": "lines_sip",
                "href": "https://xivoserver/1.1/lines_sip/1"
            }
        ]
    }


Update a SIP Line
-----------------

The update does not need to set all the fields of the edited SIP line. The update only needs to set
the modified fields.

**Errors**

+------------+--------------------------------------+--------------------------------+
| Error code | Error message                        | Description                    |
+============+======================================+================================+
| 400        | error while edit Line: <explanation> | See explanation for more infos |
+------------+--------------------------------------+--------------------------------+

::

   PUT /1.1/lines_sip/<id>

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

For every user that is associated to the line, the association between the line and the user is
removed.

If the line is provisioned to a device, the association between the line and the device is
removed. If that device had exactly 1 line provisioned on it, the device goes back in autoprov mode.

**Errors**

+------------+------------------------------------------+-------------------------------------------------------------+
| Error code | Error message                            | Description                                                 |
+============+==========================================+=============================================================+
| 400        | error while deleting Line: <explanation> | The requested line is probably associated to other objects. |
|            |                                          | See explanation for more infos                              |
+------------+------------------------------------------+-------------------------------------------------------------+
| 404        | Not found                                | The requested line was not found                            |
+------------+------------------------------------------+-------------------------------------------------------------+

::

   DELETE /1.1/lines_sip/<id>

**Example request**::

   DELETE /1.1/lines_sip/1 HTTP/1.1
   Host: xivoserver

**Example response**::

   HTTP/1.1 204 No Content
