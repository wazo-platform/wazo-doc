.. _https_certificate:

**********************
Certificates for HTTPS
**********************

X.509 certificates are used to authorize and secure communications with the server. They are mainly
used for HTTPS, but can also be used for SIPS, CTIS, WSS, etc.

There are two categories of certificates in Wazo:

* the default certificate, used for HTTPS in the web interface, REST APIs and WebSockets
* the certificates created and managed via the web interface

This article is about the former. For the latter, see :ref:`telephony_certificates`.


Default certificate
===================

Wazo uses HTTPS where possible. The certificates are generated at install time (or
during the :ref:`upgrade to 15.12+ <upgrade-note-15.12>`). The main certificate is placed in
:file:`/usr/share/xivo-certs/server.crt`.

However, this certificate is self-signed, and HTTP clients (browser or REST API client) will
complain about this default certificate because it is not signed by a trusted Certification
Authority (CA).


The default certificate is untrusted
====================================

To make the HTTP client accept this certificate, you have two choices:

* configure your HTTP client to trust the self-signed Wazo certificate by adding a new trusted CA.
  The CA certificate (or bundle) is the file :file:`/usr/share/xivo-certs/server.crt`.
* replace the self-signed certificate with your own trusted certificate.


Use your own certificate
========================

For this, follow these steps:

1. Replace the following files with your own private key/certificate pair:

   * Private key: :file:`/usr/share/xivo-certs/server.key`
   * Certificate chain: :file:`/usr/share/xivo-certs/server.crt`

   The certificate chain file ``server.crt`` must contain all necessary certificates to verify that
   it is trusted. In particular, if you got your certificate from a provider, ``server.crt`` must
   contain the intermediary certificates, allowing the client to follow the trust chain from the CA
   down to your certificate. There are three possible situations:

   * The certificate provider gave you only the certificate file. In this case, you don't have much
     choice and the certificate file will serve as ``server.crt``
   * The certificate provider gave you a complete chain file (also called bundle) and you must use
     this complete chain file as ``server.crt``.
   * The certificate provider gave you (among others) two different files: a certificate file and an
     "intermediate" file containing all intermediate certificates. You must get those two files into
     one with the following command::

      cat certificate.crt intermediate.pem > full-certificate-chain.pem

     Then ``full-certificate-chain.pem`` must be used for ``server.crt``.

   Both ``server.crt`` and ``server.key`` **must** be readable by the group ``www-data``. You can
   check with the following command::

      sudo -u www-data cat /usr/share/xivo-certs/server.{key,crt}

2. Change the hostname of Wazo for each Wazo component: the different processes of Wazo heavily use
   HTTPS for internal communication, and for these connection to establish successfully, all
   hostnames used must match the Common Name (CN) of your certificate. Basically, you must replace
   all occurrences of ``localhost`` (the default hostname) with your CN in the :ref:`configuration
   of the Wazo services <configuration-files>`. For example::

      mkdir /etc/xivo/custom
      cat > /etc/xivo/custom/custom-certificate.yml << EOF
      consul:
        host: wazo.example.com
      agentd:
        host: wazo.example.com
      ajam:
        host: wazo.example.com
      amid:
        host: wazo.example.com
      auth:
        host: wazo.example.com
      confd:
        host: wazo.example.com
      call_logd:
        host: wazo.example.com
      ctid_ng:
        host: wazo.example.com
      dird:
        host: wazo.example.com
      plugind:
        host: wazo.example.com
      websocketd:
        host: wazo.example.com
      EOF
      for config_dir in /etc/{xivo,wazo}-*/conf.d/ ; do
          ln -s "/etc/xivo/custom/custom-certificate.yml" "$config_dir/010-custom-certificate.yml"
      done

   Also, you must replace ``localhost`` in the definition of your directories in the web interface
   under :menuselection:`Configuration --> Directories`.

3. If your certificate is not self-signed, and you obtained it from a third-party CA that is trusted
   by your system, you must enable the system-based certificate verification. By default,
   certificate verification is set to consider ``/usr/share/xivo-certs/server.crt`` as the only CA
   certificate.

   The options are the following:

   * Consul: ``verify: True``
   * Other Wazo services: ``verify_certificate: True``

   The procedure is the same as 2. with more configuration for each service. For example::

      cat > /etc/xivo/custom/custom-certificate.yml << EOF
      consul:
        host: wazo.example.com
        verify: True
      agentd:
        host: wazo.example.com
        verify_certificate: True
      ajam:
        host: wazo.example.com
        verify_certificate: True
      ...

   Setting ``verify_certificate`` to ``False`` will disable the certificate verification, but the
   connection will still be encrypted. This is pretty safe as long as Wazo services stay on the same
   machine, however, this is dangerous when Wazo services are separated by an untrusted network,
   such as the Internet.

4. You need an entry in :file:`/etc/hosts` resolving your CN to ``127.0.0.1``. For this, *do not*
   edit the file manually, because your modifications will be rewritten when you "Apply system
   configuration" from the web interface. Instead, create a custom template for :file:`/etc/hosts`,
   and this template will be used when generating :file:`/etc/hosts`::

      mkdir -p /etc/xivo/custom-templates/system/etc
      sed 's/127\.0\.1\.1/127.0.0.1/' /usr/share/xivo-config/templates/system/etc/hosts > /etc/xivo/custom-templates/system/etc/hosts
      xivo-update-config

   You can check the configuration with the following command, it should give you ``127.0.0.1``::

      getent ahosts wazo.example.com

5. Edit your directories of type `xivo` to add you certificate CA path.

   In the web interface under :menuselection:`Configuration -> Directories` edit all directories.
   For each directory of type `xivo` modify the `Authentication Server Verify Certificate` and
   `Directory Server Verify Certificate` to `Custom` if using a self-signed certificate or `Yes` for
   a certificate trusted by your system.

   If you are using a self-signed certificate add the path to your certificate file in the
   `Authentication Server Custom CA Certificate` and `Directory Server Custom CA Certificate`
   fields.

6. Restart all Wazo services::

      wazo-service restart all


Troubleshooting
===============

Here are a few commands that can help find what is wrong::

   # Tell me curl, what is the problem with my certificate?
   curl https://localhost:443

   # Tell me openssl, what is the problem with my certificate?
   openssl s_client -connect localhost:443 >/dev/null </dev/null

   # Check that nginx has the right certificate loaded
   grep -R ssl /etc/nginx/sites-enabled/

   # See the certificate returned by nginx
   openssl s_client -connect localhost:443 </dev/null

   # See the certificate chain returned by nginx
   openssl s_client -connect localhost:443 </dev/null 2>/dev/null | sed -ne '/Certificate chain/,/---/p'

Note that you can replace 443 with the ports of the Wazo daemons, e.g. 9497 for wazo-auth. See the
full list in :ref:`network_ports`.
