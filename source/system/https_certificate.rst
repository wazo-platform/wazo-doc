.. _https_certificate:

*****************
HTTPS certificate
*****************

X.509 certificates are used to authorize and secure communications with the server. They are mainly
used for HTTPS, but can also be used for SIPS, CTIS, etc.

There are two categories of certificates in XiVO:

* the default certificate, used for HTTPS in the web interface and REST APIs
* the certificates created and managed via the web interface

This article is about the former. For the latter, see :ref:`telephony_certificates`.

HTTPS
=====

XiVO uses HTTPS where possible. The certificates are generated at install time (or
during the :ref:`upgrade to 15.12+ <upgrade-note-15.12>`). The main certificate is placed in
:file:`/usr/share/xivo-certs/server.crt`.

However, this certificate is self-signed, and HTTP clients (browser or REST API client) will
complain about this default certificate because it is not signed by a trusted Certification
Authority (CA). To make the HTTP client accept this certificate, you have two choices:

* replace the self-signed certificate with your own trusted certificate. For this, you can replace
  the following files:

  * Private key: :file:`/usr/share/xivo-certs/server.key`
  * Certificate: :file:`/usr/share/xivo-certs/server.crt`

* configure your HTTP client to trust the self-signed certificate by adding a new trusted CA. The CA
  certificate (or bundle) is the file :file:`/usr/share/xivo-certs/server.crt`.
