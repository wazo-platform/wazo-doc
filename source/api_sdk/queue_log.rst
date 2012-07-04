**********
Queue logs
**********

Queue logs are events logged by Asterisk in the queue_log table of the asterisk database.
Queue logs are used to generate XiVO call center statistics.


Queue log sample
================


Agent callback login
--------------------

::

   time                       |     callid      | queuename |   agent    |        event        |        data1        |      data2      |     data3     | data4 | data5
   ---------------------------+-----------------+-----------+------------+---------------------+---------------------+-----------------+---------------+-------+-------
   2012-07-03 15:27:23.896208 | 1341343640.4    | NONE      | Agent/3001 | AGENTCALLBACKLOGIN  | 1002@pcm-dev        |                 |               |       |


Agent callback logoff
---------------------

Agent/3001 is logged in queues q1 and q2.

::

   time                       |     callid      | queuename |   agent    |        event        |        data1        |      data2      |     data3     | data4 | data5
   ---------------------------+-----------------+-----------+------------+---------------------+---------------------+-----------------+---------------+-------+-------
   2012-07-03 15:28:07.348244 | NONE            | q2        | Agent/3001 | UNPAUSE             |                     |                 |               |       |
   2012-07-03 15:28:07.346320 | NONE            | q1        | Agent/3001 | UNPAUSE             |                     |                 |               |       |
   2012-07-03 15:28:07.327425 | NONE            | NONE      | Agent/3001 | UNPAUSEALL          |                     |                 |               |       |
   2012-07-03 15:28:06.249357 | NONE            | NONE      | Agent/3001 | AGENTCALLBACKLOGOFF | 1002@pcm-dev        | 43              | CommandLogoff |       |
