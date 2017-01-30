*********
CLI Tools
*********

Wazo comes with a collection of console (CLI) tools to help administer the server.

.. _xivo_dist:

xivo-dist
---------

xivo-dist is the wazo repository sources manager. It is used to switch between distributions
(production, development, release candidate, archived version). Example use cases :

* switch to production repository : ``xivo-dist phoenix``
* switch to development repository : ``xivo-dist wazo-dev``
* switch to release candidate repository : ``xivo-dist wazo-rc``
* switch to an archived version's repository (here 14.18) : ``xivo-dist xivo-14.18``


.. _wazo_reset:

wazo-reset
----------

wazo-reset is a tool to reset some of the state of a Wazo installation to a pre-wizard state.  It
does not try to reset everything and will *not* give the same result as a fresh new Wazo
installation. For example, all customizations that you have made that are not stored in the database
(e.g. installing Debian packages, adding custom configuration files, etc), will not be reset. This
tool should be used with extra care.

After using it, you need to pass the wizard once again.
