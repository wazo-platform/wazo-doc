.. _agentd-api:

***************
XiVO Agentd API
***************

Call center in XiVO are managed by the xivo-agentd daemon. This service provides a public API that
can be used to query the directories that are configured on a XiVO.

.. warning:: The 0.1 API is currently in development. Major changes could still
   happen and new resources will be added over time.


Add agent to a queue
====================

Query
-----

::

    POST /0.1/add_to_queue

Parameters
----------

+----------+-------+----------------+
| Field    | Value | Description    |
+==========+=======+================+
| agent_id | int   | Agent's ID     |
+----------+-------+----------------+
| queue_id | int   | The Queue's id |
+----------+-------+----------------+


Example request
---------------

::

    PUT /1.1/add_to_queue
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


Remove an agent to a queue
==========================

Query
-----

::

    POST /0.1/remove_from_queue

Parameters
----------

+----------+-------+----------------+
| Field    | Value | Description    |
+==========+=======+================+
| agent_id | int   | Agent's ID     |
+----------+-------+----------------+
| queue_id | int   | The Queue's id |
+----------+-------+----------------+


Example request
---------------

::

    PUT /1.1/remove_from_queue
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


Login an agent with extension and context
=========================================

Query
-----

::

    POST /0.1/login_with_extension_context

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

    PUT /1.1/login_with_extension_context
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


Login an agent with number
==========================

Query
-----

::

    POST /0.1/login_with_number

Parameters
----------

+--------+--------+---------------------+
| Field  | Value  | Description         |
+========+========+=====================+
| number | string | Number of the agent |
+--------+--------+---------------------+


Example request
---------------

::

    PUT /1.1/login_with_number
    Host: xivoserver
    Content-Type: application/json
    
    {
        "number": "2312"
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


Logoff an agent with ID
=======================

Query
-----

::

    POST /0.1/logoff_with_id

Parameters
----------

+----------+-------+-------------+
| Field    | Value | Description |
+==========+=======+=============+
| agent_id | int   | Agent's ID  |
+----------+-------+-------------+


Example request
---------------

::

    PUT /1.1/logoff_with_id
    Host: xivoserver
    Content-Type: application/json
    
    {
        "agent_id": 2231
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
