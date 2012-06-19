************
XiVO service
************

XiVO has many running services. To restart the whole stack, the *xivo-service* command can
be used to make sure the service is restarted in the right order.


Usage
-----

Stop all services::

    xivo-service stop

Start all services::

    xivo-service start

Restart all services::

    xivo-service restart

Show services status::

    xivo-service status

UDP port 5060 will be closed while services are restarting.
