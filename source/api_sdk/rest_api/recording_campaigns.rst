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

**Parameters**

* campaign_name : filter on the campaign name
* queue_id : filter on the queue id
* queue_number : filter on the queue number
* running : the campaign must be currently active (current date must be between the start date and the end date)

**Request**

::

   GET /1.0/recording_campaigns/[?param1=val1[&param2=val2]]
   Host: xivoserver:50051
   Accept: application/json

**Response**

::

   HTTP/1.1 200 OK
   Content-Type: application/json

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

Get Campaign
============

Return the recording campaign with the given id

**Parameters**

* None

**Request**

::

   GET /1.0/recording_campaigns/<id>
   Host: xivoserver:50051
   Accept: application/json

**Response**

::

   HTTP/1.1 200 OK
   Content-Type: application/json

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

Create Campaign
===============

Creates a campaign and returns the generated id.

**Parameters**

* None

**Request**

::

   POST /1.0/recording_campaigns/<id>
   Host : xivoserver:50051
   Content-Type: application/json

.. code-block:: javascript

    {
      "campaign_name": "my campaign",
      "queue_id": "2",
      ...
    }

**Response**

::

    HTTP/1.1 201 CREATED
    Content-Type: application/json

.. code-block:: javascript

   "1"


.. _update-campaign:

Update Campaign
===============

Update the recording campaign with the given id.

**Parameters**

* None

**Request**

::

   PUT /1.0/recording_campaigns/<id>
   Host: xivoserver:50051
   Content-Type: application/json

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

Delete Campaign
===============

Delete the recording campaign with the given id.

**Parameters**

* None

**Request**

::

   DELETE /1.0/recording_campaigns/<id>
   Host: xivoserver:50051

**Response**

::

   HTTP/1.1 200 OK
