*************
Web Interface
*************

Configuration for development
=============================

Default error level for XiVO web interface is E_ALL & ~E_DEPRECATED & ~E_USER_DEPRECATED & ~E_RECOVERABLE_ERROR & ~E_STRICT

If you want to display warning or other error in your browser, edit the :file:`/etc/xivo/web-interface/xivo.ini`
and replace report_type level to 3::

   [error]
   level = E_ALL
   report_type = 3
   report_mode = 1
   report_func = 1
   email = john.doe@example.com
   file = /var/log/xivo-web-interface/error.log

You may also edit :file:`/etc/xivo/web-interface/php.ini` and change the error level, but you will need to restart the cgi::

   service spawn-fcgi restart


Interactive debugging in Eclipse
================================

Instructions for Eclipse 4.5.

On your XiVO:

#. Install php5-xdebug::

      apt-get install php5-xdebug

#. Edit the :file:`/etc/php5/cgi/conf.d/20-xdebug.ini` (or :file:`/etc/php5/conf.d/20-xdebug.ini` on
   wheezy) and add these lines at the end::

      xdebug.remote_enable=1
      xdebug.remote_host="<dev_host_ip>"

   where ``<dev_host_ip>`` is the IP address of your machine where Eclipse is installed.

#. Restart spawn-fcgi::

      service spawn-fcgi restart

On your machine where Eclipse is installed:

#. Make sure you have Eclipse PDT installed
#. Create a PHP project named ``xivo-web-interface``:

   * Choose "Create project at existing location", using the :file:`xivo-web-interface` directory

#. In the Window / Preferences / PHP menu:

   * Add a new PHP server with the following information:

      * Name: anything you want
      * Base URL: ``https://<xivo_ip>``
      * Path Mapping:

        * Path on Server: :file:`/usr/share/xivo-web-interface`
        * Path in Workspace: :file:`/xivo-web-interface/src`

#. Create a new ``PHP Web Application`` debug configuration:

   * Choose the PHP server you created in last step
   * Pick some file, which can be anything if you don't "break at first line"
   * Uncheck "Auto Generate", and set the path you want your browser to open when you'll
     launch this debug configuration.

Then, to start a debugging session, set some breakpoints in the code and launch your debug configuration.
This will open the page in your browser, and when the code will hit your breakpoints, you'll be able to go
through the code step by step, etc.
