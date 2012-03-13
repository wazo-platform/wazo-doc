*********
Upgrading
*********

Upgrading to 1.2 from a previous version is not supported right now.

.. warning:: You **should** run the wizard before using xivo-upgrade

To upgrade from a prior 1.2 version, you **MUST** use xivo-upgrade::

   /usr/sbin/xivo-upgrade

This script will update xivo and restart all daemons.

From skaro-1.2.4, there are 2 options for xivo-upgrade:

* -d to only download packages, no package will be installed
* -f to force upgrade, do not ask for user confirmation
