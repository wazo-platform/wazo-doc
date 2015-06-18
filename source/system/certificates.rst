************
Certificates
************

X.509 certificates are used to secure communications and authenticate the server. They are mainly
used for HTTPS, but can also be used for SIPS, SRTP, CTIS, etc.

There are two categories of certificates in XiVO:

* the default certificate, used for HTTPS in the web interface and REST APis
* the certificates generated via the web interface, manageable in the web interface

HTTPS
=====

XiVO uses HTTPS where possible, and the certificate used for it is generated at install time (or
during the :ref:`upgrade to 15.12+ <upgrade-note-15.12>`). The main certificate is placed in
:file:`/usr/share/xivo-certs/server.crt`.

However, this certificate is self-signed, and any HTTP client (browser or REST API client) will
complain about this default certificate, because it will not be trusted. To make the HTTP client
accept this certificate, you have two choices:

* replace the self-signed certificate with your own trusted certificate. For this, you can replace
  the following files:

  * Private key: :file:`/usr/share/xivo-certs/server.key`
  * Certificate: :file:`/usr/share/xivo-certs/server.crt`

* configure your HTTP client to trust the self-signed certificate by adding a new trusted CA. The CA
  certificate (or bundle) is the file :file:`/usr/share/xivo-certs/server.crt`.

Other certificates
==================

XiVO enables you to use SIPS, SRTP or CTIS (encrypted CTI protocol), but for that, you need to
create new X.509 certificates so that they are available in the web interface. You can manage these
certificates in :menuselection:`Configuration > Certificates`.
