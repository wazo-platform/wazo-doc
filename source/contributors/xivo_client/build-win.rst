.. index:: single:XiVO Client

*********************************************
Building the XiVO Client on Windows platforms
*********************************************

This page explains how to build an executable of the XiVO Client from its sources for Windows.


Windows Prerequisites
=====================

Cygwin
------

`Cygwin Web site <http://www.cygwin.com/>`_

Click the "setup" link and execute.

During the installer, check the package:

* Devel > git


Qt SDK
------

You need the development files of the Qt 5 library, available on the `Qt website
<http://qt-project.org/downloads>`_. The currently supported Qt version is 5.4.1.


NSIS (installer only)
---------------------

You will only need NSIS installed if you want to create an installer for the XiVO Client.

`NSIS download page <http://nsis.sourceforge.net/Download>`_

During the installer, choose the full installation.

The XiVO Client NSIS script file uses the NSIS Application Association Registration Plug-in.
Download and extract the plug-in and place the DLL from /Plugins in the NSIS/Plugins folder.

`NSIS Application Association Registration Plug-in download page
<http://nsis.sourceforge.net/Application_Association_Registration_plug-in#Download>`_


Get sources
===========

In a **Cygwin shell**::

   git clone git://github.com/xivo-pbx/xivo-client-qt.git
   cd xivo-client-qt


Building
========

Path configuration
------------------

You must change the values in :file:`C:\\Cygwin\\home\\user\\xivo-client-qt\\build-deps` to match
the paths of your installed programs. You must use an editor capable of understanding Unix end of
lines, such as `Notepad++ <http://notepad-plus-plus.org>`_.

Replace ``C:\`` with ``/cygdrive/c`` and backslashes (``\``) with slashes (``/``). You must respect
the case of the directory names. Paths containing spaces must be enclosed in double quotes (``"``).

For example, if you installed NSIS in :file:`C:\\Program Files (x86)\\nsis`, you should write::

   WIN_NSIS_PATH="/cygdrive/c/Program files (x86)/nsis"


Build
-----

In a **Cygwin shell**::

   source build-deps
   export PATH=$WIN_QT_PATH/bin:$WIN_MINGW_PATH/bin:$PATH

   qmake
   mingw32-make SHELL=

Binaries are available in the ``bin`` directory.

The version of the executable is taken from the ``git describe`` command.


Launch
======

You can launch the built executable with::

   source build_deps
   PATH=$WIN_QT_PATH/bin:$PATH bin/xivoclient


Package
=======

To create the installer::

   mingw32-make pack

This will result in a ``.exe`` file in the current directory.


Build options
=============

To add a console::

   qmake CONFIG+=console

To generate debug symbols::

   mingw32-make SHELL= DEBUG=yes


Clean
-----

::

   mingw32-make distclean
