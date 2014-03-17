******************
SCCP Upgrade Notes
******************

Important modification have been made to the internal structure of the SCCP
channel driver, xivo-libsccp.

The modifications mostly affect administrators; users are not affected.

Major changes are:

* Improved support for live modifications; no more manual intervention in the
  asterisk CLI is needed.
* Improved handling of concurrency; crash and deadlock due to concurrency
  problems should not occur anymore.


CLI
===

The following commands have been removed because they were not needed:

* sccp resync
* sccp set directmedia
* sccp show lines
* sccp update config

The behavior of the following commands have been changed:

* ``module reload chan_sccp`` reloads the module configuration, without
  interrupting the telephony service.  A device will only be resetted/restarted
  if needed, and only once the device is idle. Some changes don't even require
  the device to be resetted.
* ``sccp show config`` output format has been changed a little.
* ``sccp show devices`` only show the connected devices instead of all the
  devices. This might change in the future. To get a list of all the devices,
  use ``sccp show config``.


Configuration File
==================

The format of the :file:`sccp.conf` configuration file has been changed. This
will only impact you if you are using xivo-libsccp without using XiVO.

The format has been changed because the module is now using the ACO module from
asterisk, which expect configuration file to have a specific format.

See `sccp.conf.sample`_ for a configuration file example.

.. _sccp.conf.sample: https://raw.github.com/xivo-pbx/xivo-libsccp/master/xivo-libsccp/configs/sccp.conf.sample


Other
=====

Each SCCP session/connection now use 3 file descriptors instead of 1 previously.
On XiVO, the file descriptor limit for the asterisk process is 8192, which
means that the increase in used file descriptors should not be a problem, even
on a large installation.
