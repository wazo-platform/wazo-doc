.. _wheezy:

*******************************
Debian 7 (wheezy) Upgrade Notes
*******************************

Before the upgrade
==================

* The upgrade will take longer than usual, because the whole Debian system will be upgraded
* The system must be restarted after the upgrade, because the Linux kernel will also be upgraded

LDAPS
-----

In case XiVO is using a LDAP server through SSL/TLS (LDAPS), the documentation instructed you to
append the certificate to :file:`/etc/ssl/certs/ca-certificates.crt`. However, this is the wrong way
to add a new certificate, because it will be erased by the upgrade.

To keep your certificate installed through the upgrade, you must follow the instructions given in
the :ref:`LDAP documentation <ldaps>`.


After the upgrade
=================

GRUB (Cloned Virtual Machines only)
-----------------------------------

GRUB installations on cloned virtual machines may lead to unbootable systems, if not fixed properly
before restarting the system. If xivo-upgrade detects your system is in a broken state, it will
display a few commands to repair the GRUB installation.
