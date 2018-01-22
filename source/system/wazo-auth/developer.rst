.. _wazo-auth-developer:

===========================
wazo-auth Developer's Guide
===========================

Architecture
============

wazo-auth contains 3 major components, an HTTP interface, authentication backends
and a storage module. All operations are made through the HTTP interface, tokens
are stored in postgres as well as the persistence for some of the data attached
to tokens. Backends are used to test if a supplied username/password combination
is valid and provide the xivo-user-uuid.

wazo-auth is made of the following modules and packages.


backend_plugins
---------------

the plugin package contains the wazo-auth backends that are packaged with
wazo-auth.


http_plugins
------------

The http module is the implementation of the HTTP interface.

* Validate parameters
* Calls the backend the check the user authentication
* Forward instructions to the *token_manager*
* Handle exceptions and return the appropriate status_code


controller
----------

The controller is the plumbin of wazo-auth, it has no business logic.

* Start the HTTP application
* Load all enabled plugins
* Instanciate the token_manager


token
-----

The token modules contains the business logic of wazo-auth.

* Creates and delete tokens
* Creates ACLs for Wazo
* Schedule token expiration


Plugins
=======

wazo-auth is meant to be easy to extend. This section describes how to add
features to wazo-auth.


Backends
--------

wazo-auth allows its administrator to configure one or many sources of
authentication. Implementing a new kind of authentication is quite simple.

#. Create a python module implementing the `backend interface
   <https://github.com/wazo-pbx/wazo-auth/blob/master/wazo_auth/interfaces.py>`_.
#. Install the python module with an entry point *wazo_auth.backends*

An example backend implementation is available `here
<http://github.com/wazo-pbx/wazo-auth-example-backend>`_.


External Auth
-------------

wazo-auth allows the user to enable arbitrary external authentication, store
sensible information which can be retrieved later given an appropriate ACL.

An external authentication plugin is made of the following parts.

#. A setup.py adding the plugin the the `wazo_auth.http` entry point
#. A flask_restful class implementing the route for this plugin
#. A marshmallow model that can filter the stored data to be safe for unpriviledged view
#. A plugin_info dictionary with information that should be displayed in UI concerning this plugin


The restful class should do the following:

* POST: This is where the plugin should setup any information with the external service and usually return
  a validation code and a validateion URL to the user.

* GET: After activating the external authentication, following the POST. The GET can be used to retrieve
  credentials granting access to certain resource of the external service.

* DELETE: Should remove the stored data from wazo-auth

* PUT: (optional) Could be implemented to modify the scope of the generated credentials if the external
  service allow that kind of modification.


Files::

  setup.py
  src/plugin.py


``setup.py``:

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    from setuptools import find_packages
    from setuptools import setup
    
    setup(
        name='auth_bar',
        version='0.1',
    
        packages=find_packages(),
        entry_points={
            'wazo_auth.external_auth': [
                'bar = src.plugin:BarPlugin',
            ],
        }
    )
    

``src/plugin.py``:

.. code-block:: python

    # -*- coding: utf-8 -*-
    
    from marshmallow import Schema, fields, pre_load
    from flask import request
    from wazo_auth import http
    
    
    class BarService(http.AuthResource):
    
        auth_type = 'bar'  # Should be the same as the entry point
    
        def __init__(self, external_auth_service):
            self.external_auth_service = external_auth_service
    
        @http.required_acl('auth.users.{user_uuid}.external.bar.delete')
        def delete(self, user_uuid):
            # Remove all stored data for the BAR service for this user
            self.external_auth_service.delete(user_uuid, self.auth_type)
            return '', 204
    
        @http.required_acl('auth.users.{user_uuid}.external.bar.read')
        def get(self, user_uuid):
            # The GET retrieves all stored data from the service and return the secret that is
            # required to use the Bar service

            # The GET will also need to generate a new token if the current one has expired.
            return self.external_auth_service.get(user_uuid, self.auth_type), 200
    
        @http.required_acl('auth.users.{user_uuid}.external.bar.create')
        def post(self, user_uuid):
            # Should use the body of the POST and create a token with the Bar service
            data = request.get_json(force=True)
            # The external auth service is used to store the data required by the GET
            return self.external_auth_service.create(user_uuid, self.auth_type, data), 200
    
    
    # When GET /users/:uuid/external is called this model will be used to filter the private data
    class BarSafeData(Schema):
    
        # Only the scope field will be returned
        scope = fields.List(fields.String)
    
        @pre_load
        def ensure_dict(self, data):
            return data or {}
    
    
    class BarPlugin(object):
    
        plugin_info = {'required_acl': ['view-all-contacts', 'list-email-addresses']}
    
        def load(self, dependencies):
            api = dependencies['api']
            external_auth_service = dependencies['external_auth_service']
            args = (external_auth_service,)

            # If the plugin does not register a safe mode an empty dictionary will be used when doing
            # a GET /users/:uuid/external
            external_auth_service.register_safe_auth_model('bar', BarSafeData)
    
            api.add_resource(BarService, '/users/<uuid:user_uuid>/external/bar', resource_class_args=args)
