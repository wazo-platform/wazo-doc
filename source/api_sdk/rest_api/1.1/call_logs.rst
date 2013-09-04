.. _restapi-call-logs:

*********
Call Logs
*********

Call Logs Representation
========================

**Description**

+------------+---------+--------------------------------------------------+
| Field      | Values  | Description                                      |
+============+=========+==================================================+
| Call date  | date    | MM/DD/YYYY HH:MM:SS                              |
+------------+---------+--------------------------------------------------+
| Caller     | string  |                                                  |
+------------+---------+--------------------------------------------------+
| Called     | string  |                                                  |
+------------+---------+--------------------------------------------------+
| Period     | integer | Number of seconds of the call. 0 if not answered |
+------------+---------+--------------------------------------------------+
| user Field | string  |                                                  |
+------------+---------+--------------------------------------------------+

**Example**::

   Call Date,Caller,Called,Period,user Field
   01/02/2013 00:00:00,source2 (1002),2002,2,userfield


.. _call-logs-format:

Format
------

Call logs are presented in CSV format, with the following specifications:

* field names are listed on the first line
* fields are separated by commas: ``,``
* if there is a comma in a field value, the value is surrounded by double quotes: ``"``
* the CSV file uses the character encoding UTF-8


List Call logs
==============

.. note:: For now, call logs need to be generated before listing. See :ref:`call_logs`.

::

   GET /1.1/call_logs

**Example request**::

   GET /1.1/call_logs HTTP/1.1
   Host: xivoserver
   Accept: text/csv

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: text/csv; charset=utf8

   Call Date,Caller,Called,Period,user Field
   01/01/2013 00:00:00,source1 (1001),2001,1,
   01/02/2013 00:00:00,source2 (1002),2002,2,userfield


Filtering by period
-------------------

::

   GET /1.1/call_logs?start_date=DATE&end_date=DATE


``DATE`` must be in the following format: ``YYYY-MM-DDTHH:MM:SS``. Note the ``T`` separating the
date and time. ``start_date`` and ``end_date`` must be given together ; the REST API will not accept
``start_date`` without ``end_date`` and vice-versa.

**Example request**::

   GET /1.1/call_logs?start_date=2013-01-01T00:12:34&end_date=2013-01-02T06:54:32 HTTP/1.1
   Host: xivoserver
   Accept: text/csv

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: text/csv; charset=utf8

   Call Date,Caller,Called,Period,user Field
   01/01/2013 01:00:00,source1 (1001),2001,1,
   01/02/2013 00:00:00,source2 (1002),2002,2,userfield
