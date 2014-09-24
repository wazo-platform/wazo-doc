*****************************************
Upgrade involving archive version of XiVO
*****************************************

Archive package names
=====================

Archive packages are named as follow:

+----------------+-----------------------------+
| XiVO version   | Archive package name        |
+================+=============================+
| 1.2 to 1.2.12  | pf-fai-xivo-1.2-skaro-1.2.1 |
+----------------+-----------------------------+
| 12.14 to 13.24 | xivo-fai-skaro-13.04        |
+----------------+-----------------------------+
| 13.25 to 14.17 | xivo-fai-14.06              |
+----------------+-----------------------------+


Upgrade from an archive to the latest version
=============================================

Archive version < 13.25::

   apt-get update
   apt-get install -t squeeze-xivo-skaro-$(cat /usr/share/xivo/XIVO-VERSION) xivo-fai xivo-fai-skaro
   xivo-upgrade

.. We need the old xivo-fai (squeeze), because the new xivo-fai (xivo-five) conflicts with
   xivo-fai-skaro. We need xivo-fai-skaro at least to download postgresql-9.1.

Archive version >= 13.25 and < 14.18::

   apt-get update
   apt-get install xivo-fai
   xivo-upgrade

Archive version >= 14.18::

  xivo-dist xivo-five
  xivo-upgrade

As a result, xivo-upgrade will always upgrade XiVO to the latest stable version.

Upgrade from an installed production version to a newer archive version
=======================================================================

Downgrades are not supported: you can only upgrade to a greater version.

Installed version between 1.2 and 13.24::

   apt-get update
   apt-get install xivo-fai-skaro-13.23
   apt-get purge xivo-fai-skaro
   apt-get update

Installed version after 13.25::

   apt-get update
   apt-get install xivo-fai-13.25
   apt-get purge xivo-fai
   apt-get update

Installed version after 14.18::

   xivo-dist xivo-15.12
   xivo-upgrade

As a result, xivo-upgrade will not upgrade XiVO to a greater version than the archive you chose.


Upgrade from an older archive version to a newer archive version
================================================================

Downgrades are not supported: you can only upgrade to a greater version.

We only support upgrades to archive versions >= 13.25, e.g. you can upgrade a 12.16 to 14.16, but
not 12.16 to 13.16

Source archive version between 1.2 to 13.02 (here 1.2.3 to 14.16)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   cat > /usr/share/xivo-upgrade/pre-upgrade.d/99-archive-version <<EOF
   #!/bin/sh
   apt-get install -y xivo-fai-14.16
   apt-get purge -y xivo-fai xivo-fai-skaro
   apt-get update
   EOF
   chmod +x /usr/share/xivo-upgrade/pre-upgrade.d/99-archive-version

   apt-get update
   apt-get install -y -t squeeze-xivo-skaro-1.2.3 xivo-fai xivo-fai-skaro
   apt-get purge -y pf-fai-xivo-1.2-skaro-1.2.3
   apt-get update
   apt-get install -y xivo-fai-14.16
   apt-get purge -y xivo-fai
   # redirect stderr to stdout to avoid desync between them
   xivo-upgrade 2>&1 <<-EOF
   y
   Y
   EOF
   rm -r /usr/share/xivo-upgrade/pre-upgrade.d/99-archive-version


Source archive version after 13.03 (here 13.03 to 14.16)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   # Workaround for bug #5087
   cat > /usr/share/xivo-upgrade/pre-stop.d/99-archive-version <<EOF
   #!/bin/sh
   apt-get install -y xivo-fai-14.16
   apt-get purge -y xivo-fai xivo-fai-skaro
   apt-get update
   EOF
   chmod +x /usr/share/xivo-upgrade/pre-stop.d/99-archive-version

   apt-get update
   apt-get install -t squeeze-xivo-skaro-13.03 xivo-fai xivo-fai-skaro
   apt-get purge xivo-fai-skaro-13.03
   apt-get update
   apt-get install xivo-fai-14.16
   apt-get purge xivo-fai
   xivo-upgrade
   rm /usr/share/xivo-upgrade/pre-stop.d/99-archive-version

xivo-upgrade will prompt you for an installation of the latest version, not for the archive you want
(bug `#5087 <https://projects.xivo.io/issues/5087>`_). Because of the file we added in
:file:`/usr/share/xivo-upgrade/pre-stop.d/`, xivo-upgrade will install the archive version you want.

Source archive version after 13.25 (here 13.25 to 14.16)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   # Workaround for bug #5087
   cat > /usr/share/xivo-upgrade/pre-stop.d/99-archive-version <<EOF
   #!/bin/sh
   apt-get install -y xivo-fai-14.16
   apt-get purge -y xivo-fai
   apt-get update
   EOF
   chmod +x /usr/share/xivo-upgrade/pre-stop.d/99-archive-version

   apt-get update
   apt-get install xivo-fai
   apt-get purge xivo-fai-13.25
   apt-get update
   /usr/share/xivo-upgrade/pre-stop.d/99-archive-version
   xivo-upgrade
   rm /usr/share/xivo-upgrade/pre-stop.d/99-archive-version

xivo-upgrade will prompt you for an installation of the latest version, not for the archive you want
(bug `#5087 <https://projects.xivo.io/issues/5087>`_). Because of the file we added in
:file:`/usr/share/xivo-upgrade/pre-stop.d/`, xivo-upgrade will install the archive version you want.

Source archive version after 14.18
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   xivo-dist xivo-15.12
   xivo-upgrade
