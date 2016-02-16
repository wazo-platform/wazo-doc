.. _auth-stock-plugins:

===========================
Stock Plugins Documentation
===========================

.. _auth-backends:

Backends Plugins
================

.. _auth-backends-ldap:

LDAP
----

Backend name: ldap_user

Purpose: Authenticate via an ldap user.

Work flow followed when creating a token:

* Create a DN for authentication built from the ``username`` and ``bind_dn_format``.
* Perform a simple bind on LDAP Server with the created DN and ``password``.
* Concatenate ``username`` and ``domain`` in order to search for an email (only if username is not
  an email).
* Find the user associated to the email.
* Return a token with the same access privileges as the user.

Limitations:

* Emails stored in the users **MUST** be unique. Authentication bugs might occur if the email is
  found in more than one user.

.. note:: User's email and voicemail's email are two separate things. This plugin only use the
   user's email.


Configuration
^^^^^^^^^^^^^

Configuration example:

.. code-block:: yaml
   :linenos:

   enabled_plugins:
     - ldap_user
     # you must write here all other enabled plugins to keep them enabled (see main config.yml for default)

   ldap:
       uri: ldap://example.org
       bind_dn_format: "uid={username},ou=people,dc=company,dc=org"
       domain: company.com

uri
   the URI of the LDAP server. Can only contain the scheme, host and port of an LDAP URL.

bind_dn_format
   the bind DN used to check the given username/password. The variable ``{username}`` will be
   substituted when binding.

domain (optional)
   the domain used to build the email associated with a XiVO user. This option is optional if the
   email address are used as username. In this case, the part before `@` will be the ldap username.


XiVO Admin
-----------

Backend name: xivo_admin

Purpose: Authenticate a XiVO admin.


.. _auth-backends-service:

XiVO Service
------------

Backend name: xivo_service

Purpose: Authenticate a XiVO service.


XiVO User
---------

Backend name: xivo_user

Purpose: Authenticate a XiVO user.
