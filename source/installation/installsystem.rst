*********************
Installing The System
*********************

Prerequisite
============

You must install XiVO skaro on a fresh debian system (minimal install).
You can download debian installation media from http://www.debian.org/distrib.

Get the script
==============

You can download XiVO skaro installation script from http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh::
    
    wget http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh

Installation
============

With this script you can install 3 flavours of XiVO skaro:

* production version, run the script without argument::

    bash xivo_install_skaro.sh

* release canditate version::

    bash xivo_install_skaro.sh -r

* development version::

    bash xivo_install_skaro.sh -d

You have to accept ``/etc/dahdi/genconf_parameters`` and ``/etc/security/limits.conf`` modifications.
