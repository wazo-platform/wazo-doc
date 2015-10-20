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
``/var/lib/consul/master_token``. This master token will not be used if a new
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


Agent mode
==========

It is possible to run consul on another host and have the local consul node run
as an agent only.

To get this kind of setup up and running, you will need to follow the following steps.

* Backup your consul key/value if doing a migration
* Download the the consul binary from https://dl.bintray.com/mitchellh/consul/0.5.2_linux_386.zip
* Install consul
* Copy the consul configuration from your XiVO to the new host
* Restart consul on the remote host *service consul restart*
* Add an agent configuration on the XiVO
* Enable the agent configuration in ``/etc/default/consul``
* Restart consul on the XiVO *service consul restart*
* Restore the consul backup on the remove consul host


Saving the Consul Key/Value
---------------------------

See the backup procedure :ref:`here <consul_backup>`.


Downloading Consul
------------------

For a 32 bits system

.. code-block:: sh

    wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.5.2_linux_386.zip


For a 64 bits system

.. code-block:: sh

     wget --no-check-certificate https://dl.bintray.com/mitchellh/consul/0.5.2_linux_amd64.zip


Installing Consul
-----------------

.. code-block:: sh

    unzip unzip 0.5.2_linux_386.zip
    mv consul /usr/bin/consul
    mkdir -p /etc/consul/xivo
    mkdir -p /var/lib/consul
    adduser --system --group --quiet \
                     --shell /bin/sh \
                     --home /var/lib/consul \
                     --no-create-home --disabled-login \
                     --gecos "Consul discovery service" \
                     consul


Copying the consul configuration from the XiVO to a new host
------------------------------------------------------------

.. code-block:: sh

    mkdir -p /tmp/consul/{var/lib/consul,etc/consul/xivo,etc/init.d}
    cd /tmp/consul
    scp <xivo-host>:/etc/init.d/consul ./etc/init.d
    scp -r <xivo-host>:/etc/consul ./etc
    scp -r <xivo-host>:/var/lib/consul ./var/lib
    scp -r . <consul-host>:/
    # On the remote consul host
    chown -R consul:consul /etc/consul
    chown -R consul:consul /var/lib/consul
    rm -rf /var/lib/consul/raft
    service consul start


Adding the agent configuration
------------------------------

Create the file ``/etc/consul/xivo/agent/config.json`` with the following content

.. code-block:: javascript

    {
        "node_name": "<node name>",
        "datacenter": "xivo",
        "acl_datacenter": "xivo",
        "client_addr": "0.0.0.0",
        "server": false,
        "bootstrap": false,
        "data_dir": "/var/lib/consul",
        "enable_debug": true,
        "log_level": "debug",
        "enable_syslog": true,
        "retry_join": [
            "<remote host>"
        ],
        "retry_interval": "5s",
        "disable_update_check": true
    }


The *node_name* field is an arbitrary name to give this node, ``xivo-paris`` for example.

The *remote_host* field need to be the ip address of your new consul.
Be sure the host is accessible from your XiVO and check the firewall.
See the documentation :ref:`here <network>`.


Enabling the agent configuration
--------------------------------

Add or modify ``/etc/default/consul`` to include the following lines

.. code-block:: sh

    CONFIG_DIR="/etc/consul/xivo/agent"


Update the consul section of xivo-ctid
--------------------------------------

Add a file in ``/etc/xivo-ctid/conf.d/remote_consul.yml`` with the following content

.. code-block:: yaml

    consul:
        advertise_address: <hostname to reach xivo-ctid>
        check_url: <the check URL to use to query xivo-ctid from consul>


Restoring the consul backup
---------------------------

See the documentation :ref:`here <restoring_consul>`.
