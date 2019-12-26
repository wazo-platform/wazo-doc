*******************
Proxy Configuration
*******************

If you use Wazo behind an HTTP proxy, you must do a couple of manipulations for
it to work correctly.


apt
===

Create the :file:`/etc/apt/apt.conf.d/90proxy` file with the following content::

   Acquire::http::Proxy "http://domain\username:password@proxyip:proxyport";


provd
=====

Proxy information is set with ``wazo-provd`` endpoint ``/provd/configuration/http_proxy``.


dhcp-update
===========

*This step is needed if you use the DHCP server of the Wazo. Otherwise the DHCP configuration won't be correct.*

Proxy information is set via the :file:`/etc/xivo/dhcpd-update.conf` file.

Edit the file and look for the ``[proxy]`` section.


xivo-fetchfw
============

*This step is not needed if you don't use xivo-fetchfw.*

Proxy information is set via the :file:`/etc/xivo/xivo-fetchfw.conf` file.

Edit the file and look for the ``[proxy]`` section.

wazo-auth, wazo-dird
====================

*This step is needed for external contacts integration, like Google or Microsoft Office 356, or any other external source of contacts*

Add two files ``/etc/systemd/system/wazo-auth.service.d/proxy.conf`` and ``/etc/systemd/system/wazo-dird.service.d/proxy.conf`` with the same content::

   [Service]
   Environment=HTTP_PROXY=myproxy:8000  # replace myproxy with your proxy host and 8000 with your proxy port
   Environment=HTTPS_PROXY=myproxy:8000  # replace myproxy with your proxy host and 8000 with your proxy port for HTTPS
   Environment=NO_PROXY=localhost,127.0.0.1,127.0.1.1
