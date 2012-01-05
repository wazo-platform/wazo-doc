.. index:: Contacts

************
Contact xlet
************

Overview
========

The Contacts XLet lists the people of your company, giving you access to their phone and XiVO Client status.

.. image:: /xivoclient/images/xivoclient-contacts.png

Usage
=====

The "Search" text input allows you to filter the list of people according to their name or phone number. An empty filter displays all contacts found.

If the filter matches some contacts, you can see contact objects.
Here's what a contact object looks like :

.. image:: /xivoclient/images/xivoclient-contacts-object.png

You can see three informations :

* The person's full name
* A person icon: it displays the status of its XiVO Client. Usually:
    * green means connected
    * gray means disconnected
* A phone icon: it displays the status of the phone of the user, if it has a configured phone. Usually:
    * green means that the phone is activated and hanged up
    * red means that the phone is activated and in communication
    * white means that the phone is not registered, i.e. not functional.

The colors and label of these two statuses may be configured within the XiVO Web interface.

:ref:`cti_presences`
:ref:`cti_phonehints`

You can interact in several ways with a person object :

* Holding your mouse cursor on the person or phone icon will display more details about the person and its phone.
* Double-clicking on it will call the person if its phone is activated
* Right-clicking on it will display the list of possible actions.
* Dragging and dropping it on another person icon will make the dragged user call the dropped user.

Possible actions available through right-click are :

* Call
* Hangup
* Chat
* Intercept call
* Transfer a call to this user
* Cancel a transfer
* Invite to a conference room

The available actions may differ, depending on your current phone situation (available, busy, in a conference room, ...) and on the actions allowed in your CTI profile.

:ref:`cti_profiles`

Configuration
-------------

You can modify the display of contacts within the XLet: Go in the menu XiVO Client -> Configure, tab Functions, sub-tab Contacts. You get two options :

* The maximum number of contacts displayed
* The number of columns used to display the contacts. A value of 0 will automatically display the contacts with the maximum number of columns allowed by the width of the window.
