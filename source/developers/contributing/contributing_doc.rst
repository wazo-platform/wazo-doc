*********************************
Contributing to the documentation
*********************************

XiVO documentation is generated with Sphinx, documentation project source is in git://gitorious.org/xivo-doc/xivo-doc.git

Provided you already have Python installed on your system. You need first to install Sphinx_ : ``easy_install -U Sphinx`` [1]_.

.. _Sphinx: http://sphinx.pocoo.org/ 

Quick Reference

* http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt
* http://docutils.sourceforge.net/docs/user/rst/quickref.html
* http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html

.. [1] ``easy_install`` can be found in the debian package python-setuptools : ``sudo apt-get install python-setuptools``

Documentation guideline
=======================

.. highlight:: rest

Here's the guideline/conventions to follow for the XiVO documentation.

Language
--------

The documentation must be written in english, and only in english.

Sections
--------

* ``*`` with overline, for "file title"
* ``=``, for sections
* ``-``, for subsections
* ``^``, for subsubsections

Punctuation characters should be exactly as long as the section text.

Correct::

   Section1
   ========

Incorrect::

   Section2
   ==========

Lists
-----

Bullet lists::

   * First item
   * Second item

Autonumbered lists::

   #. First item
   #. Second item

Literal blocks
--------------

Use ``::`` on the same line as the line containing text when possible.

The literal blocks must be indented with three spaces.

Correct::

   Bla bla bla::

      apt-get update

Incorrect::

   Bla bla bla:

   ::

      apt-get update

Others
------

* There should be one and only one newline at the end of each file
* Lines should be at most 99 characters
