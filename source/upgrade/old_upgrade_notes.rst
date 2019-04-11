**********************
Archived Upgrade Notes
**********************


2015
====

15.20
-----

Consult the `15.20 Roadmap <https://projects.wazo.community/versions/214>`_

* Debian has been upgraded from version 7 (wheezy) to 8 (jessie).
* CSV webservices in the web interface have been removed. Please use the :ref:`confd-api` instead.
* The CSV import format has been changed. Consult :ref:`15_20_csv_import_upgrade_notes` for further details.
* xivo-ctid now uses STARTTLS for the client connections.

  * For users already using the CTIS protocol the client can be configured to use the default port (5003)

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   15.20/jessie
   15.20/csv


15.19
-----

Consult the `15.19 Roadmap <https://projects.wazo.community/versions/236>`_

* The sound file :file:`/usr/share/asterisk/sounds/fr_FR/une.wav` has been moved to
  :file:`/usr/share/asterisk/sounds/fr_FR/digits/1F.wav`.
* If you would like to use the new `"transfer to voicemail" feature <http://projects.wazo.community/issues/5905>`_
  from the People Xlet, you'll need to update your directory definition and your directory display, i.e.:

  * edit your "internal" directory definition (Services / CTI server / Directories / Definitions)
    and add a field "voicemail" with value "voicemail_number"
  * edit your display (Services / CTI server / Directories / Display filters) and add a row with title
    "Voicemail", field type "voicemail" and field name "voicemail"
  * restart xivo-dird

* It is now possible to send an email to a user with a configured email address in the
  *people* xlet. See dird-integration-views to add the appropriate field to your
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

Consult the `15.18 Roadmap <https://projects.wazo.community/versions/234>`_

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

Consult the `15.17 Roadmap <https://projects.wazo.community/versions/233>`_

* Online call recording is now done via `automixmon
  <https://wiki.asterisk.org/wiki/display/AST/One-Touch+Features>`_ instead of automon. This has no
  impact unless you have custom dialplan that is passing directly the "w" or "W" option to the Dial
  or Queue application. In these cases, you should modify your dialplan to pass the "x" or "X"
  option instead.
* The remote directory service available from :ref:`supported phones <supported-devices>` is now
  provided by the new unified directory service, i.e. xivo-dird. Additional upgrade steps are
  required to get the full benefit of the new directory service; see the :ref:`detailed upgrade
  notes <upgrade-notes-webi-to-dird>`.
* The field ``enableautomon`` has been renamed to ``enableonlinerec`` in the users web services provided
  by the web-interface (these web services are deprecated).
* The agent status dashboard now shows that an agent is calling or receiving a non ACD call while in
  wrapup or paused.
* SIP endpoints created through the REST API will not appear in the web interface until they have
  been associated with a line
* Due to limitations in the database, only a limited number of optional parameters can be configured
  on a SIP endpoint. Consult the :ref:`xivo-confd changelog <rest-api_changelog>` for further details


Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   15.17/webi_to_dird


15.16
-----

Consult the `15.16 Roadmap <https://projects.wazo.community/versions/232>`_

* The directory column type "mobile" was removed in favor of the new "callable" type. If you have
  hand-written configuration files for xivo-dird, in section "views", subsection "displays", all
  keys "type" with value "mobile" must be changed to value "callable".
* The ``xivo-auth`` backend interface has changed, ``get_acls`` is now ``get_consul_acls``. All
  unofficial back ends must be adapted and updated. No action is required for "normal" installations.
* Voicemails can now be deleted even if they are associated to a user.


.. _upgrade_notes_15_15:

15.15
-----

Consult the `15.15 Roadmap <https://projects.wazo.community/versions/231>`_

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

See :ref:`directories` and `wazo-dird-integration` for more details


15.14
-----

* Consult the `15.14 Roadmap <https://projects.wazo.community/versions/230>`_
* Default password for ``xivo-polycom-4.0.4`` plugin version >= 1.3 is now **9486** (i.e. the word
  "xivo" on a telephone keypad).
* Default password for ``xivo-polycom-5.3.0`` plugin version >= 1.4 is now **9486**.
* Caller id management for users in confd has changed. Consult the :ref:`xivo-confd changelog <rest-api_changelog>`.
* The Local Directory Xlet is replaced with the People Xlet. Contacts are automatically migrated to
  the server. Note that the CSV format for importing contacts has changed (see :ref:`people-xlet` for
  more information).

15.13
-----

