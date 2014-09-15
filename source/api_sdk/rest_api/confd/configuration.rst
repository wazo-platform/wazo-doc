*************
Configuration
*************

Configuration parameters
========================

+-------------+--------+-------------+
| Parameter   | Values | Description |
+=============+========+=============+
| live_reload | bool   |             |
+-------------+--------+-------------+


Get live reload status
======================

Query
-----

::

    GET /1.1/configuration/live_reload

Example requests
----------------

::

    GET /1.1/configuration/live_reload HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "enabled": true
       "links": [
            {
                "rel": "configuration",
                "href: "https://xivoserver/1.1/configuration/live_reload"
            }
        ]
    }


Change live reload status
=========================

Query
-----

::

    PUT /1.1/configuration/live_reload

Example request
---------------

::

    PUT /1.1/configuration/live_reload HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    
    {
       "enabled": false
    }

Example response
----------------

::

   HTTP/1.1 204 No Content
