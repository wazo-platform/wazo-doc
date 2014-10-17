=========
xivo-dird
=========

CLI arguments
=============

::

   usage: xivo-dird [-h] [-c CONFIG_FILE] [-f] [-u USER]

   optional arguments:
     -h, --help            show this help message and exit
     -c CONFIG_FILE, --config-file CONFIG_FILE
                           The path where is the config file. Default: /etc/xivo
                           /xivo-dird/xivo-dird.yml
     -f, --foreground      Foreground, don't daemonize. Default: False
     -u USER, --user USER  The owner of the process.


Configuration file
==================

.. code-block:: yaml
   :linenos:

   debug: False
   foreground: False
   log_filename: /var/log/xivo-dird.log
   pid_filename: /var/run/xivo-dird/xivo-dird.pid
   user: www-data

   rest_api:
       wsgi_socket: /var/run/xivo-dird/xivo-dird.sock

   services:
       lookup:
           enabled: True
       reverse-lookup:
           enabled: True


Service plugin
==============

* Namespace: ``xivo_dird.services``
* Attributes:

  * ``name``: the name of the plugin. It must uniquely identify the plugin.

* Methods:

  * ``load(args)``: set up resources used by the plugin, depending on the config.
    ``args`` is a dictionary containing:

    * key ``config``: the content of the whole configuration, in dict form
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
       name = 'dummy'
       def __init__(self):
           logger.info('dummy created')

       def load(self, args):
           logger.info('dummy loaded')
