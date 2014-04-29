***************
XiVO Guidelines
***************


Inter-process communication
===========================

Our current goal is to use only two means of communication between XiVO processes:

* a REST API over HTTP for synchronous commands
* a software bus (RabbitMQ) for asynchronous events

Each component should have its own REST API and its own events and can communicate with every other
component from across a network only via those means.


Service API
===========

The current `xivo-dao`_ Git repository contains the basis of the future services Python API. The
API is split between different resources available in XiVO, such as users, groups, schedules... For
each resource, there are different modules :

.. _xivo-dao: https://github.com/xivo-pbx/xivo-dao

* service: the public module, providing possible actions. It contains only business logic and no
  technical logic. There must be no file name, no SQL queries and no URLs in this module.
* dao: the private Data Access Object. It knows where to get data and how to update it, such as SQL queries,
  file names, URLs, but has no business logic.
* model: the public class used to represent the resource. It must be self-contained and have almost no
  methods, except for computed fields based on other fields in the same object.
* notifier: private, it knows to whom and in which format events must be sent.
* validator: private, it checks input parameters from the service module.
