.. _rest-api:

********
REST API
********

The XiVO REST API is the privileged way to programmatically interact with XiVO.

Reference
=========

.. toctree::
   :maxdepth: 1

   confd/api
   provd/api
   sysconfd/api

For other services, see http://api.xivo.io.


Configuration
=============

The REST API is available via HTTPS or HTTP on port offer by the daemon. Accessing to the REST API requires to create a
webservices user in the web interface (Configuration/Management/Web Services Access):

* if an IP address is specified for the user, no authentication is needed
* if you choose not to specify an IP address for the user, you can connect to the REST API with a HTTP Digest authentication, using the user name and password you provided.
  For instance, the following command line allows to retrieve XiVO users through the REST API, using the login **admin** and the password **passadmin**::

     curl --digest --insecure --cookie '' -H 'Accept: application/json' -u admin:passadmin https://<xivo_address>:9486/1.1/users

The REST API is also available on the loopback interface via HTTP on port 9487, with no
authentication needed.


HTTP status codes
=================

Standard HTTP status codes are used. For the full definition see `IANA definition`__.

__ http://www.iana.org/assignments/http-status-codes/http-status-codes.xml

* 200: Success
* 201: Created
* 400: Incorrect syntax
* 404: Resource not found
* 406: Not acceptable
* 412: Precondition failed
* 415: Unsupported media type
* 500: Internal server error


General URL parameters
======================

All URL's starts by /1.1/, 1.1 is the current protocol version.

Example usage of general parameters::

   GET http://127.0.0.1:9487/1.1/voicemails?limit=X&skip=Y

Parameters
----------


order
   Sort the list using a column (e.g. "number"). See specific resource documentation for columns allowed.

direction
    'asc' or 'desc'. Sort list in ascending (asc) or descending (desc) order

limit
    total number of resources to show in the list. Must be a positive integer

skip
    number of resources to skip over before starting the list. Must be a positive integer

search
    Search resources. Only resources with a field containing the search term
    will be listed.


Data representation
===================

Data retrieved from the REST server
-----------------------------------

JSON is used to encode returned or sent data. Therefore, the following headers are needed:

* when the request is supposed to return JSON:
   Accept = application/json
* when the request's body contains JSON:
   Content-Type = application/json

.. note:: Optional properties can be added without changing the protocol version in the main list or in the object list itself.
          Properties will not be removed, type and name will not be modified.


Getting object lists
^^^^^^^^^^^^^^^^^^^^

``GET /1.1/objects``

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
                "id": "1",
                "prop1": "test"
            },
            {
                "id": "2",
                "prop1": "ssd"
            }
        ]
    }


Getting An Object
^^^^^^^^^^^^^^^^^

Format returned is a list of properties. The object should always have the same attributes set, the
default value being the equivalent to NULL in the content-type format.

``GET /1.1/objects/<id>``

``Response data format``

.. code-block:: javascript

    {
       "id": "1",
       "prop1": "test"
    }


Data sent to the REST server
----------------------------

The XiVO REST server implements POST and PUT methods for item creation and update respectively.
Data is created using the POST method via a root URL and is updated using the PUT method via a root
URL suffixed by /<id. The server expects to receive JSON encoded data. Only one item can be
processed per request. The data format and required data fields are illustrated in the following
example:

``Request data format``

.. code-block:: javascript

    {
       "id": "1",
       "prop1": "test"
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
