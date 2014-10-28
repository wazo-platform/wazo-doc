.. _xivo-dird-developer:

=============================
 XiVO dird developer's guide
=============================

The XiVO dird architecture uses plugins as extension points for most of it's
job. It uses `stevedore <http://stevedore.readthedocs.org>`_ to do the plugin
instantiation and discovery and `ABC <https://docs.python.org/2/library/abc.html>`_
classes to define the required interface.

Plugins in xivo-dird use setuptools's entry points. That means that installing a
new plugin to xivo-dird requires an entry point in the plugins setup.py. Each
entry point's `namespace` are documented in the appropriate documentation
section. These entry points allow xivo-dird to be able to discover and load
extensions packaged with xivo-dird or installed separetely.

Each kind of plugin does a specific job. There are three kind of plugins in
dird.

#. :ref:`dird-back-end`
#. :ref:`dird-service`
#. :ref:`dird-view`

All plugins are instantiated by the core. The core then keeps a catalog of
loaded extensions that can be supplied to other extensions.


.. _dird-back-end:

Back-End
========


.. _dird-service:

Service
=======

Service plugins add new functionality to the dird server. These functionalities
are available to views. When loaded a service plugin receives it's configuration
and a dictionary of available sources.

Some service example that come to mind include:

* A lookup service to search through all configured sources.
* A reverse lookup service to search through all configured sources and return a
  specific field of the first matching result.


Implementation details
----------------------

* Namespace: ``xivo_dird.services``
* Abstract service plugin: `BaseServicePlugin <https://github.com/xivo-pbx/xivo-dird/blob/5027-dird-daemon-with-plugins/xivo_dird/base_plugins.py#L21-L40>`_
* Abstract service: `BaseService <https://github.com/xivo-pbx/xivo-dird/blob/5027-dird-daemon-with-plugins/xivo_dird/base_plugins.py#L21-L40>`_

* Methods:

  * ``load(args)``: set up resources used by the plugin, depending on the config.
    ``args`` is a dictionary containing:

    * key ``config``: the section of the configuration file for this service in dict form
    * key ``sources``: a dictionary of source names to sources

    ``load`` must return a callable, which will be made available in the view plugins.
  * ``unload()``: free resources used by the plugin.


Example
-------

The following example add a service that will return an empty list when used.

``setup.py``:

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


``xivo_dird_service_dummy/dummy.py``:

.. code-block:: python
   :linenos:
   :emphasize-lines: 17, 23-25, 30, 35-36

   # -*- coding: utf-8 -*-

   import logging

   from xivo_dird import BaseService
   from xivo_dird import BaseServicePlugin

   logger = logging.getLogger(__name__)

   class DummyServicePlugin(BaseServicePlugin):
       """
       This plugin is responsible of instantiating and returning the
       DummyService. It manages it's life time and if necessary should
       take care of it's cleanup if necessary
       """

       def load(self, args):
           """
           Ignores all provided arguments and instanciate a DummyService that
           is returned to the core
           """
           logger.info('dummy loaded')
           self._service = DummyService()
           return self._service

       def unload(self):
           logger.info('dummy unloaded')


   class DummyService(BaseService):
       """
       A very dumb service that will return an empty list every time it is used
       """

       def __call__(self):
           return []



.. _dird-view:

View
====
