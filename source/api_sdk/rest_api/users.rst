*****
Users
*****

.. _user-properties:

User properties
===============

.. code-block:: javascript

    {
       "id": 1,
       "firstname": "Jean",
       "lastname": "Dupond",
       "callerid": "Jean Dupond",
       "username": "1234",
       "password": "1234",
       "enableclient": 1,
       "musiconhold": "my_music",
       "outcallerid": "1234",
       "mobilephonenumber": "0611111111",
       "userfield": "",
       "timezone": "Europe/Paris",
       "language": "fr_FR",
       "description": "une description",
       "ctiprofileid: 1,
       "voicemailid": 1,
       "agentid": 1,
       "entityid": 1,
       "line": {
                  "number": "44500"
               }
    }

If the user does not have a line, the "line" property is set to null.


.. _list-users:

List Users
==========

List all users.

::

   GET /1.0/users/

**Parameters**

* None

**Example request**::

   GET /1.0/users/ HTTP/1.1
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
               "id": "1",
               "firstname": "John",
               "lastname": "Doe"
           },
           {
               "id": "2",
               "firstname": "Alice",
               "lastname": "Houet"
           }
       ]
   }


.. _get-user:

Get User
========

Return a specific user.

::

   GET /1.0/users/<id>

**Parameters**

* None

**Errors**

+------------+---------------+----------------------------------+
| Error code | Error message | Description                      |
+============+===============+==================================+
| 404        | empty         | The requested user was not found |
+------------+---------------+----------------------------------+

**Example request**::

   GET /1.0/users/1 HTTP/1.1
   Host: xivoserver:50051
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
     "id": "1"
     "firstname": "John",
     "lastname": "Doe",
     ................
   }

See :ref:`user-properties` for other properties.


.. _create-user:

Create User
===========

Create a new user.

::

   POST /1.0/users/

**Parameters**

* None

**Errors**

+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| Error code | Error message                                     | Description                                                                           |
+============+===================================================+=======================================================================================+
| 400        | Incorrect parameters sent: parameter1, parameter2 | The request body contained incorrect parameters. The incorrect parameters are listed. |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+

**Example request**::

   POST /1.0/users/ HTTP/1.1
   Host: xivoserver:50051
   Content-Type: application/json

   {
     "firstname": "John",
     "lastname": "Doe",
     ................
   }

See :ref:`user-properties` for other properties.

**Example response**::

   HTTP/1.1 201 Created


.. _update-user:

Update User
===========

Update a user. If the firstname or the lastname is modified, the associated voicemail will be modified.

::

   PUT /1.0/users/<id>

**Parameters**

* None

**Errors**

+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| Error code | Error message                                     | Description                                                                           |
+============+===================================================+=======================================================================================+
| 404        | empty                                             | The requested user was not found                                                      |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| 400        | Incorrect parameters sent: parameter1, parameter2 | The request body contained incorrect parameters. The incorrect parameters are listed. |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+

**Example request**::

   PUT /1.0/users/67 HTTP/1.1
   Host: xivoserver:50051
   Content-Type: application/json

   {
     "firstname": "John",
     "lastname": "Doe",
     ................
   }

**Example response**::

   HTTP/1.1 200 OK


.. _delete-user:

Delete User
===========

Delete a user along with its SIP line if he has one. This will be rejected if the user owns a voicemail, unless a parameter "deleteVoicemail" is specified.
The user will also be removed to all queues, groups or other XiVO entities whom he is member.

::

   DELETE /1.0/users/<id>

**Parameters**

* deleteVoicemail (no value, it just needs to be present or not)

**Errors**

+------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Error code | Error message                                                                               | Description                                                                                                                     |
+============+=============================================================================================+=================================================================================================================================+
| 404        | empty                                                                                       | The requested user was not found                                                                                                |
+------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| 412        | Cannot remove a user with a voicemail. Delete the voicemail or dissociate it from the user. | The user owns a voicemail, so it cannot be deleted unless you specify the deleteVoicemail parameter                             |
+------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| 500        | The user was deleted but the device could not be reconfigured.                              | provd returned an error when trying to reconfigure the user's device                                                            |
+------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| 500        | The user was deleted but the voicemail content could not be removed.                        | sysconfd returned an error when trying to delete the user's voicemail. This can only happen if "deleteVoicemail" was specified. |
+------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

**Example request**::

   DELETE /1.0/users/67 HTTP/1.1
   Host: xivoserver:50051

**Example response**::

   HTTP/1.1 200 OK
