.. _configuration-files:

*******************
Configuration Files
*******************

This section describes some of the XiVO configuration files.


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

Configuration files for every service running on a XiVO server will respect these rules:

* Default configuration directory in :file:`/etc/xivo-{{service}}/conf.d` (e.g.
  :file:`/etc/xivo-agentd/conf.d/`)
* Default configuration file in :file:`/etc/xivo-{{service}}/config.yml` (e.g.
  :file:`/etc/xivo-agentd/config.yml`)

The files :file:`/etc/xivo-{{service}}/config.yml` should not be modified because **they will be
overridden during upgrades**. However, they may be used as examples for creating additional
configuration files as long as they respect the :ref:`configuration-priority`. Any exceptions to
these rules are documented below.


xivo-agentd
===========

* Default configuration directory: :file:`/etc/xivo-agentd/conf.d`
* Default configuration file: :file:`/etc/xivo-agentd/config.yml`


xivo-amid
=========

* Default configuration directory: :file:`/etc/xivo-amid/conf.d`
* Default configuration file: :file:`/etc/xivo-amid/config.yml`


xivo-auth
=========

* Default configuration directory: :file:`/etc/xivo-auth/conf.d`
* Default configuration file: :file:`/etc/xivo-auth/config.yml`


xivo-ctid
=========

* Default configuration directory: :file:`/etc/xivo-ctid/conf.d`
* Default configuration file: :file:`/etc/xivo-ctid/config.yml`


xivo-dao
========

* Default configuration directory: :file:`/etc/xivo-dao/conf.d`
* Default configuration file: :file:`/etc/xivo-dao/config.yml`

This configuration is read by many XiVO programs in order to connect to the Postgres database of
XiVO.


xivo-dird-phoned
================

* Default configuration directory: :file:`/etc/xivo-dird-phoned/conf.d`
* Default configuration file: :file:`/etc/xivo-dird-phoned/config.yml`


xivo-websocketd
================

* Default configuration directory: :file:`/etc/xivo-websocketd/conf.d`
* Default configuration file: :file:`/etc/xivo-websocketd/config.yml`


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

5. Restart ``xivo-agid`` service::

    service xivo-agid restart


ipbx.ini
========

* Path: :file:`/etc/xivo/web-interface/ipbx.ini`
* Purpose: This file specifies various configuration options and paths related
  to Asterisk and used by the web interface.

Here is a partial glimpse of what can be configured in file :file:`ipbx.ini` :

#. Enable/Disable modification of SIP line username and password::

      [user]
      readonly-idpwd = "true"

  When editing a SIP line, the username and password fields cannot be modified
  via the web interface. Set this option to false to enable the modification of
  both fields. This option is set to "true" by default.

.. warning:: This feature is not fully tested. It should be used only when
  absolutely necessary and with great care.
