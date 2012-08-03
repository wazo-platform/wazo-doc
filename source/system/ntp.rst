***
NTP
***

XiVO has a NTP server, that must be synchronized to a reference server. This can be a public one or customized for specific target networking architecture.
XiVO's NTP server is used by default as NTP server for the devices time reference.


Usage
=====

Show NTP service status::

   /etc/init.d/ntp status

Stop NTP service::

   /etc/init.d/ntp stop

Start NTP service::

   /etc/init.d/ntp start

Restart NTP service::

   /etc/init.d/ntp restart

Show NTP synchronization status::

   ntpq -p


Configuring NTP service
=======================

#. Edit :file:`/etc/ntp.conf`
#. Give your NTP reference servers::

    server 192.168.0.1                           # LAN existing NTP Server
    server 0.debian.pool.ntp.org iburst dynamic  # default in ntp.conf
    server 1.debian.pool.ntp.org iburst dynamic  # default in ntp.conf

#. If no reference server to synchronize to, add this to synchronize locally::

    server 127.127.1.0              # local clock (LCL)
    fudge 127.127.1.0 stratum 10    # LCL is not very reliable

#. Restart NTP service
#. Check NTP synchronization status.

.. warning:: If #5 shows that NTP doesn't use NTP configuration in :file:`/etc/ntp.conf`, maybe have
   you done a ``dhclient`` for one of your network interface and the dhcp server that gave the IP
   address also gave a NTP server address. Thus you might check if the file :file:`/var/lib/ntp/ntp.conf.dhcp`
   exists, if yes, this is used for NTP configuration prior to :file:`/etc/ntp.conf`. Remove it and
   restart NTP, check NTP synchronization status, then it should work.
