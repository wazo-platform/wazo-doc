.. _auth-stock-plugins:

===========================
Stock Plugins Documentation
===========================

.. _auth-backends:

Backends Plugins
================

XiVO Admin
-----------

Backend name: ``xivo_admin``

Purpose: Authenticate a XiVO administrator. The login/password is configured in
:menuselection:`Configuration --> Management --> Users`.


.. _auth-backends-service:

XiVO Service
------------

Backend name: ``xivo_service``

Purpose: Authenticate a XiVO :ref:`Web Services Access <web_services_access>`. The login/password is
configured in :menuselection:`Configuration --> Management --> Web Service Access`.


XiVO User
---------

Backend name: ``xivo_user``

Purpose: Authenticate a XiVO user. The login/password is configured in :menuselection:`IPBX -->
Services --> PBX Settings --> Users` in the CTI client section.


.. _auth-backends-ldap:

LDAP
----

Backend name: ``ldap_user``

Purpose: Authenticate with an LDAP user.

For example, with the given configuration:

.. code-block:: yaml

   ldap:
       uri: ldap://example.org
       bind_dn: cn=xivo,dc=example,dc=org
       bind_password: bindpass
       user_base_dn: ou=people,dc=example,dc=org
       user_login_attribute: uid
       user_email_attribute: mail

When an authentication request is received for username ``alice`` and password ``userpass``, the
backend will:

#. Connect to the LDAP server at example.org
#. Do an LDAP "bind" operation with bind DN ``cn=xivo,dc=example,dc=org`` and password ``bindpass``
#. Do an LDAP "search" operation to find an LDAP user matching ``alice``, using:

   * the base DN ``ou=people,dc=example,dc=org``
   * the filter ``(uid=alice)``
   * a SUBTREE scope

#. If the search returns exactly 1 LDAP user, do an LDAP "bind" operation with the user's DN and the
   password ``userpass``
#. If the LDAP "bind" operation is successful, search in XiVO a user with an email matching the
   ``mail`` attribute of the LDAP user
#. If a XiVO user is found, success

To use an anonymous bind instead, the following configuration would be used:

.. code-block:: yaml

   ldap:
       uri: ldap://example.org
       bind_anonymous: True
       user_base_dn: ou=people,dc=example,dc=org
       user_login_attribute: uid
       user_email_attribute: mail

The backend can also works in a "no search" mode, for example with the following configuration:

.. code-block:: yaml

   ldap:
       uri: ldap://example.org
       user_base_dn: ou=people,dc=example,dc=org
       user_login_attribute: uid
       user_email_attribute: mail

When the server receives the same authentication request as above, it will directly do an
LDAP "bind" operation with the DN ``uid=alice,ou=people,dc=example,dc=org`` and password
``userpass``, and continue at step 5.

.. note:: User's email and voicemail's email are two separate things. This plugin only use the
   user's email.


Configuration
^^^^^^^^^^^^^

``uri``
   the URI of the LDAP server. Can only contain the scheme, host and port of an LDAP URL.
``user_base_dn``
   the base dn of the user
``user_login_attribute``
   the attribute to login a user
``user_email_attribute`` (optional)
   the attribute to match with the XiVO user's email (default: mail)
``bind_dn`` (optional)
   the bind DN for searching for the user DN.
``bind_password`` (optional)
   the bind password for searching for the user DN.
``bind_anonymous`` (optional)
   use anonymous bind for searching for the user DN (default: false)
