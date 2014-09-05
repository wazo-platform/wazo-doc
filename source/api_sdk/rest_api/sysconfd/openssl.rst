.. _openssl:

*********************
OpenSSL configuration
*********************

List certificates
=================

Query
-----

::

    GET /openssl_listcertificates


Get certificate infos
=====================

Query
-----

::

    GET /openssl_certificateinfos

Export public key
=================

Query
-----

::

    GET /openssl_exportpubkey

Export SSL certificate
======================

Query
-----

::

    GET /openssl_export

Create CA certificate
=====================

Query
-----

::

    POST /openssl_createcacertificate

Create certificate
==================

Query
-----

::

    POST / openssl_createcertificate

Delete certificate
==================

Query
-----

::

    GET /openssl_deletecertificate

Import SSL certificate
======================

Query
-----

::

    POST /openssl_import

