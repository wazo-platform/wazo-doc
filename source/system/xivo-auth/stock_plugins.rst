.. _auth-stock-plugins:

===========================
Stock Plugins Documentation
===========================

Backends Plugins
================

LDAP by voicemail (EXPERIMENTAL)
--------------------------------

.. warning:: This plugin is **experimental**. It can be removed or changed without warning.

Backend name: ldap_user_voicemail

Purpose: Authenticate a ldap user.

Creation token flow:

* Format username with ``bind_dn_format``.
* Perform a simple bind on LDAP Server with given username_formatted/password.
* Concatenate username and ``domain`` to build email.
* Search through all XiVO voicemail to find email corresponding and associated XiVO user.
* Return a token with the same access of the associated XiVO user.

Limitations:

* Email defined in the voicemail section should be unique.
* A voicemail with a unique email should be associated to only 1 XiVO user.


Configuration
^^^^^^^^^^^^^

Example of ldap configuration:

.. code-block:: yaml
   :linenos:

   enabled_plugins:
     - ldap_user_voicemail

   ldap:
       uri: ldap://example.org
       bind_dn_format: "uid={username},ou=people,dc=company,dc=org"
       domain: company.com

uri
   the URI of the LDAP server. Can only contains the scheme, host and port part of an LDAP URL.

bind_dn_format
   the bind DN to check the given username/password. It is a python format string with ``username``
   as substitution variable.

domain
   the domain used to build the email associated with the XiVO user.


XiVO Admin
------------

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
