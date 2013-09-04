.. _call_logs:

*********
Call Logs
*********

Call logs must be pre-generated from CEL entries. To do so, log on to the target XiVO server and run::

   xivo-call-logs

The call logs generation is currently limited to the 20000 last CEL entries, which means that you
can not see any call older than the 2000th or so most recent call.


Search Dashboard
----------------

Call logs can be accessed using the menu :menuselection:`Services --> IPBX --> Call management --> Call Logs` page.

.. figure:: images/search_dashboard.png

   Calls Records Dashboard

Call logs are presented in a CSV file. The CSV specifications are detailed in :ref:`the REST API
documentation <call-logs-format>`.


REST API
--------

Call logs are also available from the REST API. See :ref:`restapi-call-logs`.
