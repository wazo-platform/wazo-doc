Upgrade from Wazo < 19.13
=========================

Those procedures are valid if your Wazo installation is newer than 19.03 and older than 19.10.


Upgrade to Wazo < 19.13
-----------------------

Example to upgrade to Wazo 19.05::

  wazo-dist -a wazo-19.05
  apt-get update
  apt-get install xivo-upgrade/wazo-19.05
  wazo-upgrade
  wazo-dist -m pelican-stretch


Upgrade to Wazo >= 19.13
------------------------

Example to upgrade to Wazo 19.13::

  wazo-upgrade

This will upgrade your Wazo to 19.12. From there:

1. Read the :ref:`upgrade notes<upgrade-notes-buster>`
2. Upgrade to Wazo 19.13::

     wazo-dist-upgrade -t wazo-19.13
     wazo-dist -m pelican-buster


My Wazo is stuck in a specific version
--------------------------------------

Procedures for upgrading to specific versions may freeze the version of your Wazo. Run the following commands to get the latest updates::

  wazo-dist -m pelican-stretch
  wazo-upgrade
