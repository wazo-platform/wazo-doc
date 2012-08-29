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

  'full',
  'closed',
  'joinempty',
  'leaveempty',
  'divert_ca_ratio',
  'divert_waittime',
  'answered',
  'abandoned',
  'timeout'


