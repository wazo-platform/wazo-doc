*********
Call Logs
*********

Call logs can be accessed using the menu :menuselection:`Services --> IPBX --> Call management --> Call Logs` page.

Call records can be used for:

* Search by start and end date
* Search by Channel, Caller, Called

You can export search results to CSV files.

The call logs results are currently limited to 20000 CEL entries, which represent a maximum of about 2000 calls. If you hit this limit, a message will be displayed, and the last call log entries will not be displayed.


Search Dashboard
----------------

.. figure:: images/search_dashboard.png

   Calls Records Dashboard


Search Results
--------------

.. figure:: images/search_results.png

   Calls Records Search Results


Next Generation Call Logs
-------------------------

Call logs can now be pre-generated from CEL entries. To do so, log on to the target XiVO server and run::

   xivo-call-logs

The call logs are currently generated using the first 20000 CEL entries. In order to consult generated call logs, one must query the ``call_log`` database table using the following command::

   sudo -u postgres psql asterisk -c "select * from call_log;"

It is also possible to directly generate a CSV file containing all entries in the call_log table::

   sudo -u postgres psql asterisk -c "copy call_log to '/tmp/call_logs.csv' WITH delimiter ',' NULL AS '' CSV FORCE QUOTE source_name,destination_name;"

This will generate a file call_logs.csv in the /tmp directory.
