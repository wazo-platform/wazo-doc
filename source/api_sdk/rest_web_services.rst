.. _rest-web-services-api:

*****************
REST Web Services
*****************

XiVO propose a growing number of REST web services. These are going to replace in the future actual 
:ref:`web services <web-services-api>`. Current version is a beta version accesible only via local loopback 
and shouldn't be used by user services. The data format is susceptible to revisions. Actual version is 
limited in proposed functions and there's no support of authentication nor authorisation. 


Configuration
=============

REST web services are actually available only on the XiVO loopback network interface using TCP/50050.
The configuration will be possible via the web interface later.


How to use this page
====================

This page lists REST Web Services available in XiVO. Usage is described by the unit-tests 
(see the section below) and some details are given on this page. This data can be retrieved via GET 
method and must be sent via POST or PUT methods, JSON format is used.


Where do I find Web Services usage examples?
--------------------------------------------

Listing data here would be inefficient, as this documentation can not be always up-to-date. So we're
moving it out of the documentation.

Instead, we will use unit-tests as documentation. We are developping a Python library to access Web
Services, an alpha version is available in the following file :file:`xivo_restapi/acceptance/features/ws_utils.py`

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
* 500: Internal server error


General URL parameters
======================

Pagination::

   GET http://127.0.0.1:50050/rest/IPBX/recording_campaigns/?_page=X&_pagesize=Y
   
Parameters:
 * _page - page number (items from X \* _page to (X+1) \* _pagesize) 
 * _pagesize - number of items per page


Data representation
===================

Data retrieved from the REST server
-----------------------------------

JSON is used to encode returned data. The format is as follows:
 * total - number of returned items in total
 * data - returned data

``Response data format``

.. code-block:: javascript

    {
		"total": 2, 
		"data": 
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
is not implemented systematically, please be sure to verify the documentation when in doubt. Data creation using POST method
is done via root URL and update using PUT method via root URL suffixed by /<id>/. JSON encoded data are awaited by the server, 
only one item can be processed by request. Data format and required data are represented in the following example:

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

Call recording
--------------

Campaigns
^^^^^^^^^

**List:**

* return all campaigns::

   GET http://127.0.0.1:50050/rest/IPBX/recording_campaigns/
   
* return restricted list of campaigns::

   GET http://127.0.0.1:50050/rest/IPBX/recording_campaigns/?<property>=<value>[&<property>=<value>]
 
*Properties:*
 * campaign_id 
 * campaign_name
 * start_date, end_date (format YYYY-MM-DD hh:mm:ss, i.e.: 2013-01-22 14:53:33)
 * queue_id
 * activated (True or False)

* return all activated campaigns for queue_id 2::

   GET  http://127.0.0.1:50050/rest/IPBX/recording_campaigns/?activated=True&queue_id=2

**Add::**

   POST http://127.0.0.1:50050/rest/IPBX/recording_campaigns/

**Update::**

   PUT  http://127.0.0.1:50050/rest/IPBX/recording_campaigns/<campaign_id>

``Example of campaign creation``

   POST http://127.0.0.1:50050/rest/IPBX/recording_campaigns/ with following body:
   
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


Recordings
^^^^^^^^^^

**List::**

   GET http://127.0.0.1:50050/rest/IPBX/recording_campaigns/<campaign_id>/

**Search::**

   GET http://127.0.0.1/rest/IPBX/recording_campaigns/<campaign_id>/

Search (with partial match) is done either on:

* IP address
* MAC address
* plugin name
* model name
* phone number

Example::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=search&search=00:0e:50:4e:57:b7
   

Call Center
===========

Configuration
-------------

Agents
^^^^^^

Only agents listing is supported in current version:

**List::**

   GET http://127.0.0.1:50050/rest/CallCenter/agents/


Queues
^^^^^^

Only queues listing is supported in current version:

**List::**

   GET http://127.0.0.1:50050/rest/CallCenter/queue/