* Consult the `15.13 Roadmap <https://projects.wazo.community/versions/229>`_
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

* Consult the `15.12 Roadmap <https://projects.wazo.community/versions/228>`_
* The certificate used for HTTPS in the web interface will be regenerated if the default certificate
  was used. Your browser will complain about the new certificate, and it is safe to accept it (see
  `#3656`_). See also :ref:`https_certificate`.
* If you have an :ref:`HA configuration <high-availability>`, then you should run ``xivo-sync -i`` on
  the master node to setup file synchronization between the master and the slave. File synchronization
  will then be done automatically every hour via rsync and ssh.
* xivo-auth and xivo-dird now use HTTPS, if you have custom development using these services, update
  your configuration accordingly.

.. _#3656: http://projects.wazo.community/issues/5636


15.11
-----

* Consult the `15.11 Roadmap <https://projects.wazo.community/versions/227>`_
* The call records older than 365 days will be periodically removed. The first automatic purge will
  occur in the night after the upgrade. See :ref:`purge_logs` for more details.


15.10
-----

* Consult the `15.10 Roadmap <https://projects.wazo.community/versions/223>`_


15.09
-----

* Consult the `15.09 Roadmap <https://projects.wazo.community/versions/226>`_


15.08
-----

* Consult the `15.08 Roadmap <https://projects.wazo.community/versions/225>`_
* The Dialer Xlet has been integrated in Identity Xlet.


15.07
-----

* Consult the `15.07 Roadmap <https://projects.wazo.community/versions/224>`_


15.06
-----

* Consult the `15.06 Roadmap <https://projects.wazo.community/versions/222>`_
* The provd client has been moved into a new python package, xivo_provd_client. If you have custom scripts
  using this client, you'll need to update them. See http://projects.wazo.community/issues/5469 for more
  information.
* The provd_pycli command name has been deprecated in favor of xivo-provd-cli. These 2 commands do the
  same thing, the only difference being the name of the command. The provd_pycli command name will be
  removed in 15.18, so if you have custom scripts referencing provd_pycli, you'll need to update them.
* The xivo-agentctl command name has been deprecated in favor of xivo-agentd-cli. These 2 commands do the
  same thing, the only difference being the name of the command. The xivo-agentctl command name will be
  removed in 15.18, so if you have custom scripts referencing xivo-agentctl, you'll need to update them.


15.05
-----

* Consult the `15.05 Roadmap <https://projects.wazo.community/versions/221>`_
* The Xlet identity has been modified to follow the new Wazo Client design which implies the removal
  of some details.


15.04
-----

* Consult the `15.04 Roadmap <https://projects.wazo.community/versions/220>`_


15.03
-----

* Consult the `15.03 Roadmap <https://projects.wazo.community/versions/219>`_


15.02
-----

* Consult the `15.02 Roadmap <https://projects.wazo.community/versions/218>`_


15.01
-----

* Consult the `15.01 Roadmap <https://projects.wazo.community/versions/217>`_

* The :ref:`confd REST API <confd-api>` is now more restrictive on HTTP headers. Particularly, the
  headers Accept and Content-Type must be set to (typically) ``application/json``.
* The following configuration files have been created:

  * :file:`/etc/xivo-agid/config.yml`
  * :file:`/etc/xivo-call-logd/config.yml`
  * :file:`/etc/xivo-amid/config.yml`
  * :file:`/etc/xivo-agentd/config.yml`


2014
====

14.24
-----

* Consult the `14.24 Roadmap <https://projects.wazo.community/versions/216>`_

The following security vulnerability has been fixed:

* `XIVO-2014-01 <http://mirror.wazo.community/security/XIVO-2014-01.pdf>`_: Queues and groups permit callers to make unwanted calls


14.23
-----

* Consult the `14.23 Roadmap <https://projects.wazo.community/versions/215>`_
* The "waiting calls / logged agents ratio" :ref:`queue diversion scenario <queue-diversion-waitratio>`
  has been renamed to "number of waiting calls per logged agents".
* A new :ref:`community <community-documentation>` section was added to the official documentation for all user-contributed documentation.


14.22
-----

* Consult the `14.22 Roadmap <https://projects.wazo.community/versions/213>`_
* The sheet event *Dial* on queues is now only sent to the ringing agent. The
  sheet is also sent a little later during the call, when the ringing agent is
  known.


14.21
-----

