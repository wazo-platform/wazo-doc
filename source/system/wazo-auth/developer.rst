.. _wazo-auth-developer:

===========================
wazo-auth Developer's Guide
===========================

Architecture
============

wazo-auth contains 4 major components, an HTTP interface, a celery worker,
authentication backends and a storage module. All operations are made through
the HTTP interface, tokens are stored in postgres as well as the persistence
for some of the data attached to tokens. The celery worker is used to schedule
tasks that outlive the lifetime of the wazo-auth process. Backends are used
to test if a supplied username/password combination is valid and provide the
xivo-user-uuid.

wazo-auth is made of the following modules and packages.


plugins
-------

the plugin package contains the wazo-auth backends that are packaged with
wazo-auth.


http
----

The http module is the implementation of the HTTP interface.

* Validate parameters
* Calls the backend the check the user authentication
* Forward instructions to the *token_manager*
* Handle exceptions and return the appropriate status_code


controller
----------

The controller is the plumbin of wazo-auth, it has no business logic.

* Start the HTTP application
* Start the celery worker
* Load all enabled plugins
* Instanciate the token_manager


token
-----

The token modules contains the business logic of wazo-auth.

* Creates and delete tokens
* Creates ACLs for Wazo
* Schedule token expiration


tasks
-----

The tasks module contains implementation of celery tasks that are executed by
the worker.

* Called by the celery worker
* Forwards instructions to the *token manager*


extension
---------

This is a place holder for a global variable for the celery app. It will be
removed and should not be used.


Other modules that should not need documentation are *helpers*, *config*, *interfaces*


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
<http://github.com/wazo-pbx/xivo-auth-example-backend>`_.
