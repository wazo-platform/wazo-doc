.. _line-extension-associations:

***************************
Line Extension Associations
***************************

Connects an extension with a line, allowing the line to be called by dialing a
number.  A line can be associated with one or more extensions. The context of
an extension determines from what source a call can arrive

Currently, this service only supports extensions inside the following context
types:

internal
    Used for calling a line with an internal number (e.g. "1000\@default")

incall
    Used for calling a line from the outside (e.g. "from-extern" with a DID)


Association Representation
==========================

+--------------+-------+-----------------------+
| Field        | Value | Description           |
+==============+=======+=======================+
| line_id      | int   | Line's ID.            |
+--------------+-------+-----------------------+
| extension_id | int   | Extension's ID.       |
+--------------+-------+-----------------------+

Get the Extension associated to a Line
======================================

Query
-----

::

    GET /lines/<line_id>/extensions

Errors
------

+------------+---------------------------------------------------+-------------+
| Error code | Error message                                     | Description |
+============+===================================================+=============+
| 404        | Line with id=<line_id> does not exist             |             |
+------------+---------------------------------------------------+-------------+


Example Request
---------------

::

    GET /lines/34/extensions
    Host: xivoserver
    Accept: application/json


Example Response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "total": 2,
        "items":
        [
            {
                "line_id": 34,
                "extension_id": 12,
                "links": [
                    {
                        "rel": "lines",
                        "href": "https://xivoserver/1.1/lines/34"
                    },
                    {
                        "rel": "extensions",
                        "href": "https://xivoserver/1.1/extensions/12"
                    }
                ]
            },
            {
                "line_id": 34,
                "extension_id": 13,
                "links": [
                    {
                        "rel": "lines",
                        "href": "https://xivoserver/1.1/lines/34"
                    },
                    {
                        "rel": "extensions",
                        "href": "https://xivoserver/1.1/extensions/13"
                    }
                ]
            }
        ]
    }


Get the Line associated to an Extension
=======================================

Query
-----

::

    GET /extensions/<extension_id>/line

Errors
------

+------------+-------------------------------------------------------+-------------+
| Error code | Error message                                         | Description |
+============+=======================================================+=============+
| 404        | Extension with id=<extension_id> does not exist       |             |
+------------+-------------------------------------------------------+-------------+


Example Request
---------------

::

    GET /extensions/48/line
    Host: xivoserver
    Accept: application/json


Example Response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "line_id": 34,
        "extension_id": 48,
        "links": [
            {
                "rel": "lines",
                "href": "https://xivoserver/1.1/lines/34"
            },
            {
                "rel": "extensions",
                "href": "https://xivoserver/1.1/extensions/48"
            }
        ]
    }


Associate an Extension to a Line
================================

.. note:: Because of technical limitations, a line can only have a single
    'internal' extension associated (i.e. an extension with a context of type
    'internal')

Query
-----

::

    POST /lines/<line_id>/extensions


Input
-----

+--------------+----------+--------+------------------------+
| Field        | Required | Values | Description            |
+==============+==========+========+========================+
| extension_id | yes      | int    | Must be an existing id |
+--------------+----------+--------+------------------------+


Errors
------

+------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Error code | Error message                                                                                         | Description                                                                      |
+============+=======================================================================================================+==================================================================================+
| 404        | Line with id=<line_id> does not exist                                                                 |                                                                                  |
+------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| 400        | Invalid parameters: line with id <line_id> already has an extension with a context of type 'internal' | Only one extension with a context of type 'internal' can be associated to a line |
+------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| 400        | Invalid parameters: extension is associated to a line                                                 | An extension can be associated to only one line                                  |
+------------+-------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

Example request
---------------

::

    POST /1.1/lines/75/extensions
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
        "total": 1,
        "items":
        [
            {
                "line_id": 75,
                "extension_id": 46,
                "links": [
                    {
                        "rel": "lines",
                        "href": "https://xivoserver/1.1/lines/75"
                    },
                    {
                        "rel": "extensions",
                        "href": "https://xivoserver/1.1/extensions/46"
                    }
                ]
            }
        ]
    }


Dissociate an Extension from a Line
===================================

Any devices that are attached to a line must be removed before dissociating
an extension from its line. A device can be dissociated by resetting it to
autoprov mode.  Consult the documentation on :ref:`restapi-device` for further
details.


Query
-----

::

    DELETE /1.1/lines/<line_id>/extensions/<extension_id>


Errors
------

+------------+---------------------------------------------------------------+-------------+
| Error code | Error message                                                 | Description |
+============+===============================================================+=============+
| 404        | Line with id=<line_id> does not exist                         |             |
+------------+---------------------------------------------------------------+-------------+
| 404        | Extension with id=<extension_id> does not exist               |             |
+------------+---------------------------------------------------------------+-------------+
| 400        | Invalid parameters: A device is still associated to the line  |             |
+------------+---------------------------------------------------------------+-------------+


Example request
---------------

::

    DELETE /1.1/lines/32/extensions/16
    Host: xivoserver


Example response
----------------

::

    HTTP/1.1 204 No Content
