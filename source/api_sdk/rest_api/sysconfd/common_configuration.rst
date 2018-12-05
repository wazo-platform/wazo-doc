.. _common_configuration:

********************
Common configuration
********************

Apply configuration
===================

Query
-----

::

    GET /commonconf_apply



Generate configuration
======================

Query
-----

::

    POST /commonconf_generate


Change ownership of the Asterisk autoprov configuration files
=============================================================

Query
-----

::

   POST /exec_request_handlers

    {"chown_autoprov_config": "foo"}


Example:
--------

.. code:: sh

    curl -X POST -H 'Content-Type: application/json' "http://localhost:8668/exec_request_handlers" -d '{"chown_autoprov_config": "foo"}'
