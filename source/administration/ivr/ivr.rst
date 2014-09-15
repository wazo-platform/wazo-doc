.. _ivr:

***************************
Interractive Voice Response
***************************

Introduction
============

   *Interactive voice response (IVR) is a technology that allows a computer to interact with humans
   through the use of voice and DTMF tones input via keypad. In telecommunications, IVR allows
   customers to interact with a company’s host system via a telephone keypad or by speech recognition,
   after which they can service their own inquiries by following the IVR dialogue.*

   -- Wikipedia

The IVR function is not yet available in graphic mode in XiVO. This functionality is currently
supported using scripts, also named dialplan.


Use Case : Minimal IVR
======================

Flowchart
---------

.. figure:: images/ivr2.png
   :scale: 40%


Configuration File and Dialplan
-------------------------------

First step, you need to create a configuration file, that contain an asterisk context and your IVR
dialpan. In our exemple, both (file and context) are named dp-ivr-exemple.

.. figure:: images/ivr1.png


Copy all these lines in the newly created configuration file (in our case, dp-ivr-example) :

::

   [dp-ivr-exemple]

   exten = s,1,NoOp(### dp-ivr-exemple.conf ###)
   same = n,NoOp(the system pick up the call and wait for 1 seconde before continue)
   same = n,Answer(1000)

   same = n,NoOp(the system play the first part of the audio file « welcome to … »)
   same = n(first),Playback(${GV_DIRECTORY_SOUNDS}/svi-exemple-welcome-sound)

   same = n,NoOp(variable « counter » is set to 0)
   same = n(begining),Set(counter=0)

   same = n,NoOp(variable "counter" is uptated +1 and the label "start" is define)
   same = n(start),Set(counter=$[${counter} + 1])

   same = n,NoOp(counter variable is now = ${counter})
   same = n,NoOp(waiting for 1 seconde before read the message that indicate all choices)
   same = n,Wait(1)
   same = n,NoOp(spreading the message ivr-exemple-choices that contain all choices)
   same = n,Background(/var/lib/xivo/sounds/customer-sounds/ivr-exemple-choices)
   same = n,NoOp(waiting for DTMF during 5s)
   same = n,Waitexten(5)

   ;##### CHOICE 1 #####
   exten = 1,1,NoOp(pressed digit is 1, redirect to the 8000 in ${XIVO_BASE_CONTEXT} context)
   exten = 1,n,goto(${XIVO_BASE_CONTEXT},8000,1)

   ;##### CHOICE 2 #####
   exten = 2,1,NoOp(pressed digit is 2, redirect to the 8833 in ${XIVO_BASE_CONTEXT} context)
   exten = 2,n,goto(${XIVO_BASE_CONTEXT},8833,1)

   ;##### CHOICE 3 #####
   exten = 3,1,NoOp(pressed digit is 3, redirect to the 8547 in ${XIVO_BASE_CONTEXT} context)
   exten = 3,n,goto(${XIVO_BASE_CONTEXT},8547,1)


   ;##### CHOICE 4 #####
   exten = 4,1,NoOp(pressed digit is 4, redirect to start label in this context)
   exten = 4,n,goto(s,start)

   ;##### TIMEOUT #####
   exten = t,1,NoOp(no digit pressed until 5s, call is redirected to the 8000)
   exten = t,n,goto(${XIVO_BASE_CONTEXT},8000,1)


   ;##### INVALID CHOICE #####
   exten = i,n,NoOp(counter variable is less than 3, then goto label "start" else goto "s")
   exten = i,n(fail),Gotoif($[${counter}<3]?s,start)
   exten = i,n,NoOp(more than 3 errors, then the guide ivr-exemple-error is played)
   exten = i,n,Playback(${GV_DIRECTORY_SOUNDS}/ivr-exemple-error)
   exten = i,n,NoOp(call is now hang up)
   exten = i,n,Hangup()
   exten = i,1,NoOp(pressed digit is unvalid and less than 3 errors : the guide ivr-exemple-invalid-choice now is played)
   exten = i,n,Playback(${GV_DIRECTORY_SOUNDS}/ivr-exemple-invalid-choice)


IVR internal dial
-----------------

To call the script dp-ivr-exemple from an internal phone you must create an entry in the default
context.  The best way is add the number in the file xivo-extrafeatures.conf.

.. figure:: images/ivr3.png

::

   exten => 8899,1,Goto(dp-ivr-exemple,s,1)


IVR external dial
-----------------

To call the script dp-ivr-exemple from an external phone, you must create an entry in the
"Incoming calls" section (1). Then create the DID number conforme as your range of externals
numbers (2) and redirect the call to the script dp-ivr-exemple with the command :

::

   Goto(dp-ivr-exemple,s,1)


.. figure:: images/ivr4.png


Use Case : IVR with a schedule
==============================

In lot of case, you need to associate your IVR to a schedule to indicate when your company is closed.

Flowchart
---------

.. figure:: images/ivr5.png


Create Schedule
---------------

First step, create your shcedule (1) from the menu Call management | Schedules
In the General tab, give a name (3) to your schedule and configure the open’s hours (4) and select the sound which is played when the company is closed.

In the Closed hours tab (6), configure all special closed days (7) and select the sound that indicate to the caller that the company is exceptionally closed.

The IVR script is now only available during workdays

.. figure:: images/ivr6.png


Use Case : IVR with submenu
===========================

Flowchart
---------

.. figure:: images/ivr7.png


Configuration File and Dialplan
-------------------------------

Copy all these lines (2 contexts) in a configuration file on your XiVO server :

::

   [dp-ivr-exemple]

   exten = s,1,NoOp(### dp-ivr-exemple.conf ###)
   same = n,NoOp(the system pick up the call and wait for 1 seconde before continue)
   same = n,Answer(1000)

   same = n,NoOp(the system play the first part of the audio file « welcome to … »)
   same = n(first),Playback(${GV_DIRECTORY_SOUNDS}/svi-exemple-welcome-sound)

   same = n,NoOp(variable « counter » is set to 0)
   same = n(begining),Set(counter=0)

   same = n,NoOp(variable "counter" is uptated +1 and the label "start" is define)
   same = n(start),Set(counter=$[${counter} + 1])

   same = n,NoOp(counter variable is now = ${counter})
   same = n,NoOp(waiting for 1 seconde before read the message that indicate all choices)
   same = n,Wait(1)
   same = n,NoOp(spreading the message ivr-exemple-choices that contain all choices)
   same = n,Background(/var/lib/xivo/sounds/customer-sounds/ivr-exemple-choices)
   same = n,NoOp(waiting for DTMF during 5s)
   same = n,Waitexten(5)

   ;##### CHOICE 1 #####
   exten = 1,1,NoOp(pressed digit is 1, redirect to the 8000 in ${XIVO_BASE_CONTEXT} context)
   exten = 1,n,goto(${XIVO_BASE_CONTEXT},8000,1)

   ;##### CHOICE 2 #####
   exten = 2,1,NoOp(pressed digit is 2, redirect to the 8833 in ${XIVO_BASE_CONTEXT} context)
   exten = 2,n,goto(${XIVO_BASE_CONTEXT},8833,1)

   ;##### CHOICE 3 #####
   exten = 3,1,NoOp(pressed digit is 3, redirect to the submenu dp-ivr-submenu)
   exten = 3,n,goto(dp-ivr-submenu,s,1)


   ;##### CHOICE 4 #####
   exten = 4,1,NoOp(pressed digit is 4, redirect to start label in this context)
   exten = 4,n,goto(s,start)

   ;##### TIMEOUT #####
   exten = t,1,NoOp(no digit pressed until 5s, call is redirected to the 8000)
   exten = t,n,goto(${XIVO_BASE_CONTEXT},8000,1)


   ;##### INVALID CHOICE #####
   exten = i,n,NoOp(counter variable is less than 3, then goto label "start" else goto "s")
   exten = i,n(fail),Gotoif($[${counter}<3]?s,start)
   exten = i,n,NoOp(more than 3 errors, then the guide ivr-exemple-error is played)
   exten = i,n,Playback(${GV_DIRECTORY_SOUNDS}/ivr-exemple-error)
   exten = i,n,NoOp(call is now hang up)
   exten = i,n,Hangup()
   exten = i,1,NoOp(pressed digit is unvalid and less than 3 errors : the guide ivr-exemple-invalid-choice now is played)
   exten = i,n,Playback(${GV_DIRECTORY_SOUNDS}/ivr-exemple-invalid-choice)


   [dp-ivr-submenu]

   exten = s,1,NoOp(### dp-ivr-submenu ###)
   same = n,NoOp(the system pick up the call and wait for 1 seconde before continue)
   same = n,Answer(1000)

   same = n,NoOp(variable « counter » is set to 0)
   same = n(begining),Set(counter=0)

   same = n,NoOp(variable "counter" is uptated +1 and the label "start" is define)
   same = n(start),Set(counter=$[${counter} + 1])

   same = n,NoOp(counter variable is now = ${counter})
   same = n,NoOp(waiting for 1 seconde before read the message that indicate all choices)
   same = n,Wait(1)
   same = n,NoOp(spreading the message ivr-exemple-choices that contain all choices)
   same = n,Background(/var/lib/xivo/sounds/customer-sounds/ivr-exemple-submenu-choices)
   same = n,NoOp(waiting for DTMF during 5s)
   same = n,Waitexten(5)

   ;##### CHOICE 1 #####
   exten = 1,1,NoOp(pressed digit is 1, redirect to the 8000 in ${XIVO_BASE_CONTEXT} context)
   exten = 1,n,goto(${XIVO_BASE_CONTEXT},8000,1)

   ;##### CHOICE 2 #####
   exten = 2,1,NoOp(pressed digit is 2, redirect to the 8001 in ${XIVO_BASE_CONTEXT} context)
   exten = 2,n,goto(${XIVO_BASE_CONTEXT},8001,1)

   ;##### CHOICE 3 #####
   exten = 3,1,NoOp(pressed digit is 3, redirect to the previous menu dp-ivr-exemple)
   exten = 3,n,goto(dp-ivr-exemple,s,1)


   ;##### TIMEOUT #####
   exten = t,1,NoOp(no digit pressed until 5s, call is redirected to the 8000)
   exten = t,n,goto(${XIVO_BASE_CONTEXT},8000,1)


   ;##### INVALID CHOICE #####
   exten = i,n,NoOp(counter variable is less than 3, then goto label "start" else goto "s")
   exten = i,n(fail),Gotoif($[${counter}<3]?s,start)
   exten = i,n,NoOp(more than 3 errors, then the guide ivr-exemple-error is played)
   exten = i,n,Playback(${GV_DIRECTORY_SOUNDS}/ivr-exemple-error)
   exten = i,n,NoOp(call is now hang up)
   exten = i,n,Hangup()
   exten = i,1,NoOp(pressed digit is unvalid and less than 3 errors : the guide ivr-exemple-invalid-choice now is played)
   exten = i,n,Playback(${GV_DIRECTORY_SOUNDS}/ivr-exemple-invalid-choice)
