.. _mail_configuration:

****
Mail
****

.. index:: mail

This section describes how to configure the mail server shipped with XiVO (Postfix) and the way XiVO handles mails.

The following options can be configured :

* Domain Name messaging : the server's displayed domain. Will appear in "Received" mail headers.
* Source address of the server : domain part of headers "Return-Path" and "From".
* Relay SMTP and FallBack relay SMTP : relay mail servers.
* Rewriting shipping addresses : Canonical address Rewriting. See `Postfix caononical documentation <http://www.postfix.org/ADDRESS_REWRITING_README.html#canonical>`_ for more info.

.. warning::
   Postfix, the mail server shipped with XiVO, should be stopped on an installed XiVO with no valid and reachable DNS servers configured. If Postfix is not stopped, messages will bounce in queues and could end up affecting core pbx features.

If you need to disable Postfix here is how you should do it::

     /etc/init.d/postfix stop
     insserv -r postfix

If you ever need to enable Postfix again::

    insserv postfix
    /etc/init.d/postfix start

Alternatively, you can empty Postfix's queues by issuging the following commands on the XiVO server::

    postsuper -d ALL
