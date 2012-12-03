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


Qt SDK
------

You need the development files of the Qt library (MinGW version).

`Qt SDK download page <http://qt-project.org/downloads>`_

You will also need MinGW itself, which is not embedded in the Qt installer.

`MinGW Installation notes <http://www.mingw.org/wiki/Getting_Started>`_

You will need these parts of MinGW::

   mingw-get install gcc g++ mingw32-make


NSIS (optional)
---------------

You will only need NSIS installed if you want to create an installer for the
XiVO Client.

`NSIS download page <http://nsis.sourceforge.net/Download>`_


Path configuration
------------------

You must change the values in :file:`xivoclient-all.pri` to match the paths of
your installed programs.


Get sources
===========

In a **Cygwin shell**::

   git clone git://git.xivo.fr/official/xivo-client-qt.git


Building
========

In a **Cygwin shell**::

   source xivoclient-all.pri
   export PATH=$WIN_QT_PATH/bin:$WIN_MINGW_PATH/bin:$PATH

   qmake
   mingw32-make

Binaries are available in the ``bin`` directory.

The version of the executable is taken from the ``git describe`` command.


Build options
-------------

To add a console::

   qmake CONFIG+=console

To generate debug symbols::

   mingw32-make DEBUG=yes


Cleaning
--------

::

   mingw32-make distclean


Launch
======

You can launch the built executable with::

   bin/xivoclient


Package
=======

To create the installer::

   mingw32-make pack

This will result in a ``.exe`` file in the current directory.
