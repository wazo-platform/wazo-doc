.. index:: single:XiVO Client

.. _build_xivoclient:

**************************
 Building the XiVO Client
**************************

This page explains how to build an executable of the XiVO Client from its sources for GNU/Linux and Windows.

Prerequisites
=============

GNU/Linux
---------

* Qt library development files (package libqt4-dev on Debian and derivatives)
* OpenSSL development files (package libssl-dev)
* Git (package git-core)

Windows
-------

Cygwin
^^^^^^

`Cygwin Web site <http://http://www.cygwin.com/>`_

Just click the "setup" link and execute.

During the installer, be sure to check the packages :

* Devel > git

Optionnally, if you want the automatic documentation generation, check :

* Devel > doxygen

Qt SDK
^^^^^^

`Qt SDK download page <http://qt.nokia.com/downloads>`_

The SDK is rather big, so if you want to keep it to a reasonable size, you should uncheck in the installer everything fancy, such as mobile devices SDK. Just keep one Desktop Qt component checked and some documentation.

Get sources
===========

In a bash or Cygwin shell, enter :::

 $ git clone git://git.proformatique.com/official/xivo-client-qt.git

Note for Windows users
======================

All make commands are to be entered in a Qt command shell, by replacing ``make`` with ``mingw32-make``.

Building
========

Launch qmake to generate the Makefile ::

 $ cd xivo-client-qt
 $ qmake

This will also generate a file ``versions.mak`` that contains version informations about the code being compiled. It is necessary for compilation.

You can then launch ``make`` ::

 $ make

Binaries are available in the ``bin`` directory.

Debug build
-----------

Add ``DEBUG=yes`` on the command line ::

 $ make DEBUG=yes

Cleaning
--------

::

 $ make distclean

Launch
======

On GNU/Linux systems, you can launch the built executable with :::

 $ LD_LIBRARY_PATH=bin bin/xivoclient

On Windows ::

 > bin\xivoclient
