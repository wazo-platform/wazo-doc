******
Agents
******

.. _agent_properties:

Agent properties
================

.. code-block:: javascript

   {
      "id": 19,
      "autologoff": 0,
      "group": null,
      "language": "",
      "firstname": "Chuck",
      "passwd": "",
      "lastname": "N",
      "number": "2123",
      "context": "default",
      "numgroup": 1,
      "preprocess_subroutine": null,
      "description": ""
   }


.. _list-agents:

List Agents
===========

List all agents.

::

   GET /1.0/CallCenter/agents/

**Parameters**

* None

**Example request**::

   GET /1.0/CallCenter/agents/ HTTP/1.1
   Host: xivoserver:50051
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   [
      {
         "id": 19,
         "autologoff": 0,
         ...
      },
      {
         "id": 20,
         "autologoff": 0,
         ...
      }
   ]
