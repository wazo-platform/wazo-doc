*******************
Recording campaigns
*******************

Recording campaigns aim at recording all the calls on a given queue for a given period of time.


.. _campaign-properties:

Recording Campaign properties
=============================

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

List Campaigns
==============

List all recording campaigns.

::

   GET /1.0/recording_campaigns/

**Parameters**

* campaign_name : filter on the campaign name
* queue_id : filter on the queue id
* queue_number : filter on the queue number
* running : the campaign must be currently active (current date must be between the start date and the end date)

**Example request**::

   GET /1.0/recording_campaigns/[?param1=val1[&param2=val2]] HTTP/1.1
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

Get Campaign
============

Return the recording campaign with the given id

::

   GET /1.0/recording_campaigns/<id>

**Parameters**

* None

**Example request**::

   GET /1.0/recording_campaigns/1 HTTP/1.1
   Host: xivoserver:50051
   Accept: application/json

**Example response**::

   HTTP/1.1 200 OK
   Content-Type: application/json

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

Create Campaign
===============

Creates a campaign and returns the generated id.

::

   POST /1.0/recording_campaigns/

**Parameters**

* None

**Example request**::

   POST /1.0/recording_campaigns/ HTTP/1.1
   Host : xivoserver:50051
   Content-Type: application/json

   {
     "campaign_name": "my campaign",
     "queue_id": "2",
     ...
   }

**Example response**::

   HTTP/1.1 201 CREATED
   Content-Type: application/json

   "1"


.. _update-campaign:

Update Campaign
===============

Update the recording campaign with the given id.

::

   PUT /1.0/recording_campaigns/<id>

**Parameters**

* None

**Example request**::

   PUT /1.0/recording_campaigns/1 HTTP/1.1
   Host: xivoserver:50051
   Content-Type: application/json

   {
     "campaign_name": "my campaign",
     "queue_id": "2",
     ...
   }

**Example response**::

   HTTP/1.1 200 OK


.. _delete-campaign:

Delete Campaign
===============

Delete the recording campaign with the given id.

::

   DELETE /1.0/recording_campaigns/<id>

**Parameters**

* None

**Example request**::

   DELETE /1.0/recording_campaigns/1 HTTP/1.1
   Host: xivoserver:50051

**Example response**::

   HTTP/1.1 200 OK
