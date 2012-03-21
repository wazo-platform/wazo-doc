*********
Upgrading
*********

.. warning::

   Before upgrading from XiVO 1.2.3 or earlier, you must do the following::

      wget http://mirror.xivo.fr/xivo_current.key -O - | apt-key add -

.. warning::

   Upgrading from 1.2.0 or 1.2.1 require a special procedure before executing xivo-upgrade::

      apt-get update
      apt-get install xivo-upgrade
      /usr/bin/xivo-upgrade

To upgrade your XiVO to the latest version, you **must** use xivo-upgrade::

   xivo-upgrade

.. note:: You can't use xivo-upgrade if you have not run the wizard

This script will update XiVO and restart all daemons.

There are 2 options for xivo-upgrade:

* ``-d`` to only download packages, no package will be installed
* ``-f`` to force upgrade, do not ask for user confirmation

Note that upgrading to XiVO 1.2 from a previous version (i.e. XiVO 1.1) is not supported right now.
