*********************
Installing the System
*********************

Please refer to the section :ref:`Troubleshooting <troubleshooting>` if ever you have errors during the installation.

There are three official ways to install XiVO:

* using the official ISO image
* using a minimal Debian installation and the XiVO installation script
* using a PXE environment (not detailed here)

XiVO can be installed on both virtual (QEMU/KVM, VirtualBox, ...) and physical machines. That said, since
Asterisk is sensible to timing issues, you might get better results by installing XiVO on real
hardware.

Installing from the ISO image
=============================

The ISO image for XiVO |version| can be found at http://mirror.xivo.fr/iso/xivo-current.
Download the iso, boot from it and follow the instructions on the installation prompt. 
We suggest that you *choose english as locale when prompted*.
At the end of the installation, you can continue by running the :ref:`configuration wizard. <configuration_wizard>`

Installing from a minimal Debian installation
=============================================

XiVO can be installed directly over a **32-bit** Debian squeeze. When doing so, you are strongly
advised to start with a clean and minimal installation of Debian squeeze. The latest installation image
for Debian squeeze can be found at http://www.debian.org/distrib/.

Once you have your Debian squeeze properly installed, log into it and download the XiVO installation script::

   wget http://mirror.xivo.fr/fai/xivo-migration/xivo_install_skaro.sh

And run it::

   bash xivo_install_skaro.sh

.. note::

   For testing purposes, you can alternatively install the release candidate or developement version
   of XiVO. Beware that there is no guarantee that these versions will work nor
   upgrade correctly.

   To install the release candidate version::

      bash xivo_install_skaro.sh -r

   To install the developement version::

      bash xivo_install_skaro.sh -d

Installing from a PXE
=====================

You can visit the `XiVO blog <http://blog.xivo.fr/index.php?q=pxe>`_ for more details on how to install from a PXE.
