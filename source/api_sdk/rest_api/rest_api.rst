.. _rest-api:

********
REST API
********

XiVO proposes a growing number of REST web services.

In the future, these services will replace existing
:ref:`web services <web-services-api>`. The current version is version 1.


Configuration
=============

REST web services are :

* Available on the XiVO loopback network interface on port TCP/50050.
* Available on https on port TCP/50051, authentication is configured using web service configuration menu using XiVO administration interface.

How to use this page
====================

This page lists the REST Web Services available in XiVO. Their usage is described in the unit-tests
(see the section below) and some details are given on this page. Data can be retrieved via the HTTP GET
method and must be sent via POST or PUT methods. Data in encoded in JSON format.


Where do I find Web Services usage examples?
--------------------------------------------

Listing data here would be inefficient, as this documentation cannot be always up-to-date. So we're
moving it out of the documentation.

Instead, we will use unit-tests as documentation. We are developping a Python library to access Web
Services. An alpha version is available in the following file :file:`xivo-restapi/acceptance/features/ws_utils.py`

This page will be updated together with the library.

``xivo-restapi`` source code is available in the ``xivo-restapi``
`Git repository on git.xivo.fr <http://git.xivo.fr/?p=official/xivo-restapi.git;a=summary>`_.

If you want information about the users Web Services, for example, have a look at the following file
:file:`xivo_restapi/rest/tests/test_API_campaigns.py`
(`online version <http://git.xivo.fr/?p=official/xivo-restapi.git;a=blob;f=xivo-restapi/xivo_restapi/services/tests/test_campagne_management.py;h=9e468e3552c91fabd89e5c03434293009e8785bd;hb=HEAD>`_).


HTTP status codes
=================

Standard HTTP status codes are used. For the full definition see `IANA definition`__.

__ http://www.iana.org/assignments/http-status-codes/http-status-codes.xml

* 200: Success
* 201: Created
* 400: Incorrect syntax (only for requests to add)
* 404: Resource not found (for queries only view and delete)
* 412: Precondition failed
* 500: Internal server error


General URL parameters
======================

All URL's starts by /rest/1.0/, 1.0 is the current protocol version.

Pagination::

   GET http://127.0.0.1:50050/rest/IPBX/users/?_page=X&_pagesize=Y

Parameters:
 * _page - page number (items from X \* _page to (X+1) \* _pagesize)
 * _pagesize - number of items per page


Data representation
===================

Data retrieved from the REST server
-----------------------------------

JSON is used to encode returned data. The format is as follows:
 * total - number of returned items in total
 * items - returned data

``Response data format``

.. code-block:: javascript

    {
        "total": 2,
        "items":
        [
            {
                "id": "1"
                "campaign_name": "test1",
                "start_date": "2013-01-22 14:53:33",
                "end_date": "2013-01-22 17:53:36",
                "queue_id": "1",
                "queue_number": "6001",
                "queue_display_name": "welcome",
                "queue_name": "welcome",
                "activated": "True",
                "base_filename": "test1-file-",
            },
            {
                "id": "2"
                "campaign_name": "ssd",
                "start_date": "2013-01-15 14:54:45",
                "end_date": "2013-01-24 00:00:00",
                "queue_id": "2",
                "queue_number": "6002",
                "queue_name": "accueil",
                "queue_display_name": "accueil",
                "activated": "True",
                "base_filename": "ssd-file-",
            }
        ]
    }


Data sent to the REST server
----------------------------

The XiVO REST server implements POST and PUT methods for item creation and update respectively. The PUT method
is not implemented systematically, please be sure to verify the documentation when in doubt. Data created using the POST method
is done via root URL and updates using the PUT method via root URL suffixed by /<id>/. The servers expected to receive JSON encoded data. Only one item can be processed per request. The data format and required data fields are illustrated in the following example:

``Request data format``

.. code-block:: javascript

    {
        "id": "1"
        "campaign_name": "new_campaign",
        "start_date": "2013-01-22 14:53:33",
        "end_date": "2013-01-22 17:53:36",
        "queue_id": "1",
        "activated": "True",
        "base_filename": "new_campaign-file-",
    }

When updating, only the id and updated members are needed, omitted members are left intact.


IPBX
====

Users
-----
Users are XiVO objects using phone sets, users can associated with lines, can be in groups or can have phone keys.

+--------+-------------------+-----------------------------------------------+
| Method | Ressource         | Description                                   |
+========+===================+===============================================+
| GET    | :ref:`ipbx-users` | Return a list of XiVO users, can be paginated |
+--------+-------------------+-----------------------------------------------+

.. _ipbx-users:

GET /IPBX/users/
----------------

Return a list of xivo users

