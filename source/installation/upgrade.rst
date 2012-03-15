*********
Upgrading
*********

Upgrading to XiVO 1.2 from a previous version (i.e. XiVO 1.1) is not supported right now.

To upgrade to the latest version, you **MUST** use xivo-upgrade::

   /usr/sbin/xivo-upgrade

.. note:: You can't use xivo-upgrade if you have not run the wizard

This script will update XiVO and restart all daemons.

There are 2 options for xivo-upgrade:

* ``-d`` to only download packages, no package will be installed
* ``-f`` to force upgrade, do not ask for user confirmation
