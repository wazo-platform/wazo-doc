*********************
Installing the System
*********************

There is three official ways to install XiVO:

* using the official ISO image
* using a minimal Debian installation and the XiVO installation script
* using a PXE environment (not detailed here)

XiVO can be installed on both virtual (QEMU/KVM, VirtualBox, ...) and physical machines. That said, since
VoIP/Asterisk is sensible to timing issues, you might get better results by installing XiVO on real
hardware.


Installing from the ISO image
=============================

The ISO image for XiVO |version| can be found at http://mirror.xivo.fr/iso/.


Installing from a minimal Debian installation
=============================================

XiVO can be installed directly over a **32-bit** Debian squeeze. When doing so, you are strongly
advised to start with a clean and minimal installation of Debian squeeze. Latest installation image
for Debian squeeze can be found at http://www.debian.org/distrib/.

Once you have your properly installed Debian squeeze, log into it and download the XiVO installation script::

   wget http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh

And run it::

   bash xivo_install_skaro.sh

.. note::

   For testing purposes, you can alternatively install the release candidate or developement version
   of XiVO from the script. Beware that there is no guarantee that these versions will work nor
   upgrade correctly.

   To install the release candidate version::

      bash xivo_install_skaro.sh -r

   To install the developement version::

      bash xivo_install_skaro.sh -d
