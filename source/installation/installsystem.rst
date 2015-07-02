*********************
Installing the System
*********************

Please refer to the section :ref:`Troubleshooting <troubleshooting>` if ever you have errors during the installation.

There are two official ways to install XiVO:

* using the official ISO image
* using a minimal Debian installation and the XiVO installation script

.. note:: For other unsupported ways of install XiVO please consult the bottom of the page


XiVO can be installed on both virtual (QEMU/KVM, VirtualBox, ...) and physical machines. That said, since
Asterisk is sensitive to timing issues, you might get better results by installing XiVO on real
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

XiVO can be installed directly over a **32-bit** or a **64-bit (beta)** Debian Wheezy. When doing so, you are strongly
advised to start with a clean and minimal installation of Debian Wheezy. The latest installation image
for Debian Wheezy can be found at https://www.debian.org/releases/wheezy/debian-installer.

Requirements
^^^^^^^^^^^^

The installed Debian must:

* use the architecure ``i386`` or ``amd64``
* have a default locale with charset UTF-8

.. note:: the use of ``amd64`` debian image is experimental


Installation
^^^^^^^^^^^^

Once you have your Debian Wheezy properly installed, download the XiVO installation script::

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


Unsupported installation methods
================================

Unofficial ways of installing:

* By PXE. More details available on our `XiVO blog <http://blog.xivo.io/index.php?q=pxe>`_
