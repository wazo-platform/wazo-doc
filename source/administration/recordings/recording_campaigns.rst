*******************
Recording Campaigns
*******************

Introduction
============

In order to improve reception quality in a call center, it can be useful record some calls
to help agents improving their communication skills. It becomes possible thanks to the 
recording campaigns, whose goal is to record all the calls on a specific queue
for a given period of time. Creating several campaigns will allow to monitor several queues
at once. A campaign will automatically stop when its end date is reached, and its recordings
are easily accessible.


Campaign management
===================

Recording campaigns are accessible via the
:menuselection:`Service --> IPBX --> IPBX Settings --> Recordings` page.

Creating a campaign
-------------------

* Click on the "Add" button
* Specify a name, a start date, an end date and a targetted queue for your campaign
* Save your modifications

Two campaigns cannot cannot record the same queue on a concurrent period of time.
For instance, if a campaign is recording the queue "Sales" from 2012-01-01 to 
2012-02-28, it is not possible to create another campaign for the queue "Sales" from
2012-01-30 to 2012-03-31.


Managing the recordings
-----------------------

The calls are recorded to the .wav format.

To see all the recordings of a given campaign, click on its name.

Each recording can be downloaded by clicking on the "Download" button, and deleted 
by clicking on the "Delete" button.

It is possible to perform a search on the recordings on the fields "Agent" and "Caller".

Every day, the recordings older than 31 days will be automatically deleted. This will
occur around midnight.

Logging
-------

One log file is specifically generated to monitor the recordings. It can be accessed via
:menuselection:`Service --> IPBX --> Control --> Asterisk log files`.

