.. _xivo-confd-developer:

==============================
Developer's Guide (xivo-confd)
==============================

xivo-confd is made of plugins and each of them is build with the following architecture.

.. figure:: images/xivo-confd-plugin-architecture.png

   Plugin architecture of xivo-confd


``Resource``
   the public class used to represent the resource. It must be self-contained
   and have almost no methods, except for computed fields based on other fields
   in the same object.
``Service``
   the public module, providing possible actions. It contains only business
   logic and no technical logic. There must be no file name, no SQL queries and
   no URLs in this module.
``Dao``
   the private Data Access Object. It knows where to get data and how to update
   it, such as SQL queries, file names, URLs, but has no business logic.
``Notifier``
   private, it knows to whom and in which format events must be sent.
``Validator``
  private, it checks input parameters from the service module.
