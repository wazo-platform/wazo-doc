**********************************
Managing DHCP server configuration
**********************************

This page considers the configuration files of the DHCP server in :file:`/etc/dhcp/dhcpd_update/`.


Who modifies the files
======================

The files are updated with the command ``dhcpd-update``, which is also run when updating the provisioning plugins. This commands fetches configurations files from the ``provd.wazo.community`` server.


How to update the source files
==============================


Ensure your modifications are working
-------------------------------------

* On a XiVO, edit manually the file :file:`/etc/dhcp/dhcpd_update/*.conf`
* ``service isc-dhcp-server restart``
* If errors are shown in :file:`/var/log/daemon.log`, check your modifications


Edit the files
--------------

* Edit the files in the Git repo ``xivo-provd-plugins``, directory :file:`dhcp/`
* Push your modifications
* Go in :file:`dhcp/`
* Run ``make upload`` to push your modifications to ``provd.wazo.community``. There is no ``testing`` version of these files. Once the files are uploaded, they are available for all XiVO installations.