* Consult the `14.21 Roadmap <https://projects.wazo.community/versions/212>`_
* The :ref:`confd REST API <confd-api>` is now accessible via HTTPS on port 9486 and via HTTP on
  port 9487 (localhost only). These ports are replacing the 50051 and 50050 ports respectively.  It
  will still be possible to access the confd REST API via the 50051 and 50050 ports for the next
  year, but you are advised to update your confd REST API clients as soon as possible.
* The old (unsupported) ami-proxy is now replaced by an ami-proxy built in xivo-ctid.
  You must `uninstall the old ami-proxy <https://github.com/wazo-pbx/xivo-tools/tree/master/ami-proxy>`_ before activating the built-in version. See
  :ref:`troubleshooting xivo-ctid <cti-ami-proxy>` to learn how to activate.


14.20
-----

* Consult the `14.20 Roadmap <https://projects.wazo.community/versions/211>`_
* Default parameters for all Cisco SPA ATA plugins have changed to be better suited for european faxes.
* Following the `POODLE attack <https://www.openssl.org/~bodo/ssl-poodle.pdf>`_ (CVE-2014-3566), SSL 3.0
  has been disabled for the web interface and the xivo-confd REST API.

If you have Aastra phones and are using the remote directory on them, consult the following detailed upgrade notes:

.. toctree::
   :maxdepth: 1

   14.20/aastra_remote_directory


14.19
-----

* Consult the `14.19 Roadmap <https://projects.wazo.community/versions/210>`_


14.18
-----

* Consult the `14.18 Roadmap <https://projects.wazo.community/versions/209>`_
* xivo-fai packages were replaced with xivo-dist : a new tool to handle repositories sources.
  Upon upgrade, xivo-dist is installed and run and all xivo-fai packages are purged.
  :ref:`Consult xivo-dist use cases <wazo_dist>`


14.17
-----

* Consult the `14.17 Roadmap <https://projects.wazo.community/versions/208>`_
* DAHDI configuration file :file:`/etc/dahdi/modules` is no more created by default and must now be
  maintained manually. No action is needed upon upgrade but be aware that the upstream sample file
  is now available in :file:`/usr/share/dahdi/modules.sample`. See
  :ref:`dahdi modules documentation <load_dahdi_modules>` for detailed info.
* The new `CCSS feature` will not be enabled upon upgrade, you must explicitly enable it
  in the :menuselection:`IPBX --> IPBX Services --> Extensions` menu.


14.16
-----

* Consult the `14.16 Roadmap <https://projects.wazo.community/versions/207>`_
* See the :ref:`changelog <rest-api_changelog>` for xivo-confd's REST API
* DAHDI is upgraded to 2.10.0. If the upgrade process asks about :file:`/etc/dahdi/modules`, we
  recommend that you keep the old version of the file.
* Asterisk now inserts CEL and queue log entries via the ODBC asterisk modules instead of
  the pgsql modules.


14.15
-----

* Consult the `14.15 Roadmap <https://projects.wazo.community/versions/206>`_
* Duplicate function keys will be deleted upon upgrade. If multiple function keys pointing to
  the same destination are detected for a given user, only the one with the lowest position will
  be kept. To see the list of deleted function keys, check the xivo-upgrade log file such as::

     grep MIGRATE_FK /var/log/xivo-upgrade.log

.. toctree::
   :maxdepth: 1

   14.15/dahdi_2.9.2


14.14
-----

* Consult the `14.14 Roadmap <https://projects.wazo.community/versions/205>`_
* See the :ref:`changelog <rest-api_changelog>` for REST API
* Upon an important freeze of Asterisk, Asterisk will be restarted. See the `associated ticket
  <https://projects.wazo.community/issues/5165>`_ for more information.


14.13
-----

* Consult the `14.13 Roadmap <https://projects.wazo.community/versions/204>`_
* See the :ref:`changelog <rest-api_changelog>` for REST API
* Skills-based routing: for an agent which doesn't have the skill X, the rule X < 10 was
  previously evaluated to true, since not having the skill X was equivalent to having it with a
  value of 0. This behaviour has changed, and the same expression is now evaluated to false. If you
  are using skills-based routing, you'll need to check that your rules are still doing what you
  expect. See :ref:`skill evaluation <skill-evaluation>` for more information.


14.12
-----

* Consult the `14.12 Roadmap <https://projects.wazo.community/versions/203>`_
* All provisioning plugins were modified. Although not mandatory, it is strongly advised to update
  all used plugins.
* The function key 'Activate voicemail' was removed as it was a duplicate of existing function key
  'Enable voicemail'. All users having the 'Activate voicemail' function key will have to be
  reconfigured with a 'Enable voicemail' function key in order to keep the equivalent feature.
