.. _agent-queue-association:

***********************
Agent Queue Association
***********************

Service for associating an agent with a queue.


Association Representation
==========================

Description
-----------

+----------+-------+-------------------+
| Field    | Value | Description       |
+==========+=======+===================+
| agent_id | int   | Agent's ID        |
+----------+-------+-------------------+
| queue_id | int   | The Queue's id    |
+----------+-------+-------------------+
| penalty  | int   | The penalty value |
+----------+-------+-------------------+


Edit an Agent - Queue association
=================================

Query
-----

::

    PUT /1.1/queues/<queue_id>/memberships/agents/<agent_id>


Errors
------

+------------+---------------------------------------------------------------------+-------------+
| Error code | Error message                                                       | Description |
+============+=====================================================================+=============+
| 404        | Agent with id=<agent_id> is not associated with queue id=<queue_id> |             |
+------------+---------------------------------------------------------------------+-------------+
| 404        | Agent with id=<agent_id> does not exist                             |             |
+------------+---------------------------------------------------------------------+-------------+


Example request
---------------

::

    PUT /1.1/queues/3/memberships/agents/18
    Host: xivoserver
    Content-Type: application/json
    
    {
        "penalty": 5
    }
    

Example response
----------------

::

    HTTP/1.1 200 OK
    
    {
        "agent_id": 18,
        "queue_id": 3,
        "penalty": 5
    }
