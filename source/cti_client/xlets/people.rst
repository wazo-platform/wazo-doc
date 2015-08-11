.. index:: People

.. _people-xlet:

************
People Xlet
************

Overview
========

The People XLet lists the people of your company and personal contacts, giving you access to their
phone, XiVO Client status and other informations configured by the administrator.

.. figure:: /cti_client/xlets/images/cti_client-people.png

#. Display result of the search
#. Display favorite contacts
#. Display personal contacts
#. Filter/search contacts
#. Contacts requested
#. Call the contact by clicking when the mouse is over the number
#. View/call the mobile number by clicking on the down-arrow when mouse is over the number
#. Mark/unmark the contact as favorite
#. Edit personal contact
#. Remove personal contact
#. Create personal contact
#. Import personal contacts with CSV file
#. Export personal contacts in CSV file

.. figure:: /cti_client/xlets/images/cti_client-people-status.png

#. XiVO Client status (see :ref:`presence_option`)
#. Phone status (see :menuselection:`Services --> CTI Server --> Status --> Phone hints` page)
#. Agent status (logged in or logged out)

.. note:: Most informations (e.g. columns displayed, personal contacts allowed, search directories,
          etc.) are configured (and customizable) through :ref:`xivo-dird`.


Contact Import via CSV file
===========================

Imported files should have the following structure::

   firstname,lastname,number,email,company,fax,mobile
   John,Doe,5555551111,my@email,xivo,5555552222,5555553333

* The field order is not important.
* The file must be encoded in ``UTF-8``.


Contact Export via CSV file
===========================

The file has the same structure as the import file, with a supplementary field: ``id``, which is the
internal contact ID from XiVO.

* The first line (the list of field names) is ordered in alphabetical order.
* The file will be encoded in ``UTF-8``.
