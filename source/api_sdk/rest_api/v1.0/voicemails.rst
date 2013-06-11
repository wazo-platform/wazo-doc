**********
Voicemails
**********

Voicemail properties
====================

.. code-block:: javascript

    {
       "id": 1,
       "email": "john.doe@bar.com",
       "fullname":"John Doe",
       "mailbox": "123",
       "password": "123",
       "attach": 1,
       "skipcheckpass" : 0,
       "deleteaftersend" : 0
    }


.. _list-voicemails:

List Voicemails
===============

List all voicemails.

::

   GET /1.0/voicemails

**Parameters**

* None

**Example request**::

   GET /1.0/voicemails HTTP/1.1
   Host: xivoserver:50051
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items":
       [
           {
               "uniqueid": 1,
               "mailbox": "123",
               "password": "123",
               "email": "foo@bar.com"
           },
           {
               "uniqueid": 2,
               "mailbox": "456",
               "password": "456",
               "email": "xivo@avencall.com"
           }
       ]
   }


.. _update-voicemail:

Update Voicemail
================

Update a voicemail.


::

   PUT /1.0/voicemails/<id>

**Parameters**

* None

**Errors**

+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| Error code | Error message                                     | Description                                                                           |
+============+===================================================+=======================================================================================+
| 404        | empty                                             | The requested voicemail was not found                                                 |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| 400        | Incorrect parameters sent: parameter1, parameter2 | The request body contained incorrect parameters. The incorrect parameters are listed. |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+

**Example request**::

   PUT /1.0/voicemails/37 HTTP/1.1
   Host: xivoserver:50051
   Content-Type: application/json

   {
     "password": "7895",
     "email": "xivo@avencall.com"
   }

**Example response**::

   HTTP/1.1 200 OK
