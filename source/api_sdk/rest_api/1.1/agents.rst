******
Agents
******

Agent Representation
====================

**Description**

id
   *read-only* **integer**

firstname
   **string**

   If the agent has no firstname, then this field is an empty string.

lastname
   **string**

   If the agent has no lastname, then this field is an empty string.

number
   *read-only* **string**

   A number uniquely identifying the agent.

password
   **string**

   The password the agent needs to enter when login in/login out via a phone.

   If the agent has no password, then this field is an empty string.

**Example**::

   {
       "id": 1,
       "firstname": "John",
       "lastname": "G.",
       "number": "101",
       "password": ""
   }


List Agents
===========

List all agents.

::

   GET /1.1/agents

**Example request**::

   GET /1.1/agents HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items": [
           {
               "id": 1,
               "firstname": "John",
               "lastname": "G.",
               "number": "101",
               "password": "",
           },
           {
               "id": 2,
               "firstname": "Alice",
               "lastname": "Houet",
               "number": "102",
               "password": ""
           }
       ]
   }
