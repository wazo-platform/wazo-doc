*************
Function Keys
*************

Service for configuring what a function key will do when pressed. A function
key can accomplish different actions depending on their type and destination.

This service does not add a function key to a device. Consult
the documentation on function key templates for further details.

.. warning:: The function key template service has not been implemented yet


Function Key Representation
===========================

Description
-----------

+----------------+---------+-------------------------------------------------------------------+
| Field          | Values  | Description                                                       |
+================+=========+===================================================================+
| id             | integer | (Read-only)                                                       |
+----------------+---------+-------------------------------------------------------------------+
| type           | string  | See `Function Key Types`_ for more details                        |
+----------------+---------+-------------------------------------------------------------------+
| destination    | string  | See `Function Key destinations for speed dials`_ for more details |
+----------------+---------+-------------------------------------------------------------------+
| destination_id | integer | See `Function Key destinations for speed dials`_ for more details |
+----------------+---------+-------------------------------------------------------------------+


Example
-------

::

   {
       "id": "1",
       "type": "speeddial",
       "destination": "user",
       "destination_id": 34,
       "links": [
            {
                "rel": "func_keys",
                "href: "https://xivoserver/1.1/func_keys/1"
            }
        ]
    }


Function Key Types
------------------

A type determines what kind of action a function key can accomplish.
Here is a list of available types and what action they trigger:

speeddial
    Call another extension. (e.g. a user, a queue, a group, etc).

transfer
    Transfer the current call to another extension.

dtmf
    Emit a dial tone, as if you pressed a number on the dialpad (e.g. 3, 5, 6).

line
    Key for accessing the phone's line (i.e. emit or answer calls by pressing on the key).

directory
    Search for a contact in the phone directory.

park
    Park the current call in a parking lot.

dnd
    Activate Do-Not-Disturb on the phone.

app_services
    Start a custom application on the phone.


Function Key destinations for speed dials
-----------------------------------------

A destination determines the number to dial when using 'speeddial' function
keys. Destinations are configured by specifying the type of destination and its
id.  Destinations are pre-generated every time a new resource is created. In
other words, a new destination will appear in the `List of Function Key
Destinations`_ every time a user, group, queue, etc is created. Therefore,
function keys do not need to be created manually. However, there is an
exception to this rule: Function keys of type 'custom' cannot be pre-generated
because the user must manually enter the number to dial.


Here is a list of available destination types:

user
    A User

group
    Conference group

queue
    Calling queue

conference
    Conference room

custom
    A custom number to dial, defined by the user

bs_filter
    Boss/Secretary filter

service
    A predefined user service [1]_.

paging
    Paging


.. [1] List of currently supported services:

        - Phone Status (phonestatus)
        - Sound Recording (recsnd)
        - Call recording (callrecord)
        - Incoming call filtering (incallfilter)
        - Do not disturbe (enablednd)
        - Group Interception (pickup)
        - Listen to online calls (calllistening)
        - Directory access (directoryaccess)
        - Disable all forwaring (fwdundoall)
        - Enable Voicemail (enablevm)
        - Reach the Voicemail (vmusermsg)
        - Delete messages from voicemail (vmuserpurge)


Example
~~~~~~~

To configure a function key that would dial the extension of user "Bob" (who has the id 12), you
would have a "destination" of type "user" with the "destination_id" 12.

Here is an example of the JSON representation for this user::

    {
        "type": "speeddial",
        "destination": "user",
        "destination_id": 12
    }


List of Function Key Destinations
=================================

Query
-----

::

    GET /1.1/func_keys


Parameters
----------


order
   Sort the list using a column (e.g. "destination"). Columns allowed: type, destination

direction
    'asc' or 'desc'. Sort list in ascending (asc) or descending (desc) order

limit
    total number of function keys to show in the list. Must be a positive integer

skip
    number of function keys to skip over before starting the list. Must be a positive integer

search
    Search function keys. Only function keys with a field containing the search term
    will be listed.

Errors
------

+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| Error code | Error message                                                        | Description                                                              |
+============+======================================================================+==========================================================================+
| 400        | Invalid parameters: limit must be a positive number                  | the 'limit' parameter must be a number                                   |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: skip must be a positive number                   | the 'skip' parameter must be a number                                    |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: ordering parameter '<field>' does not exist      | you must use one of the fields available in a device when sorting a list |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: direction parameter '<direction>' does not exist | use either 'asc' or 'desc' as a direction when sorting a list            |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+


Example requests
----------------

