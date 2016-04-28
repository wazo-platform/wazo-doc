.. _upgrade:

*********
Upgrading
*********

Upgrading a XiVO is done by executing commands through a terminal on the
server. You can connect to the server either through SSH or with a physical
console.

To upgrade your XiVO to the latest version, you **must** use the ``xivo-upgrade`` script. You can
start an upgrade with the command::

   xivo-upgrade

.. note::
   * You can't use xivo-upgrade if you have not run the wizard yet
   * Upgrading from a version prior to XiVO 1.2 is not supported.
   * When upgrading XiVO, you **must** also upgrade **all** associated XiVO
     Clients. There is currently no retro-compatibility on older XiVO Client
     versions.

This script will update XiVO and restart all services.

There are 2 options you can pass to xivo-upgrade:

* ``-d`` to only download packages without installing them. **This will still upgrade the package containing xivo-upgrade and xivo-service**.
* ``-f`` to force upgrade, without asking for user confirmation


``xivo-upgrade`` uses the following environment variables:

* ``XIVO_CONFD_PORT`` to set the port used to query the :ref:`HTTP API of xivo-confd <confd-api>`
  (default is 9486)


Upgrade procedure
=================

* Consult the `roadmaps <https://projects.xivo.io/projects/xivo/roadmap?tracker_ids%5B%5D=1&tracker_ids%5B%5D=2&completed=1>`_ starting from your current version to the current prod version.
* Read all existing Upgrade Notes (see below) starting from your version to the latest version.
* For custom setups, follow the required procedures described below (e.g. HA cluster).
* To download the packages beforehand, run ``xivo-upgrade -d``. This is not mandatory, but it does
  not require stopping any service, so it may be useful to reduce the downtime of the server while
  upgrading.
* When ready, run ``xivo-upgrade`` which will start the upgrade process. **Telephony services will
  be stopped during the process**
* When finished, check that all services are running (the list is displayed at the end of the upgrade).
* Check that services are correctly working like SIP registration, ISDN link status,
  internal/incoming/outgoing calls, XiVO Client connections etc.


.. _version_specific_upgrade:

Version-specific upgrade procedures
===================================

Upgrading from XiVO 14.01, 14.02, 14.03, 14.04 installed from the ISO
---------------------------------------------------------------------

In those versions, xivo-upgrade keeps XiVO on the same version. You must do the following, before
the normal upgrade::

   echo "deb http://mirror.xivo.io/debian/ xivo-five main" > /etc/apt/sources.list.d/xivo-upgrade.list \
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

   wget http://mirror.xivo.io/xivo_current.key -O - | apt-key add -


Upgrading from XiVO 12.13 and before
------------------------------------

When upgrading from XiVO 12.13 or earlier, you must do the following, before the normal upgrade::

   apt-get update
   apt-get install debian-archive-keyring


Upgrading from XiVO 1.2.1 and before
------------------------------------

Upgrading from 1.2.0 or 1.2.1 requires a special procedure before executing ``xivo-upgrade``::

   apt-get update
   apt-get install xivo-upgrade
   /usr/bin/xivo-upgrade

.. _upgrading-a-cluster:

Upgrading a cluster
===================

Here are the steps for upgrading a cluster, i.e. two XiVO with :ref:`high-availability`:

#. On the master : deactivate the database replication by commenting the cron in
   :file:`/etc/cron.d/xivo-ha-master`
#. On the slave, deactivate the xivo-check-master-status script cronjob by commenting the line in
   :file:`/etc/cron.d/xivo-ha-slave`
#. On the slave, start the upgrade::

    xivo-slave:~$ xivo-upgrade

#. When the slave has finished, start the upgrade on the master::

    xivo-master:~$ xivo-upgrade

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


Troubleshooting
===============

Postgresql
----------

When upgrading XiVO, if you encounter problems related to the system locale, see
:ref:`postgresql_localization_errors`.


xivo-upgrade
------------

If xivo-upgrade fails or aborts in mid-process, the system might end up in a faulty condition. If in
doubt, run the following command to check the current state of xivo's firewall rules::

   iptables -nvL

If, among others, it displays something like the following line (notice the DROP and 5060)::

   0     0 DROP       udp  --  *      *       0.0.0.0/0            0.0.0.0/0           udp dpt:5060

Then your XiVO will not be able to register any SIP phones. In this case, you must delete the DROP
rules with the following command::

   iptables -D INPUT -p udp --dport 5060 -j DROP

Repeat this command until no more unwanted rules are left.


Upgrade Notes
=============

16.05
-----

Consult the `16.05 Roadmap <https://projects.xivo.io/versions/241>`_

* The ``view``, ``add``, ``edit``, ``delete`` and ``deleteall`` actions of the "lines" web service
  provided by the web interface have been removed.  As a reminder, note that the web services
  provided by the web interface are deprecated.


