******************
Debugging Asterisk
******************

To debug asterisk crashes or freezes, you need the following packages on your xivo::

   apt-get install gdb asterisk-dbg xivo-libsccp-dbg

.. warning:: When installing theses packages you should take care that it doesn't drag a new version
    of asterisk since it would restart your asterisk


Debugging Asterisk Crash
========================

When asterisk crashes, it usually leaves a core file in :file:`/var/spool/asterisk/`.

You can create a backtrace from a core file named ``core_file`` with::

   gdb -batch -ex "bt full" -ex "thread apply all bt" asterisk core_file > bt-threads.txt


Debugging Asterisk Freeze
=========================

You can create a backtrace of a running asterisk process with::

   gdb -batch -ex "thread apply all bt" asterisk $(pidof asterisk) > bt-threads.txt

If your version of asterisk has been compiled with the DEBUG_THREADS flag, you can
get more information about locks with::

   asterisk -rx "core show locks" > core-show-locks.txt

.. note:: Debugging freeze without this information is usually a lot more difficult.

Optionally, other information that can be interesting:

* the output of ``asterisk -rx 'core show channels'``
* the verbose log of asterisk just before the freeze


Recompiling Asterisk
====================

It's relatively straightforward to recompile the asterisk version of your xivo with the
DEBUG_THREADS and DONT_OPTIMIZE flag, which make debugging an asterisk problem easier.

The steps are:

#. Uncomment the ``deb-src`` line for the xivo sources::

      sed -i 's/^#deb-src/deb-src/' /etc/apt/sources.list.d/xivo*

#. Fetch the asterisk source package::

      mkdir -p ~/ast-rebuild
      cd ~/ast-rebuild
      apt-get update
      apt-get source asterisk

#. Install the build dependencies::

      apt-get install build-essential
      apt-get build-dep asterisk

#. Enable the DEBUG_THREADS and DONT_OPTIMIZE flag::

      cd <asterisk-source-folder>
      vim debian/rules

#. Update the changelog by appending ``+debug1`` in the package version::

      vim debian/changelog

#. Rebuild the asterisk binary packages::

      dpkg-buildpackage -us -uc

This will create a couple of .deb files in the parent directory, which you can install
via dpkg.


External links
==============

* https://wiki.asterisk.org/wiki/display/AST/Debugging
* http://blog.xivo.fr/index.php?post/2012/10/24/Visualizing-asterisk-deadlocks
