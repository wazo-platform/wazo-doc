.. _auth-stock-plugins:

===========================
Stock Plugins Documentation
===========================

Backends Plugins
================

LDAP by voicemail (EXPERIMENTAL)
--------------------------------

.. warning:: This plugin is **EXPERIMENTAL** It may be removed or changed without further notice.

Backend name: ldap_user_voicemail

Purpose: Authenticate via an ldap user.

Work flow followed when creating a token:

* Create a DN for authentication built from the ``username`` and ``bind_dn_format``.
* Perform a simple bind on LDAP Server with the created DN and ``password``.
* Concatenate ``username`` and ``domain`` in order to search for an email.
* Search through all of XiVO's voicemails for the corresponding email
* Find the user associated to the voicemail
* Return a token with the same access privileges as the user

Limitations:

* Emails stored in the voicemails **MUST** be unique. Authentication bugs might occur if the email is
  found in more than one voicemail.
* The voicemail with the email **MUST** be associated to only one user. Authentication bugs might
  occur if a voicemail is associated to multiple users.


Configuration
^^^^^^^^^^^^^

Configuration example:

.. code-block:: yaml
   :linenos:

   enabled_plugins:
     - ldap_user_voicemail

   ldap:
       uri: ldap://example.org
       bind_dn_format: "uid={username},ou=people,dc=company,dc=org"
       domain: company.com

uri
   the URI of the LDAP server. Can only contain the scheme, host and port of an LDAP URL.

bind_dn_format
   the bind DN used to check the given username/password. The variable ``{username}`` will be
   substituted when binding. 

domain
   the domain used to build the email associated with a XiVO user.


XiVO Admin
-----------

Backend name: xivo_admin

Purpose: Authenticate a XiVO admin.


XiVO Service
------------

Backend name: xivo_service

Purpose: Authenticate a XiVO service.


XiVO User
---------

Backend name: xivo_user

Purpose: Authenticate a XiVO user.
