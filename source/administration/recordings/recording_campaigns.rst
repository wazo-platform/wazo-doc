.. _recording-campaigns:

*******************
Recording Campaigns
*******************


Introduction
============

In order to improve the reception quality of a call center and help agents improve
their communication skills, it can be useful to record some calls. This becomes
possible with the use of recording campaigns, whose goal is to record all the calls
on a specific queue for a given period of time. Creating several campaigns will allow
you to monitor several queues at once. A campaign will automatically stop when its end date
is reached. Campaign recordings in XiVO are easily accessible through the web interface.

.. note::
   * These campaigns will only work for queues whose context is **default**.
   * This functionnality is available only on demand. It requires specific operations to become available.


Campaign management
===================

Recording campaigns are accessible via the
:menuselection:`Service --> IPBX --> IPBX Settings --> Recordings` page.


Creating a campaign
-------------------

* Click on the "Add" button
* Specify a name, a start date, an end date and a targetted queue for your campaign
* Save your modifications

Two campaigns cannot record the same queue for an overlapping period of time.
For instance, if a campaign is recording the queue "Sales" from 2012-01-01 to
2012-02-28, it is not possible to create another campaign for the queue "Sales" from
2012-01-30 to 2012-03-31.


Deleting a campaign
-------------------

A campaign can be deleted by clicking on the "Delete" button. It is not possible to delete
a campaign which still contains some recordings.


Managing the recordings
-----------------------

The calls are recorded as .wav files.

To see all the recordings for a given campaign, click on its name.

Each recording can be downloaded by clicking on the "Download" button, and deleted
by clicking on the "Delete" button.

It is possible to perform a search on the recordings. Searches will be filtered using the fields "Agent" and "Caller".

Recordings older than 31 days will be automatically deleted. Deletion will occur every day around midnight.


Logging
-------

Accesses to the recordings (such as download, deletion, automatic deletion) are logged to the file
`xivo-recording.log`. This file can be accessed via :menuselection:`Service --> IPBX --> Control --> Asterisk log files`.


Activate recordings
===================

To activate the recordings, you will need to follow these steps:

* Download the debian package:

  $ wget http://mirror.xivo.fr/iso/extra/xivo-recording-campaigns_0.1_all.deb

* Install the package:

  $ dpkg -i xivo-recording-campaigns_0.1_all.deb

.. warning::

    If you have previously installed the recordings manually, debian will issue a warning
    about the file ``/etc/asterisk/extensions_extra.d/xivo-recording.conf``. If you have
    not modified this file, you can press 'Y' to overwrite the file with the one provided by the
    package.
