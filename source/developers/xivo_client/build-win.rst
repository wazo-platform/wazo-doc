.. index:: single:XiVO Client

*********************************************
Building the XiVO Client on Windows platforms
*********************************************

This page explains how to build an executable of the XiVO Client from its
sources for Windows.


Windows Prerequisites
=====================

You will need Cygwin installed, as well as the Qt SDK.

Cygwin
------

`Cygwin Web site <http://www.cygwin.com/>`_

Click the "setup" link and execute.

During the installer, be sure to check the packages :

* Devel > git

Optionally, if you want the automatic documentation generation, check :

* Devel > doxygen

If you keep the default path for Cygwin (:file:`C:\\cygwin`), you're done. If you
changed it, you have to change the line in :file:`xivoclient-all.pri` to set the new
Cygwin path.


Qt SDK
------

`Qt SDK download page <http://qt.nokia.com/downloads>`_

The SDK is rather big, so if you want to keep it to a reasonable size, you
should uncheck in the installer everything fancy, such as mobile devices
SDK. Required elements are:

* Dev tools > Desktop Qt > one of them
* Miscellaneous > MinGW


Get sources
===========

In a **Cygwin shell**::

   $ git clone git://git.xivo.fr/official/xivo-client-qt.git


Building
========

Launch qmake to generate the Makefile ; in a **Qt command shell**::

   > cd C:\cygwin\path\to\xivo-client-qt
   > qmake

This will also generate a file ``versions.mak`` that contains version
informations about the code being compiled. It is necessary for compilation and
packaging.

You can then launch ``make``::

   > mingw32-make

Binaries are available in the ``bin`` directory.

The version of the executable is taken from the ``git describe`` command.


Build options
-------------

To generate debug symbols::

   > mingw32-make DEBUG=yes


Cleaning
--------

::

   > mingw32-make distclean


Launch
======

You can launch the built executable with::

   > bin\xivoclient


Package
=======

You will need NSIS installed.

If you keep the default path for NSIS (:file:`C:\\Program Files (x86)\\NSIS`),
you're done. If you changed it, you have to change the line in
:file:`xivoclient-all.pri` to set the new NSIS path.

Packing
-------

To create the installer::

   > mingw32-make pack

This will result in a ``.exe`` file in the current directory. You may have to
rename the file to set the right version.
