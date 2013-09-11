.. _call_logs:

*********
Call Logs
*********

Call logs must be pre-generated from CEL entries. To do so, log on to the target XiVO server and run::

   xivo-call-logs

You can specify the number of CEL entries to consider. For example, to generate calls using the
100,000 last unprocessed CEL entries::

   xivo-call-logs -c 100000

The call logs generation is limited to the N last unprocessed CEL entries (default 20,000). This
means that successive calls to ``xivo-call-logs`` will process N more CELs, making about N/10 more
calls available in call logs, going further back in history, while processing new calls as well.


Search Dashboard
----------------

Call logs can be accessed using the menu :menuselection:`Services --> IPBX --> Call management --> Call Logs` page.

.. figure:: images/search_dashboard.png

   Calls Records Dashboard

Call logs are presented in a CSV file. The CSV specifications are detailed in :ref:`the REST API
documentation <call-logs-format>`.

Specifying no start date returns all available call logs. Specifying a start date and no end date
returns all call logs from start date until now.


REST API
--------

Call logs are also available from the REST API. See :ref:`restapi-call-logs`.
