*********
Phonebook
*********

A global phone book can be defined in ``IPBX Service -> Phone book``. The phone book can be used from
the XiVO client, from the phones directory look key if the phone is compatible and are used to set
the Caller ID for incoming calls.

You can add entries one by one or you can mass-import from a CSV file.

Mass-import contacts
====================

Go in the ``IPBX Services -> Phonebook`` section and move your mouse cursor on the '+' button in the
upper right corner. Select "Import a file".

The file to be imported must be a CSV file, with a pipe character '|' as field delimiter. The file
must be encoded in UTF-8.

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

Displayed fields
================

It's possible to add more fields to the display in the CTI client. The display can be customized in
the web interface under ``Services -> CTI server -> Directories -> Display filter``.

Fields that can be displayed are set in ``Directories -> Definitions -> xivodir``

The field name will be used to refer to this field in the directory display.

The fields in definition can be used with the following syntax ``{db-[field-name]}``

General phone book section
--------------------------

These fields are set in the General tab of the phone book.

* phonebook.description
* phonebook.displayname
* phonebook.email
* phonebook.firstname
* phonebook.fullname
* phonebook.lastname
* phonebook.society
* phonebook.title
* phonebook.url

Phone numbers
-------------

These are the different phone numbers that are available

* phonebooknumber.fax
* phonebooknumber.home
* phonebooknumber.mobile
* phonebooknumber.office
* phoneboomnumber.other

Addresses
---------

Each configured address can be accessed

Address uses the following syntax ``phonebookaddress.[location].[field]``.

Locations
^^^^^^^^^

* home
* office
* other

Fields
^^^^^^

* address1
* address2
* city
* country
* state
* zipcode

Each line is a field that will be displayed in the directory xlet.

.. figure::  images/phone_book_display.png
   :scale: 85% 

Adding the fax to the directory display
---------------------------------------

#. In the definition section, add a field name ``fax`` with the value ``phonebooknumber.fax.number``.
#. In the display filter section add a field with field title ``Fax`` and display format ``{db-fax}``.
#. Restart the CTI Server

Now the fax should be available displayed in the Directory xlet.
