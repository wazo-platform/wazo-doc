*************************
Profiling Python Programs
*************************

Profiling CPU/Time Usage
========================

Here's an example on how to profile xivo-ctid for CPU/time usage:

#. Stop the monit daemon::

      service monit stop

#. Stop the process you want to profile, i.e. xivo-ctid::

      service xivo-ctid stop

#. Start the service in foreground mode running with the profiler::

      python -m cProfile -o test.profile /usr/bin/xivo-ctid -f

   This will create a file named ``test.profile`` when the process terminates.

   To profile xivo-confgend, you must use this command instead of the one above::

      twistd -p test.profile --profiler=cprofile --savestats -no --python=/usr/bin/xivo-confgend

   Note that profiling multi-threaded program (xivo-agid, xivo-confd) doesn't work reliably.

   The :ref:`debug-daemons` section documents how to launch the various Wazo services
   in foreground/debug mode.

#. Examine the result of the profiling::

      $ python -m pstats test.profile
      Welcome to the profile statistics browser.
      % sort time
      % stats 15
      ...
      % sort cumulative
      % stats 15


Measuring Code Coverage
=======================

Here's an example on how to measure the code coverage of xivo-ctid.

This can be useful when you suspect a piece of code to be unused and you
want to have additional information about it.

#. Install the following packages::

      apt-get install python-pip build-essential python-dev

#. Install coverage via pip::

      pip install coverage

#. Run the program in foreground mode with ``coverage run``::

      service monit stop
      service xivo-ctid stop
      coverage erase
      coverage run /usr/bin/xivo-ctid -f

   The :ref:`debug-daemons` section documents how to launch the various Wazo service
   in foreground/debug mode.

#. After the process terminates, use ``coverage html`` to generate
   an HTML coverage report::

      coverage html --include='*xivo_cti*'

   This will generate an :file:`htlmcov` directory in the current directory.

#. Browse the coverage report.

   Either copy the directory onto your computer and open it with a web browser,
   or start a web server on the Wazo::

      cd htmlcov
      python -m SimpleHTTPServer

   Then open the page from your computer (i.e. not on the Wazo)::

      firefox http://<wazo-hostname>:8000


External Links
==============

* `Official python documentation <http://docs.python.org/library/profile.html>`_
* `PyMOTW <http://blog.doughellmann.com/2008/08/pymotw-profile-cprofile-pstats.html>`_
* `coverage.py <http://nedbatchelder.com/code/coverage/>`_
