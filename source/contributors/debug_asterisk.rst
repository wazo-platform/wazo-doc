******************
Debugging Asterisk
******************

Precondition
============

To debug asterisk crashes or freezes, you need the following debug packages on your XiVO:

+----------------+---------------------------------------------------------------+---------------------------------------------------------------+
|General rule    |XiVO < 14.18                                                   |XiVO >= 14.18                                                  |
|                |                                                               |                                                               |
+================+===============================================================+===============================================================+
|Example version |14.12                                                          |14.18                                                          |
+----------------+---------------------------------------------------------------+---------------------------------------------------------------+
|Commands        |::                                                             |::                                                             |
|                |                                                               |                                                               |
|                |   apt-get install xivo-fai-14.12                              |   xivo-dist xivo-14.18                                        |
|                |   apt-get update                                              |   apt-get update                                              |
|                |   apt-get install gdb                                         |   apt-get install gdb                                         |
|                |   apt-get install -t xivo-14.12 asterisk-dbg xivo-libsccp-dbg |   apt-get install -t xivo-14.18 asterisk-dbg xivo-libsccp-dbg |
|                |                                                               |                                                               |
+----------------+---------------------------------------------------------------+---------------------------------------------------------------+


So There is a Problem with Asterisk. Now What ?
===============================================

#. Find out the time of the incident from the people most likely to know
#. Determine if there was a segfault

   #. The command ``grep segfault /var/log/syslog`` should return a line such as the following::

       Oct 16 16:12:43 xivo-1 kernel: [10295061.047120] asterisk[1255]: segfault at e ip b751aa6b sp b5ef14d4 error 4 in libc-2.11.3.so[b74ad000+140000]

   #. Note the exact time of the incident from the segfault line.
   #. Follow the `Debugging Asterisk Crash`_ procedure.

#. If you observe some of the following common symptoms, follow the `Debugging Asterisk Freeze`_
   procedure.

   * The output of command ``service asterisk status`` says Asterisk PBX is running.
   * No more calls are distributed and phones go to ``No Service``.
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

It's relatively straightforward to recompile the asterisk version of your XiVO with the
DEBUG_THREADS and DONT_OPTIMIZE flag, which make debugging an asterisk problem easier.

The steps are:

#. Uncomment the ``deb-src`` line for the XiVO sources::

      sed -i 's/^# *deb-src/deb-src/' /etc/apt/sources.list.d/xivo*

#. Fetch the asterisk source package::

      mkdir -p ~/ast-rebuild
      cd ~/ast-rebuild
      apt-get update
      apt-get install -y build-essential
      apt-get source asterisk

#. Install the build dependencies::

      apt-get build-dep -y asterisk

#. Enable the DEBUG_THREADS and DONT_OPTIMIZE flag::

      cd <asterisk-source-folder>
      vim debian/rules

#. Update the changelog by appending ``+debug1`` in the package version::

      vim debian/changelog

#. Rebuild the asterisk binary packages::

      dpkg-buildpackage -us -uc

This will create a couple of .deb files in the parent directory, which you can install
via dpkg.

Recompiling a vanilla version of Asterisk
-----------------------------------------

It is sometimes useful to produce a "vanilla" version of Asterisk, i.e. a version of Asterisk that
has none of the XiVO patches applied, to make sure that the problem is present in the original
upstream code. This is also sometimes necessary before opening a ticket on the `Asterisk issue
tracker <https://issues.asterisk.org>`_.

The procedure is similar to the one described above. Before calling ``dpkg-buildpackage``, you just need to:

#. Make sure ``quilt`` is installed::

      apt-get install -y quilt

#. Unapply all the currently applied patches::

      quilt pop -a

#. Remove all the lines in the ``debian/patches/series`` file::

      truncate -s0 debian/patches/series

When installing a vanilla version of Asterisk on a XiVO, you'll need stop monit, otherwise it will
restart asterisk every few minutes.


Running Asterisk under Valgrind
===============================

#. Install valgrind::

      apt-get install valgrind

#. Recompile asterisk with the DONT_OPTIMIZE flag.
#. Edit :file:`/etc/asterisk/modules.conf` so that asterisk doesn't load unnecessary modules.
   This step is optional. It makes asterisk start (noticeably) faster and often makes the
   output of valgrind easier to analyze, since there's less noise.
#. Edit :file:`/etc/asterisk/asterisk.conf` and comment the ``highpriority`` option. This step
   is optional.
#. Stop monit and asterisk::

      monit quit
      service asterisk stop

#. Stop all unneeded XiVO services. For example, it can be useful to stop xivo-ctid, so that
   it won't interact with asterisk via the AMI.
#. Copy the valgrind.supp file into /tmp. The valgrind.supp file is located in the contrib
   directory of the asterisk source code.
#. Execute valgrind in the /tmp directory::

      cd /tmp
      valgrind --leak-check=full --log-file=valgrind.txt --suppressions=valgrind.supp --vgdb=no asterisk -G asterisk -U asterisk -fnc

Note that when you terminate asterisk with Control-C, asterisk does not unload the modules before
exiting. What this means is that you might have lots of "possibly lost" memory errors due to that.
If you already know which modules is responsible for the memory leak/bug, you should explicitly
unload it before terminating asterisk.

Running asterisk under valgrind takes a lots of extra memory, so make sure you have enough RAM.


External links
==============

* https://wiki.asterisk.org/wiki/display/AST/Debugging
* http://blog.xivo.io/visualizing-asterisk-deadlocks.html
* https://wiki.asterisk.org/wiki/display/AST/Valgrind
