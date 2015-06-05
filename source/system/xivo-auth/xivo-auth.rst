.. _xivo-auth:

=========
XiVO auth
=========

xivo-auth is a scalable, extendable and configurable authentification service.
It uses an HTTP interface to emit tokens to users who can then use those tokens
to identify and authenticate themselves with other services compatible with
xivo-auth.


Usage
=====

xivo-auth is use through HTTP requests, its default port is 9794. As a user, the
most common operation is to get a new token. This is done with the POST method.

Alice retrieves a token using her username/password::

    $ # Alice creates a new token, using the xivo_user backend
    $ curl -X POST -H 'Content-Type: application/json' -u 'alice:s3cre7' "localhost:9497/0.1/token" -d '{"backend": "xivo_user"}';echo
    {...}

    $

In this example Alice used here XiVO cti client login and password. The
authentification source is determined by the backend in the POST data.

Alice could also have specified an expiration time on her POST request. The
expiration value is the number of seconds before the token expires.

After retrieving her token, Alice can query other services that use xivo-auth
and send here token to those service. Those services can then use this token
on Alice's behalf to access her personnal storage.

If Alice wants to revoke her token before it's expiration::

    $ curl -X DELETE -H 'Content-Type: application/json' "localhost:9497/0.1/token/<XXX add the token here>"
    $


Usage for services using xivo-auth
==================================

A service that require authentification and identification can use xivo-auth to
externalise the burden of authentification. The new service can then accept a
token as part of its operations to authenticate the user using the service.

Once a service receives a token from one of its user, it will need to check the
validity of that token. There are 2 forms of verification, one that only check
if the token is valid and the other returning information about this token's
session if it is valid.

Checking if a token is valid::

    $ curl -i -X HEAD -H 'Content-Type: application/json' "localhost:9497/0.1/token/<XXX add the token here>"
    204

    $ # get more information about this token
    $ curl -X GET -H 'Content-Type: application/json' "localhost:9497/0.1.token<XXX add the token here>"
    {...}

    $


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
