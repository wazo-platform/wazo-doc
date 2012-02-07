*********************
Installing the system
*********************

There is three official ways to install XiVO:

* using the official ISO image
* using a minimal Debian installation and the XiVO installation script
* using a PXE environment

Installing from the ISO image
=============================

The latest ISO image for XiVO |version| can be found at http://mirror.xivo.fr/iso/.

Installing from a minimal Debian installation
=============================================

XiVO can be installed over an already installed **32-bit** Debian squeeze. When doing so, you are
advised to start with a clean and minimal installation of Debian squeeze.

Latest installation image for Debian squeeze can be found at http://www.debian.org/distrib/.

Getting the installation script
-------------------------------

Download the XiVO installation script from http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh::

    wget http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh

With this script you can install 3 flavors of XiVO skaro:

* production version, by running the script without argument::

    bash xivo_install_skaro.sh

* release candidate version::

    bash xivo_install_skaro.sh -r

* development version::

    bash xivo_install_skaro.sh -d

.. note::
   When asked about the :file:`/etc/security/limits.conf` configuration file, answer ``Y``.
