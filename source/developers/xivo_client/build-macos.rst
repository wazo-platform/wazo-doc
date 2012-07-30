.. index:: single:XiVO Client

**********************************
Building the XiVO Client on Mac OS
**********************************

This page explains how to build an executable of the XiVO Client from its
sources for Mac OS.


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

In a bash shell, enter::

   $ git clone git://git.xivo.fr/official/xivo-client-qt.git


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

You can launch the built executable with::

   $ DYLD_LIBRARY_PATH=bin open bin/xivoclient.app/Contents/MacOS/xivoclient


Package
=======

To create the app bundle::

   $ make pack

This will result in a ``.dmg`` file in the current directory.

The version of the package is taken from the ``git describe`` command.
