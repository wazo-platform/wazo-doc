.. _upgrade:

*********
Upgrading
*********

Upgrading a Wazo is done by executing commands through a terminal on the
server. You can connect to the server either through SSH or with a physical
console.

To upgrade your Wazo to the latest version, you **must** use the ``wazo-upgrade`` script. You can
start an upgrade with the command::

   wazo-upgrade

.. note::
   * You can't use wazo-upgrade if you have not run the wizard yet
   * Upgrading from a :ref:`deprecated version<deprecated_versions>` is not supported.
   * When upgrading Wazo, you **must** also upgrade **all** associated XiVO Clients. There is
     currently no retro-compatibility on older XiVO Client versions. The only exception is Wazo
     16.16, which is compatible with XiVO Client 16.13.

This script will update Wazo and restart all services.

There are 2 options you can pass to wazo-upgrade:

* ``-d`` to only download packages without installing them. **This will still upgrade the package containing wazo-upgrade**.
* ``-f`` to force upgrade, without asking for user confirmation

``wazo-upgrade`` uses the following environment variables:

* ``XIVO_CONFD_PORT`` to set the port used to query the :ref:`HTTP API of xivo-confd <confd-api>`
  (default is 9486)


Upgrade procedure
=================

* Consult the `roadmaps <https://projects.wazo.community/projects/xivo/roadmap?tracker_ids%5B%5D=1&tracker_ids%5B%5D=2&completed=1>`_ starting from your current version to the current prod version.
* Read all existing Upgrade Notes (see below) starting from your version to the latest version.
* For custom setups, follow the required procedures described below (e.g. HA cluster).
* To download the packages beforehand, run ``wazo-upgrade -d``. This is not mandatory, but it does
  not require stopping any service, so it may be useful to reduce the downtime of the server while
  upgrading.
* When ready, run ``wazo-upgrade`` which will start the upgrade process. **Telephony services will
  be stopped during the process**
* When finished, check that all services are running (the list is displayed at the end of the upgrade).
* Check that services are correctly working like SIP registration, ISDN link status,
  internal/incoming/outgoing calls, Wazo Client connections etc.


.. _version_specific_upgrade:

Version-specific upgrade procedures
===================================

Upgrading from XiVO 16.13 and before
------------------------------------

When upgrading from XiVO 16.13 or before, you must use the special :ref:`XiVO to Wazo upgrade
procedure <upgrading-to-wazo>` instead of simply running ``xivo-upgrade``.


Upgrading from XiVO 14.01, 14.02, 14.03, 14.04 installed from the ISO
---------------------------------------------------------------------

In those versions, xivo-upgrade keeps XiVO on the same version. You must do the following, before
the normal upgrade::

   echo "deb http://mirror.wazo.community/debian/ xivo-five main" > /etc/apt/sources.list.d/xivo-upgrade.list \
   && apt-get update \
   && apt-get install xivo-fai \
   && rm /etc/apt/sources.list.d/xivo-upgrade.list \
   && apt-get update


Upgrading from XiVO 13.24 and before
------------------------------------

When upgrading from XiVO 13.24 or earlier, you must do the following, before the normal upgrade:

#. Ensure that the file :file:`/etc/apt/sources.list` is *not* configured on ``archive.debian.org``.
   Instead, it must be configured with a non-archive mirror, but still on the ``squeeze``
   distribution, even if it is not present on this mirror. For example::

    deb http://ftp.us.debian.org/debian squeeze main

#. Add ``archive.debian.org`` in another file::

    cat > /etc/apt/sources.list.d/squeeze-archive.list <<EOF
    deb http://archive.debian.org/debian/ squeeze main
    EOF

And after the upgrade::

   rm /etc/apt/sources.list.d/squeeze-archive.list


Upgrading from XiVO 13.03 and before
------------------------------------

When upgrading from XiVO 13.03 or earlier, you must do the following, before the normal upgrade::

   wget http://mirror.wazo.community/xivo_current.key -O - | apt-key add -


