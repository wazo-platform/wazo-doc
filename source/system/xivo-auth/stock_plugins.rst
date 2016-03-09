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

* Perform a simple bind with one of the following method.

  * Bind with ``bind_dn`` / ``bind_password``
  * Bind anonymous
  * No bind for search (user DN = "``{user_login_attribute}={username},{user_base_dn}``")

* Perform a search on ``user_base_dn`` to find the value of ``user_login_attribute``.
* Match the value of ``user_login_attribute`` to ``username`` and return the user DN.
* Bind with user DN and retrieve the ``user_email_attribute`` value.
* Find the XiVO user associated to the ``user_email_attribute`` value.
* Return a token with the same access privileges as the user.

.. note:: User's email and voicemail's email are two separate things. This plugin only use the
   user's email.


Configuration
^^^^^^^^^^^^^

Configuration example:

.. code-block:: yaml
   :linenos:

   ldap:
       uri: "ldap://example.org"
       bind_dn: "cn=xivo-auth,ou=people,dc=company,dc=org"
       bind_password: "X1V0-4u|H"
       bind_anonymous: false
       user_base_dn: "ou-people,dc=company,dc=org"
       user_login_attribute: "userPrincipalName"
       user_email_attribute: "userPrincipalName"

uri
   the URI of the LDAP server. Can only contain the scheme, host and port of an LDAP URL.
user_base_dn
   the base dn of the user
user_login_attribute
   the attribute to login a user
user_email_attribute (optional)
   the attribute to match with the XiVO user's email (default: mail)
bind_dn (optional)
   the bind DN for searching for the user DN.
bind_password (optional)
   the bind password for searching for the user DN.
bind_anonymous (optional)
   use anonymous bind for searching for the user DN (default: false)


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
