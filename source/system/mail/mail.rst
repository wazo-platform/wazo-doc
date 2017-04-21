.. _mail_configuration:

****
Mail
****

.. index:: mail

This section describes how to configure the mail server shipped with Wazo (Postfix) and the way Wazo
handles mails.

In :menuselection:`Configuration --> Network --> Mail`, the following options can be configured:

* :guilabel:`Domain Name messaging` : the server's displayed domain. Will appear in "Received" mail
  headers.
* :guilabel:`Source address of the server` : domain part of headers "Return-Path" and "From".
* :guilabel:`Relay SMTP` and :guilabel:`FallBack relay SMTP` : relay mail servers.
* :guilabel:`Rewriting shipping addresses` : Canonical address Rewriting. See `Postfix canonical
  documentation <http://www.postfix.org/ADDRESS_REWRITING_README.html#canonical>`_ for more info.

.. warning::
   Postfix, the mail server shipped with Wazo, should be stopped on an installed Wazo with no valid
   and reachable DNS servers configured. If Postfix is not stopped, messages will bounce in queues
   and could end up affecting core pbx features.

If you need to disable Postfix here is how you should do it::

     systemctl stop postfix
     systemctl disable postfix

If you ever need to enable Postfix again::

    systemctl enable postfix
    systemctl start postfix

Alternatively, you can empty Postfix's queues by issuging the following commands on the Wazo
server::

    postsuper -d ALL


Configure Wazo for authenticated SMTP
=====================================

Let's say we want to send mails from Wazo through the following SMTP server:

* SMTP host: ``smtp.example.com``
* SMTP port: ``587``
* SMTP user: ``smtp_user@example.com``
* SMTP password: ``smtp_password``

In :menuselection:`Configuration --> Mail`:

* set `Relay SMTP` to ``smtp.example.com:587``
* set `Source address of the server` to ``example.com``
* set `Rewriting shipping addresses` to something like ``asterisk stmp_user\nroot stmp_user\nxivo-agid stmp_user``

Then apply the changed in :menuselection:`Configuration --> Apply system configuration`.

Create a custom template for Postfix configuration::

   mkdir -p /etc/xivo/custom-templates/mail/etc/postfix
   cp /usr/share/xivo-config/templates/mail/etc/postfix/main.cf /etc/xivo/custom-templates/mail/etc/postfix/main.cf

Then, add at the end of the file ``/etc/xivo/custom-templates/mail/etc/postfix/main.cf``::

   smtp_sasl_auth_enable = yes
   smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
   smtp_sasl_security_options = noanonymous

Create the file ``/etc/postfix/sasl_passwd``::

   smtp.example.com:587 stmp_user@example.com:smtp_password

The SMTP hostname must be the exact same value than :menuselection:`Configuration --> Mail --> Relay
SMTP`.

The file containing the credentials must have specific permissions::

   chmod 400 /etc/postfix/sasl_passwd

Then regenerate the Postfix configuration (this does the same thing than
:menuselection:`Configuration --> Apply system configuration`)::

   update-xivo-config
