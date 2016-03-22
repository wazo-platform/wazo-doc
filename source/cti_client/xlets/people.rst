.. index:: People

.. _people-xlet:

************
People Xlet
************

Overview
========

The People XLet lists the people of your company and personal contacts, giving you access to their
phone, status and other information configured by the administrator.

.. figure:: /cti_client/xlets/images/cti_client-people-actions.png

1. Display results of the search
2. Display favorite contacts
3. Search contacts
4. Call a contact
5. Transfer a call to a contact
6. Transfer a call to a contact's voicemail
7. Chat with a contact
8. Send an email to a contact
9. Bookmark/unmark the contact as a favorite


.. figure:: /cti_client/xlets/images/cti_client-people-personal.png

1. View all personal contacts
2. Edit or remove a personal contact
3. Create a personal contact
4. Import personal contacts from a CSV file
5. Export personal contacts to a CSV file
6. Delete all personal contacts


.. figure:: /cti_client/xlets/images/cti_client-people-status.png

1. XiVO Client status (see :ref:`presence_option`)
2. Phone status (see :menuselection:`Services --> CTI Server --> Status --> Phone hints` page)
3. Agent status (logged in or logged out)

.. note:: Most information (e.g. columns displayed, allowed actions, searched directories,
          etc.) is configurable through the :ref:`web interface <directories>`.


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


Copying the number or email address
===================================

It is possible to copy a contact's number or email address to the system's
clipboard. To do so, right click on a contact's action menu and select the value
you wish to copy.


.. note:: When using a mac without a right mouse button use `ctrl-Left click` to show the copy menu.
