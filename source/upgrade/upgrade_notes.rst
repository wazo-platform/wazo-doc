.. _upgrade-notes:

*************
Upgrade notes
*************

20.01
=====

* The default protocol configured for consul is now ``HTTP`` instead of ``HTTPS`` since it's only
  available on ``localhost``. The ``HTTPS`` remains available via the port ``8501``.

Consult the  `20.01 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10065>`_ for more information.


19.17
=====

* The default Ansible installation installs the development version of Wazo Platform. If
  you have not changed the ``wazo_distribution_upgrade`` variable, all the subsequent upgrades will
  stay on the development version. This is the expected behavior, but it was not visible in the
  installation procedure. To make your Wazo Platform use the stable version, use the following
  command::

    wazo-dist -m pelican-buster

  This command will take effect at the next Wazo Platform upgrade.

* ``wazo-dird`` phone plugins have been migrated to ``wazo-phoned``. If you used the phone routes
  from ``wazo-dird`` directly, you must use the new routes in ``wazo-phoned``.

* The conference rooms created in Wazo 18.03 or before (using asterisk ``meetme`` module) will not
  work anymore because they rely on DAHDI. If you were still using those conference rooms, you must
  create new conference rooms using the conferences API or the ``wazo-ui`` interface.

* ``DAHDI`` is not longer a mandatory dependency of Wazo: it will not be installed on new installs
  anymore. Upgraded Wazo Platform will keep DAHDI installed if it was configured in
  ``/etc/asterisk/dahdi_channels.conf``. Otherwise, DAHDI will be removed. To install or remove
  DAHDI manually, see :ref:`chan_dahdi`.

* Some dependencies have been removed from the ``asterisk`` package. If you used one of the following
  modules you must install the ``wazo-asterisk-extra-modules`` to keep using those modules. Note that
  all modules listed here are disabled by default on Wazo. You have to manually modify
  ``/etc/asterisk/modules.conf`` to use them.

  * ``app_jack``
  * ``cdr_pgsql``
  * ``cdr_radius``
  * ``cdr_tds``
  * ``cel_radius``
  * ``cel_tds``
  * ``chan_also``
  * ``chan_console``
  * ``chan_mgcp``
  * ``chan_motif``
  * ``chan_oss``
  * ``chan_phone``
  * ``chan_skinny``
  * ``chan_unistim``
  * ``res_calendar_caldav``
  * ``res_calendar_ews``
  * ``res_calendar_exchange``
  * ``res_calendar_icalendar``
  * ``res_calendar``
  * ``res_snmp``
  * ``res_xmpp``


Consult the  `19.17 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10061>`_ for more information.


19.16
=====

* ``xivo-amid-client`` has been renamed to ``wazo-amid-client``

* ``wazo-auth`` http configuration section have been moved onto the rest_api
  section, eg::

    rest_api:
      https:
        listen: <ip>
        port: <port>
        certificate: </path/to/cert>
        private_key: </path/to/key>

  becomes::

    rest_api:
      listen: <ip>
      port: <port>
      certificate: </path/to/cert>
      private_key: </path/to/key>

* The default value for Asterisk PJSIP configuration parameter ``rtptimeout`` has been set to 7200
  seconds on new installs only. The change was done to automatically delete ghost calls that might
  get stuck. If you wish to modify this value, use the ``/asterisk/sip/general`` endpoint in
  ``wazo-confd`` API.

Consult the  `19.16 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10054>`_ for more information.


19.15
=====

* We have standardize the stevedore entry point namespace for our python client. If you have custom
  plugins, Be sure to use the full client name for the namespace. (e.g. ``auth_client.commands`` -->
  ``wazo_auth_client.commands``)

* The directed call pickup extension ``*8XXXX`` has been disabled by default on new installations,
  because it made it possible for any user to pickup any other user, including users for whom it
  should not be possible. This does not apply to upgrades, but if you wish to disable this feature,
  you can do it with ``wazo-confd`` ``/extensions/features`` API endpoint.

Consult the  `19.15 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10046>`_ for more information.


19.14
=====

* A new version (v2) of websocket protocol has been created. See :ref:`Wazo WebSocket
  <wazo-websocketd>` for more information

  The v1 is now deprecated and should not be used anymore. Also it does not return the attribute
  ``msg`` in all payloads as it was always empty.

