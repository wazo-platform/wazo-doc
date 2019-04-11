*********
CLI Tools
*********

Wazo comes with a collection of console (CLI) tools to help administer the server.


wazo-auth-cli
-------------

``wazo-auth-cli`` is a command-line interface to interact with the REST API of ``wazo-auth``. It
provides mainly authentication-related features.

See ``wazo-auth-cli --help`` for a list of available operations.


wazo-dist-upgrade
-----------------

``wazo-dist-upgrade`` is used to upgrade Wazo when a Debian upgrade is required.
``wazo-dist-upgrade`` can only be used after ``wazo-upgrade``.

wazo-plugind-cli
----------------

``wazo-plugind-cli`` is a command-line interface to interact with the REST API of ``wazo-plugind``.
It provides mainly plugin-related features.

See ``wazo-plugind-cli --help`` for a list of available operations.


wazo-service
------------

``wazo-service`` is used to control and print the status of the Wazo services.


.. _wazo_reset:

wazo-reset
----------

wazo-reset is a tool to reset some of the state of a Wazo installation to a pre-wizard state.  It
does not try to reset everything and will *not* give the same result as a fresh new Wazo
installation. For example, all customizations that you have made that are not stored in the database
(e.g. installing Debian packages, adding custom configuration files, etc), will not be reset. This
tool should be used with extra care.

After using it, you need to pass the wizard once again.


wazo-upgrade
------------

``wazo-upgrade`` is used to upgrade Wazo to a later version. Beginning with Wazo 17.17,
``wazo-upgrade`` will not upgrade to a later Debian version. For this, you have to use
``wazo-dist-upgrade``.


xivo-agentd-cli
---------------

``xivo-agentd-cli`` is a command-line interface to interact with the REST API of ``xivo-agentd``.
It provides mainly agent-related features.

``xivo-agentd-cli`` has an interactive REPL mode. You can access it with the command
``xivo-agentd-cli``. It should prompt you for a password that is empty by default. Once in the
interactive mode, enter ``help`` for a list of available operations.


.. _wazo_dist:

wazo-dist
---------

wazo-dist is the wazo repository sources manager. It is used to switch between distributions
(production, development, release candidate, archived version). Example use cases :

* switch to production repository : ``wazo-dist phoenix``
* switch to development repository : ``wazo-dist wazo-dev-stretch``
* switch to release candidate repository : ``wazo-dist wazo-rc-stretch``
* switch to an archived version's repository: ``wazo-dist wazo-18.02``


xivo-provd-cli
--------------

``xivo-provd-cli`` is a command-line interface to interact with the REST API of ``xivo-provd``. It
provides mainly provisioning-related features.

``xivo-provd-cli`` has an interactive REPL mode. You can access it with the command
``xivo-provd-cli``. It should prompt you for a password that is empty by default. Once in the
interactive mode, enter ``help`` for a list of available operations.