List all available function key destinations::

    GET /1.1/func_keys HTTP/1.1
    Host: xivoserver
    Accept: application/json

List function key destinations, sort by destination in descending order::

    GET /1.1/func_keys?order=destination&direction=desc
    Host: xivoserver
    Accept: application/json

List only the first 10 function key destinations containing the word "user"::

    GET /1.1/func_keys?search=user&limit=10
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items": [
            {
                "id": "1",
                "type": "speeddial",
                "destination": "user",
                "destination_id": 12,
                "links": [
                    {
                        "rel": "func_keys",
                        "href: "https://xivoserver/1.1/func_keys/1"
                    }
                ]
            },
            {
                "id": "2",
                "type": "transfer",
                "destination": "queue",
                "destination_id": 24,
                "links": [
                    {
                        "rel": "func_keys",
                        "href: "https://xivoserver/1.1/func_keys/2"
                    }
                ]
            }
        ]
    }


Get a Function Key Destination
==============================


Query
-----

::

    GET /1.1/func_keys/<id>

Example request
---------------

::

    GET /1.1/func_keys/1 HTTP/1.1
    Host: xivoserver
    Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

    {
        "id": "1",
        "type": "speeddial",
        "destination": "user",
        "destination_id": 12,
        "links": [
            {
                "rel": "func_keys",
                "href: "https://xivoserver/1.1/func_keys/2"
            }
        ]
    }


Create a Function Key Destination
=================================

Most function keys are automatically generated upon the creation of a
desintation resource ( See `Function Key destinations for speed dials`_ for further details).
This action is for creating function keys that cannot be pre-generated (i.e.
custom speed dials and other types of function keys)

.. warning:: Not implemented yet



Query
-----

::

    POST /1.1/func_keys

Input
-----

+----------------+----------+---------+-------------------------------------------------------------------+
| Field          | Required | Values  | Notes                                                             |
+================+==========+=========+===================================================================+
| type           | yes      | string  | See `Function Key Types`_ for more details                        |
+----------------+----------+---------+-------------------------------------------------------------------+
| destination    | yes      | string  | See `Function Key destinations for speed dials`_ for more details |
+----------------+----------+---------+-------------------------------------------------------------------+
| destination_id | yes      | integer | destination's id                                                  |
+----------------+----------+---------+-------------------------------------------------------------------+


Errors
------

+------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Error code | Error message                                                 | Description                                                                                    |
+============+===============================================================+================================================================================================+
| 500        | Error while creating Function Key: <explanation>              | See explanation for more details.                                                              |
+------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| 400        | Missing parameters: <list of missing fields>                  |                                                                                                |
+------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| 400        | Invalid parameters: type <type> does not exist                | Please use one of the function key types listed in `Function Key Types`_                       |
+------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| 400        | Invalid parameters: destination of type <type> does not exist | Please use one of the destination types listed in `Function Key destinations for speed dials`_ |
+------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| 400        | Nonexistent parameters : <destination> <id> does not exist    | The destination you are trying to associate with does not exist                                |
+------------+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+

Example request
---------------

::

   POST /1.1/func_keys HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
        "type": "speeddial",
        "destination": "user",
        "destination_id": 12
   }

Example response
----------------

::

   HTTP/1.1 201 Created
   Location: /1.1/func_keys/1
   Content-Type: application/json

   {
        "id": "1",
        "type": "speeddial",
        "destination": "user",
        "destination_id": 12
        "links": [
            {
                "rel": "func_keys",
                "href: "https://xivoserver/1.1/func_keys/1"
            }
        ]
   }


Delete a Function Key Destination
=================================

Most function keys are automatically removed upon the deletion of a desintation
resource ( See `Function Key destinations for speed dials`_ for further details). This action
is for deleting function keys that cannot be removed automatically (i.e.
custom speed dials and other types of function keys)

.. warning:: Not implemented yet

Errors
------


+------------+--------------------------------------------------+------------------------------------------------------------+
| Error code | Error message                                    | Description                                                |
+============+==================================================+============================================================+
| 400        | error while deleting Function Key: <explanation> | See error message for more details                         |
+------------+--------------------------------------------------+------------------------------------------------------------+
| 404        | Not found                                        | The requested function key was not found or does not exist |
+------------+--------------------------------------------------+------------------------------------------------------------+

Query
-----

::

   DELETE /1.1/func_keys/<id>

Example request
---------------

::

   DELETE /1.1/func_keys/1 HTTP/1.1
   Host: xivoserver

Example response
----------------

::

   HTTP/1.1 204 No Content

