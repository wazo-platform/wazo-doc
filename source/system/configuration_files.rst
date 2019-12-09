.. _configuration-files:

*******************
Configuration Files
*******************

This section describes some of the Wazo configuration files.


.. _configuration-priority:

Configuration priority
======================

Usually, the configuration is read from two locations: a configuration file ``config.yml`` and a
configuration directory ``conf.d``.

Files in the ``conf.d`` extra configuration directory:

* are used in alphabetical order and the first one has priority
* are ignored when their name starts with a dot
* are ignored when their name does not end with ``.yml``

For example:

``.01-critical.yml``::

  log_level: critical

``02-error.yml.dpkg-old``::

  log_level: error

``10-debug.yml``::

  log_level: debug

``20-nodebug.yml``::

  log_level: info

The value that will be used for ``log_level`` will be ``debug`` since:

* ``10-debug.yml`` comes before ``20-nodebug.yml`` in the alphabetical order.
* ``.01-critical.yml`` starts with a dot so is ignored
* ``02-error.yml.dpkg-old`` does not end with ``.yml`` so is ignored


File configuration structure
============================

Configuration files for every service running on a Wazo server will respect these rules:

* Default configuration directory in :file:`/etc/xivo-{{service}}/conf.d` (e.g.
  :file:`/etc/wazo-agentd/conf.d/`)
* Default configuration file in :file:`/etc/xivo-{{service}}/config.yml` (e.g.
  :file:`/etc/wazo-agentd/config.yml`)

The files :file:`/etc/xivo-{{service}}/config.yml` should not be modified because **they will be
overridden during upgrades**. However, they may be used as examples for creating additional
configuration files as long as they respect the :ref:`configuration-priority`. Any exceptions to
these rules are documented below.


wazo-auth
=========

* Default configuration directory: :file:`/etc/wazo-auth/conf.d`
* Default configuration file: :file:`/etc/wazo-auth/config.yml`


wazo-agentd
===========

* Default configuration directory: :file:`/etc/wazo-agentd/conf.d`
* Default configuration file: :file:`/etc/wazo-agentd/config.yml`


wazo-amid
=========

* Default configuration directory: :file:`/etc/wazo-amid/conf.d`
* Default configuration file: :file:`/etc/wazo-amid/config.yml`


wazo-confgend
=============

* Default configuration directory: :file:`/etc/wazo-confgend/conf.d`
* Default configuration file: :file:`/etc/wazo-confgend/config.yml`
* Default templates directory: :file:`/etc/wazo-confgend/templates`


xivo-dao
========

* Default configuration directory: :file:`/etc/xivo-dao/conf.d`
* Default configuration file: :file:`/etc/xivo-dao/config.yml`

This configuration is read by many Wazo programs in order to connect to the Postgres database of
Wazo.


wazo-phoned
===========

* Default configuration directory: :file:`/etc/wazo-phoned/conf.d`
* Default configuration file: :file:`/etc/wazo-phoned/config.yml`


wazo-provd
==========

* Default configuration directory: :file:`/etc/wazo-provd/conf.d`
* Default configuration file: :file:`/etc/wazo-provd/config.yml`


wazo-websocketd
===============

* Default configuration directory: :file:`/etc/wazo-websocketd/conf.d`
* Default configuration file: :file:`/etc/wazo-websocketd/config.yml`


.. _xivo_ring.conf:

xivo_ring.conf
==============

* Path: :file:`/etc/xivo/asterisk/xivo_ring.conf`
* Purpose: This file can be used to change the ringtone played by the phone depending on the
  origin of the call.

.. warning:: Note that this feature has not been tested for all phones and all call flows.
  This page describes how you can customize this file but does not intend to list all validated
  call flows or phones.


This file :file:`xivo_ring.conf` consists of :

* profiles of configuration (some examples for different brands are already included: ``[aastra]``,
  ``[snom]`` etc.)
* one section named ``[number]`` where you apply the profile to an extension or a context etc.

Here is the process you should follow if you want to use/customize this feature :

#. Create a new profile, e.g.::

    [myprofile-aastra]

#. Change the ``phonetype`` accordingly, in our example::

    [myprofile-aastra]
    phonetype = aastra

#. Chose the ringtone for the different type of calls (note that the ringtone names are
   brand-specific)::

    [myprofile-aastra]
    phonetype = aastra
    intern = <Bellcore-dr1>
    group = <Bellcore-dr2>

#. Apply your profile, in the section ``[number]``

  * to a given list of extensions (e.g. 1001 and 1002)::

      1001@default = myprofile-aastra
      1002@default = myprofile-aastra

  * or to a whole context (e.g. default)::

     @default = myprofile-aastra

5. Restart ``wazo-agid`` service::

    service wazo-agid restart


.. _asterisk-configuration:

Asterisk configuration files
============================

Asterisk configuration files are located at `/etc/asterisk`. These files are packaged with
Wazo and you should not modify files that are located at the root of this directory.

To add you own configurations, you must add a new configuration file in the corresponding `.d`
directory.

For example, if you need to add a new user to the `manager.conf` configuration file, you would
add a new file `/etc/asterisk/manager.d/my_new_user.conf` with the following content::

.. code-block: ini

 [my_new_user]
 secret=v3ry5ecre7
 deny=0.0.0.0/0.0.0.0
 permit=127.0.0.1/255.255.255.0
 read = system

The same logic applies to all Asterisk configuration files except `asterisk.conf` and `modules.conf`.


Modifying the modules.conf
--------------------------

The ``/etc/asterisk/modules.conf`` file is automatically generated before Asterisk starts. Modifying
its content will do nothing as it's going to be overritten on the next Asterisk restart.

To enable modules in the ``modules.conf`` file the administrator has to configure :ref:`wazo-confgend`
to add the required modules to the content of the generated file.

This is done by adding the module name to the `enabled_asterisk_modules` section of the configuration.

Enabling res_cli_aliases
^^^^^^^^^^^^^^^^^^^^^^^^

1. Enable `res_cli_aliases.so` in the `wazo-confgend` configuration::

     cat <<EOF > /etc/wazo-confgend/conf.d/res_cli_aliases.yml
     enabled_asterisk_modules:
         res_cli_aliases.so: true
     EOF

2. Restart `wazo-confgend`::

     systemctl restart wazo-confgend

3. Check that your changes work by looking at the generated `modules.conf`::

     wazo-confgen asterisk/modules.conf

4. Restart Asterisk::

     systemctl restart asterisk
