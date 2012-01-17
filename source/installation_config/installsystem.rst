*********************
Installing The System
*********************

Prerequisite
============

You must install XiVO skaro on a fresh debian system (minimal install). You can download debian installation media from http://www.debian.org/distrib

Installation
============

* You can download XiVO skaro installation script from http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh

::
    
 wget <nowiki>http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh</nowiki>

* With this script you can install 3 flavours of XiVO skaro:

- production version, run the script without argument:

::
    ./xivo_install_skaro.sh

- release canditate version:

::
    ./xivo_install_skaro.sh -r

- development version

::
    ./xivo_install_skaro.sh -d

Configuration
=============

After the installation, you have to go through the post installation procedure postinstall_ to complete the configuration.
