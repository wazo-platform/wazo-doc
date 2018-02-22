Upgrade from Wazo >= 18.01
==========================

Those procedures are valid if your Wazo installation is newer than 18.01.

Upgrade to specific Wazo
------------------------

Example to upgrade to Wazo 18.02::

  wazo-dist wazo-18.02
  apt-get update
  apt-get install xivo-upgrade/wazo-18.02
  wazo-upgrade
  wazo-dist phoenix-stretch


My Wazo is stuck in a specific version
--------------------------------------

Procedures for upgrading to specific versions may freeze the version of your Wazo. Run the following commands to get the latest updates::

  wazo-dist phoenix-stretch
  wazo-upgrade
