*********
CLI Tools
*********

Wazo comes with a collection of console (CLI) tools to help administer the server.


wazo-auth-cli
-------------

``wazo-auth-cli`` is a command-line interface to interact with the REST API of ``wazo-auth``. It
provides mainly authentication-related features.

See ``wazo-auth-cli --help`` for a list of available operations.


wazo-plugind-cli
----------------

``wazo-plugind-cli`` is a command-line interface to interact with the REST API of ``wazo-plugind``.
It provides mainly plugin-related features.

See ``wazo-plugind-cli --help`` for a list of available operations.


.. _wazo_reset:

wazo-reset
----------

wazo-reset is a tool to reset some of the state of a Wazo installation to a pre-wizard state.  It
does not try to reset everything and will *not* give the same result as a fresh new Wazo
installation. For example, all customizations that you have made that are not stored in the database
(e.g. installing Debian packages, adding custom configuration files, etc), will not be reset. This
tool should be used with extra care.

After using it, you need to pass the wizard once again.


xivo-agentd-cli
---------------

``xivo-agentd-cli`` is a command-line interface to interact with the REST API of ``xivo-agentd``.
It provides mainly agent-related features.

``xivo-agentd-cli`` has an interactive REPL mode. You can access it with the command
``xivo-agentd-cli``. It should prompt you for a password that is empty by default. Once in the
interactive mode, enter ``help`` for a list of available operations.


.. _xivo_dist:

xivo-dist
---------

xivo-dist is the wazo repository sources manager. It is used to switch between distributions
(production, development, release candidate, archived version). Example use cases :

* switch to production repository : ``xivo-dist phoenix``
* switch to development repository : ``xivo-dist wazo-dev-stretch``
* switch to release candidate repository : ``xivo-dist wazo-rc``
* switch to an archived version's repository (here 14.18) : ``xivo-dist xivo-14.18``


xivo-provd-cli
--------------

``xivo-provd-cli`` is a command-line interface to interact with the REST API of ``xivo-provd``. It
provides mainly provisioning-related features.

``xivo-provd-cli`` has an interactive REPL mode. You can access it with the command
``xivo-provd-cli``. It should prompt you for a password that is empty by default. Once in the
interactive mode, enter ``help`` for a list of available operations.
