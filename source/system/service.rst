************
xivo-service
************

Wazo has many running services. To restart the whole stack, the *xivo-service* command can
be used to make sure the service is restarted in the right order.


Usage
-----

Show all services status::

   xivo-service status

Stop XiVO services::

   xivo-service stop

Start XiVO services::

   xivo-service start

Restart XiVO services::

   xivo-service restart

The commands above will only act upon Wazo services. Appending an argument
``all`` will also act upon ``nginx`` and ``postgresql``. Example::

   xivo-service restart all

UDP port 5060 will be closed while services are restarting.
