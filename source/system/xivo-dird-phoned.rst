.. _xivo-dird-phoned:

================
XiVO dird phoned
================

xivo-dird-phoned is an interface to use directory service with phone. It offers a simple REST
interface to authenticate a phone and search result from :ref:`xivo-dird`.


Usage
=====

xivo-dird-phoned is used through HTTP requests, using HTTP and HTTPS. Its default port is 9498
and 9499. As a user, the common operation is to search through directory from a phone. The phone
need to send 1 parameter in the query string:

* `xivo_user_uuid` (optional): The XiVO user uuid that the phone is associated. It's used to search
  through personal contacts (see :ref:`dird_services_personal`)

.. note:: Since most phones dont't support HTTPS, a small protection is to configure
          authorized_subnets in :ref:`configuration-files` or in :menuselection:`Services -->
          General settings --> Phonebook --> Hosts`


Launching xivo-dird-phoned
==========================

On command line, type ``xivo-dird-phoned -h`` to see how to use it.
