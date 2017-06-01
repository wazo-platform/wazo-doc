.. _call_logs:

*********
Call Logs
*********

Call logs allow users to see the history of the calls placed and received by Wazo.

.. note:: The oldest call logs are periodically removed. See :ref:`purge_logs` for more details.


Search Dashboard
================

Call logs can be accessed using the menu :menuselection:`Services --> IPBX --> Call management --> Call Logs` page.

.. figure:: images/search_dashboard.png

   Calls Records Dashboard

Specifying no start date returns all available call logs. Specifying a start date and no end date
returns all call logs from start date until now.

Call logs are presented in a CSV format. Here's an example::

   Call Date,Caller,Called,Period,user Field
   2015-01-02T00:00:00,Alice (1001),1002,2,userfield

The CSV format has the following specifications:

* field names are listed on the first line
* fields are separated by commas: ``,``
* if there is a comma in a field value, the value is surrounded by double quotes: ``"``
* the UTF-8 character encoding is used


REST API
========

Call logs are also available from :ref:`xivo-call-logd REST API <call-logd-api>`.


Categorize call logs with custom tags
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes, it's useful to separate call logs according to a specific value (department, city, etc.).
It's possible with the ``User field`` of a user and the ``tags`` of a call log. Each ``User field``
will be copied into the ``tags`` for a call log and each ``User field`` must be separated by a
comma.


Example
-------

Your company has employees in the `accounting` and `sales` departments. To list call logs from the
`sales` department, you must set the ``User field`` of each user to ``sales``. Now when a user
tagged with ``sales`` places or receives a call, this call will be also tagged ``sales``. You can now
filter call logs by tags ``sales``.


Manual generation
=================

Call logs can also be generated manually. To do so, log on to the target Wazo server and run::

   xivo-call-logs

To avoid running for too long in one time, the call logs generation is limited to the N last
unprocessed CEL entries (default 20,000). This means that successive calls to ``xivo-call-logs``
will process N more CELs, making about N/10 more calls available in call logs, going further back in
history, while processing new calls as well.

You can specify the number of CEL entries to consider. For example, to generate calls using the
100,000 last unprocessed CEL entries::

   xivo-call-logs -c 100000


Regeneration of call logs
=========================

Since call logs are based on CEL, they can be deleted and generated without problems. To regenerate
the last month of call logs::

   xivo-call-logs delete -d 30
   xivo-call-logs generate -d 30  // the default behavior of xivo-call-logs command is `generate`

Technicals
==========

Call logs are pre-generated from CEL entries. The generation is done automatically
by xivo-call-logd. xivo-call-logs is also run nightly to generate call logs from
CEL that were missed by xivo-call-logd.
