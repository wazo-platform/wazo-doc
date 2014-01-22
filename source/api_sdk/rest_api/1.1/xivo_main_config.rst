***********************
XiVO Main configuration
***********************


Configuration representation
============================

Description
-----------

+-------------+---------+-----------------------------------------+
| Field       | Values  | Description                             |
+=============+=========+=========================================+
| live_reolad | boolean | Enable live reload of the configuration |
+-------------+---------+-----------------------------------------+


Example
-------

::

   {
       "live_reolad": true
       "links": [
            {
                "rel": "xivo_main_config",
                "href: "https://xivoserver/1.1/xivo_main_config"
            }
        ]
    }


Get XiVO Main configuration
===========================

Query
-----

::

    GET /1.1/xivo_main_config

Example requests
----------------

::

    GET /1.1/xivo_main_config HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "live_reolad": true
       "links": [
            {
                "rel": "xivo_main_config",
                "href: "https://xivoserver/1.1/xivo_main_config"
            }
        ]
    }


Edit XiVO Main configuration
============================

Query
-----

::

    PUT /1.1/xivo_main_config

Example request
---------------

::

    PUT /1.1/xivo_main_config HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    
    {
       "live_reolad": true
    }

Example response
----------------

::

   HTTP/1.1 204 No Content
