******
Queues
******

.. _queue_properties:

Queue properties
================

.. code-block:: javascript

    {
        "id": 1,
        "name": "my_queue",
        "displayname": "My queue",
        "number": "2000",
        "context": "default",
        "data_quality": 0,
        "hitting_callee": 0,
        "hitting_caller": 0,
        "retries": 0,
        "ring": 0,
        "transfer_user": 0,
        "transfer_call": 0,
        "write_caller": 0,
        "write_calling": 0,
        "url": "",
        "announceoverride": "",
        "timeout": 0,
        "preprocess_subroutine": "test-subroutine",
        "announce_holdtime": 0,
        "waittime": 0,
        "waitratio": 0
    }


.. _list-queues:

List Queues
===========

List all queues.

::

   GET /1.0/CallCenter/queues/

**Parameters**

* None

**Example request**::

   GET /1.0/CallCenter/queues/ HTTP/1.1
   Host: xivoserver:50051
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   [
       {
           "id": 1,
           "name": "my_queue",
           ...
       },
       {
           "id": 2,
           "name": "your_queue",
           ...
       }
   ]
