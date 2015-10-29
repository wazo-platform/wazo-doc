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


Default certificate
===================

XiVO uses HTTPS where possible. The certificates are generated at install time (or
during the :ref:`upgrade to 15.12+ <upgrade-note-15.12>`). The main certificate is placed in
:file:`/usr/share/xivo-certs/server.crt`.

However, this certificate is self-signed, and HTTP clients (browser or REST API client) will
complain about this default certificate because it is not signed by a trusted Certification
Authority (CA).


The default certificate is untrusted
====================================

To make the HTTP client accept this certificate, you have two choices:

* configure your HTTP client to trust the self-signed XiVO certificate by adding a new trusted CA.
  The CA certificate (or bundle) is the file :file:`/usr/share/xivo-certs/server.crt`.
* replace the self-signed certificate with your own trusted certificate.


Use your own certificate
========================

For this, follow the steps:

1. Replace the following files with your own private key/certificate pair:

  * Private key: :file:`/usr/share/xivo-certs/server.key`
  * Certificate: :file:`/usr/share/xivo-certs/server.crt`

2. Change the hostname of XiVO for each XiVO component: the different processes of XiVO heavily use
   HTTPS for internal communication, and for these connection to establish succesfully, all
   hostnames used must match the Common Name (CN) of your certificate. Basically, you must replace
   all occurences of ``localhost`` (the default hostname) with your CN in the :ref:`configuration of the
   XiVO services <configuration-files>`. For example::

      mkdir /etc/xivo/custom
      cat > /etc/xivo/custom/custom-certificate.yml << EOF
      consul:
        host: xivo.example.com
      auth:
        host: xivo.example.com
      dird:
        host: xivo.example.com
      ajam:
        host: xivo.example.com
      agent:
        host: xivo.example.com
      EOF
      for config_dir in /etc/xivo-*/conf.d/ ; do
          ln -s "/etc/xivo/custom/custom-certificate.yml" "$config_dir/010-custom-certificate.yml"
      done

   Also, you must replace ``localhost`` in the definition of your directories in the web interface
   under :menuselection:`Configuration --> Directories`.

3. If your certificate is not self-signed, and you obtained if from a system-trusted CA, you must
   also override the ``verify_certificate`` option to ``True``. By default, ``verify_certificate``
   is set to consider ``/usr/share/xivo-certs/server.crt`` as self-signed. The procedure is the same
   as 2. with more configuration for each service. For example::

      cat > /etc/xivo/custom/custom-certificate.yml << EOF
      consul:
        host: xivo.example.com
        verify_certificate: True
      auth:
        host: xivo.example.com
        verify_certificate: True
      ...

   Setting ``verify_certificate`` to ``False`` will disable the certificate verification, but the
   connection will still be encrypted. This is pretty safe as long as XiVO services stay on the same
   machine, however, this is dangerous when XiVO services are separated by an untrusted network,
   such as the Internet.

4. Restart all XiVO services::

      xivo-service restart all
