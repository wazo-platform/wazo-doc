*************
Web Interface
*************

Configuration for development
=============================

Default error level for XiVO web interface is E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED & ~E_RECOVERABLE_ERROR & ~E_STRICT

If you want to display warning or other error in your browser, edit the :file:`/etc/pf-xivo/web-interface/xivo.ini`
and replace report_type level to 3

::

      [error]
      level = 2047
      report_type = 3
      report_mode = 1
      report_func = 1
      email = john.doe@example.com
      file = /var/log/pf-xivo-web-interface/error.log



Interactive debugging in Eclipse
================================

On your XiVO:

#. Install php5-xdebug::

      $ apt-get install php5-xdebug

#. Edit the :file:`/etc/php5/conf.d/xdebug.ini` and add these lines at the end::

      xdebug.remote_enable=On
      xdebug.remote_host="<dev_host_ip>"
      xdebug.remote_port=9000
      xdebug.remote_handler="dbgp"

   where ``<dev_host_ip>`` is the IP address of your machine where Eclipse is installed.
   Of course, your XiVO must be able to reach this IP address.

#. Restart spawn-fcgi::

      $ /etc/init.d/spawn-fcgi restart

On your machine where Eclipse is installed:

#. Make sure you have `Eclipse PDT <http://www.eclipse.org/pdt/downloads/>`_ installed
#. In the Eclipse preferences, on the PHP / Debug page:

   * Set the PHP Debugger to XDebug
   * Add a new PHP server with the following information:

      * Name: anything you want
      * Base URL: ``https://<xivo_ip>``

#. Create a new ``PHP Web Application`` debug configuration:

   * Choose the PHP server you create on last step
   * Pick some file, which can be anything if you don't "break at first line"
   * Uncheck "Auto Generate", and set the path you want your browser to open when you'll
     launch this debug configuration.

Then, to start a debugging session, set some breakpoints in the code and launch your debug configuration.
This will open the page in your browser, and when the code will hit your breakpoints, you'll be able to go
through the code step by step, etc.
