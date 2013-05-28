.. _rest-api:

********
REST API
********

XiVO proposes a growing number of REST web services.

In the future, these services will replace existing
:ref:`web services <web-services-api>`. The current version is version 1.0


Configuration
=============

REST web services are :

* Available on the XiVO loopback network interface on port TCP/50050.
* Available on https on port TCP/50051, authentication is configured using web service configuration menu using XiVO administration interface.

How to use this page
====================

This page lists the REST Web Services available in XiVO.
Data is retrieved via the HTTP GET method, created using POST, updated using PUT and deleted using DELETE method.
Data is encoded in JSON format.


HTTP status codes
=================

Standard HTTP status codes are used. For the full definition see `IANA definition`__.

__ http://www.iana.org/assignments/http-status-codes/http-status-codes.xml

* 200: Success
* 201: Created
* 400: Incorrect syntax (only for requests to add)
* 404: Resource not found (for queries only view and delete)
* 406: Not acceptable
* 412: Precondition failed
* 415: Unsupported media type
* 500: Internal server error


General URL parameters
======================

All URL's starts by /1.0/, 1.0 is the current protocol version.

Pagination::

   GET http://127.0.0.1:50050/1.0/users/?_page=X&_pagesize=Y

Parameters:
 * _page - page number (items from X \* _page to (X+1) \* _pagesize)
 * _pagesize - number of items per page


..    note:: Parameters starting by an _ means that it is not relevant to the data definition, but used 
             to control how objects are sent back from the server to the client.

Data representation
===================

Data retrieved from the REST server
-----------------------------------

JSON is used to encode returned or sent data. Therefore, the following headers are needed:

* when the request is supposed to return JSON:
   Accept = application/json
* when the request's body contains JSON:
   Content-Type = application/json

..   note:: Optional properties can be added without changing the protocol version in the main list or in the object list itself. 
            Properties will not be removed, type and name will not be modified.

Getting object lists
^^^^^^^^^^^^^^^^^^^^
``GET /1.0/objects/``

When returning lists the format is as follows:
 * total - number of items in total in the system configuration (optional)
 * items - returned data as an array of object properties list.

Other optional properties can be added later.

``Response data format``

.. code-block:: javascript

    {
        "total": 2,
        "items":
        [
            {
                "id": "1"
                "prop1": "test",
                .......
            },
            {
                "id": "2"
                "prop1": "ssd",
                ......
            }
        ]
    }

Getting An Object
^^^^^^^^^^^^^^^^^
Format returned is a list of properties.

``GET /1.0/objects/<id>/``

``Response data format``

.. code-block:: javascript

    {
       "id": "1"
       "prop1": "test",
       .......
    }



Data sent to the REST server
----------------------------

The XiVO REST server implements POST and PUT methods for item creation and update respectively.
Data is created using the POST method via a root URL and is
updated using the PUT method via a root URL suffixed by /<id>/.
The server expects to receive JSON encoded data.
Only one item can be processed per request. The data format and required data fields are illustrated in the following example:

``Request data format``

.. code-block:: javascript

    {
       "id": "1"
       "prop1": "test",
       .......
     }

When updating, only the id and updated properties are needed, omitted properties are not updated.
Some properties can also be optional when creating an object.

Errors
------

A request to the web services may return an error. An error will always be associated to an
HTTP error code, and eventually to one or more error messages. The following errors are common to all web services:

+------------+----------------+-------------------------------------------------------------------------------------------------------------+
| Error code | Error message  | Description                                                                                                 |
+============+================+=============================================================================================================+
| 406        | empty          | Accept header missing or contains an unsupported content type                                               |
+------------+----------------+-------------------------------------------------------------------------------------------------------------+
| 415        | empty          | Content-Type header missing or contains an unsupported content type                                         |
+------------+----------------+-------------------------------------------------------------------------------------------------------------+
| 500        | list of errors | An error occured on the server side; the content of the message depends of the type of errors which occured |
+------------+----------------+-------------------------------------------------------------------------------------------------------------+

The 400, 404 and 412 errors depend on the web service you are requesting. They are separately described for each of them.