16.04
-----

Consult the `16.04 Roadmap <https://projects.xivo.io/versions/240>`_

* :ref:`cti-protocol` is now in version *2.1*
* The field :guilabel:`Rightcall Code` from :menuselection:`Services -> IPBX -> IPBX Settings ->
  Users` under :guilabel:`Services` tab  will overwrite all password call permissions for the user.
* Faxes stored on FTP servers are now converted to PDF by default. See :ref:`fax-ftp` if you want
  to keep the old behavior of storing faxes as TIFF files.


16.03
-----

Consult the `16.03 Roadmap <https://projects.xivo.io/versions/239>`_

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

Consult the `16.02 Roadmap <https://projects.xivo.io/versions/238>`_

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

Consult the `16.01 Roadmap <https://projects.xivo.io/versions/237>`_

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


15.20
-----

Consult the `15.20 Roadmap <https://projects.xivo.io/versions/214>`_

* Debian has been upgraded from version 7 (wheezy) to 8 (jessie).
* CSV webservices in the web interface have been removed. Please use the :ref:`confd-api` instead.
* The CSV import format has been changed. Consult :ref:`15_20_csv_import_upgrade_notes` for further details.
* The :ref:`bus-chat_message_event` bus message has been added.
* xivo-ctid now uses STARTTLS for the client connections.

  * For users already using the CTIS protocol the client can be configured to use the default port (5003)

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   15.20/jessie
   15.20/csv


15.19
-----

Consult the `15.19 Roadmap <https://projects.xivo.io/versions/236>`_

* The sound file :file:`/usr/share/asterisk/sounds/fr_FR/une.wav` has been moved to
  :file:`/usr/share/asterisk/sounds/fr_FR/digits/1F.wav`.
* If you would like to use the new `"transfer to voicemail" feature <http://projects.xivo.io/issues/5905>`_
  from the People Xlet, you'll need to update your directory definition and your directory display, i.e.:

  * edit your "internal" directory definition (Services / CTI server / Directories / Definitions)
    and add a field "voicemail" with value "voicemail_number"
  * edit your display (Services / CTI server / Directories / Display filters) and add a row with title
    "Voicemail", field type "voicemail" and field name "voicemail"
  * restart xivo-dird

* It is now possible to send an email to a user with a configured email address in the
  *people* xlet. See :ref:`dird-integration-views`  to add the appropriate field to your
  configured displays.
* The *Contacts* xlet (aka. *Search*) has been removed in favor of the :ref:`people-xlet`. You may
  need to do some manual configuration in the directories for the People Xlet to be fully
  functional. See :ref:`the detailed upgrade notes <15_19_people_xlet_upgrade_notes>` for more details.
* If you need context separation in the People Xlet, you will have to **manually configure**
  xivo-dird to keep it working, see :ref:`15-19-dird-context-separation`. This procedure is only
  temporary, later versions will handle the context separation automatically.
* xivo-agentd now uses mandatory token authentication for its REST API. If you have custom
  development using this service, update your program accordingly.
* Some actions that used to be available in the *contact* xlets are not
  implemented in the *people* xlet yet.

  * Cancel transfer is only available using the *switchboard* xlet
  * Hanging up a call is only possible using the *switchboard* xlet
  * Call interception is not available anymore
  * Conference room invitation is not available anymore

Please consult the following detailed upgrade notes for more information:


.. toctree::
   :maxdepth: 1

   15.19/people-xlet-directory
   15.19/context-separation


15.18
-----

Consult the `15.18 Roadmap <https://projects.xivo.io/versions/234>`_

* The provd_pycli command (deprecated in 15.06) has been removed in favor of xivo-provd-cli. If you
  have custom scripts referencing provd_pycli, you'll need to update them.
* The xivo-agentctl command (deprecated in 15.06) has been removed in favor of xivo-agentd-cli. If you
  have custom scripts referencing xivo-agentctl, you'll need to update them.
* xivo-agentd now uses HTTPS. If you have custom development using this service, update your
  configuration accordingly. The xivo-agentd-client library, used to interact with xivo-agentd, has
  also been updated to use HTTPS by default.
* xivo-confd ports 50050 and 50051 have been removed. Please use 9486 and 9487 instead

**Configuration File Upgrade Notes**

The file format of configuration files for daemons exposing an HTTP/S API has changed.  The
following services have been affected :

 * xivo-agentd
 * xivo-amid
 * xivo-auth
 * xivo-confd
 * xivo-ctid
 * xivo-dird
 * xivo-dird-phoned

Ports and listening addresses are now organised in the following fashion:

