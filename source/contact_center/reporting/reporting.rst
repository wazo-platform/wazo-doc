*********
Reporting
*********

You may use your own reporting tools to be able to produce your own reports provided **you do not use the XiVO server original tables**,
but copy the tables to your own data server. You may use the following procedure as a template :

* Allow remote database access on XiVO
* Create a postgresql account read only on asterisk database
* Create target tables in your database located on the data server
* Copy the statistic table content to your data server



Statistic Data Table Content
============================

stat_call_on_queue
------------------

+----------+---------------+-------------------------------------------------------------------------------------------------------+
| Field    | Values        | Description                                                                                           |
|          |               |                                                                                                       |
+==========+===============+=======================================================================================================+
| id       | generated     |                                                                                                       |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| callid   | numeric value | This call id is also used in the CEL table and can be used to get call detail information             |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| time     | Call time     |                                                                                                       |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| ringtime |               | Ringing duration time in seconds                                                                      |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| talktime |               | Talk time duration in seconds                                                                         |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| waittime |               | Wait time duration in seconds                                                                         |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| status   |               | See status description below                                                                          |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| queue_id |               | Id of the queue, the name of the queue can be found in table ``stat_queue``, using this name          |
|          |               | queue details can be found in table ``queuefeatures``                                                 |
+----------+---------------+-------------------------------------------------------------------------------------------------------+
| agent_id |               | Id of the agent, the agent name can be found in table ``stat_agent``, using this name                 |
|          |               | agent details can be found in table ``agentfeatures`` using the number in the second part of the name |
|          |               | Exemple : Agent/1002 is agent with number 1002 in table ``agentfeatures``                             |
+----------+---------------+-------------------------------------------------------------------------------------------------------+

Queue Call Status
-----------------
+-----------------+--------------------------------------------------------------------------------------------------------+
| Status          | Description                                                                                            |
|                 |                                                                                                        |
+=================+========================================================================================================+
| full            | Call was not queued because queue was full, happens when the number of calls                           |
|                 | is greater than the maximum number of calls allowed to wait                                            |
+-----------------+--------------------------------------------------------------------------------------------------------+
| closed          | Closed due to the schedule applied to the queue                                                        |
+-----------------+--------------------------------------------------------------------------------------------------------+
| joinempty       | No agents were available in the queue to take the call (follows the join empty parameter of the queue) |
+-----------------+--------------------------------------------------------------------------------------------------------+
| leaveempty      | No agents available while the call was waiting in the qeuue                                            |
+-----------------+--------------------------------------------------------------------------------------------------------+
| divert_ca_ratio | Call diverted because the ratio number of agent number of calls waiting configured was exceeded        |
+-----------------+--------------------------------------------------------------------------------------------------------+
| divert_waittime | Call diverted because the maximum expected waiting time configured was exceeded                        |
+-----------------+--------------------------------------------------------------------------------------------------------+
| answered        | Call was answered                                                                                      |
+-----------------+--------------------------------------------------------------------------------------------------------+
| abandoned       | Call hangup by the caller                                                                              |
+-----------------+--------------------------------------------------------------------------------------------------------+
| timeout         | Call stayed longer than the maximum time allowed in queue parameter                                    |
+-----------------+--------------------------------------------------------------------------------------------------------+

stat_queue_periodic Table
-------------------------

This table is an aggregation of the table
+-----------------+------------------------------------------------------+
| Field           | Description                                          |
|                 |                                                      |
+=================+======================================================+
| id              | Generated id                                         |
+-----------------+------------------------------------------------------+
| time            | time period, all counters are aggregated for an hour |
+-----------------+------------------------------------------------------+
| answered        | Number of answered calls during the time period      |
+-----------------+------------------------------------------------------+
| abandoned       | Number of abandoned calls su                         |
+-----------------+------------------------------------------------------+
| total           |                                                      |
+-----------------+------------------------------------------------------+
| full            |                                                      |
+-----------------+------------------------------------------------------+
| closed          |                                                      |
+-----------------+------------------------------------------------------+
| joinempty       |                                                      |
+-----------------+------------------------------------------------------+
| leaveempty      |                                                      |
+-----------------+------------------------------------------------------+
| divert_ca_ratio |                                                      |
+-----------------+------------------------------------------------------+
| divert_waittime |                                                      |
+-----------------+------------------------------------------------------+
| timeout         |                                                      |
+-----------------+------------------------------------------------------+
| queue_id        |                                                      |
+-----------------+------------------------------------------------------+

