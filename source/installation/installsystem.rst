.. _install:

*********************
Installing the System
*********************

Please refer to the section :ref:`Troubleshooting <troubleshooting>` if ever you have errors during the installation.

There are two official ways to install XiVO:

* using the official ISO image
* using a minimal Debian installation and the XiVO installation script

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

XiVO can be installed directly over a **32-bit** or a **64-bit** Debian jessie. When doing so, you are strongly
advised to start with a clean and minimal installation of Debian jessie.

The latest installation image for Debian jessie can be found at https://www.debian.org/releases/jessie/debian-installer.


Requirements
^^^^^^^^^^^^

The installed Debian must:

* use the architecure ``i386`` or ``amd64``
* have a default locale with charset UTF-8

In case you want to migrate a XiVO from ``i386`` to ``amd64``, see :ref:`migrate_i386_to_amd64`.


Installation
^^^^^^^^^^^^

Once you have your Debian jessie properly installed, download the XiVO installation script and make
it executable::

   wget http://mirror.xivo.io/fai/xivo-migration/xivo_install
   chmod +x xivo_install

And run it::

   ./xivo_install

At the end of the installation, you can continue by running the :ref:`configuration
wizard. <configuration_wizard>`


Alternatives versions
^^^^^^^^^^^^^^^^^^^^^

For testing purposes, you can alternatively install the release candidate or development version of
XiVO. Beware that there is no guarantee that these versions will work nor upgrade correctly, so you
should not use them on a production server.

To install the release candidate version::

   ./xivo_install -r

To install the development version::

   ./xivo_install -d

The installation script can also be used to install an :ref:`archive version <archive-version>` of
XiVO (14.18 or later only). For example, if you want to install XiVO 16.03::

   ./xivo_install -a 16.03

When installing an archive version, note that:

* version 14.18 to 15.19 of XiVO can only be installed on a Debian 7 (wheezy) system
* the 64-bit versions of XiVO are only available starting from 15.16


Other installation methods
==========================

It's also possible to install XiVO by PXE. More details available on our blog:

* `<http://blog.xivo.io/around-xivo-describe-industrial-installation-process.html>`_
* `<http://blog.xivo.io/around-xivo-pxe-server-setup.html>`_
* `<http://blog.xivo.io/around-xivo-pxe-and-preseeding.html>`_
