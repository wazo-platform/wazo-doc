.. _xivo-confgend-developer:

===============================
XiVO confgend developer's guide
===============================

xivo-confgend uses drivers to implement the logic required to generate
configuration files.  It uses `stevedore <http://docs.openstack.org/developer/stevedore/>`_
to do the driver instantiation and discovery.

Plugins in xivo-confgend use setuptools' entry points. That means that
installing a new plugin to xivo-confgend requires an entry point in the plugin's
*setup.py*.


Drivers
-------

Driver plugin are classes that are used to generate the content of a
configuration file.

The implementation of a plugin should have the following properties.

#. It's ``__init__`` method should take one argument
#. It should have a ``generate`` method which will return the content of the file
#. A setup.py adding an entry point


The ``__init__`` method argument is the content of the configuration of
xivo-confgend. This allows the driver implementor to add values to the
configuration in ``/etc/xivo-confgend/conf.d/*.yml`` and these values will be
available in the driver.

The generate method has no argument, the configuration provided to the
``__init__`` should be sufficient for most cases. ``generate`` is called within a
``scoped_session`` of xivo-dao, allowing the usage of xivo-dao without prior setup
in the driver.

The namespaces used for entry points in xivo-confgend have the following form:

    confgend.<resource>.<filename>

as an example, a generator for sip.conf would have the following namespace:

    confgend.asterisk.sip.conf

Here is a typical setup.py:

.. code-block:: python
   :linenos:

   #!/usr/bin/env python
   # -*- coding: utf-8 -*-

   from setuptools import setup
   from setuptools import find_packages


   setup(
       name='XiVO confgend driversample',
       version='0.0.1',

       description='An example driver',

       packages=find_packages(),

       entry_points={
           'confgend.asterisk.sip.conf': [
               'my_driver = src.driver:MyDriver',
           ],
       }
   )

With the following package structure::

   .
   ├── setup.py
   └── src
       └── driver.py  # declares a class MyDriver with methods __init__ and generate
