********
Security
********

This page gives an overview of security best practices that should be applied to a Wazo
installation. This is not an exhaustive documentation but a starting point that should
be read to avoid common security issues.

Most of this page is aimed at servers that are accessible from the Internet.


fail2ban
========

Wazo comes with a pre-configured fail2ban. Fail2ban will block IP addresses that tried and
failed to gain access to the server. There are 3 jails that a configured.


asterisk-xivo
-------------

The "asterisk-xivo" jail watches the Asterisk log file for failed registration attempts.

The goal of this jail is make brute force attacks against SIP accounts harder.


xivo-provd
----------

The "xivo-provd" jail will block attempts to create new devices and request for configuration files.

The goal of this jail is limit DOS attacks by creating new devices and to protect against
brute force attacks trying to guess configuration file names.


sshd
----

The "sshd" jail protects against SSH brute force attacks.


Firewall
========

Wazo comes with iptables installed but does not configure any security rules. It is used by fail2ban
and by wazo-upgrade to block phone registration during an upgrade.


Devices
=======

Your devices, phones and gateways, should not be accessible from the Internet. If you have no choice
the passwords should be changed.

Some devices allow Wazo to change the password from the auto provisioning system. To change the default
values from the web-interface go to :menuselection:`Configuration -> Provisioning -> Template device`.

The admin and user password should be modified.


Open ports
==========

See the list of network ports that are listening to `0.0.0.0` in the :ref:`network_ports` page. Change the
service configurations for service that do not need to be accessible.