* ``xivo-confgend`` has been renamed to ``wazo-confgend``

  * The custom configuration files have been moved to :file:`/etc/wazo-confgend/conf.d`
  * The log file has been renamed to :file:`wazo-confgend.log`
  * The plugin entry points have been renamed from ``xivo`` to ``wazo``. Plugins enabled in custom
    configuration files should use the new name.
  * The entry point identifier has been changed from ``xivo_confgend`` to ``wazo_confgend``. If you
    have developed custom plugins for confgend you should use the new identifier in your
    :file:`setup.py`.

* ``xivo-confgend-client`` has been renamed to ``wazo-confgend-client``

  * If you used the ``xivo-confgen`` CLI tool you will now have to use ``wazo-confgen``

* If you are upgrading a Wazo that was originally installed in 18.03 or earlier, the old directory
  configuration is now replaced with a new profile ``default`` for each tenant. The migration of the
  old directory configuration must be done manually, since there is no way to automatically detect
  the tenant for each directory configuration. To allow this migration, the old configuration is
  dumped in ``/var/backups/xivo/dird_sources.yml`` during the upgrade to Wazo Platform 19.14. The
  administrator must then recreate the directory configuration manually using the API or web
  interface.

* There is a `known bug <https://wazo-dev.atlassian.net/browse/WAZO-1254>`_ that will remove
  pre-recorded sound files provided by the ``xivo-sounds-*``, .e.g ``xivo-sounds-fr-ca``. If you had
  installed one of these packages manually, you need to install the corresponding ``wazo-sounds-*``
  package manually, e.g. ``wazo-sounds-fr-ca``. Upgrades to Wazo >= 19.15 are not affected by this
  bug.


Consult the  `19.14 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10045>`_ for more information.


19.13
=====

* **Debian has been upgraded from version 9 (stretch) to 10 (buster).**
  Please consult the following detailed upgrade notes for more information:

 .. toctree::
    :maxdepth: 1

    19.13/buster


* ``xivo-amid`` has been renamed to ``wazo-amid``

  * The custom configuration has been moved to ``/etc/wazo-amid/conf.d/``.
  * The log file has been renamed to ``wazo-amid.log``.
  * The NGINX proxy has been recreated in ``/etc/nginx/locations/https-enabled/wazo-amid``.

Consult the  `19.13 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10029>`_ for more information.


19.12
=====

General
-------

.. Major changes

* All administration interfaces ``xivo-web-interface`` and ``wazo-admin-ui`` have been removed. They
  are replaced by ``wazo-ui``. To install it, run the following command after the upgrade: ``apt
  install wazo-ui``.
* The Wazo Client and ``xivo-ctid`` have been removed.
* ``wazo-dird`` is now configured using its REST API. The previous configuration files have been
  removed and a new profile ``default`` is now created for each new tenant.
* `Entity` concept has been replaced by `Tenant`. The previous concept was not completely sealed and
  we have fixed it with the `tenant`.

  * Existing devices are migrated automatically to the tenant of their first associated line. If a
    device is in autoprov mode, it will be migrated to the default tenant. See
    :ref:`intro-provisioning` for more information on how device tenants are handled.
  * Agents are now multi-tenant. Agents created using the rest API that were not logged into a queue
    and that were not associated to a user have been deleted.
  * Skills are migrated to the tenant of the agent with whom they are associated. If a skill was not
    associated with an agent, it has been deleted.
  * All the existing skill rules have been associated to the tenant of the first queue found in the
    database. If there were no queue configured in the system, the skill rules have been deleted.
  * Call logs are now multi-tenant. Each call log that cannot be associated to a tenant has been
    associated to the ``master`` tenant. Also for all call logs created after the upgrade, if the
    tenant cannot be extracted from call informations, they will be associated to the master tenant.

  .. toctree::
     :maxdepth: 1

     19.03/sounds

  * We needed to do some guesswork for ambiguous resources that shared other resources from
    different entities. These resources have been migrated to the most logical tenants. However, it
    may be possible that they are still associated to resources that were migrated to different
    tenants. When this happens, you need to fix them manually and to make sure to remove the
    affected resources or to recreate them in the right tenants. Even if they still work, these
    configurations are invalid and shall be removed automatically in future upgrades. Therefore,
    you should review the following resources:

      * call permissions
      * ivr
      * moh
      * pagings

.. Minor changes

