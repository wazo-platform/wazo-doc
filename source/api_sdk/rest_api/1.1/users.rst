*****
Users
*****

.. TODO should either document the user-line association model (i.e. a line's main
   user vs secondary user and related constraint) or add a link to where this is
   documented

User Representation
===================

**Description**

+-----------+---------+-----------------------------------------------------------------------------------------------------------------------+
| Field     | Values  | Description                                                                                                           |
+===========+=========+=======================================================================================================================+
| id        | int     | Read-only                                                                                                             |
+-----------+---------+-----------------------------------------------------------------------------------------------------------------------+
| firstname | string  | If the user has no firstname, then this field is an empty string.                                                     |
+-----------+---------+-----------------------------------------------------------------------------------------------------------------------+
| lastname  | string  | If the user has no lastname, then this field is an empty string.                                                      |
+-----------+---------+-----------------------------------------------------------------------------------------------------------------------+
| userfield | boolean | A custom field which purpose is left to the client. If the user has no userfield, then this field is an empty string. |
+-----------+---------+-----------------------------------------------------------------------------------------------------------------------+

**Example**::

   {
       "id": 1,
       "firstname": "John",
       "lastname": "Doe",
       "userfield": ""
   }


List Users
==========

The users are listed in ascending order on lastname, then firstname.

::

   GET /1.1/users


**Parameters**

q
   List only users matching this filter.

   The filter is done on the firstname, lastname and firstname + lastname and is case insensitive.

   Example: ``q=john``

include
   A comma separated list of additional information to include for each user.

   By default, no additional information is included.

   Valid values: ``voicemail``.

   Example: ``include=voicemail``


.. warning:: filtering on the line number is not implemented yet

**Example request**::

   GET /1.1/users HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items":
       [
           {
               "id": 1,
               "firstname": "John",
               "lastname": "Doe",
               "userfield": ""
           },
           {
               "id": 2,
               "firstname": "Alice",
               "lastname": "Houet",
               "userfield": ""
           }
       ]
   }

Response if the query parameter ``include=voicemail`` is included::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items":
       [
           {
               "id": 1,
               "firstname": "John",
               "lastname": "Doe",
               "userfield": "",
               "voicemail": {
                  "voicemail_id": 3
               }
           },
           {
               "id": 2,
               "firstname": "Alice",
               "lastname": "Houet",
               "userfield": "",
               "voicemail": null
           }
       ]
   }


Get User
========

::

   GET /1.1/users/<id>

**Parameters**

include
   See `List Users`_.

**Example request**::

   GET /1.1/users/1 HTTP/1.1
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": 1
       "firstname": "John",
       "lastname": "Doe",
       "userfield": ""
   }


Create User
===========

::

   POST /1.1/users

**Input**

+-----------+----------+--------+
| Field     | Required | Values |
+===========+==========+========+
| firstname | yes      | string |
+-----------+----------+--------+
| lastname  | no       | string |
+-----------+----------+--------+
| userfield | no       | string |
+-----------+----------+--------+

**Example request**::

   POST /1.1/users HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
       "firstname": "John",
       "lastname": "Doe",
       "userfield": ""
   }

**Example response**::

   HTTP/1.1 201 Created
   Location: /1.1/users/1
   Content-Type: application/json

   {
       "id": 1
   }


Update User
===========

The update does not need to set all the fields of the edited user. The update only needs to set the modified fields.

If the firstname or the lastname is modified, the associated voicemail is also updated.

::

   PUT /1.1/users/<id>

**Example request**::

   PUT /1.1/users/67 HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

   {
       "firstname": "Jonathan"
   }

**Example response**::

   HTTP/1.1 204 No Content


Delete User
===========

Delete a user along with its line if he has one.
The user will also be removed from all queues, groups or other XiVO entities whom he is member.

::

   DELETE /1.1/users/<id>

**Errors**

+------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Error code | Error message                                                                               | Description                                                                                         |
+============+=============================================================================================+=====================================================================================================+
| 404        | empty                                                                                       | The requested user was not found                                                                    |
+------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| 412        | Cannot remove a user with a voicemail. Delete the voicemail or dissociate it from the user. | The user owns a voicemail, so it cannot be deleted unless you specify the deleteVoicemail parameter |
+------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| 500        | The user was deleted but the device could not be reconfigured.                              | provd returned an error when trying to reconfigure the user's device                                |
+------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| 500        | The user was deleted but the voicemail content could not be removed.                        | sysconfd returned an error when trying to delete the user's voicemail.                              |
+------------+---------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

