.. _call_logs:

*********
Call Logs
*********

Call logs can be accessed using the menu :menuselection:`Services --> IPBX --> Call management --> Call Logs` page.

Call logs can be filtered by period of time.

Results are delivered in a CSV file export.

The call logs results are currently limited to 20000 CEL entries, which represent a maximum of about 2000 calls. This limitation comes from REST API.


Search Dashboard
----------------

.. figure:: images/search_dashboard.png

   Calls Records Dashboard


.. _next-gen-call-logs:

Next Generation Call Logs
-------------------------

Call logs can now be pre-generated from CEL entries. To do so, log on to the target XiVO server and run::

   xivo-call-logs

The call logs are currently generated using the first 20000 CEL entries. In order to consult
generated call logs, you can use the new REST API. See :ref:`restapi-call-logs`.
