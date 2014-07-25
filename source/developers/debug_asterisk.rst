******************
Debugging Asterisk
******************

To debug asterisk crashes or freezes, you need the following packages on your xivo::

   apt-get install gdb asterisk-dbg xivo-libsccp-dbg

.. warning:: When installing theses packages you should take care that it doesn't drag a new version
    of asterisk since it would restart your asterisk


So There is a Problem with Asterisk. Now What ?
===============================================

#. Find out the time of the incident from the people most likely to know
#. Determine if there was a segfault

   #. The command ``grep segfault /var/log/syslog`` should return a line such as the following::

       Oct 16 16:12:43 xivo-1 kernel: [10295061.047120] asterisk[1255]: segfault at e ip b751aa6b sp b5ef14d4 error 4 in libc-2.11.3.so[b74ad000+140000]

   #. Note the exact time of the incident from the segfault line.
   #. Follow the `Debugging Asterisk Crash`_ procedure.

#. If you observe some of the following common symtoms, follow the `Debugging Asterisk Freeze`_
   procedure.

   * The output of command ``service asterisk status`` says Asterisk PBX is running.
   * No more calls are distributed and Phones go to ``No Service``.
   * Command ``core show channels`` returns only headers (no data) right before returning

#. Fetch Asterisk logs for the day of the crash (make sure file was not already logrotated)::

    cp -a /var/log/asterisk/full /var/local/`date +"%Y%m%d"`-`hostname`-asterisk-full.log

#. Fetch xivo-ctid logs for the day of the crash (make sure file was not already logrotated)::

    cp -a /var/log/xivo-ctid.log /var/local/`date +"%Y%m%d"`-`hostname`-xivo-ctid.log

#. Open a new issue on the `bugtracker <https://projects.xivo.io/projects/xivo/issues/new>`_ with
   following information

   * Tracker: Bug
   * Status: New
   * Category: Asterisk
   * In versions: The version of your XiVO installation where the crash/freeze happened
   * Subject : ``Asterisk Crash`` or ``Asterisk Freeze``
   * Description : Add as much context as possible, if possible, a scenario that lead to the issue,
     the date and time of issue, where we can fetch logs and backtrace
   * Attach logs and backtrace (if available) to the ticket (issue must be saved, then edited and
     files attached to a comment).


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
* http://blog.xivo.io/index.php?post/2012/10/24/Visualizing-asterisk-deadlocks
