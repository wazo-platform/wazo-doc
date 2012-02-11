************
Introduction
************

The auto-provisioning feature found in XiVO make it possible to provision, i.e.
configure, a lots of telephony devices in an efficient and effortless way.

How it works
============

Here's a simplified view of how auto-provisioning is supported on a typical SIP hardphone:

#. The phone is powered on
#. During its boot process, the phone sends a DHCP request to obtain its network configuration
#. A DHCP server replies with the phone network configuration + an HTTP URL
#. The phone use the provided URL to retrieve a common configuration file, a
   MAC-specific configuration file, a firmware image and some language files.

Building on this, configuring one of the supported phone on XiVO is as simple as:

#. :ref:`dhcpd-config`
#. :ref:`Installing the required provd plugin <provd-plugins-mgmt>`
#. Powering on the phone
#. Dialing the user's provisioning code from the phone

And *voila*, once the phone has rebooted, your user is ready to make and receive calls.
No manual editing of configuration files nor fiddling in the phone's web interface.

External links
==============

* `Introduction to provd plugin model <http://blog.xivo.fr/index.php?post/2011/04/11/Introduction-to-the-plugin-model-of-the-new-provisioning-server>`_
* `HTTP/TFTP requests processing in provd - part 1 <http://blog.xivo.fr/index.php?post/2012/02/09/HTTP/TFTP-requests-processing-in-provd-part-1>`_
