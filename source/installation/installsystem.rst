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

* Download the ISO image. (`latest version`_) (`all versions`_)
* Boot from the ISO image, select ``Install`` and follow the instructions. You must select a locale
  with charset UTF-8.
* At the end of the installation, you can continue by running the :ref:`configuration
  wizard. <configuration_wizard>`

.. _all versions: http://mirror.xivo.io/iso/archives
.. _latest version: http://mirror.xivo.io/iso/xivo-current


Installing from a minimal Debian installation
=============================================

XiVO can be installed directly over a **32-bit** Debian Wheezy. When doing so, you are strongly
advised to start with a clean and minimal installation of Debian Wheezy. The latest installation image
for Debian Wheezy can be found at https://www.debian.org/releases/wheezy/debian-installer.

Requirements
^^^^^^^^^^^^

The installed Debian must:

* be in the architecure ``i386``
* have a default locale with charset UTF-8

Installation
^^^^^^^^^^^^

Once you have your Debian Wheezy properly installed, log into it and download the XiVO installation script::

   wget http://mirror.xivo.io/fai/xivo-migration/xivo_install_current.sh

And run it::

   bash xivo_install_current.sh

.. note::

   For testing purposes, you can alternatively install the release candidate or developement version
   of XiVO. Beware that there is no guarantee that these versions will work nor
   upgrade correctly.

   To install the release candidate version::

      bash xivo_install_current.sh -r

   To install the developement version::

      bash xivo_install_current.sh -d

At the end of the installation, you can continue by running the :ref:`configuration
wizard. <configuration_wizard>`


Installing from a PXE
=====================

You can visit the `XiVO blog <http://blog.xivo.io/index.php?q=pxe>`_ for more details on how to install from a PXE.
