*******************
Proxy Configuration
*******************

If you use XiVO behind an HTTP proxy, you must do a couple of manipulations for
it to work correctly.


Global configuration
====================

Some programs are able to use proxy information the ``http_proxy`` environment variables.
You can set and export this variable with::

   export http_proxy=http://domain\username:password@proxyip:proxyport

where

* domain : the user's domain
* username : the username used to login via the proxy
* password : the password used to login via the proxy
* proxyip : the IP of the proxy
* proxyport : the port used by the proxy

If you need to have these settings ready at each connection, you can store them in your
:file:`~/.bashrc` file.

If you need to reset the ``http_proxy`` environment variable, issue the command::
    
    unset http_proxy

apt
===

Create the :file:`/etc/apt/apt.conf.d/90proxy` file with the following content::

   Acquire::http::Proxy "http://domain\username:password@proxyip:proxyport";


provd
=====

Proxy information is set via the :menuselection:`Configuration --> Provisioning --> General`
page.


dhcp-update
===========

*This step is needed if you use the DHCP server of the XiVO. Otherwise the DHCP configuration won't be correct.*

Proxy information is set via the :file:`/etc/xivo/dhcpd-update.conf` file.

Edit the file and look for the ``[proxy]`` section.


xivo-fetchfw
============

*This step is not needed if you don't use xivo-fetchfw.*

Proxy information is set via the :file:`/etc/xivo/xivo-fetchfw.conf` file.

Edit the file and look for the ``[proxy]`` section.


External links
==============

* `XiVO 1.1 and proxy server <https://wiki.xivo.io/index.php/XiVO_1.1-Gallifrey/XiVO_and_proxy_server>`_
