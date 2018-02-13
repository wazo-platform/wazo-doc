.. index:: single:Wazo Client

**********************************************
Building the Wazo Client for Windows platforms
**********************************************

This page explains how to build an executable of the Wazo Client from its sources for Windows. It uses cross-compilation from a Docker container, so you do not need a Windows machine to build. The following instructions are made to run on a Linux host.


Prerequisites
=============

* Docker installed on your machine, and access to Internet.
* A copy of the Wazo Client source code including the Git repository. This directory must be clean of binary files (``.o``, ``.dll``, ``.exe``, etc.).


Building the package
====================

Go to the ``wazo-client-qt`` cloned directory and run (first step will take a long time, about 1 hour)::

   docker build -t wazopbx/windows-x86-qt:5.5.0 -f packaging/windows/Dockerfile-windows-x86-qt packaging/windows
   docker build -t wazopbx/windows-x86-wazo-client-qt:qt-5.5.0 -f packaging/windows/Dockerfile-windows-x86-wazo-client-qt packaging/windows
   docker rm wazo-client-qt-build-win32
   docker run --name wazo-client-qt-build-win32 -v $PWD:/usr/src/wazo-client-qt wazopbx/windows-x86-wazo-client-qt:qt-5.5.0
   mkdir -p ./bin
   docker cp wazo-client-qt-build-win32:/usr/src/wazo-client-qt-build/bin/package-win32 ./bin

You will find the installer ready to install in ``./bin/package-win32``.


Build options
=============

For more options, you have to edit ``packaging/windows/Dockerfile-windows-x86-wazo-client-qt``.

To add a console::

   qmake CONFIG+=console

To generate debug symbols::

   make DEBUG=yes


Clean
-----

::

   make distclean
