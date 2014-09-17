Apply configuration
===================

When done, you have to restart asterisk and dahdi::

   /etc/init.d/monit stop
   /etc/init.d/asterisk stop
   /etc/init.d/dahdi stop
   /etc/init.d/dahdi start
   /etc/init.d/asterisk start
   /etc/init.d/monit start