* User authentication has been updated with the following changes:

  * User passwords cannot be returned in plain text anymore.
  * Users export (export CSV) cannot export passwords anymore.
  * Processing time to import users (import CSV) has been increased significantly if the field
    ``password`` is provided.
  * Fields ``username`` and ``password`` in ``wazo-confd`` API ``/users`` are now ignored for
    authentication and must be considered invalid. They have been replaced by ``wazo-auth`` API.
  * Field ``enabled`` for ``wazo-confd`` API ``/users/<user_id>/cti`` is now ignored for
    authentication and must be considered invalid. It has been replaced by ``wazo-auth`` API.

* Invalid user email address (e.g. ``invalid@``) have been deleted automatically during upgrade.
* All agents will have to log out and log back in to receive calls from queues. You may use the
  command ``wazo-agentd-cli -c "relog all"`` to do this.
* The procedure for custom certificates, especially for Let's Encrypt certificates, has been
  simplified. See :ref:`https_certificate`.
* People using the ``xivo-aastra-2.6.0.2019`` will have to upgrade to plugin version 1.9.2 or later
* ``wazo-provd`` now uses YAML configuration. The defaults can be overridden in the
  :file:`/etc/wazo-provd/conf.d/` directory. See :ref:`configuration-files`.
* The provisioning option :ref:`dhcp-integration` is now enabled by default. There is no REST API to
  disable this feature.
* Call pickups that have been created using the REST API or ``wazo-admin-ui`` have the interceptors
  and targets mixed up. Since call pickups created using the "orange" web-interface did not have
  that bug, we could not fix the existing configuration automatically. Faulty call pickups have to
  be edited and users moved from interceptors to targets and vice versa.
* Since the feature for managing certificates from the "orange" web-interface is gone, all
  certificates must now be managed manually. The directory to access to certificates is
  :file:`/var/lib/xivo/certificates` and is not backuped or synchronized for HA anymore.
* If a group or queue was named ``general``, then it has been renamed with one or more suffix ``_``
  (e.g. ``general_``). The name ``general`` is not allowed anymore.
* ``xivo-sysconfd`` is now asynchronous by default. This implies that changes made via the API or
  via a web interface may take some time to take effect after the action. If you rely on Asterisk
  being reloaded when configuring resources. See :ref:`sysconfd-configuration` to set the
  ``synchronous`` option to ``true``.
* Upgrade from version older than 15.01 are not supported anymore.
* If a custom context (created using the REST API or wazo-admin-ui) was named with the following
  names, then it has been renamed with one or more suffix ``_``. Also if the context name had
  invalid characters (i.e. space), then invalid characters are replaced by ``_``. All custom
  configuration should be updated to reflect the changes.

  * `authentication`
  * `general`
  * `global`
  * `globals`
  * `parkedcalls`
  * `xivo-features`
  * `zonemessages`

* The ``wazo-google`` and ``wazo-microsoft`` plugins have been copied to the ``wazo-auth`` and
  ``wazo-dird`` repo. You **must** uninstall that plugin if you installed it manually from source to
  avoid conflicts between the supported version and the legacy version.


Asterisk related
----------------

* Asterisk version has been updated:

  .. toctree::
     :maxdepth: 1

     18.12/asterisk_16

* Wazo now uses ``res_pjsip`` instead of ``chan_sip``.

  * All custom lines with interface ``SIP/something`` must be changed to ``PJSIP/something``
  * All custom dialplan using the ``SIP_HEADER`` dialplan function must be changed to
    ``PJSIP_HEADER`` function
  * The ``SIPAddHeader`` and ``SIPRemoveHeader`` dialplan application must be changed to
    ``PJSIP_HEADER`` function

* The username for all SIP devices in ``autoprov`` mode has been changed. Devices in ``autoprov``
  mode will have to be restarted before entering the provisioning code.
* Asterisk configuration files can now be customized in the :file:`/etc/asterisk/*.d/` directories.
  If you had custom configuration in :file:`/etc/asterisk/*.conf` you will have to create a new file
  in the corresponding :file:`*.d` directory to use your customized configuration. Files named
  :file:`*.conf.dpkg-old` will be left in :file:`/etc/asterisk` if this operation is required. See
  :ref:`asterisk-configuration` for more details.
* The skill rules internal names have been changed to use the format ``skillrule-<id>``. If you were
  using custom dialplan with a preprocess subroutine to handle your skill rules, we recommend
  removing it and using the REST API (see :ref:`skill-apply`). If you really want to keep it, you
  must change the name used in the variable ``XIVO_QUEUESKILLRULESET`` to use the new format.
* Asterisk logs (:file:`/var/log/asterisk/full`) now contain milliseconds
* The ``tenant_name`` variable has been removed from the call recording templates in favor of the
  ``tenant_uuid``. If the ``tenant_name`` was used in the directory name, a symlink can be used to
  keep the same name.


