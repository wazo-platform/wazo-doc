.. _xivo-to-wazo:

**************************
XiVO to Wazo Upgrade Notes
**************************

The Wazo project is a continuation of the original XiVO project. Programs, packages, plugins, etc,
still use the "xivo" name as to not break backward compatibility. In this regard, upgrading from
XiVO 16.13 to Wazo 16.16 is no different from upgrading XiVO 16.10 to XiVO 16.13, for example.

More information about the Wazo project is available on the `Wazo blog <http://blog.wazo.community>`_.


.. _using-wazo-infrastructure:

Using the Wazo Infrastructure on your XiVO
==========================================

This step is only needed if you are in at least one of the following situations:

* you don't intend to upgrade to Wazo right away, i.e. you want to continue using your
  XiVO installation in its current version for some time
* you are currently using XiVO in version 14.17 or earlier

In this case, you'll need to run the following commands::

   # --no-check-certificate is needed only if you are affected by http://projects.wazo.community/issues/6024
   wget --no-check-certificate https://raw.githubusercontent.com/wazo-pbx/xivo-upgrade/master/bin/use-wazo-infrastructure
   chmod +x use-wazo-infrastructure
   ./use-wazo-infrastructure

The ``use-wazo-infrastructure`` script adds lines to the :file:`/etc/hosts` file such that hostnames
that used to refer to the infrastructure of the XiVO project (e.g. mirror.xivo.io) now points to the
infrastructure of the Wazo project (e.g. mirror.wazo.community).

The script can be run multiple times. If you want to revert the modification done by the script,
just execute it with the ``--revert`` option.

The modification done by this script will be automatically reverted when you'll upgrade to Wazo.


.. _upgrading-to-wazo:

Upgrading to Wazo
=================

The upgrade procedure slightly differs depending on which version of XiVO you are currently using.
Earlier version of XiVO requires additional steps to be performed.

First, if your XiVO is in version 14.17 or earlier, you'll need to :ref:`configure it to use the
Wazo infrastructure <using-wazo-infrastructure>` if it wasn't previously done.

Next, if your XiVO is in version 13.25 or earlier, you'll need to upgrade it to version 13.25 or
later by following the usual XiVO :ref:`upgrade procedures <upgrade>`.

Finally, if your XiVO is between version 13.25 and 14.17, you'll need to manually install xivo-dist::

   apt-get update
   apt-get install -y xivo-dist

Your XiVO can now be upgraded to Wazo by running the following commands::

   sed -i -e 's/xivo\.io/wazo.community/' -e 's/xivo-five/phoenix/' -e 's/xivo-dev/wazo-dev/' -e 's/xivo-rc/wazo-rc/' /etc/apt/sources.list.d/xivo-dist.list
   xivo-upgrade


After the Upgrade
-----------------

You should make sure that you don't have any reference left to the xivo.io domain on your Wazo. In
particular, you should check the :file:`/etc` directory with the command::

   grep -rF xivo.io /etc
