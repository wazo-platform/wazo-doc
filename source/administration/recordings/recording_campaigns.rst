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

The campaign deletion is not yet implemented.


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

Two log files are specifically generated to monitor the recordings:

* /var/log/xivo_recording_agi.log: a "technical" log, allowing to track any errors
  during the recording process
* /var/log/asterisk/xivo-recording.log: a log listing the various accesses to the
  recordings (download, deletion, automatic deletion). This log file is accessible via
  the web interface, in 

