.. index:: single:XiVO Client

**********************************
Building the XiVO Client on Mac OS
**********************************

This page explains how to build an executable of the XiVO Client from its sources for Mac OS.


Mac OS Prerequisites
=====================

Developer tools
---------------

You will need an Apple developer account to get development tools, such as GCC. To log in or sign
in, go to the `Developer portal of Apple`_. In the Downloads section, get the Command line Tools for
XCode and install them. You might want to get XCode too, but it is rather big.

.. _Developer portal of Apple: https://developer.apple.com/downloads/index.action

Qt SDK
------

You need the development files of the Qt 5 library, available on the `Qt website
<http://qt-project.org/downloads>`_.


Get sources
===========

In a bash shell, enter::

   $ git clone git://github.com/xivo-pbx/xivo-client-qt.git


Building
========


Launch qmake to generate the Makefile::

   $ cd xivo-client-qt
   $ /path/to/qt5/bin/qmake -spec macx-g++

This will also generate a file ``versions.mak`` that contains version informations about the code
being compiled. It is necessary for compilation and packaging.

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

You can launch the built executable with::

   $ DYLD_LIBRARY_PATH=bin bin/xivoclient.app/Contents/MacOS/xivoclient


Package
=======

You need to have the bin directory of Qt in your $PATH.

To create the app bundle::

   $ make pack

This will result in a ``.dmg`` file in the current directory.

The version of the package is taken from the ``git describe`` command.