Renaming
--------

* The following services have been renamed:

  * ``xivo-agentd`` to ``wazo-agentd``
  * ``xivo-agid`` to ``wazo-agid``
  * ``xivo-confd`` to ``wazo-confd``
  * ``xivo-ctid-ng`` to ``wazo-calld``
  * ``xivo-dird`` to ``wazo-dird``
  * ``wazo-dird-phoned`` to ``wazo-phoned``
  * ``xivo-provd`` to ``wazo-provd``
  * ``xivo-nginx`` to ``wazo-nginx``

* Each service has the following changes:

  * The custom configuration has been moved to :file:`/etc/<new-service-name>/conf.d/`.
  * The log file has been renamed to :file:`<new-service-name>.log`.
  * The NGINX proxy has been recreated in
    :file:`/etc/nginx/locations/https-enabled/<new-service-name>`
  * Entrypoints for custom Python plugins have been renamed to :file:`<new_service_name.*`.
  * Environment variable for ``wazo-upgrade`` has been renamed from ``XIVO_CONFD_PORT`` to
    ``WAZO_CONFD_PORT``.
  * All users that are logged in Wazo, i.e. who have an authentication token, must logout and log
    back in, to apply the change of authorizations names (ACL).

* The following Python clients have been renamed. If you were using the old one in your
  Python code you should use the new one.

  * ``xivo-agentd-client`` to ``wazo-agentd-client``
  * ``xivo-confd-client`` to ``wazo-confd-client``
  * ``xivo-dird-client`` to ``wazo-dird-client``
  * ``xivo-provd-client`` to ``wazo-provd-client``

* ``xivo-agentd-cli`` has been renamed to ``wazo-agentd-cli``
* ``xivo-provd-cli`` has been renamed to ``wazo-provd-cli``
* ``xivo-dhcpd-update`` has been renamed to ``wazo-dhcpd-update``
* The fail2ban jail was renamed from ``asterisk-xivo`` to ``asterisk-wazo``.
* Chat messages, user and device presences are now handled by ``wazo-chatd`` instead of
  ``wazo-calld`` and ``MongooseIM``.

   * All chat messages will be deleted after the upgrade.

* The :file:`/var/lib/xivo/sounds` directory has been migrated to :file:`/var/lib/wazo/sounds` and
  the directory :file:`/var/lib/xivo` is considered deprecated. Please update all custom references
  to this path.


Developers
----------

* The following daemons have been updated to Python 3. If you have written or installed a custom
  plugin for those daemons, you must ensure that the plugins are compatible with Python 3.

  * ``wazo-auth``
  * ``wazo-calld``
  * ``wazo-confd``
  * ``wazo-dird``

* The following backends in ``wazo-auth`` have been removed. All following users have been
  migrated to ``wazo_user`` backend.

  * ``xivo_admin``
  * ``xivo_service``
  * ``xivo_user``

* ``wazo-auth`` API to implement a ``wazo-auth`` backend has been changed in 18.02.
  The compatibility code that allowed old backends to keep working has been removed.

  * The ``get_ids`` method has been removed.

* ACL templating has been modified: when generating multiple ACLs with one template, ACL were
  separated with ``\n``. They are now separated with ``:`` (colon). ``\n`` is not interpreted
  anymore. You should hence replace any ``\n`` with ``:`` in your ACLs.
* ``wazo-provd`` now uses ``wazo-auth`` to authenticate all requests and uses HTTPS. It is no longer
  possible to deactivate authentication. Therefore, all calls to the REST API will need to be made
  using HTTPS and a token generated with ``wazo-auth``.
* ``wazo-provd-cli`` has been updated to remove the username and password command line arguments
  since they are no longer used.

* The configuration of ``rest_api`` section for ``wazo-confd`` configuration file has changed. See
  `wazo-confd changelog 19.06
  <https://github.com/wazo-platform/wazo-confd/blob/master/CHANGELOG.md#1906>`_ for more
  information.

* All API related to ``cti profile`` have been removed. See `wazo-confd changelog 19.08
  <https://github.com/wazo-platform/wazo-confd/blob/master/CHANGELOG.md#1908>`_ for more
  information.

* Creating a resource using the REST API now requires the ``Wazo-Tenant`` HTTP header when the
  created resource is not in the same tenant as its creator.
