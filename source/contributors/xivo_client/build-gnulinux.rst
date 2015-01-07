.. index:: single:XiVO Client

***********************************************
Building the XiVO Client on GNU/Linux platforms
***********************************************

This page explains how to build an executable of the XiVO Client from its sources for GNU/Linux.


Prerequisites
=============

* Qt5 library development files: `Qt website <http://qt-project.org/downloads>`_ (Ubuntu packages ``qt5-default qt5-qmake qttools5-dev-tools qttools5-dev``)
* openGL development library - libGL (Debian package ``libgl1-mesa-dev``)
* Git (Debian package ``git``)
* Generic software building tools : ``make``, ``g++`` ... (Debian package ``build-essential``)


Get sources
===========

In a bash shell::

   $ git clone git://github.com/xivo-pbx/xivo-client-qt.git


Building
========

You need to have the Qt5 binaries (qmake, lrelease, ...) in your $PATH.

Launch qmake to generate the Makefile::

   $ cd xivo-client-qt
   $ /path/to/qt5/bin/qmake

This will also generate a file ``versions.mak`` that contains version informations about the code
being compiled. It is necessary for compilation and packaging.

You can then launch ``make``::

   $ make

Binaries are available in the ``bin`` directory.

The version of the executable is taken from the ``git describe`` command.


Build options
-------------

To generate debug symbols::

   $ make DEBUG=yes

To compile the unit tests of the XiVO Client::

   $ qmake CONFIG+=tests

or, if you have a recent version of Google Mock (e.g. on Debian Wheezy)::

   $ qmake CONFIG+=tests CONFIG+=gmock

To compile the XiVO Client ready for functional tests::

   $ make FUNCTESTS=yes


Cleaning
--------

::

   $ make distclean


Launch
======

You can launch the built executable with::

   $ LD_LIBRARY_PATH=bin bin/xivoclient

Package
=======

To create the Debian package, usable on Debian and Ubuntu, you first need to modify
:file:`build-deps` to locate the Qt 5 installation directory::

   $ /path/to/qt5/bin/qmake -spec linux-g++
   $ make
   $ make pack

This will result in a ``.deb`` file in the current directory.

The version of the package is taken from the ``git describe`` command.
