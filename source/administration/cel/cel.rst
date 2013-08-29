.. _call_logs:

*********
Call Logs
*********

Call logs can be filtered by period of time.

Results are delivered in a CSV file export.

The call logs results are currently limited to the 20000 last CEL entries, which represent a maximum
of about 2000 most recent calls.

Call logs must be pre-generated from CEL entries. To do so, log on to the target XiVO server and run::

   xivo-call-logs


Search Dashboard
----------------

Call logs can be accessed using the menu :menuselection:`Services --> IPBX --> Call management --> Call Logs` page.

.. figure:: images/search_dashboard.png

   Calls Records Dashboard


REST API
--------

Call logs are also available from the new REST API. See :ref:`restapi-call-logs`.
