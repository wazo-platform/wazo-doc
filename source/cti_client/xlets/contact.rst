.. index:: Contacts

************
Contact Xlet
************

Overview
========

The Contacts XLet lists the people of your company, giving you access to their
phone and XiVO Client status.

.. figure:: /cti_client/images/cti_client-contacts.png


Usage
=====

The "Search" text input allows you to filter the list of people according to
their name or phone number. An empty filter displays all contacts found.

If the filter matches some contacts, you can see contact objects.
Here's what a contact object looks like :

.. figure:: /cti_client/images/cti_client-contacts-object.png

You can see three informations :

* The person's full name
* A person icon: it displays the status of its XiVO Client. Usually:

  * green means connected
  * gray means disconnected

* A phone icon: it displays the status of the phone of the user, if it has a
  configured phone. Usually:

  * green means that the phone is activated and hanged up
  * red means that the phone is activated and in communication
  * white means that the phone is not registered, i.e. not functional.

The colors and label of these two statuses may be configured within the XiVO Web
interface.

.. TODO :ref:`cti_presences`
.. TODO :ref:`cti_phonehints`

You can interact in several ways with a person object :

* Holding your mouse cursor on the person or phone icon will display more
  details about the person and its phone.
* Double-clicking on it will call the person if its phone is activated
* Right-clicking on it will display the list of possible actions.
* Dragging and dropping it on another person icon will make the dragged user
  call the dropped user.

Possible actions available through right-click are :

* Call
* Hangup
* Chat
* Intercept call
* Transfer a call to this user
* Cancel a transfer
* Invite to a conference room

The available actions may differ, depending on your current phone situation
(available, busy, in a conference room, ...) and on the actions allowed in your
CTI profile.

.. TODO :ref:`cti_profiles`


Configuration
-------------

You can modify the display of contacts within the XLet: Go in the menu XiVO
Client -> Configure, tab Functions, sub-tab Contacts. You get two options :

* The maximum number of contacts displayed
* The number of columns used to display the contacts. A value of 0 will
  automatically display the contacts with the maximum number of columns allowed
  by the width of the window.

Transfers
---------

Many transfers scenarios are supported from the XiVO contact xlet. Blind and
attended tranfers can be done by right clicking a contact.

.. important:: To be able to transfer calls using the XiVO client you have to enable the
    transfer service from the user configuration (or the queue configuration if used)
    form in the web-interface.

Attended Transfers
^^^^^^^^^^^^^^^^^^

.. important:: For the Attended Transfer to work properly in all expected cases you must take care 
    of the value of the options below:
    
    :menuselection:`Services ---> IPBX ---> Services IPBX ---> Extensions ---> Advanced ---> Parking`:
    
    * option `Allow DTMF based transfers when picking up parked call` should be set to ``Caller`` to be
      able to initiate an attended transfer for a call picked from a parking,
    * option `Allow DTMF based hangups when picking up parked call` should be set to ``Caller`` to be 
      able to abort an attended transfer picked up from a parking,

Usage :

#. Answer an incoming call, 
#. Search an user in the Contact xlet,
#. Right clic on the user icon and choose `Attended transfer`,

    #. If the selected user has also a mobile, you can choose its mobile,
    #. You can abort the attended transfer by dialing ``*0`` on your phone (see note below),
    #. You can finish the attended transfer by hanging up the call,


Other important options to look to are :

* :menuselection:`Services ---> IPBX ---> Services IPBX ---> Extensions ---> General -> Transfers` :
  option `Timeout for answer on attended transfer` should be set to a value below the mean ringing time of most users on
  the XiVO if you want the attented transfer be aborted automatically after this timeout,
* :menuselection:`Services ---> IPBX ---> Services IPBX ---> Extensions ---> General` : the option `Hangup` 
  must be set to ``*0`` if you want to use ``*0`` to abort attended transfer.


