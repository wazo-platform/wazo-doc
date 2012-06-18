******************
Debugging Asterisk
******************


Collecting debug information
----------------------------

See https://wiki.asterisk.org/wiki/display/AST/Collecting+Debug+Information

Asterisk segfault
-----------------

If asterisk segfault it should - in most cases - leave a coredump in :file:`/var/spool/asterisk/`.

Here's how to run extract a backtrace from a coredump left by asterisk after a segfault :

#. Install asterisk debug packages::

      apt-get install asterisk-dbg xivo-libsccp-dbg

#. Install ``gdb``::

      apt-get install gdb

#. Create a backtrace from the coredump where ``core_file`` is the path towards the coredump
   left by asterisk and ``backtrace_file.txt`` the name of the backtrace file you are going to generate::

      gdb -se "asterisk" -ex "bt full" -ex "thread apply all bt" --batch -c core_file > backtrace_file.txt

