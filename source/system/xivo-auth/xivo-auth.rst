.. _xivo-auth:

=========
xivo-auth
=========

xivo-auth is a scalable, extendable and configurable authentication service.
It uses an HTTP interface to emit tokens to users who can then use those tokens
to identify and authenticate themselves with other services compatible with
xivo-auth.

The HTTP API reference is at http://api.xivo.io.

.. toctree::
   :maxdepth: 1

   changelog
   developer
   stock_plugins


Usage
=====

xivo-auth is used through HTTP requests, using HTTPS. Its default port is 9497.
As a user, the most common operation is to get a new token. This is done with
the POST method.

Alice retrieves a token using her username/password::

    $ # Alice creates a new token, using the xivo_user backend, expiring in 10 minutes
    $ curl -k -X POST -H 'Content-Type: application/json' -u 'alice:s3cre7' "https://localhost:9497/0.1/token" -d '{"backend": "xivo_user", "expiration": 600}';echo
    {"data": {"issued_at": "2015-06-05T10:16:58.557553", "token": "1823c1ee-6c6a-0cdc-d869-964a7f08a744", "auth_id": "63f3dc3c-865d-419e-bec2-e18c4b118224", "xivo_user_uuid": "63f3dc3c-865d-419e-bec2-e18c4b118224", "expires_at": "2015-06-05T11:16:58.557595"}}

In this example Alice used here XiVO CTI client login ``alice`` and password ``s3cre7``. The
authentication source is determined by the :ref:`backend <auth-backends>` in the POST data.

Alice could also have specified an expiration time on her POST request. The
expiration value is the number of seconds before the token expires.

After retrieving her token, Alice can query other services that use xivo-auth
and send her token to those service. Those services can then use this token
on Alice's behalf to access her personal storage.

If Alice wants to revoke her token before its expiration::

    $ curl -k -X DELETE -H 'Content-Type: application/json' "https://localhost:9497/0.1/token/1823c1ee-6c6a-0cdc-d869-964a7f08a744"

See http://api.xivo.io for more details about the HTTP API.

See :ref:`service-authentication` for details about the authentication process.

Usage for services using xivo-auth
==================================

A service that requires authentication and identification can use xivo-auth to
externalise the burden of authentication. The new service can then accept a
token as part of its operations to authenticate the user using the service.

Once a service receives a token from one of its user, it will need to check the
validity of that token. There are 2 forms of verification, one that only checks
if the token is valid and the other returns information about this token's
session if it is valid.

Checking if a token is valid::

    $ curl -k -i -X HEAD -H 'Content-Type: application/json' "https://localhost:9497/0.1/token/1823c1ee-6c6a-0cdc-d869-964a7f08a744"
    HTTP/1.1 204 NO CONTENT
    Content-Type: text/html; charset=utf-8
    Content-Length: 0
    Date: Fri, 05 Jun 2015 14:49:50 GMT
    Server: pcm-dev-0

    $ # get more information about this token
    $ curl -k -X GET -H 'Content-Type: application/json' "https://localhost:9497/0.1/token/1823c1ee-6c6a-0cdc-d869-964a7f08a744";echo
    {"data": {"issued_at": "2015-06-05T10:16:58.557553", "token": "1823c1ee-6c6a-0cdc-d869-964a7f08a744", "auth_id": "63f3dc3c-865d-419e-bec2-e18c4b118224", "xivo_user_uuid": "63f3dc3c-865d-419e-bec2-e18c4b118224", "expires_at": "2015-06-05T11:16:58.557595"}}


Launching xivo-auth
===================

::

    usage: xivo-auth [-h] [-c CONFIG_FILE] [-u USER] [-d] [-f] [-l LOG_LEVEL]

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_FILE, --config-file CONFIG_FILE
                            The path to the config file
      -u USER, --user USER  User to run the daemon
      -d, --debug           Log debug messages
      -f, --foreground      Foreground, don't daemonize
      -l LOG_LEVEL, --log-level LOG_LEVEL
                            Logs messages with LOG_LEVEL details. Must be one of:
                            critical, error, warning, info, debug. Default: None


HTTP API Reference
==================

The complete HTTP API documentation is at http://api.xivo.io.

See also the :ref:`auth_changelog`.


Development
===========

See :ref:`xivo-auth-developer`.
