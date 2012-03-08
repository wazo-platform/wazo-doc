*********
Phonebook
*********

In the section IPBX Services -> Phonebook, you can import a list of people and phone numbers that will be available from both the directory phone key, if the phone is compatible, and the Directory Xlet in the XiVO Client.

You can add entries one by one or you can mass-import from a CSV file.

Mass-import contacts
====================

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