The error messages are contained in a JSON list, even if there is only one error message:

.. code-block:: javascript

   [ message_1, message_2, ... ]


XiVO
====

Agents
------
An agent is responsible for answering calls on one or several queues.

+--------+--------------------+---------------------------------+
| Method | Ressource          | Description                     |
+========+====================+=================================+
| GET    | :ref:`list-agents` | Return a list of all the agents |
+--------+--------------------+---------------------------------+

.. _agent_properties:

Agent properties
^^^^^^^^^^^^^^^^

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

GET /1.0/CallCenter/agents/
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return a list all the agents :

**Parameters**

* None

**Request**

::

 GET /1.0/CallCenter/agents/
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

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


Users
-----
Users are XiVO objects using phone sets, users can associated with lines, can be in groups or can have phone keys.

+--------+--------------------+-----------------------------+
| Method | Ressource          | Description                 |
+========+====================+=============================+
| GET    | :ref:`list-users`  | Return a list of XiVO users |
+--------+--------------------+-----------------------------+
| GET    | :ref:`get-user`    | Return a specific XiVO user |
+--------+--------------------+-----------------------------+
| POST   | :ref:`create-user` | Create a XiVO user          |
+--------+--------------------+-----------------------------+
| PUT    | :ref:`update-user` | Update a XiVO user          |
+--------+--------------------+-----------------------------+


.. _user-properties:

User properties
^^^^^^^^^^^^^^^

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

If the user does not have a line, the "line" property is not displayed.

.. _list-users:

GET /1.0/users/
^^^^^^^^^^^^^^^
Return a list of xivo users :

**Parameters**

* None

**Request** :

``GET https://xivoserver:50051/1.0/users/``

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
        "total": 2,
        "items":
        [
            {
                "id": "1",
                "firstname": "John",
                "lastname": "Doe",
            },
            {
                "id": "2",
                "firstname": "Alice",
                "lastname": "Houet",
            }
        ]
    }


.. _get-user:

GET /1.0/users/<id>
^^^^^^^^^^^^^^^^^^^
Return a specific user

**Parameters**

* None

**Request**

::

 GET /1.0/users/1 HTTP/1.1
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
      "id": "1"
      "firstname": "John",
      "lastname": "Doe",
      ................
    }

See :ref:`user-properties` for other properties.

**Errors**

+------------+---------------+----------------------------------+
| Error code | Error message | Description                      |
+============+===============+==================================+
| 404        | empty         | The requested user was not found |
+------------+---------------+----------------------------------+


.. _create-user:

POST /1.0/users/
^^^^^^^^^^^^^^^^
Create a user

**Parameters**

* None

**Request**

:::::::::::

 POST /1.0/users/ HTTP/1.1
 Host : xivoserver:50051
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
      "firstname": "John",
      "lastname": "Doe",
      ................
    }

See :ref:`user-properties` for other properties.


**Response**

::::::::::::

 HTTP/1.1 201 Created
 Location: https://xivoserver:50051/1.0/users/38

**Errors**

+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| Error code | Error message                                     | Description                                                                           |
+============+===================================================+=======================================================================================+
| 400        | Incorrect parameters sent: parameter1, parameter2 | The request body contained incorrect parameters. The incorrect parameters are listed. |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+

.. _update-user:

PUT /1.0/users/<id>
^^^^^^^^^^^^^^^^^^^
Update a user. If the firstname or the lastname is modified, the associated voicemail will be modified.

**Parameters**

* None

**Request**

::

 PUT /1.0/users/67 HTTP/1.1
 Host : xivoserver:50051
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
      "email": "John@amaryt.com",
      "voicemailid": 17
    }

**Response**

::

 HTTP/1.1 200 OK
 Location: https://xivoserver:50051/1.0/users/67

**Errors**

+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| Error code | Error message                                     | Description                                                                           |
+============+===================================================+=======================================================================================+
| 404        | empty                                             | The requested user was not found                                                      |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| 400        | Incorrect parameters sent: parameter1, parameter2 | The request body contained incorrect parameters. The incorrect parameters are listed. |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+

Voicemails
----------

