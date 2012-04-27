.. index:: single:XiVO Client

.. _build_xivoclient:

************************
Building the XiVO Client
************************

This page explains how to build an executable of the XiVO Client from its
sources for GNU/Linux and Windows.


GNU/Linux Prerequisites
=======================

* Qt library development files (package ``libqt4-dev`` on Debian and derivatives)
* Git (package ``git``)
* Generic software building tools : ``make``, ``g++`` ... (package ``build-essential``)


Windows Prerequisites
=====================

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


Mac OS Prerequisites
=====================

Developer tools
---------------

You will need an Apple developer account to get development tools, such as
GCC. To log in or sign in, go to http://connect.apple.com. In the Downloads
section, get the Command line Tools for XCode and install them. You might want
to get XCode too, but it is rather big.


Qt SDK
------

`Qt SDK download page <http://qt.nokia.com/downloads>`_

The SDK is rather big, so if you want to keep it to a reasonable size, you
should uncheck in the installer everything fancy, such as mobile devices
SDK. Just keep one Desktop Qt component checked.


Add Qt to your PATH
-------------------

Once the Qt SDK is installed, by default in your home directory, you should add
the Qt binaries directory to your shell path. For BASH, you should edit the file
~/.profile (or create it) and add the following lines ::

   PATH=/Users/demo-mac/QtSDK/Desktop/Qt/4.8.0/gcc/bin:$PATH
   export PATH

The path shown here is only an example, you should adapt it to your
installation.


Get sources
===========

In a bash or Cygwin shell, enter::

   $ git clone git://git.xivo.fr/official/xivo-client-qt.git


Note for Windows users only
===========================

All make commands are to be entered in a Qt command shell, by replacing ``make``
with ``mingw32-make``.


Building
========

Launch qmake to generate the Makefile::

   $ cd xivo-client-qt
   $ qmake

This will also generate a file ``versions.mak`` that contains version
informations about the code being compiled. It is necessary for compilation and
packaging.

You can then launch ``make``::

   $ make

Binaries are available in the ``bin`` directory.

The version of the executable is taken from the ``git describe`` command.


Debug build
-----------

Add ``DEBUG=yes`` on the command line::

   $ make DEBUG=yes


Cleaning
--------

::

   $ make distclean


Launch
======

On GNU/Linux systems, you can launch the built executable with::

   $ LD_LIBRARY_PATH=bin bin/xivoclient

On Windows::

   > bin\xivoclient

On Mac OS::

   $ DYLD_LIBRARY_PATH=bin open bin/xivoclient.app/Contents/MacOS/xivoclient


Pack
====

Prerequisites for Windows
-------------------------

You will need NSIS installed.

If you keep the default path for NSIS (:file:`C:\\Program Files (x86)\\NSIS`),
you're done. If you changed it, you have to change the line in
:file:`xivoclient-all.pri` to set the new NSIS path.

Packing
-------

To create packages (that means an installer for Windows, a Debian package for
Debian and Ubuntu or an app bundle for Mac OS), the same command is used::

   $ make pack

This will result in a ``.exe`` or ``.deb`` or ``.dmg`` file in the current directory,
depending on your platform.

The version of the package is taken from the ``git describe`` command.
