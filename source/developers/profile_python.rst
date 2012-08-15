*************************
Profiling Python Programs
*************************

Profiling
=========

Here's how to profile a python program on XiVO:

#. Add the non-free repository to :file:`/etc/apt/sources.list`.

#. Install the ``python-profiler`` package::

      $ apt-get update
      $ apt-get install python-profiler

#. Stop the monit daemon::

      $ /etc/init.d/monit stop

#. Stop the process you want to profile, i.e. xivo-ctid for example::

      $ /etc/init.d/xivo-ctid stop

#. Start the service in foreground mode running with the profiler::

      $ python -m cProfile -o test.profile /usr/bin/xivo-ctid -d

   This will create a file named ``test.profile`` when the process will
   terminate.

   The :ref:`debug-daemons` section documents how to launch the various XiVO service
   in foreground/debug mode.

#. Examine the result of the profiling::

      $ python -m pstats test.profile
      Welcome to the profile statistics browser.
      % sort time
      % stats 15
      ...
      % sort cumulative
      % stats 15


External Links
==============

* `Official python documentation <http://docs.python.org/library/profile.html>`_
* `PyMOTW <http://blog.doughellmann.com/2008/08/pymotw-profile-cprofile-pstats.html>`_
