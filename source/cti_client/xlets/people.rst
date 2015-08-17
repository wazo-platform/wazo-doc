.. index:: People

.. _people-xlet:

************
People Xlet
************

Overview
========

The People XLet lists the people of your company and personal contacts, giving you access to their
phone, status and other information configured by the administrator.

.. figure:: /cti_client/xlets/images/cti_client-people.png

#. Display results of the search
#. Display favorite contacts
#. Display personal contacts
#. Filter/search contacts
#. Contacts requested
#. Call the contact by clicking the phone number
#. View/call the mobile number by clicking on the arrow when the mouse is over the number
#. Bookmark/unmark the contact
#. Edit the personal contact
#. Remove the personal contact
#. Create a personal contact
#. Import personal contacts from a CSV file
#. Export personal contacts to a CSV file
#. Delete all personal contacts

.. figure:: /cti_client/xlets/images/cti_client-people-status.png

#. XiVO Client status (see :ref:`presence_option`)
#. Phone status (see :menuselection:`Services --> CTI Server --> Status --> Phone hints` page)
#. Agent status (logged in or logged out)

.. note:: Most information (e.g. columns displayed, allowed actions, searched directories,
          etc.) is configurable through :ref:`xivo-dird`.


Importing contacts via CSV file
===============================

Imported files should have the following structure::

   firstname,lastname,number,email,company,fax,mobile
   John,Doe,5555551111,my@email,xivo,5555552222,5555553333

* The field order is not important.
* The file must be encoded in ``UTF-8``.
* Invalid lines of the CSV file will be skipped and an error will be displayed in the import report.


Exporting contacts via CSV file
===============================

The file has the same structure as the import file, with a supplementary field: ``id``, which is the
internal contact ID from XiVO.

* The first line (the list of field names) is ordered in alphabetical order.
* The file will be encoded in ``UTF-8``.
