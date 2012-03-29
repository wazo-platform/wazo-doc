.. index:: Local directory

********************
Local Directory Xlet
********************

Overview
========

The local directory xlet allow a user to add personnal contacts to the XiVO client.

.. figure:: /cti_client/images/cti_client-localdir.png


Usage
=====

The ``New Contact`` button allow the user to add a new contact to his local contact file.

The ``Export Contacts`` button allow the user to save a copy of his local contacts in a file in CSV format.

The ``Import Contacts`` button allow the user to import a CSV file containing new contacts into his local directory.

The ``Search`` button allow the user to find an occurence of a string in his local directory. Clicking the "Ok" button multiple times in the search dialog will find the next occurence of the searched string.

The ``Remove all contacts`` button deletes all contacts from the user's local directory.


File format
===========

Imported files should have the following structure::

   firstname,lastname,phonenumber,emailaddress,company,faxnumber,mobilenumber
   Robert,Toto,5555555555,my@email,xivo,1234,5551231234
