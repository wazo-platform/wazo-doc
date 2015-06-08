******
Consul
******

The default `consul <https://consul.io>`_ installation in XiVO uses the
configuration file in ``/etc/consul/xivo/*.json``. All files in this directory
are installed with the package and *should not* be modified by the
administrator. To use a different configuration, the adminstrator can add it's
own configuration file at another location and set the new configuration
directory in the ``/etc/default/consul`` file.

The default installation generates a master token that can be retrieved in
``/usr/lib/consul/master_token``. This master token will not be used if a new
configuration is supplied.


Variables
=========

The following variables can be overridden in the ``/etc/default/consul`` file.

.. code-block:: sh

    CONFIG_DIR=/etc/consul/xivo         # The configuration directory
    USER=consul                         # The user used to run the consul process
    GROUP=consul                        # The group used to run the consul process
    PIDDIR=/var/run/consul              # The directory where the pidfile will be written
    PIDFILE=/var/run/consul/consul.pid  # The name of the pidfile (PIDDIR must match)
