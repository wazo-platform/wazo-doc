.. _agentd-api:

***************
XiVO agentd API
***************

Agent statuses in XiVO are managed by the xivo-agentd daemon. This service
provides a public API that can be used to query and update agent login and pause
statuses on a XiVO.

.. warning:: The 0.1 API is currently in development. Major changes could still
   happen and new resources will be added over time.


Add an Agent to a Queue
=======================

Query
-----

::

    POST /0.1/members


Parameters
----------

+----------+-------+-------------+
| Field    | Value | Description |
+==========+=======+=============+
| agent_id | int   | Agent's ID  |
+----------+-------+-------------+
| queue_id | int   | Queue's ID  |
+----------+-------+-------------+


Example request
---------------

::

    POST /0.1/members
    Host: xivoserver
    Content-Type: application/json

    {
        "agent_id": 5,
        "queue_id": 15
    }


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Remove an Agent from a Queue
============================

Query
-----

::

    DELETE /0.1/members


Parameters
----------

+----------+-------+-------------+
| Field    | Value | Description |
+==========+=======+=============+
| agent_id | int   | Agent's ID  |
+----------+-------+-------------+
| queue_id | int   | Queue's ID  |
+----------+-------+-------------+


Example request
---------------

::

    DELETE /0.1/members
    Host: xivoserver
    Content-Type: application/json

    {
        "agent_id": 5,
        "queue_id": 15
    }


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Login an Agent with Number to Extension and Context
===================================================

Query
-----

::

    POST /0.1/agents/by-number/<agent_number>/login


Parameters
----------

+-----------+--------+----------------------------+
| Field     | Value  | Description                |
+===========+========+============================+
| extension | string | Extension to log the agent |
+-----------+--------+----------------------------+
| context   | string | Context to log the agent   |
+-----------+--------+----------------------------+


Example request
---------------

::

    POST /0.1/agents/by-number/<agent_number>/login
    Host: xivoserver
    Content-Type: application/json

    {
        "extension": "2312",
        "context": "office-1"
    }


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Login an Agent with ID to Extension and Context
===============================================

Query
-----

::

    POST /0.1/agents/<agent_id>/login


Parameters
----------

+-----------+--------+----------------------------+
| Field     | Value  | Description                |
+===========+========+============================+
| extension | string | Extension to log the agent |
+-----------+--------+----------------------------+
| context   | string | Context to log the agent   |
+-----------+--------+----------------------------+


Example request
---------------

::

    POST /0.1/agents/<agent_id>/login
    Host: xivoserver
    Content-Type: application/json

    {
        "extension": "2312",
        "context": "office-1"
    }


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Relog All Agents
================

Query
-----

::

    POST /0.1/agents/all/relog


Example request
---------------

::

    POST /0.1/agents/all/relog
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Logoff an agent with ID
=======================

Query
-----

::

    POST /0.1/agents/<agent_id>/logoff


Example request
---------------

::

    POST /0.1/agents/<agent_id>/logoff
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Logoff an Agent with Number
===========================

Query
-----

::

    POST /0.1/agents/by-number/<agent_number>/logoff


Example request
---------------

::

    POST /0.1/agents/by-number/<agent_number>/logoff
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Logoff All Agents
=================

Query
-----

::

    POST /0.1/agents/all/logoff


Example request
---------------

::

    POST /0.1/agents/all/logoff
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Pause an agent with number
==========================

Query
-----

::

    POST /0.1/agents/by-number/<agent_number>/pause


Example request
---------------

::

    POST /0.1/agents/by-number/<agent_number>/pause
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Unpause an Agent with Number
============================

Query
-----

::

    POST /0.1/agents/by-number/<agent_number>/unpause


Example request
---------------

::

    POST /0.1/agents/by-number/<agent_number>/unpause
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 204 OK


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Get Agent Status with ID
========================

Query
-----

::

    GET /0.1/agents/<agent_id>/status


Example request
---------------

::

    GET /0.1/agents/<agent_id>/status
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
 
    {
      "id":  54,
      "number": "2312",
      "logged": True,
      "extension": "43563",
      "context": "office-1"
    }


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Get Agent Status with Number
============================

Query
-----

::

    GET /0.1/agents/by-number/<agent_number>/status


Example request
---------------

::

    GET /0.1/agents/by-number/<agent_number>/status
    Host: xivoserver
    Content-Type: application/json
    


Example response
----------------

::

    HTTP/1.1 200 OK
    
    {
      "id":  54,
      "number": "2312",
      "logged": True,
      "extension": "43563",
      "context": "office-1"
    }


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+


Get All Agent Statuses
======================

Query
-----

::

    GET /0.1/agents/all/statuses


Example request
---------------

::

    GET /0.1/agents/all/statuses
    Host: xivoserver
    Content-Type: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
    
    [
       {
         "id":  54,
         "number": "2312",
         "logged": True,
         "extension": "43563",
         "context": "office-1"
       },
    ]


Errors
------

+------------+---------------+-----------------------------+
| Error code | Error message | Description                 |
+============+===============+=============================+
| 404        | Not found     | The resource does not exist |
+------------+---------------+-----------------------------+