Voicemails are XiVO objects with several properties such as a phone number, a e-mail, etc...

+--------+-------------------------+-----------------------------+
| Method | Ressource               | Description                 |
+========+=========================+=============================+
| GET    | :ref:`list-voicemails`  | Return a list of voicemails |
+--------+-------------------------+-----------------------------+
| PUT    | :ref:`update-voicemail` | Update a voicemail          |
+--------+-------------------------+-----------------------------+

Voicemail properties
^^^^^^^^^^^^^^^^^^^^

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

GET /1.0/voicemails/
^^^^^^^^^^^^^^^^^^^^

Return a list of all voicemails :

**Parameters**

* None

**Request**

``GET https://xivoserver:50051/1.0/voicemails``

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

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

PUT /1.0/voicemails/<voicemailid>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a voicemail.

**Parameters**

* None

**Request**

::

 PUT /1.0/voicemails/37 HTTP/1.1
 Host : xivoserver:50051
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
      "password": "7895",
      "email": "xivo@avencall.com"
    }

**Response**

::

 HTTP/1.1 200 OK
 Location: https://xivoserver:50051/1.0/voicemails/37

**Errors**

+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| Error code | Error message                                     | Description                                                                           |
+============+===================================================+=======================================================================================+
| 404        | empty                                             | The requested voicemail was not found                                                 |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+
| 400        | Incorrect parameters sent: parameter1, parameter2 | The request body contained incorrect parameters. The incorrect parameters are listed. |
+------------+---------------------------------------------------+---------------------------------------------------------------------------------------+



Queues
------
A queue is an object on which calls are stored until they are answered by an agent.

+--------+--------------------+---------------------------------+
| Method | Ressource          | Description                     |
+========+====================+=================================+
| GET    | :ref:`list-queues` | Return a list of all the queues |
+--------+--------------------+---------------------------------+

.. _queue_properties:

Queue properties
^^^^^^^^^^^^^^^^

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

GET /1.0/CallCenter/queues/
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return a list all the queues :

**Parameters**


* None

**Request**

::

 POST /1.0/CallCenter/queues/
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    
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

Recording campaigns
-------------------
Recording campaigns aim at recording all the calls on a given queue for a given period of time.

+--------+------------------------+-----------------------------+
| Method | Ressource              | Description                 |
+========+========================+=============================+
| GET    | :ref:`list-campaigns`  | Return a list of campaigns  |
+--------+------------------------+-----------------------------+
| GET    | :ref:`get-campaign`    | Return a specific campaign  |
+--------+------------------------+-----------------------------+
| POST   | :ref:`create-campaign` | Create a recording campaign |
+--------+------------------------+-----------------------------+
| PUT    | :ref:`update-campaign` | Update a recording campaign |
+--------+------------------------+-----------------------------+
| DELETE | :ref:`delete-campaign` | Delete a recording campaign |
+--------+------------------------+-----------------------------+


.. _campaign-properties:

Recording Campaign properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

    {
        "id": "1",
        "campaign_name": "new_campaign",
        "start_date": "2013-01-22 14:53:33",
        "end_date": "2013-01-22 17:53:36",
        "queue_id": "1",
        "activated": "True",
        "base_filename": "new_campaign-file-"
    }


.. _list-campaigns:

GET /1.0/recording_campaigns/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return a list of recording campaigns :

**Parameters**

* campaign_name : filter on the campaign name
* queue_id : filter on the queue id
* queue_number : filter on the queue number
* running : the campaign must be currently active (current date must be between the start date and the end date)

**Request**

::

 GET /1.0/recording_campaigns/[?param1=val1[&param2=val2]]
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
        "total": 2,
        "items":
        [
            {
                 "id": "1"
                 "campaign_name": "campaign1",
                 ...
            },
            {
                 "id": "2"
                 "campaign_name": "campaign2",
                 ...
            }
        ]
    }

.. _get-campaign:

GET /1.0/recording_campaigns/<id>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return the recording campaign with the given id

**Parameters**

* None

**Request**

::

 GET /1.0/recording_campaigns/<id>
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
        "total": 1,
        "items":
        [
            {
                 "id": "1"
                 "campaign_name": "campaign1",
                 ...
            }
        ]
    }

