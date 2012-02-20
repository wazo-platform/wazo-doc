***************
Getting started
***************

.. toctree::
   :maxdepth: 2

   Contact Center <contactcenter/contact_center>
   Conference Room <conference_room/conference_room>


Setting Up Your First Phone Set
===============================

Boss secretary filter
=====================

The boss secretary filter allow to set a secretary or a boss role to a user. Filters can then be
created to filter calls directed to a boss using different strategies.

Defining a role
---------------

The secretary or boss role can be set in the user's configuration page under the service tab. To use
this feature, at least one boss and one secretary must be defined.

.. figure:: images/user_bs_filter.png
   :scale: 85%

Creating a filter
-----------------

The filter is used to associate a boss to one or many secretaries and to set a ring strategy. The
call filter can be added in Services > Call management > Call filters.

Usage
-----

The call filter function can be activated and deactivated by the boss using the \*37 extension. The
extension is defined in IPBX services > Extensions.

The call filter has to be activated for each secretary if more than one is defined for a given boss.

The extension to use is ``*37<boss number>*<secretary number>``.

For a boss with extension 100 and 2 secretaries with extensions 101 and 102 the boss would have to
type ``*37100*101`` and ``*37100*102``.

Function keys
-------------

A more convenient way to active the boss secretary filter is to assign a function key on the boss'
phone. In the user's configuration under ``Func Keys``. A function key can be added for each
secretaries of a boss.

If supervision is activated, the key will light up when filter is activated for this secretary.

Interconnections
================

Caller ID
---------

When setting up an interconnection with the public network or another PBX, it is possible to set a
caller ID in different places. Each way to configure a caller ID has it's own use case.

The format for a caller ID is the following ``"My Name" <9999>`` If you don't set the number part of
the caller ID, the dialplan's number will be used instead. This might not be a good option in most
cases.


Outgoing call caller ID
^^^^^^^^^^^^^^^^^^^^^^^

When you create an outgoing call, it's possible to set the it to internal, using the check box in
the outgoing call configuration menu. When this option is activated, the caller's caller ID will be
forwarded to the trunk. This option is use full when the other side of the trunk can reach the user
with it's caller ID number.

.. figure:: images/outgoing_call_internal.png
   :scale: 85%

When the caller's caller ID is not usable to the called party, the outgoing call's caller id can
be fixed to a given value that is more use full to the outside world. Giving the public number here
might be a good idea.

.. figure:: images/outgoing_call_callerid.png
   :scale: 85%

A user can also have a forced caller ID for outgoing calls. This can be use full for someone who has
his own public number. This option can be set in the user's configuration page. The Outgoing
Caller ID id option must be set to Customize. The user can also set his outgoing caller ID to
anonymous.

.. figure:: images/user_custom_callerid.png
   :scale: 85%

The order of precedence when setting the caller ID in multiple place is the following.

#. Internal
#. User's outgoing caller ID
#. Outgoing call
#. Default caller ID


Voice Mail
==========

Internationalization
====================

Advanced Using Sub Routines
===========================

Parking and Paging
==================

Interactive Voice Response
==========================

Fax
===

XiVO And Asterisk
=================

Phonebook
=========

In the section IPBX Services -> Phonebook, you can import a list of people and phone numbers that will be available from both the directory phone key, if the phone is compatible, and the Directory Xlet in the XiVO Client.

You can add entries one by one or you can mass-import from a CSV file.

Mass-import contacts
--------------------

Go in the IPBX Services -> Phonebook section and move your mouse cursor on the '+' button in the upper right corner. Select "Import a file".

The file to be imported must be a CSV file, with a pipe character '|' as field delimiter. The file must be encoded in UTF-8.

Mandatory headers are :

* title (possible values : "mr", "mrs", "ms")
* displayname

Optional headers are :

* firstname
* lastname
* society
* mobilenumber [#numeric]_
* email
* url
* description
* officenumber [#numeric]_
* faxnumber [#numeric]_
* officeaddress1
* officeaddress2
* officecity
* officestate
* officezipcode
* officecountry [#country]_
* homenumber [#numeric]_
* homeaddress1
* homeaddress2
* homecity
* homestate
* homezipcode
* homecountry [#country]_
* othernumber [#numeric]_
* otheraddress1
* otheraddress2
* othercity
* otherstate
* otherzipcode
* othercountry [#country]_

.. [#numeric] These fields must contain only numeric characters, no space, point, etc.
.. [#country] These fields must contain ISO country codes. The complete list is described `here`_.
.. _here: http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm
