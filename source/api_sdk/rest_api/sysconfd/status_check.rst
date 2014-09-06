.. _status_check:

************
Status check
************

Status
======

Query
-----

::

    GET /status_check

Example request
---------------

::

    GET /status_check HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
        "status": "up"
    }
