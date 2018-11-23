.. _web_services_access:

*******************
Web Services Access
*******************

You may configure Web Services / REST API permissions in :menuselection:`Configuration -->
Management --> Web Services Access`.

Web services access may have two different meanings:

* Who may access REST APIs of various Wazo daemons, and which resources in those REST APIs?
* Who may access PHP web services under ``https://wazo.example.com/xivo/configuration/json.php/*``?


REST API access and permissions
===============================

Those REST API interfaces are documented on http://api.wazo.community. They all require an authorization
token, obtained by giving valid credentials to the REST API of wazo-auth. The relevant settings are:

* Login/Password: the wazo-auth credentials
* ACL: The list of authorized REST API resources. See :ref:`rest-api-acl`.

Unlike PHP web services, there is no host-based authorization, so the ``Host`` setting is not
relevant.

A few REST API access are automatically generated during the installation of Wazo, so that Wazo
services may authenticate each other.

You will probably only need to create such a REST API access when you want another non-Wazo service
to communicate with Wazo via REST API.


PHP web services
================

.. warning:: **DEPRECATED**

Those web services are deprecated. There is no documentation about their usage, and the goal is to
remove them.

They are still protected with HTTP authentication, requiring a login and password. The
relevant settings are:

* Login/Password: the HTTP authentication credentials
* Host: the authorized hosts that are allowed to make HTTP requests:

  * Empty value: HTTP authentication
  * Non-empty value: no HTTP authentication, all requests coming from this host will be accepted.
    Valid hosts may be: a hostname, an IP address, a CIDR block.

There is no fine-grained permissions: either the user has access to every PHP web services, or none.


xivo-confd
==========

.. warning:: **DEPRECATED**

There is also a special case for authentication with xivo-confd. See :ref:`rest-api` for more details.