.. _upgrading-a-cluster:

Upgrading a cluster
===================

Here are the steps for upgrading a cluster, i.e. two Wazo with :ref:`high-availability`:

#. On the master : deactivate the database replication by commenting the cron in
   :file:`/etc/cron.d/xivo-ha-master`
#. On the slave, deactivate the xivo-check-master-status script cronjob by commenting the line in
   :file:`/etc/cron.d/xivo-ha-slave`
#. On the slave, start the upgrade::

    xivo-slave:~$ wazo-upgrade

#. When the slave has finished, start the upgrade on the master::

    xivo-master:~$ wazo-upgrade

#. When done, launch the database replication manually::

    xivo-master:~$ xivo-master-slave-db-replication <slave ip>

#. Reactivate the cronjobs (see steps 1 and 2)


Upgrading to/from an archive version
====================================

.. toctree::
   :maxdepth: 1

   archives


Upgrading from i386 (32 bits) to amd64 (64 bits)
================================================

.. toctree::
   :maxdepth: 1

   migrate_i386_to_amd64


Unsupported versions
====================

.. toctree::
   :maxdepth: 1

   version_deprecation_policy


Troubleshooting
===============

Postgresql
----------

When upgrading Wazo, if you encounter problems related to the system locale, see
:ref:`postgresql_localization_errors`.


wazo-upgrade
------------

If wazo-upgrade fails or aborts in mid-process, the system might end up in a faulty condition. If in
doubt, run the following command to check the current state of xivo's firewall rules::

   iptables -nvL

If, among others, it displays something like the following line (notice the DROP and 5060)::

   0     0 DROP       udp  --  *      *       0.0.0.0/0            0.0.0.0/0           udp dpt:5060

Then your Wazo will not be able to register any SIP phones. In this case, you must delete the DROP
rules with the following command::

   iptables -D INPUT -p udp --dport 5060 -j DROP

Repeat this command until no more unwanted rules are left.


Upgrade Notes
=============

17.11
-----

Consult the `17.11 Roadmap <https://projects.wazo.community/versions/263>`_

* wazo-plugind REST API version ``0.1`` has been deprecated and will be removed in Wazo ``18.02``. See changelog for version :ref:`plugind_changelog_v02`

17.10
-----

Consult the `17.10 Roadmap <https://projects.wazo.community/versions/262>`_


17.09
-----

Consult the `17.09 Roadmap <https://projects.wazo.community/versions/261>`_

* Codecs can now be customized in the `/etc/asterisk/codecs.d/` directory. If you had custom configuration
  in `/etc/asterisk/codecs.conf` you will have to create a new file in `codecs.d` to use your customized
  configuration. A file named `codecs.conf.dpkg-old` will be left in `/etc/asterisk` if this operation is
  required.
* Provd plugins from the addons repository have been merged into the main plugin repository. If you
  were using the addons repository you can safely switch back to the stable repository. See
  :ref:`alternative-plugins-repo` for more details.
* The command ``xivo-call-logs`` has been deprecated in favor of ``wazo-call-logs``.
* The command ``xivo-service`` has been deprecated in favor of ``wazo-service``.
* If you have a :ref:`custom certificate configured<https_certificate>`, you will need to add a new
  symlink for the new daemon wazo-webhookd::

    ln -s "/etc/xivo/custom/custom-certificate.yml" "/etc/wazo-webhookd/conf.d/010-custom-certificate.yml"


17.08
-----

Consult the `17.08 Roadmap <https://projects.wazo.community/versions/260>`_

* The call logs has been improved by adding ``date_end`` and ``date_answer`` informations. If you want
  to add these new informations to the old call logs, you need to regenerate them. For example, to
  regenerate the last month of call logs::

    xivo-call-logs delete -d 30
    xivo-call-logs generate -d 30

  This is only useful if you plan to use the call logs REST API to read calls that have been placed
  before the upgrade.
