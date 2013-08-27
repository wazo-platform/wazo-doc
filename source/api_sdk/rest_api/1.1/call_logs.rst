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


List Extension
==============

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