* Authentication policies now have a ``tenant_uuid`` and the relationship between tenants and
  policies has been removed. If you did use policies with tenant association, the policy is now
  associated to one of its tenant. This feature is not used yet in Wazo, so most likely you are not
  affected.
* ``wazo-confd`` REST API does not allow to manage ``call-logs`` anymore.

* ``wazo-provd`` API URL has been updated to remove the ``provd`` prefix when present and add the
  API version number, which is ``0.2``. All affected services and ``wazo-provd-client`` have been
  updated.  Example: ``/provd/dev_mgr`` is now ``/0.2/dev_mgr`` and ``/api/api.yml`` is now
  ``/0.2/api/api.yml``

Consult the roadmaps for more information:

   * `18.14 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10003>`_
   * `19.01 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10007>`_
   * `19.02 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10009>`_
   * `19.03 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10013>`_
   * `19.04 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10014>`_
   * `19.05 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10017>`_
   * `19.06 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10020>`_
   * `19.07 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10022>`_
   * `19.08 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10023>`_
   * `19.09 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10024>`_
   * `19.10 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10026>`_
   * `19.11 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10027>`_
   * `19.12 <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10028>`_


18.03
=====

* If you have a :ref:`custom certificate configured<https_certificate>`, you will need to add a new
  symlink for wazo-upgrade::

    mkdir -p /etc/wazo-upgrade/conf.d
    ln -s "/etc/xivo/custom/custom-certificate.yml" "/etc/wazo-upgrade/conf.d/010-custom-certificate.yml"

* Default passwords for phones' web interfaces have been changed. You can change the password in
  :menuselection:`Configuration --> Provisioning --> Template device`.

* The default NAT option in General SIP settings has been automatically changed from
  ``auto_force_rport`` to ``auto_force_rport,auto_comedia``. This makes NAT configuration easier but
  has no impact on environments without NAT.

  * In the rare cases where you want to keep ``nat=auto_force_rport`` you must explicitly change
    this value in the administation interface :menuselection:`Services --> IPBX --> General Settings
    --> SIP Protocol` in tab `Default`. See `Asterisk sip.conf sample
    <https://github.com/asterisk/asterisk/blob/15.1.1/configs/samples/sip.conf.sample#L869>`_ for
    more informations.

* The NAT configuration of every SIP line and SIP trunk has been automatically changed from
  ``nat=auto_force_rport`` to nothing, so that they inherit this setting from the General SIP
  settings.


18.02
=====

* For wazo-auth backend developers: The API to implement a wazo-auth backend has changed.
  Old implementations have to be updated. If the BaseAuthenticationBackend class was used
  as a base class for the backend the `get_metadata` method from the base class will use
  `get_ids` to generate the result of `get_metadata`.

  * The `get_ids` method has been removed.
  * The `get_metadata` method has been added.


18.01
=====

* **Debian has been upgraded from version 8 (jessie) to 9 (stretch).**
  Please consult the following detailed upgrade notes for more information:

 .. toctree::
    :maxdepth: 1

    18.01/stretch

* If you *did not* setup a custom X.509 certificate for HTTPS (e.g. from Let's Encrypt), the
  certificate will be regenerated to include SubjectAltName fields. The two main reasons are Chrome
  compatibility and avoiding a lot of log warnings. This implies that you will have to add a new
  exception in your browser to access the Wazo web interface or services like `Unicom
  <https://phone.wazo.community>`_.

* If you *did* setup a custom X.509 certificate for HTTPS (e.g. from Let's Encrypt), you will have
  to add a link to the wazo-auth-cli configuration using the following command.

  .. code-block:: sh

    ln -s "/etc/xivo/custom/custom-certificate.yml" "/etc/wazo-auth-cli/conf.d/010-custom-certificate.yml"


* The Python API for xivo-confd plugins has been updated to reflect Python API of other daemons. If
  you have created a custom xivo-confd plugin, you must update it:

  .. code-block:: python
     :emphasize-lines: 4-5
     :caption: plugin.old.py

     class Plugin(object):

        def load(self, core):
            api = core.api
            config = core.config


  .. code-block:: python
     :emphasize-lines: 4-5
     :caption: plugin.py

     class Plugin(object):

        def load(self, dependencies):
            api = dependencies['api']
            config = dependencies['config']

* The web interface no longer validates the queue skill rules fields added in
  :menuselection:`Services --> Call Center --> Configuration --> Skill rules`. If a rule is wrong,
  it will appear in the Asterisk console.


Archives
========

.. toctree::
   :maxdepth: 2

   old_upgrade_notes
