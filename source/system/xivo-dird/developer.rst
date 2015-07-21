.. _xivo-dird-developer:

=============================
 XiVO dird developer's guide
=============================

.. figure:: images/startup.png

   xivo-dird startup flow

The XiVO dird architecture uses plugins as extension points for most of its
job. It uses `stevedore <http://docs.openstack.org/developer/stevedore/>`_ to do the plugin
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

.. figure:: images/query.png

   xivo-dird HTTP query

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
are used by the services to get results from each configured directory.

Given one LDAP back-end, I can configure a source from the LDAP at alpha.example.com and another
source from the other LDAP at beta.example.com. Both of these sources use the LDAP back-end.


Implementation details
----------------------

* Namespace: ``xivo_dird.backends``
* Abstract source plugin: `BaseSourcePlugin <https://github.com/xivo-pbx/xivo-dird/blob/master/xivo_dird/plugins/base_plugins.py#L67>`_
* Methods:

  * ``name``: the name of the source, typically retrieved from the configuration injected to
    ``load()``
  * ``load(args)``: set up resources used by the plugin, depending on the config.
    ``args`` is a dictionary containing:

    * key ``config``: the source configuration for this instance of the back-end
    * key ``main_config``: the whole configuration of xivo-dird

  * ``unload()``: free resources used by the plugin.
  * ``search(term, args)``: The search method returns a list of dictionary.

    * Empty values should be ``None``, instead of empty string.
    * ``args`` is a dictionary containing:

      * key ``token_infos``: data associated to the authentification token (see :ref:`xivo-auth`)

  * ``list(uids, args)``: The list method returns a list of dictionary from a list of uids. Each uid
    is a string identifying a contact within the source.

    * ``args`` is a dictionary containing:

      * key ``token_infos``: data associated to the authentification token (see :ref:`xivo-auth`)

The typical configuration file for a given back-end will look like this:

.. code-block:: yaml
   :linenos:

   type: <back-end name>
   name: <source-name>
   unique_column: id
   search_columns:
       - firstname
   format_columns:
       ln: "{lastname}"
       fn: "{firstname}"
       telephoneNumber: "{number}"


The following keys are mandatory: xivo-dird will not load the source if they are not present:

type
   the name of the back-end plugin. It should match the extension point in the setup.py

name
   is the name of this given configuration. The name is used to associate the source to profiles.

The remaining keys are conventional: they are not required by xivo-dird, but it's a good idea to
use these for your configuration format.

unique_column
   This column is what makes an entry unique in this source. The ``unique_column`` is used to
   build the ``uid`` that is passed to the list method to fetch a list of results by unique ids.

search_columns
   This list of columns is used to try and match an entry when searching this source.

format_columns
    This section is used to add or modify columns. The values are python format strings using the
    raw search result as argument.


The implementation of the back-end should take these values into account and return results
accordingly.


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
* Abstract service plugin: `BaseServicePlugin <https://github.com/xivo-pbx/xivo-dird/blob/master/xivo_dird/plugins/base_plugins.py#L21>`_
* Abstract service: `BaseService <https://github.com/xivo-pbx/xivo-dird/blob/master/xivo_dird/plugins/base_plugins.py#L43>`_

* Methods:

  * ``load(args)``: set up resources used by the plugin, depending on the config.
    ``args`` is a dictionary containing:

    * key ``config``: the whole configuration file in dict form
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

View plugins add new routes to the HTTP application in xivo-dird, in particular the REST API of
xivo-dird: they define the URLs to which xivo-dird will respond and the formatting of data received
and sent through those URLs.

For example, we can define a REST API formatted in JSON with one view and the same API formatted in
XML with another view. Supporting the directory function of a phone is generally a matter of
adding a new view for the format that the phone consumes.


Implementation details
----------------------

* Namespace: ``xivo_dird.views``
* Abstract view plugin: `BaseViewPlugin <https://github.com/xivo-pbx/xivo-dird/blob/master/xivo_dird/plugins/base_plugins.py#L52>`_

* Methods:

  * ``load(args)``: set up resources used by the plugin, depending on the config. Typically,
    register routes on Flask. Those routes would typically call a service.
    ``args`` is a dictionary containing:

    * key ``config``: the section of the configuration file for all views in dict form
    * key ``services``: a dictionary of services, indexed by name, which may be called from a route
    * key ``http_app``: the `Flask application`_ instance
    * key ``rest_api``: a `Flask-RestFul Api`_ instance

      .. _Flask application: http://flask.pocoo.org/
      .. _Flask-RestFul Api: http://flask-restful.readthedocs.org/en/latest/quickstart.html#a-minimal-api

  * ``unload()``: free resources used by the plugin.


Example
-------

The following example adds a simple view: ``GET /0.1/directories/ping`` answers ``{"message": "pong"}``.

``dummy.py``:

.. code-block:: python
   :linenos:
   :emphasize-lines: 20, 26-32

   # -*- coding: utf-8 -*-

   import logging

   from flask_restful import Resource

   logger = logging.getLogger(__name__)


   class PingViewPlugin(object):

       name = 'ping'

       def __init__(self):
           logger.debug('dummy view created')

       def load(self, args):
           logger.debug('dummy view args: %s', args)

           args['rest_api'].add_resource(PingView, '/0.1/directories/ping')

       def unload(self):
           logger.debug('dummy view unloaded')


   class PingView(Resource):
       """
       Simple API using Flask-Restful: GET /0.1/directories/ping answers "pong"
       """

       def get(self):
           return {'message': 'pong'}