.. code-block:: yaml

    rest_api:
      https:
        enabled: true
        port: 9486
        listen: 0.0.0.0
        certificate: /usr/share/xivo-certs/server.crt
        private_key: /usr/share/xivo-certs/server.key
        ciphers: "ALL:!aNULL:!eNULL:!LOW:!EXP:!RC4:!3DES:!SEED:+HIGH:+MEDIUM"
      http:
        enabled: true
        port: 9487
        listen: 127.0.0.1

If you have any custom configuration files for these daemons, please modify them accordingly.
Consult :ref:`network_ports` for further details on which network services are available for each
daemon.


15.17
-----

Consult the `15.17 Roadmap <https://projects.xivo.io/versions/233>`_

* Online call recording is now done via `automixmon
  <https://wiki.asterisk.org/wiki/display/AST/One-Touch+Features>`_ instead of automon. This has no
  impact unless you have custom dialplan that is passing directly the "w" or "W" option to the Dial
  or Queue application. In these cases, you should modify your dialplan to pass the "x" or "X"
  option instead.
* The remote directory service available from :ref:`supported phones <official-devices>` is now
  provided by the new unified directory service, i.e. xivo-dird. Additional upgrade steps are
  required to get the full benefit of the new directory service; see the :ref:`detailed upgrade
  notes <upgrade-notes-webi-to-dird>`.
* The field ``enableautomon`` has been renamed to ``enableonlinerec`` in the users web services provided
  by the web-interface (these web services are deprecated).
* The agent status dashboard now shows that an agent is calling or receiving a non ACD call while in
  wrapup or paused.
* The :ref:`bus-service_registered_event` and :ref:`bus-service_deregistered_event` bus messages have
  been added.
* SIP endpoints created through the REST API will not appear in the web interface until they have
  been associated with a line
* Due to limitations in the database, only a limited number of optional parameters can be configured
  on a SIP endpoint. Consult the :ref:`confd_changelog` for further details


Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   15.17/webi_to_dird


15.16
-----

Consult the `15.16 Roadmap <https://projects.xivo.io/versions/232>`_

* The directory column type "mobile" was removed in favor of the new "callable" type. If you have
  hand-written configuration files for xivo-dird, in section "views", subsection "displays", all
  keys "type" with value "mobile" must be changed to value "callable".
* The ``xivo-auth`` backend interface has changed, ``get_acls`` is now ``get_consul_acls``. All
  unofficial back ends must be adapted and updated. No action is required for "normal" installations.
* Voicemails can now be deleted even if they are associated to a user.


.. _upgrade_notes_15_15:

15.15
-----

Consult the `15.15 Roadmap <https://projects.xivo.io/versions/231>`_

**Voicemail Upgrade Notes**

 * Voicemail webservices in the web interface have been removed. Please use the :ref:`confd-api` instead.
 * Voicemail IMAP configuration has been migrated to the new ``Advanced`` tab.
 * Voicemail option ``Disable password checking`` has been converted to ``Ask password``. The value has also been
   inverted. (e.g. If ``Disable password checking`` was false, ``Ask password`` is true.) ``Ask password`` is activated
   by default.
 * After an upgrade, if ever you have errors when searching for voicemails, please try clearing cookies in your web browser.
 * A voicemail must be dissociated from any user prior to being deleted. Voicemail are dissociated by editing the
   user and clicking on the ``Delete voicemail`` button in the ``Voicemail`` tab. This constraint will disappear in
   future versions.
 * Deleting a user will dissociate any voicemail that was attached, but will not delete it nor any messages.
 * Creating a line is no longer necessary when attaching a voicemail to a user.
 * The following fields have been modified when importing a CSV file:

+--------------------+----------------------+------------+-------------------+
| Old name           | New name             | Required ? | New default value |
+====================+======================+============+===================+
| voicemailmailbox   | voicemailnumber      | yes        |                   |
+--------------------+----------------------+------------+-------------------+
| voicemailskippass  | voicemailaskpassword | no         | 1                 |
+--------------------+----------------------+------------+-------------------+
|                    | voicemailcontext     | yes        |                   |
+--------------------+----------------------+------------+-------------------+

**Directories**

 * Concatenated fields in directories are now done in the directory definitions instead of the displays
 * The field column in directory displays are now field names from the directory definition. No more `{db-*}` are required
 * In the directory definitions fields can be modified using a python format string with the fields comming from the source.
 * Most of the configuration for xivo-dird is now generated from xivo-confgen using the values in the web interface.
 * The `remote directory` xlet has been removed in favor of the new `people` xlet.

See :ref:`directories` and :ref:`xivo-dird-integration` for more details


15.14
-----

* Consult the `15.14 Roadmap <https://projects.xivo.io/versions/230>`_
* Default password for ``xivo-polycom-4.0.4`` plugin version >= 1.3 is now **9486** (i.e. the word
  "xivo" on a telephone keypad).
