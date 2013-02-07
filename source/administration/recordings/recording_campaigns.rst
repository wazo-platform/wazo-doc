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

This functionnality is available only on demand. It requires an additionnal configuration
file which you can found at the end of this page.

Campaign management
===================

Recording campaigns are accessible via the
:menuselection:`Service --> IPBX --> IPBX Settings --> Recordings` page.

Creating a campaign
-------------------

* Click on the "Add" button
* Specify a name, a start date, an end date and a targetted queue for your campaign
* Save your modifications

Two campaigns cannot cannot record the same queue for an overlapping period of time.
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

Dialplan
========

::

  ;; Global Queue Sub routine for recording activation
  [xivo-subrgbl-queue]
  exten = s,1,NoOp(### Sub routine determinates whether the call is to be recorded - Queue ${XIVO_QUEUENAME}###)
  same  =  n,Set(QR_RECORDQUEUE=0) ; Init QR_RECORDQUEUE
  same  =  n,AGI(/usr/bin/xivo_recording_agi.py,determinateRecord)
  same  =  n,NoOp(# Filename: ${QR_BASE_FILENAME}-${UNIQUEID})
  same  =  n,GotoIf($["${QR_RECORDQUEUE}" = "1"]?:norecord)
  same  =  n,Set(XIVO_QUEUESUB=pre-record-queue)
  same  =  n,Set(__QR_CALLER_NB=${CALLERID(num)})
  same  =  n(norecord),Return()

  ; sub routine
  [pre-record-queue]
  exten = s,1,NoOp(### Sub routine starts recording and saves call details ###)
  same  =  n, NoOp(## The call is about to be answered by ${CHANNEL} ##)
  same  =  n,GotoIf($["${CUT(CUT(CHANNEL,@,2),-,1)}" = "agentcallback"]?:noagent)
  same  =  n,Set(QR_AGENT_ID=${CUT(CUT(CHANNEL,@,1),-,2)})
  same  =  n,Set(QR_QUEUENAME=${QUEUENAME})
  same  =  n,Set(QR_TIME=${STRFTIME(${EPOCH},,%Y-%m-%d %H:%M:%S)})
  same  =  n,AGI(/usr/bin/xivo_recording_agi.py,saveCallDetails)
  same  =  n,NoOp(# Filename: ${QR_FILENAME})
  same  =  n,MixMonitor(/var/lib/pf-xivo/sounds/campagnes/${QR_FILENAME},b)
  same  =  n(noagent),Return()

