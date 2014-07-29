.. _agent-queue-association:

***********************
Agent Queue Association
***********************

.. warning:: This service is experimental

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


Get an Agent - Queue association
================================

Query
-----

::

    GET /1.1/queues/<queue_id>/memberships/agents/<agent_id>


Errors
------

+------------+---------------------------------------------------------------------+-------------+
| Error code | Error message                                                       | Description |
+============+=====================================================================+=============+
| 404        | Queue with id=<queue_id> is not associated with agent id=<agent_id> |             |
+------------+---------------------------------------------------------------------+-------------+
| 404        | Queue with id=<queue_id> does not exist                             |             |
+------------+---------------------------------------------------------------------+-------------+


Example request
---------------

::

    GET /1.1/queues/3/memberships/agents/18
    Host: xivoserver


Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "agent_id": 18,
        "queue_id": 3,
        "penalty": 5
    }


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
| 404        | Queue with id=<queue_id> is not associated with agent id=<agent_id> |             |
+------------+---------------------------------------------------------------------+-------------+
| 404        | Queue with id=<queue_id> does not exist                             |             |
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

    HTTP/1.1 204 OK
