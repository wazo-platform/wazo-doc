.. _xivo-dird:
===========
 XiVO dird
===========

xivo-dird is the directory server for XiVO. It offers a simple REST interface
to query all directories that are configured. xivo-dird is meant to be
extendable with plugins.

.. toctree::
   :maxdepth: 1

   developer


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


Plugins
=======

At the moment, there are three extension points in xivo-dird:

* backends
* services
* views


backends
--------

Backend plugins allow xivo-dird to query many kinds of directories, see
:ref:`backend-plugins` for more information about the implementation of a new
backend plugin.


views
-----

View plugins add new route to the HTTP application in xivo-dird. The view is
responsible to format the result for the consumer. Supporting the directory
function of a phone is generally a matter of adding a new view for the format
that the phone consumes. See :ref:`view-plugins` for more information about the
implementation of a new view plugin.


Plugins in xivo-dird use python's entry points. That means that installing a new
plugin to xivo-dird requires an entry point in the plugins setup.py. Each entry
point `namespace` are documented in there respective documentation xivo-dird
will be able to discover the plugin and load it with the documented arguments.

Here is an example ``setup.py`` with an ``entry_points`` section:

.. code-block:: python
   :linenos:
   :emphasize-lines: 20-25

   #!/usr/bin/env python
   # -*- coding: utf-8 -*-

   from setuptools import setup
   from setuptools import find_packages


   setup(
       name='xivo_dird_service_dummy_plugin',
       version='0.0.1',

       description='dummy service for xivo-dird',

       author='Avencall',
       author_email='dev@avencall.com',

       url='https://github.com/xivo-pbx/xivo-dird',

       packages=find_packages(),

       entry_points={
           'xivo_dird.services': [
               'dummy = xivo_dird_service_dummy.dummy:DummyServicePlugin',
           ],
       }
   )


.. _configuration-file:

Configuration file
==================

.. code-block:: yaml
   :linenos:

   debug: False
   foreground: False
   log_filename: /var/log/xivo-dird.log
   log_level: info
   pid_filename: /var/run/xivo-dird/xivo-dird.pid
   user: www-data

   rest_api:
       wsgi_socket: /var/run/xivo-dird/xivo-dird.sock

   enabled_plugins:
      backends:
          - csv
          - ldap
          - phonebook
      services:
          - lookup
      views:
          - aastra_xml
          - default_json

   views:
       displays:
           switchboard_display:
               -
                   title: Firstname
                   default: Unknown
                   field: firstname
               -
                   title: Lastname
                   default: Unknown
                   field: lastname
           default_display:
               -
                   title: Firstname
                   field: fn
               -
                   title: Location
                   default: Canada
                   field: country
               -
                   title: Number
                   field: number
        profile_to_display:
            default: default_display
            switchboard: switchboard_display

   services:
       lookup:
           default:
               sources:
                   - my_csv
                   - ldap_quebec
                timeout: 0.5
            switchboard:
                sources:
                    - my_csv
                    - xivo_phonebook
                    - ldap_quebec
                timeout: 1


.. _backend-plugins:

Backend plugin
==============

A backend implements the api to access a directory source. Each backend instance
is called a source.

Given a ldap backend I can configure a source going to alpha.example.com and another
on beta.example.com.


* Namespace: ``xivo_dird.backends``

* Methods:

  * ``name``: the name of the source, retrieved from the configuration file

  * ``load(args)``: set up resources used by the plugin, depending on the config.
    ``args`` is a dictionary containing:

    * key ``config``: the source configuration for this instance of the backend
  * ``unload()``: free resources used by the plugin.


Configuration
-------------

A typical source configuration file will contain the following fields:

* type: is the name of the backend name found in the setup.py
* name: is the name of this configuration
* unique_columns: is used to distinguish between 2 entries favorites are based on unique columns
* search_columns: are the columns used to compare to a searched term
* columns_map: is a mapping between the source columns and the display columns configured in the views

.. code-block:: yaml
   :linenos:

   type: csv
   name: csv_customers
   unique_columns:
       - id
   search_columns:
       - firstname
   source_to_display_columns:
       lastname: ln
       firstname: fn
       number: telephoneNumber


.. _view-plugins:

HTTP views plugin
=================

A view plugin adds URLs to the HTTP server in dird and are responsible of
transforming the results from services to the expected format for that URL.

A use case for a view plugin would be to add support for a new phone's directory
function.

* Namespace: ``xivo_dird.http_views``

* Methods:

  * ``load(args)``: add the routes to the http app
    ``args`` is a dictionary containing:

    * key ``config``: the views configuration contained in the main xivo-dird
      configuration file.
    * key ``http_app``: the flask application of the core
    * key ``services``: a dictionary of services

  * ``unload``: free resources used by the plugin.