* Log files have changed for the following daemons (previously in :file:`/var/log/daemon.log`):

  * xivo-provd: :file:`/var/log/xivo-provd.log`
  * xivo-agid: :file:`/var/log/xivo-agid.log`
  * xivo-sysconfd: :file:`/var/log/xivo-sysconfd.log`


14.11
-----

* Consult the `14.11 Roadmap <https://projects.wazo.community/versions/202>`_
* The API URL ``/lines/<id>/extension`` is now deprecated. Use ``/lines/<id>/extensions``
  instead.


14.10
-----

* Consult the `14.10 Roadmap <https://projects.wazo.community/versions/201>`_
* Custom MOH have been `fixed`_, but can not be used for playing uploaded files anymore. See
  :ref:`moh`.

.. _fixed: https://projects.wazo.community/issues/5038


14.09
-----

* Consult the `14.09 Roadmap <https://projects.wazo.community/versions/200>`_
* REST API 1.0 is no more. All code, tests and documentation was removed from XiVO.
  All code developped for REST API 1.0 must now be adapted to use REST API 1.1.

.. _upgrade_note_14.08:

14.08
-----

* Consult the `14.08 Roadmap <https://projects.wazo.community/versions/199>`_
* The ``xivo`` database has been merged into the ``asterisk`` database. The database
  schema has also been altered in a way that it might make the upgrade longer than
  usual.

Please consult the following detailed updated notes for more information:

.. toctree::
   :maxdepth: 1

   14.08/database_merge


14.07
-----

* Consult the `14.07 Roadmap <https://projects.wazo.community/versions/198>`_
* Configuration for phones used for the switchboard has changed.

Please consult the following detailed updated notes for more information:

.. toctree::
   :maxdepth: 1

   14.07/switchboard_plugin


14.06
-----

* Consult the `14.06 Roadmap <https://projects.wazo.community/versions/197>`_
* The Wazo Client now uses Qt 5 instead of Qt 4. There is nothing to be aware of unless you
  are :ref:`building your own version <build_wazoclient>` of it.


14.05
-----

* Consult the `14.05 Roadmap <https://projects.wazo.community/versions/196>`_
* The :ref:`cti-protocol` has been updated.
* The specification of the 'answered-rate' queue statistic has changed to
  exclude calls on a closed queue
* The switchboard can now choose which incoming call to answer
* The package versions do not necessarily contain the current XiVO version, it may contain older
  versions. Only the package ``xivo`` is guaranteed to have the current XiVO version.

Please consult the following detailed updated notes for more information:

.. toctree::
   :maxdepth: 1

   14.05/dahdi_2.9.0
   14.05/sccp_next


14.04
-----

* Consult the `14.04 Roadmap <https://projects.wazo.community/versions/195>`_
* Live reload of the configuration can be enabled and disabled using the REST API
* The generation of call logs for unanswered calls from the Wazo Client have
  been improved.


14.03
-----

* Consult the `14.03 Roadmap <https://projects.wazo.community/versions/194>`_
* A migration script adds an index on the linkedid field in the cel table.
  Tests have shown that this operation can last up to 11.5 minutes on a XiVO
  Corporate with 18 millions CELs. xivo-upgrade will thus be slightly longer.
* Two new daemons are now operationnal, xivo-amid and xivo-call-logd:

  * xivo-amid constantly reads the AMI and sends AMI events to the RabbitMQ bus
  * xivo-call-logd generates call-logs in real time based on AMI LINKEDID_END
    events read on the bus
* An increase in load average is expected with the addition of these two new
  daemons.
* The cron job calling xivo-call-logs now runs once a day at 4:25 instead of
  every 5 minutes.


14.02
-----

* Consult the `14.02 Roadmap <https://projects.wazo.community/versions/193>`_
* PHP Web services has been removed from documentation
* REST API 1.0 Web services has been removed from documentation
* REST API 1.1 User-Line-Extension service is replaced by User-Line and Line-Extension services


14.01
-----

* Consult the `14.01 Roadmap <https://projects.wazo.community/versions/192>`_
* The following paths have been renamed:

  * :file:`/etc/pf-xivo` to :file:`/etc/xivo`
  * :file:`/var/lib/pf-xivo` to :file:`/var/lib/xivo`
  * :file:`/usr/share/pf-xivo` to :file:`/usr/share/xivo`

You must update any dialplan or configuration file using these paths