* Default password for ``xivo-polycom-5.3.0`` plugin version >= 1.4 is now **9486**.
* Caller id management for users in confd has changed. Consult the :ref:`confd_changelog`.
* The Local Directory Xlet is replaced with the People Xlet. Contacts are automatically migrated to
  the server. Note that the CSV format for importing contacts has changed (see :ref:`people-xlet` for
  more information).

15.13
-----

* Consult the `15.13 Roadmap <https://projects.xivo.io/versions/229>`_
* Asterisk has been upgraded from version 11.17.1 to 13.4.0, which is a major Asterisk upgrade.
* An `ARI <https://wiki.asterisk.org/wiki/display/AST/Getting+Started+with+ARI>`_ user has been
  added to :file:`/etc/asterisk/ari.conf`. If you have configured Asterisk HTTP server to bind on a
  publicly reachable address (in :file:`/etc/asterisk/http.conf`), then you should update your
  configuration to prevent unauthorized access on your Asterisk.
* The xivo-dird configuration option `source_to_display_columns` has been
  removed in favor of the new option `format_columns`. All source configuration
  using the `source_to_display_columns` must be updated. A migration script will
  automatically modify source configuration in the `/etc/xivo-dird/sources.d`
  directory.

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   15.13/asterisk_13


.. _upgrade-note-15.12:

15.12
-----

* Consult the `15.12 Roadmap <https://projects.xivo.io/versions/228>`_
* The certificate used for HTTPS in the web interface will be regenerated if the default certificate
  was used. Your browser will complain about the new certificate, and it is safe to accept it (see
  `#3656`_). See also :ref:`https_certificate`.
* If you have an :ref:`HA configuration <high-availability>`, then you should run ``xivo-sync -i`` on
  the master node to setup file synchronization between the master and the slave. File synchronization
  will then be done automatically every hour via rsync and ssh.
* xivo-auth and xivo-dird now use HTTPS, if you have custom development using these services, update
  your configuration accordingly.

.. _#3656: http://projects.xivo.io/issues/5636


15.11
-----

* Consult the `15.11 Roadmap <https://projects.xivo.io/versions/227>`_
* The call records older than 365 days will be periodically removed. The first automatic purge will
  occur in the night after the upgrade. See :ref:`purge_logs` for more details.


15.10
-----

* Consult the `15.10 Roadmap <https://projects.xivo.io/versions/223>`_


15.09
-----

* Consult the `15.09 Roadmap <https://projects.xivo.io/versions/226>`_


15.08
-----

* Consult the `15.08 Roadmap <https://projects.xivo.io/versions/225>`_
* The Dialer Xlet has been integrated in Identity Xlet.


15.07
-----

* Consult the `15.07 Roadmap <https://projects.xivo.io/versions/224>`_


15.06
-----

* Consult the `15.06 Roadmap <https://projects.xivo.io/versions/222>`_
* The provd client has been moved into a new python package, xivo_provd_client. If you have custom scripts
  using this client, you'll need to update them. See http://projects.xivo.io/issues/5469 for more
  information.
* The provd_pycli command name has been deprecated in favor of xivo-provd-cli. These 2 commands do the
  same thing, the only difference being the name of the command. The provd_pycli command name will be
  removed in 15.18, so if you have custom scripts referencing provd_pycli, you'll need to update them.
* The xivo-agentctl command name has been deprecated in favor of xivo-agentd-cli. These 2 commands do the
  same thing, the only difference being the name of the command. The xivo-agentctl command name will be
  removed in 15.18, so if you have custom scripts referencing xivo-agentctl, you'll need to update them.


15.05
-----

* Consult the `15.05 Roadmap <https://projects.xivo.io/versions/221>`_
* The Xlet identity has been modified to follow the new XiVO Client design which implies the removal
  of some details.


15.04
-----

* Consult the `15.04 Roadmap <https://projects.xivo.io/versions/220>`_


15.03
-----

* Consult the `15.03 Roadmap <https://projects.xivo.io/versions/219>`_


15.02
-----

* Consult the `15.02 Roadmap <https://projects.xivo.io/versions/218>`_


15.01
-----

* Consult the `15.01 Roadmap <https://projects.xivo.io/versions/217>`_

* The :ref:`confd REST API <confd-api>` is now more restrictive on HTTP headers. Particularly, the
  headers Accept and Content-Type must be set to (typically) ``application/json``.
* The following configuration files have been created:

  * :file:`/etc/xivo-agid/config.yml`
  * :file:`/etc/xivo-call-logd/config.yml`
  * :file:`/etc/xivo-amid/config.yml`
  * :file:`/etc/xivo-agentd/config.yml`


Archives
--------

.. toctree::
   :maxdepth: 2

   old_upgrade_notes
