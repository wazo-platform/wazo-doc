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

#. A flask_restful class implementing the route for this plugin
#. A marshmallow model that can filter the stored data to be safe for unpriviledged view
#. A setup.py adding the plugin the the `wazo_auth.http` entry point


The restful class should do the following:

* POST: This is where the plugin should setup any information with the external service and usually return
  a validation code and a validateion URL to the user.

* GET: After activating the external authentication, following the POST. The GET can be used to retrieve
  credentials granting access to certain resource of the external service.

* DELETE: Should remove the stored data from wazo-auth

* PUT: (optional) Could be implemented to modify the scope of the generated credentials if the external
  service allow that kind of modification.


A minimal example without the external auth besiness logic can be found in the `tests <https://github.com/wazo-pbx/wazo-auth/blob/master/integration_tests/assets/external_auth/service_plugin/src/plugin.py>`_.
