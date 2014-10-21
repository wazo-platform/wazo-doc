=========
xivo-dird
=========

CLI arguments
=============

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
               -
                   type: status
           default_display:
               -
                   title: Firstname
                   field: fn
               -
                   title: Localtion
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



Service plugin
==============

* Namespace: ``xivo_dird.services``
* Attributes:

  * ``name``: the name of the plugin. It must uniquely identify the plugin.

* Methods:

  * ``load(args)``: set up resources used by the plugin, depending on the config.
    ``args`` is a dictionary containing:

    * key ``config``: the section of the configuration file for this service in dict form
    * key ``sources``: a dictionary of source names to sources

    ``load`` must return a callable, which will be made available in the view plugins.
  * ``unload()``: free resources used by the plugin.


Example
-------

``setup.py``:

.. code-block:: python
   :linenos:

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

``xivo_dird_service_dummy/dummy.py``:

.. code-block:: python
   :linenos:

   # -*- coding: utf-8 -*-

   import logging

   logger = logging.getLogger(__name__)

   class DummyServicePlugin(object):

       def __init__(self):
           logger.info('dummy created')

       def load(self, args):
           logger.info('dummy loaded')


Backend plugin
==============

A backend implements the api to acces a directory source. Each backend instance
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
