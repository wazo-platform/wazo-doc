.. _line-extension-association:

**************************
Line Extension Association
**************************


Association Representation
==========================

Description
-----------

+--------------+-------+-----------------------+
| Field        | Value | Description           |
+==============+=======+=======================+
| line_id      | int   | Line's ID. Read-only. |
+--------------+-------+-----------------------+
| extension_id | int   | Extension's ID.       |
+--------------+-------+-----------------------+

Get the Extension associated to a Line
======================================

Query
-----

::

    GET /lines/<line_id>/extension

Errors
------

+------------+---------------------------------------------------+-------------+
| Error code | Error message                                     | Description |
+============+===================================================+=============+
| 404        | Line with id=<line_id> does not exist             |             |
+------------+---------------------------------------------------+-------------+
| 404        | Line with id=<line_id> does not have an extension |             |
+------------+---------------------------------------------------+-------------+


Example Request
---------------

::

    GET /lines/34/extension
    Host: xivoserver
    Accept: application/json


Example Response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "line_id": 34,
        "extension_id": 12,
        "links": [
            {
                "rel": "lines_sip",
                "href": "https://xivoserver/1.1/lines_sip/34"
            },
            {
                "rel": "extensions",
                "href": "https://xivoserver/1.1/extensions/12"
            }
        ]
    }


Associate an Extension to a Line
================================

Query
-----

::

    POST /lines/<line_id>/extension


Input
-----

+--------------+----------+--------+------------------------+
| Field        | Required | Values | Description            |
+==============+==========+========+========================+
| extension_id | yes      | int    | Must be an existing id |
+--------------+----------+--------+------------------------+


Errors
------

+------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| Error code | Error message                                                       | Description                                                               |
+============+=====================================================================+===========================================================================+
| 404        | Line with id=<line_id> does not exist                               |                                                                           |
+------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| 400        | Nonexistent parameters: extension_id <extension_id> does not exist  |                                                                           |
+------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| 400        | Invalid parameters: line with id <line_id> already has an extension | You must unassociate the current extension before reassociating a new one |
+------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+


Example request
---------------

::

    POST /1.1/lines/75/extension
    Host: xivoserver
    Content-Type: application/json

    {
        "extension_id": 46
    }


Example response
----------------

::

    HTTP/1.1 201
    Location: /1.1/lines/75/extension

    {
        "line_id": 75,
        "extension_id": 46,
        "links": [
           {
               "rel": "lines_sip",
               "href": "https://xivoserver/1.1/lines_sip/75"
           },
           {
               "rel": "extensions",
               "href": "https://xivoserver/1.1/extensions/46"
           }
        ]
    }


Dissociate an Extension from a Line
===================================

Any devices that are attached to the line must be removed before dissociating an extension from its
line. A device can be dissociated be resetting it to autoprov mode.
Consult the documentation on :ref:`restapi-device` for further details.


Query
-----

::

    DELETE /1.1/lines/<line_id>/extension


Errors
------

+------------+---------------------------------------------------------------+-------------+
| Error code | Error message                                                 | Description |
+============+===============================================================+=============+
| 404        | Line with id=<line_id> does not exist                         |             |
+------------+---------------------------------------------------------------+-------------+
| 400        | Invalid parameters:  A device is still associated to the line |             |
+------------+---------------------------------------------------------------+-------------+


Example request
---------------

::

    DELETE /1.1/lines/<line_id>/extension
    Host: xivoserver


Example response
----------------

::

    HTTP/1.1 204 No Content