.. _create-campaign:

POST /1.0/recording_campaigns/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a campaign and returns the generated id.

**Parameters**

* None

**Request**

::

 GET /1.0/recording_campaigns/<id>
 Host : xivoserver:50051
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
      "campaign_name": "my campaign",
      "queue_id": "2",
      ...
    }

**Response**

::

 HTTP/1.1 201 CREATED
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

   "1"

.. _update-campaign:

PUT /1.0/recording_campaigns/<id>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update the recording campaign with the given id.

**Parameters**

* None

**Request**

::

 PUT /1.0/recording_campaigns/<id>
 Host : xivoserver:50051
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
      "campaign_name": "my campaign",
      "queue_id": "2",
      ...
    }

**Response**

::

 HTTP/1.1 200 OK

.. _delete-campaign:

DELETE /1.0/recording_campaigns/<id>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete the recording campaign with the given id.

**Parameters**

* None

**Request**

::

 PUT /1.0/recording_campaigns/<id>
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK

Recordings
----------
A recording represents the sound file of a conversation in the scope of a recording campaign.

+--------+--------------------------+--------------------------------------------------+
| Method | Ressource                | Description                                      |
+========+==========================+==================================================+
| GET    | :ref:`list-recordings`   | Return a list of recordings for a given campaign |
+--------+--------------------------+--------------------------------------------------+
| GET    | :ref:`search-recordings` | Searches a recording with some specific criteria |
+--------+--------------------------+--------------------------------------------------+
| POST   | :ref:`create-recording`  | Creates a recording                              |
+--------+--------------------------+--------------------------------------------------+
| DELETE | :ref:`delete-recording`  | Delete a recording                               |
+--------+--------------------------+--------------------------------------------------+


.. _recording-properties:

Recording properties
^^^^^^^^^^^^^^^^^^^^

.. code-block:: javascript

    {
        "cid": "123.456",
        "start_time": "2013-01-22 14:53:33",
        "caller": "0231156897",
        "client_id": "abcd",
        "filename": "file.wav",


.. _list-recordings:

GET /1.0/recording_campaigns/<campaign_id>/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return a list of recordings for the given campaign:

**Parameters**

* None

**Request**

::

 GET /1.0/recording_campaigns/<campaign_id>/
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
        "total": 2,
        "items":
        [
            {
                 "cid": "123.456"
                 "campaign_id": 1,
                 ...
            },
            {
                 "cid": "456.789"
                 "campaign_id": 1,
                 ...
            }
        ]
    }

.. _search-recordings:

GET /1.0/recording_campaigns/<campaign_id>/search
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searches recordings in the given campaign whose fields "caller" or "agent_no" match the specified key:

**Parameters**

* None

**Request**

::

 GET /1.0/recording_campaigns/<campaign_id>/search/?key=<searched number>
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
        "total": 2,
        "items":
        [
            {
                 "cid": "123.456"
                 "campaign_id": 1,
                 ...
            },
            {
                 "cid": "456.789"
                 "campaign_id": 1,
                 ...
            }
        ]
    }

.. _create-recording:

POST /1.0/recording_campaigns/<campaign_id>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a recording in the given campaign. It is the responsibility of the caller to send a unique cid. However, it is advisable
to use the cid generated by Asterisk for the associated call.

**Parameters**

* None

**Request**

::

 POST /1.0/recording_campaigns/<campaign_id>/
 Host : xivoserver:50051
 Content-Type: application/json;charset=UTF-8

.. code-block:: javascript

    {
      "cid": "123.456"
      "campaign_id": 1,
      ...
    }

**Response**

::

 HTTP/1.1 201 CREATED

.. _delete-recording:

DELETE /1.0/recording_campaigns/<campaign_id>/<recording_cid>
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes the recording in the given campaign, with the given cid.

**Parameters**

* None

**Request**

::

 DELETE /1.0/recording_campaigns/<campaign_id>/<recording_cid>
 Host : xivoserver:50051

**Response**

::

 HTTP/1.1 200 OK
