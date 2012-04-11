********************
Skills-Based Routing
********************

Introduction
============
   *A call center agent is the person who handles incoming or outgoing customer 
   calls for a business. A call center agent might handle account inquiries, 
   customer complaints or support issues. Other names for a call center agent 
   include customer service representative (CSR), telephone sales or service 
   representative (TSR), attendant, associate, operator, account executive 
   or team member.*

   -- SearchCRM

In this respect, agents in XiVO have no fixed line and can login from any registered device.


Getting Started
===============

* Create a user with a SIP line and a provisioned device.
* Create agents.
* Create a queue adding created agent as member of queue.

Creating agents
================

Service > Call center > Agents > General
----------------------------------------

These settings are specific for a given agent.


Service > Call center > Agents > Users
--------------------------------------

These settings are specific for a given agent.


Service > Call center > Agents > Queues
---------------------------------------

These settings are specific for a given agent.


Service > Call center > Agents > Advanced
-----------------------------------------

These settings are specific for a given agent.

* Require a DTMF_ to pick a call (ackcall) : When enabled, the key configured in parameter "acceptdtmf" MUST be pressed to pick a call.
* Accept call DTMF (acceptdtmf) : Configured key used to pick up DTMF calls (if ackcall is enabled)
* End call DTMF (enddtmf) : Configured key used to end DTMF calls (if endcall is enabled)

Service > IPBX > General settings > Advanced > Agent
-----------------------------------------------------

These settings are global for all agents.

* Press DTMF to hangup (endcall) : When enabled, the key configured in parameter "enddtmf" CAN be pressed to end a call. Usefull for Agent callback login. Without this setting, the enddtmf parameter is unused. 

.. _DTMF: http://en.wikipedia.org/wiki/Dtmf
