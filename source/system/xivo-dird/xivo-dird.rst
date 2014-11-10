.. _xivo-dird:

===========
 XiVO dird
===========

xivo-dird is the directory server for XiVO. It offers a simple REST interface
to query all directories that are configured. xivo-dird is meant to be
extendable with plugins.

.. toctree::
   :maxdepth: 1

   configuration
   developer
   stock_plugins


.. _xivo-dird-usage:

Launching xivo-dird
===================

::

   usage: xivo-dird [-h] [-c CONFIG_FILE] [-d] [-f] [-l LOG_LEVEL] [-u USER]

   optional arguments:
     -h, --help            show this help message and exit
     -c CONFIG_FILE, --config-file CONFIG_FILE
                           The path where is the config file. Default: /etc/xivo
                           /xivo-dird/xivo-dird.yml
     -d, --debug           Log debug messages. Overrides log_level. Default:
                           False
     -f, --foreground      Foreground, don't daemonize. Default: False
     -l LOG_LEVEL, --log-level LOG_LEVEL
                           Logs messages with LOG_LEVEL details. Must be one of:
                           critical, error, warning, info, debug. Default: info
     -u USER, --user USER  The owner of the process.


Terminology
===========

Back-end
--------

A back-end is a plugin implementation to query a given directory.


Source
------

A source is an instance of a back-end. Given a csv back-end I can have many
configurations, each of these configurations is called a source. For example,
I could have the customer-csv and the employee-csv sources. All using the csv
back-end.


Plugins
-------

A plugin is an extension point in xivo-dird. It is a way to add or modify the
functionality of xivo-dird.


API
===

Lookup
------

The `lookup` query will return a list of result matching the searched term. The
result will be retrieved from all configured directories for the given profile.

This route is provided by the `default_json_view` plugin using the `lookup`
plugin and all configured sources for the given profile.


Query
-----

::

    GET /0.1/directories/lookup/<profile>


Parameters
----------

Mandatory
^^^^^^^^^

profile
    The lookup profile. It determines which directories to search. See
    :ref:`configuration-file`.


Optional
^^^^^^^^

term
    the search term that we are looking for

`*`
    any other arguments will be forwarded to the configured source and may be
    interpreted or ignored. Extra arguments can also be used by other plugins
    to add other functionalities.


Errors
------

+------------+---------------+-----------------------------------+
| Error code | Error message | Description                       |
+============+===============+===================================+
|        404 | Not found     | The lookup profile does not exist |
+------------+---------------+-----------------------------------+


Example requests
----------------

Search for the term ``Bob``

.. code-block:: http

    GET /0.1/directories/lookup/default?term=Bob HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

Header
^^^^^^

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json


Content
^^^^^^^

.. code-block:: javascript
   :linenos:
   :emphasize-lines: 7, 15

    {
      "term": "Bob",
      "column_headers": ["Firstname", "Lastname", "Phone number", "Mobile", "Fax", "Email", "Agent"],
      "column_types": [null, "name", "number_office", "number_mobile", "fax", "email", "relation_agent"],
      "results": [
        {
          "column_values": ["Bob", "Marley", "5555555", "5556666", "5553333", "mail@example.com", null],
          "relations": {
            "agent": null,
            "user": null,
            "endpoint": null
          },
          "source": "my_ldap_directory"
        }, {
          "column_values": ["Charlie", "Boblin", "5555556", "5554444", "5552222", "mail2@example.com", null],
          "relations": {
            "agent": {
              "id": 12,
              "xivo_id": "ad2f36c7-b0f3-48da-a63c-37434fed479b"
            },
            "user": {
              "id": 34,
              "xivo_id": "ad2f36c7-b0f3-48da-a63c-37434fed479b"
            },
            "endpoint": {
              "id": 56,
              "xivo_id": "ad2f36c7-b0f3-48da-a63c-37434fed479b"
            },
          },
          "source": "internal"
        }
      ]
    }