* If you have setup a custom X.509 certificate for HTTPS (e.g. from Let's Encrypt), you have to
  update your config in ``/etc/xivo/custom/custom-certificate.yml``, according to the :ref:`updated
  documentation <https_certificate>`, namely for the config regarding ``plugind``.


17.07
-----

Consult the `17.07 Roadmap <https://projects.wazo.community/versions/259>`_


17.06
-----

Consult the `17.06 Roadmap <https://projects.wazo.community/versions/258>`_

* Upgrade from version older than 13.01 are not supported anymore.


17.05
-----

Consult the `17.05 Roadmap <https://projects.wazo.community/versions/257>`_

* `python-flask-cors` has been updated from 1.10.3 to 3.0.2. Configuration files with custom `allow_headers` will
  have to be updated to the new syntax. The following command can be used to see if you have a configuration file
  which needs to be updated.

  .. code-block:: sh

     for f in $(find /etc/*/conf.d -name '*.yml'); do grep -H allow_headers $f; done

  The old config in ``/etc/xivo-*/conf.d`` looked like::

     rest_api:
       cors:
         allow_headers: Content-Type, X-Auth-Token

  The new config in ``/etc/xivo-*/conf.d`` looks like::

     rest_api:
       cors:
         allow_headers: ["Content-Type", "X-Auth-Token"]

  See also the reference ticket `#6617 <https://projects.wazo.community/issues/6617>`_.


17.04
-----

Consult the `17.04 Roadmap <https://projects.wazo.community/versions/256>`_


17.03
-----

Consult the `17.03 Roadmap <https://projects.wazo.community/versions/255>`_


17.02
-----

Consult the `17.02 Roadmap <https://projects.wazo.community/versions/254>`_

* A few more services are now available by default on port TCP/443 (the complete list is documented
  in the :ref:`nginx` section). This does not pose any additional security risk by default, but if
  you have extra strict requirements about security, they can be manually disabled.


17.01
-----

Consult the `17.01 Roadmap <https://projects.wazo.community/versions/253>`_


16.16
-----

Wazo 16.16 is the *first public release* of the project under the Wazo name. It
is also the first release of Wazo under the "phoenix" codename.

Consult the `16.16 Roadmap <https://projects.wazo.community/versions/252>`_

* A :ref:`special procedure <xivo-to-wazo>` is required to upgrade from XiVO to Wazo.
* Asterisk has been upgraded from version 13.11.2 to 14.2.1, which is a major Asterisk upgrade.
* If you are using :ref:`custom sheets <custom-call-form>` that are stored locally, they *must* now
  be readable by the system user ``xivo-ctid``. Make sure that this user has read access to the UI
  file of your custom sheets.
* Switchboard statistics have been removed. The existing statistics data remain in the database for
  later migration but no more statistics will be collected.
* The ``conference`` destination type in incalls REST API has been renamed to ``meetme``.
* The phonebook has been migrated from the web interface to xivo-dird. The phonebook contacts
  from the web interface have been moved to new dird-phonebooks. For users with many entities
  on the same Wazo, this will create one phonebook for each entity. The configuration has been
  updated to keep the previous behavior. No manual actions are required for installations with only one entity or
  if one phonebook by entity is the desired configuration. If only one phonebook is desired for all entities, some
  of the duplicate phonebooks can be deleted from the web interface and their matching configuration
  can also be removed.

  * The list of phonebooks can be modified in :menuselection:`Services --> IPBX --> IPBX services --> Phonebook`
  * The list of phonebooks sources can be modified in:

    * :menuselection:`Configuration --> Management --> Directories`
    * :menuselection:`Services --> CTI Server --> Directories --> Definitions`

  * The selected phonebooks for reverse lookups can be modified in :menuselection:`Services --> CTI Server --> Directories --> Reverse directories`
  * Direct directories can be modified in :menuselection:`Services --> CTI Server --> Directories --> Direct directories`

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   16.16/xivo_to_wazo
   16.16/asterisk_14


16.13
-----

XiVO 16.13 is the *last public release* of the project under the name XiVO.

Consult the `16.13 Roadmap <https://projects.wazo.community/versions/249>`_

* Previously, a user's :abbr:`DND (Do Not Distrub)` was effective only if this user had DND enabled
  *and* the DND extension (\*25 by default) was also enabled. Said differently, disabling the DND
  extension meant that no user could effectively be in DND. Starting from XiVO 16.13, a user's DND
  is effective regardless of the state of the DND extension. The following features are impacted in
  the same way: call recording, incoming call filtering, forward on non-answer, forward on busy and
  unconditional forward.
* If you have manually added nginx configuration files to the :file:`/etc/nginx/locations/http`
  directory, you'll need to move these files to :file:`/etc/nginx/locations/http-available` and then
  create symlinks to them in the :file:`/etc/nginx/locations/http-enabled` directory. This also
  applies to the https directory. See :ref:`nginx`.
* A regression has been introduced in the switchboard statistics. See `issue 6443
  <http://projects.wazo.community/issues/6443>`_.


16.12
-----

Consult the `16.12 Roadmap <https://projects.wazo.community/versions/248>`_


16.11
-----

Consult the `16.11 Roadmap <https://projects.wazo.community/versions/247>`_

* Fax reception: the "log" backend type has been removed. You should remove references to it in your
  :file:`/etc/xivo/asterisk/xivo_fax.conf` if you were using it. Now, every time a fax is processed,
  a log line is added to :file:`/var/log/xivo-agid.log`.


16.10
-----

Consult the `16.10 Roadmap <https://projects.wazo.community/versions/246>`_

* The config file ``/etc/xivo/xivo-confgend.conf`` has been replaced with
  ``/etc/xivo-confgend/config.yml`` and ``/etc/xivo-confgend/conf.d``. Custom modifications to this
  file are not migrated automatically, so manual intervention is required to migrate custom values
  to the ``conf.d`` directory. The file ``/etc/xivo/xivo-confgend/asterisk/contexts.conf`` has been
  moved to ``/etc/xivo-confgend/templates/contexts.conf``, but custom modification are left
  untouched. See also :ref:`configuration-files` for more details about configuration files in XiVO.


16.09
-----

Consult the `16.09 Roadmap <https://projects.wazo.community/versions/245>`_

* The XiVO Client now uses xivo-ctid-ng to do transfers. Those new transfers cannot be cancelled
  with the ``*0`` DTMF sequence and there is no interface in the XiVO Client to cancel a transfer
  for profiles other than the switchboard (bug `#6321`_). This will be addressed in a later version.

* Transfers started from the XiVO Client do not respect the ``Dial timeout on transfer`` option
  anymore (bug `#6322`_). This feature will be reintroduced in a later version.

.. _#6321: http://projects.wazo.community/issues/6321
.. _#6322: http://projects.wazo.community/issues/6322


16.08
-----

Consult the `16.08 Roadmap <https://projects.wazo.community/versions/244>`_

* :ref:`cti-protocol` is now in version *2.2*
* Some :ref:`security features have been added to the XiVO provisioning server <provd-security>`.
  To benefit from these new features, you'll need to :ref:`update your xivo-provd plugins to meet
  the system requirements <provd-security-requirements>`.

  If you have many phones that are connected to your XiVO through a NAT equipment, you should review
  the default configuration to make sure that the IP address of your NAT equipment don't get banned
  unintentionally by your XiVO.

* Newly created groups and queues now ignore call forward requests from members by default.
  Previously, call forward requests from members were always followed. This only applies to call
  forward configured directly on the member's phone: call forward configured via \*21 have always
  been ignored in these cases.

  Note that during the upgrade, the previous behaviour is kept for already existing queues and groups.

  This behaviour is now configurable per queue/group, via the "Ignore call forward requests from
  members" option under the "Application" tab. We recommend enabling this option.


16.07
-----

Consult the `16.07 Roadmap <https://projects.wazo.community/versions/243>`_

* If you were affected by the `bug #6213 <http://projects.wazo.community/issues/6213>`_, i.e. if your agent
  login time statistics were incorrect since your upgrade to XiVO 15.20 or later, and you want to
  fix your statistics for that period of time, you'll need to `manually apply a fix
  <http://projects.wazo.community/issues/6213#note-3>`_.


16.06
-----

Consult the `16.06 Roadmap <https://projects.wazo.community/versions/242>`_


16.05
-----

Consult the `16.05 Roadmap <https://projects.wazo.community/versions/241>`_

* The ``view``, ``add``, ``edit``, ``delete`` and ``deleteall`` actions of the "lines" web service
  provided by the web interface have been removed.  As a reminder, note that the web services
  provided by the web interface are deprecated.


16.04
-----

Consult the `16.04 Roadmap <https://projects.wazo.community/versions/240>`_

* :ref:`cti-protocol` is now in version *2.1*
* The field :guilabel:`Rightcall Code` from :menuselection:`Services -> IPBX -> IPBX Settings ->
  Users` under :guilabel:`Services` tab  will overwrite all password call permissions for the user.
* Faxes stored on FTP servers are now converted to PDF by default. See :ref:`fax-ftp` if you want
  to keep the old behavior of storing faxes as TIFF files.


16.03
-----

Consult the `16.03 Roadmap <https://projects.wazo.community/versions/239>`_

* The new section :menuselection:`Services --> Statistics --> Switchboard` in the web interface will
  only be visible by a non-root administrator after adding the corresponding permissions in the
  administrator configuration.
* Update the switchboard configuration page for the statistics in
  :ref:`switchboard_configuration_multi_queues`.
* The API for associating a line to a device has been replaced. Consult the :ref:`confd_changelog` for further details
* The configuration parameters of *xivo_ldap_user* plugin of *xivo-auth* has been changed. See
  :ref:`xivo_ldap plugin <auth-backends-ldap>`.
* The user's email is now a unique constraint. Every duplicate email will be deleted during
  the migration. (This does not apply to the voicemail's email)


16.02
-----

Consult the `16.02 Roadmap <https://projects.wazo.community/versions/238>`_

* The experimental *xivo_ldap_voicemail* plugin of *xivo-auth* has been removed. Use the new
  :ref:`xivo_ldap plugin <auth-backends-ldap>`.
* Bus messages in the *xivo* exchange are now sent with the content-type `application/json`.
  Some libraries already do the message conversion based the content-type. Kombu users will
  receive a python dictionnary instead of a string containing json when a message is received.
* :ref:`xivo-ctid encryption <ctid-encryption>` is automatically switched on for every XiVO server
  and XiVO Client >= 16.02. If you really don't want encryption, you must disable it manually on
  the server after the upgrade. In that case, XiVO Clients will ask whether to accept the connection
  the first time.


16.01
-----

Consult the `16.01 Roadmap <https://projects.wazo.community/versions/237>`_

* The page :menuselection:`Configuration --> Management --> Web Services Access --> Acces rights`
  has been removed. Consequently, every Web Services Access has now all access rights on the web
  services provided by the web interface. These web services are deprecated and will be removed
  soon.
* During the upgrade, if no CA certificates were trusted at the system level, all the CA
  certificates from the ca-certificates package will be added. This is done to resolve an issue with
  installations from the ISO and PXE. In the (rare) case you manually configured the ca-certificates
  package to trust no CA certificates at all, you'll need to manually reconfigure it via
  ``dpkg-reconfigure ca-certificates`` after the upgrade.
* *xivo-ctid* uses *xivo-auth* to authenticate users. See :ref:`authentication`.
* the `service_discovery` section of the *xivo-ctid* configuration has changed. If you have set up
  :ref:`contact_and_presence_sharing`, you should update your xivo-ctid configuration.
* the :ref:`cti-protocol` is now versioned and a message will be displayed if the server and a
  client have incompatible protocol versions.


Archives
--------

.. toctree::
   :maxdepth: 2

   old_upgrade_notes