**Example request**::

   DELETE /1.1/users/67 HTTP/1.1
   Host: xivoserver

**Example response**::

   HTTP/1.1 204 No Content


Get Lines Associated to User
============================

::

   GET /1.1/user_links/<userid>

**Example request**::

   GET /1.1/user_links/1/
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json
   Link: http://xivoserver/user_links/42

   {
       "total": 1,
       "items": [
           {
               "id": "83"
               "user_id": "42",
               "line_id": "42324",
               "extension_id": "2132",
               "main_user": true,
               "main_line": true,
               "links" : [
                   {
                       "rel": "users",
                       "href": "https://xivoserver/1.1/users/42"
                   },
                   {
                       "rel": "lines",
                       "href": "https://xivoserver/1.1/lines_sip/42324"
                   },
                   {
                       "rel": "extensions",
                       "href": "https://xivoserver/1.1/extensions/2132"
                   }
               ]
           }
       ]
   }

or, if no line is associated to the user::

   HTTP/1.1 404 Not Found


Associate Line to User
======================

Associate (or update) a line to a user.

Note that, on update, if the user is associated to a different line (i.e. different
line ID):

* the user old line is not deleted.
* the user old line must still be in a valid state, i.e. with 1 main user if
  the line has at least 1 secondary user, else an error is returned.

::

   POST /1.1/user_links

**Input**

+--------------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field        | Required | Values  | Description                                                                                                                                                                                                               |
+==============+==========+=========+===========================================================================================================================================================================================================================+
| user_id      | yes      | int     | Must be an existing id                                                                                                                                                                                                    |
+--------------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| line_id      | yes      | int     | Must be an existing id                                                                                                                                                                                                    |
+--------------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| extension_id | yes      | int     | Must be an existing id                                                                                                                                                                                                    |
+--------------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| main_user    | no       | boolean | May always be true, may not be false if the user has no line yet. If not given, the user will be the main user of the line if no other user is currently associated to the line. Else, the user will be a secondary user. |
+--------------+----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example request**::

   POST /1.1/user_links
   Host: xivoserver
   Content-Type: application/json

   {
       "user_id": "42",
       "line_id": "42324",
       "extension_id": "2132",
       "main_user": true
   }

**Example response**::

   HTTP/1.1 201 Created
   Location: /1.1/user_links/63
   Content-Type: application/json

   {
       "id": 63,
       "links" : [
           {
               "rel": "user_links",
               "href": "https://xivoserver/1.1/user_links/63"
           }
       ]
   }


Deassociate Line From User
==========================

If the user is the main user of the line and there is at least 1 secondary user associated to this line, an error is returned.

::

   DELETE /1.1/user_links/<user_link_id>

**Example request**::

   DELETE /1.1/user_links/42 HTTP/1.1
   Host: xivoserver

**Example response**::

   HTTP/1.1 204 No Content


Get Voicemail Associated to User
================================

::

   GET /1.1/users/<id>/voicemail

**Example request**::

   GET /1.1/users/1/voicemail
   Host: xivoserver
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json
   Link: http://xivoserver/voicemails/42

   {
       "id": 42,
       "links" : [
           {
               "rel": "voicemails",
               "href": "https://xivoserver/1.1/voicemails/42"
           }
       ]
   }

or, if no voicemail is associated to the user::

   HTTP/1.1 404 Not Found


Associate Voicemail to User
===========================

Associate (or update) a voicemail to a user.

Note that, on update, if the user is associated to a different voicemail (i.e.
different voicemail ID), the user old voicemail is not deleted.

::

   PUT /1.1/users/<id>/voicemail

**Example request**::

   POST /1.1/users/1/voicemail
   Host: xivoserver
   Content-Type: application/json

   {
       "id": 3
   }

**Example response**::

   HTTP/1.1 204 No Content


Deassociate Voicemail From User
===============================

Deassociate a voicemail from a user.

::

   DELETE /1.1/users/<id>/voicemail

**Parameters**

deleteVoicemail
   If present (whatever the value), the voicemail is also deleted.

**Example request**::

   DELETE /1.1/users/1/voicemail HTTP/1.1
   Host: xivoserver

**Example response**::

   HTTP/1.1 204 No Content
