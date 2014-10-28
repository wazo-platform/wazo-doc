.. _xivo-dird-developer:

=============================
 XiVO dird developer's guide
=============================

The XiVO dird architecture uses plugins as extension points for most of its
job. It uses `stevedore <http://stevedore.readthedocs.org>`_ to do the plugin
instantiation and discovery and `ABC <https://docs.python.org/2/library/abc.html>`_
classes to define the required interface.

Plugins in xivo-dird use setuptools' entry points. That means that installing a
new plugin to xivo-dird requires an entry point in the plugin's setup.py. Each
entry point's `namespace` is documented in the appropriate documentation
section. These entry points allow xivo-dird to be able to discover and load
extensions packaged with xivo-dird or installed separately.

Each kind of plugin does a specific job. There are three kinds of plugins in
dird.

#. :ref:`dird-back-end`
#. :ref:`dird-service`
#. :ref:`dird-view`

All plugins are instantiated by the core. The core then keeps a catalogue of
loaded extensions that can be supplied to other extensions.

The following setup.py shows an example of a python library that add a plugin
of each kind to xivo-dird:

.. code-block:: python
   :linenos:
   :emphasize-lines: 15-26

   #!/usr/bin/env python
   # -*- coding: utf-8 -*-

   from setuptools import setup
   from setuptools import find_packages


   setup(
       name='XiVO dird plugin sample',
       version='0.0.1',

       description='An example program',

       packages=find_packages(),

       entry_points={
           'xivo_dird.services': [
               'my_service = dummy:DummyServicePlugin',
           ],
           'xivo_dird.backends': [
               'my_backend = dummy:DummyBackend',
           ],
           'xivo_dird.views': [
               'my_view = dummy:DummyView',
           ],
       }
   )


.. _dird-back-end:

Back-End
========

Back-ends are used to query directories. Each back-end implements a way to query
a given directory. Each instance of a given back-end is called a source. Sources
are used by the services to get results from each configured directories.

Given a ldap back-end, I can configure a source to point to alpha.example.com
and another to beta.example.com. Both of these sources use the ldap back-end.


Implementation details
----------------------

* Namespace: ``xivo_dird.backends``
* Abstract source plugin: `BaseSourcePlugin <https://github.com/xivo-pbx/xivo-dird/blob/5027-dird-daemon-with-plugins/xivo_dird/base_source_plugin.py#L21-L76>`_
* Methods:

  * ``name``: the name of the source, retrieved from the configuration file
  * ``load(args)``: set up resources used by the plugin, depending on the config.
    ``args`` is a dictionary containing:
    * key ``config``: the source configuration for this instance of the back-end
  * ``unload()``: free resources used by the plugin.
  * ``search(term, args)``: The search method returns a list of dictionary
  * ``list(uids)``: The list method returns a list of dictionary from a list of uids.

The typical configuration file for a given back-end will look like this:

.. code-block:: yaml
   :linenos:

   type: <back-end name>
   name: <source-name>
   unique_columns:
       - id
   search_columns:
       - firstname
   source_to_display_columns:
       lastname: ln
       firstname: fn
       number: telephoneNumber


* type: is the name of the back-end plugin. It should match the extension point in the setup.py
* name: is the name of this given configuration. The name is used to associate the source to profiles.
* unique_columns: This list of columns is what make an entry in this source unique.
* search_columns: This list of columns is used to try and match an entry when searching this source.
* source_to_display_columns: This section is used to add column names to the result.

The implementation of the back-end should take these values into account and
return results accordingly. It is possible for a source to have no
`unique_columns` in that case, it might be impossible to use this source for
certain actions that are based on the list method. The `unique_columns` are
used to build the `uid` that is passed to the list method to fetch a list of
results by unique ids. The `search` and `list` methods *should* apply the
`source_to_display_columns` transformation to the result before returning.


Example
-------

The following example add a backend that will return random names and number.

``dummy.py``:

.. code-block:: python
   :linenos:
   :emphasize-lines: 18-20, 22-23

   # -*- coding: utf-8 -*-

   import logging

   logger = logging.getLogger(__name__)

   class DummyBackendPlugin(object):

       def name(self):
           return 'my_local_dummy'

       def load(self, args):
           logger.info('dummy backend loaded')

       def unload(self):
           logger.info('dummy backend unloaded')

       def search(self, term, args):
           nb_results = random.randint(1, 20)
           return _random_list(nb_results)

       def list(self, unique_ids):
           return _random_list(len(unique_ids))

       def _random_list(self, nb_results):
           columns = ['Firstname', 'Lastname', 'Number']
           return [_random_entry(columns) for _ in xrange(nb_results)]

       def _random_entry(self, columns):
           random_stuff = [_random_string() for _ in xrange(len(columns))]
           return dict(zip(columns, random_stuff))

       def _random_string(self):
           return ''.join(random.choice(string.lowercase) for _ in xrange(5))




.. _dird-service:

Service
=======

Service plugins add new functionality to the dird server. These functionalities
are available to views. When loaded, a service plugin receives its configuration
and a dictionary of available sources.

Some service examples that come to mind include:

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

The following example adds a service that will return an empty list when used.

``dummy.py``:

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
       This plugin is responsible fow instantiating and returning the
       DummyService. It manages its life time and should take care of
       its cleanup if necessary
       """

       def load(self, args):
           """
           Ignores all provided arguments and instantiate a DummyService that
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
