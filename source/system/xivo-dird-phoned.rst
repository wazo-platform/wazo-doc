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
need to send 2 parameters in the query string:

* `vendor`: the vendor of the phone (e.g. cisco, aastra, yealink, etc..). It's needed
  to send informations formatted in proper XML.
* `xivo_user_uuid` (optional): The XiVO user uuid that the phone is associated. It's used to search
  through personal contacts (see :ref:`dird_services_personal`)

.. note:: Since most phone doesn't support HTTPS, a small protection is to configure
          authorized_subnets in :ref:`configuration-files` or in :menuselection:`Services -->
          General settings --> Phonebook --> Hosts`


Configuration example
^^^^^^^^^^^^^^^^^^^^^

To allow xivo-dird-phoned to search in xivo-dird, you need to configure a lookup profile in
xivo-dird. The name should be the same as configured in xivo-dird-phoned.

``xivo-dird-phoned``
::

    dird:
        default_profile: default_phone

``xivo-dird``
::

    services:
        lookup:
            default_phone:
                sources:
                    - xivo
                    - personal


.. note:: Your device need to be associated to a user in XiVO >= 15.15 to take effect.


Launching xivo-auth
===================

::

    usage: xivo-dird-phoned [-h] [-c CONFIG_FILE] [-u USER] [-d] [-f] [-l LOG_LEVEL]

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG_FILE, --config-file CONFIG_FILE
                            The path to the config file
      -u USER, --user USER  User to run the daemon
      -d, --debug           Log debug messages
      -f, --foreground      Foreground, don't daemonize
      -l LOG_LEVEL, --log-level LOG_LEVEL
                            Logs messages with LOG_LEVEL details. Must be one of:
                            critical, error, warning, info, debug. Default: None
