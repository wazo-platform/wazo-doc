.. _upgrade-notes:

*************
Upgrade notes
*************

18.04
=====

* Invalid user email will be deleted automatically during upgrade.
* Asterisk configuration files can now be customized in the :file:`/etc/asterisk/*.d/` directories.
  If you had custom configuration in :file:`/etc/asterisk/*.conf` you will have to create a new file
  in the corresponding `.d` directory to use your customized configuration. Files named
  :file:`*.conf.dpkg-old` will be left in :file:`/etc/asterisk` if this operation is required. See
  :ref:`asterisk-configuration` for more details.
* The user authentication has been updated with the following impacts:

  * User's password cannot be returned in plain text anymore.
  * Users export (export CSV) cannot export password anymore.
  * Time to import users (import CSV) has been increased significatively if the field password is provided.
  * Fields `username` and `password` in xivo-confd API `/users` don't have impact anymore on authentication and must be considered as invalid. To change these values, use wazo-auth API instead.
  * Fields `enabled` for xivo-confd API `/users/<user_id>/cti` don't have impact anymore on authentication and must be considered as invalid. To change this value, use wazo-auth API instead.
  * In wazo-auth, the backend `xivo_user` has been removed.
  * In xivo-ctid, the default authentication backend is now `wazo_user`.

* Default phone passwords are now auto-generated. Switchboard users with a Snom device will now have to add a configuration file to store the username and password. See :ref:`switchboard_device_snom`
* Creating user using the REST API now requires the Wazo-Tenant HTTP header when the created user is not in the same tenant has its creator.
* Tenants have automatically created to match configured entities.


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

* The NAT configuration of every SIP line and SIP trunk has been automatically changed from ``nat=auto_force_rport`` to nothing, so that they inherit this setting from the General SIP settings.

Consult the `18.03 Roadmap <https://projects.wazo.community/versions/272>`_ for more information.


18.02
=====

* For wazo-auth backend developers: The API to implement a wazo-auth backend has changed.
  Old implementations have to be updated. If the BaseAuthenticationBackend class was used
  as a base class for the backend the `get_metadata` method from the base class will use
  `get_ids` to generate the result of `get_metadata`.

  * The `get_ids` method has been remove.
  * The `get_metadata` method has been added.

Consult the `18.02 Roadmap <https://projects.wazo.community/versions/264>`_ for more information.


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

* The web interface no longer validates the queue skill rules fields added in :menuselection:`Services --> Call Center --> Configuration --> Skill rules`. If a rule is wrong, it will appear in the Asterisk console.

Consult the `18.01 Roadmap <https://projects.wazo.community/versions/271>`_ for more information.


17.17
=====

* The default NAT option has changed from ``no`` to ``auto_force_rport``. This makes NAT
  configuration easier but has no impact on environments without NAT.

  * In the rare cases where you want to keep ``nat=no`` you must explicitly change this value in the
    administation interface :menuselection:`Services --> IPBX --> General Settings --> SIP Protocol`
    in tab `Default`. See `Asterisk sip.conf sample
    <https://github.com/asterisk/asterisk/blob/15.1.1/configs/samples/sip.conf.sample#L869>`_ for
    more informations.

* The ``sources`` section of the ``xivo-dird`` service configuration has been changed to be a key-value setting.

  * If you have configured directories manually in ``/etc/xivo-dird`` you should update your manual configuration:

  .. code-block:: yaml
     :emphasize-lines: 4-6
     :caption: old.yml

     services:
       lookup:
         default:
           sources:
             - source_one
             - source_two
           timeout: 2


  .. code-block:: yaml
     :emphasize-lines: 4-6
     :caption: new.yml

     services:
       lookup:
         default:
           sources:
             source_one: true
             source_two: true
           timeout: 2

* The ``enabled_plugins`` section of the ``xivo-confd`` service configuration has been changed. If
  you have configured enabled plugins manually you should update your manual configuration

  * This section is now a key-value setting.

  * All plugins have been renamed without the suffix ``_plugins``.

  .. code-block:: yaml
     :caption: old.yml

     enabled_plugins:
       - user_plugin
       - conference_plugin


  .. code-block:: yaml
     :caption: new.yml

     enabled_plugins:
       user: true
       conference: true

* There is a new ``channelvars`` option in ``/etc/asterisk/manager.d/99-general.conf``. If you have
  manually configured ``channelvars`` already, you will have to manually merge the Wazo version with
  your version for them to work together.

Consult the `17.17 Roadmap <https://projects.wazo.community/versions/270>`_ for more information.


17.16
=====

* You must update the Wazo Client to 17.16. See the :ref:`Wazo Client compatibility table <cti_client_compatibility>`.

* The *enabled_plugins* section of the ``wazo-auth`` service has been renamed *enabled_backend_plugins* and is now a dictionary.

  * If you have hand made configuration to modify the list of enabled backends it should be modified see ``/etc/wazo-auth/config.yml``

* The *ldap_user* backend in ``wazo-auth`` is now disabled in the base configuration file.

  * If you are using the ``ldap_user`` authentication backend a file with the following content should be added to ``/etc/wazo-auth/conf.d``

    .. code-block:: yaml
    
       enabled_backend_plugins:
         ldap_user: true

* The *enabled_plugins* section of the ``xivo-dird`` service is now a dictionary.

  * If you have hand made configuration to modify the list of enabled plugins, it should be modified see ``/etc/xivo-dird/config.yml``

* wazo-admin-ui has been upgraded to python3. All plugins by `Wazo Team` has been migrated, but if
  you have installed a non-official/custom plugin that add something to the new interface, it
  probably broken. To fix this, you must convert your plugin to python3 or wait an available upgrade
  from the maintainer.

* If you have setup a custom X.509 certificate for HTTPS (e.g. from Let's Encrypt), you have to
  update your config in ``/etc/xivo/custom/custom-certificate.yml``, according to the :ref:`updated
  documentation <https_certificate>`, namely for the config regarding ``websocketd``.

Consult the `17.16 Roadmap <https://projects.wazo.community/versions/269>`_ for more information.


17.15
=====

* ``xivo-call-logd`` has been renamed ``wazo-call-logd``

  * The custom configuration has been moved to ``/etc/wazo-call-logd/conf.d/``.
  * The log file has been renamed to ``wazo-call-logd.log``.
  * The NGINX proxy has been recreated in ``/etc/nginx/locations/https-enabled/wazo-call-logd``

* ``Asterisk`` has been upgraded to version 15.0.0

  * If you have installed asterisk modules manually, you will have to install the asterisk 15 version, otherwise Asterisk will crash when starting.

Consult the `17.15 Roadmap <https://projects.wazo.community/versions/268>`_ for more information.


17.14
=====

* ``xivo-auth`` has been renamed ``wazo-auth``

  * If you have developed a ``xivo-auth`` authentication backend the name of the entry point has
    changed to ``wazo_auth.backends``. You should make this modification in your plugin's ``setup.py``
    file in the ``entry_point`` section.
  * If your custom development use service discovery to find ``xivo-auth``, you will have to search for
    the ``wazo-auth`` service instead of ``xivo-auth``.

* We released a new version of the CTI client, rebranded as `Wazo Client 17.14.1`. It is compatible
  with all previous versions of Wazo (i.e. not before 16.16). See also the :ref:`compatibility table
  <cti_client_compatibility>`.

Consult the `17.14 Roadmap <https://projects.wazo.community/versions/267>`_ for more information.


17.13
=====

Consult the `17.13 Roadmap <https://projects.wazo.community/versions/266>`_ for more information.


17.12
=====

* Wazo has a new database named ``mongooseim``. The :ref:`backup-restore procedure<backup>` has been
  updated to include this new database.

Consult the `17.12 Roadmap <https://projects.wazo.community/versions/265>`_ for more information.


17.11
=====

* wazo-plugind REST API version ``0.1`` has been deprecated and will be removed in Wazo ``18.02``. See changelog for version :ref:`rest-api_changelog`

Consult the `17.11 Roadmap <https://projects.wazo.community/versions/263>`_ for more information.


17.10
=====

Consult the `17.10 Roadmap <https://projects.wazo.community/versions/262>`_ for more information.


17.09
=====

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

Consult the `17.09 Roadmap <https://projects.wazo.community/versions/261>`_ for more information.


17.08
=====

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

Consult the `17.08 Roadmap <https://projects.wazo.community/versions/260>`_ for more information.


17.07
=====

Consult the `17.07 Roadmap <https://projects.wazo.community/versions/259>`_ for more information.


17.06
=====

* Upgrade from version older than 13.01 are not supported anymore.

Consult the `17.06 Roadmap <https://projects.wazo.community/versions/258>`_ for more information.


17.05
=====

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

Consult the `17.05 Roadmap <https://projects.wazo.community/versions/257>`_ for more information.


17.04
=====

Consult the `17.04 Roadmap <https://projects.wazo.community/versions/256>`_ for more information.


17.03
=====

Consult the `17.03 Roadmap <https://projects.wazo.community/versions/255>`_ for more information.


17.02
=====

* A few more services are now available by default on port TCP/443 (the complete list is documented
  in the :ref:`nginx` section). This does not pose any additional security risk by default, but if
  you have extra strict requirements about security, they can be manually disabled.

Consult the `17.02 Roadmap <https://projects.wazo.community/versions/254>`_ for more information.


17.01
=====

Consult the `17.01 Roadmap <https://projects.wazo.community/versions/253>`_ for more information.


16.16
=====

Wazo 16.16 is the *first public release* of the project under the Wazo name. It
is also the first release of Wazo under the "phoenix" codename.

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

Consult the `16.16 Roadmap <https://projects.wazo.community/versions/252>`_ for more information.


16.13
=====

XiVO 16.13 is the *last public release* of the project under the name XiVO.

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

Consult the `16.13 Roadmap <https://projects.wazo.community/versions/249>`_ for more information.


16.12
=====

Consult the `16.12 Roadmap <https://projects.wazo.community/versions/248>`_ for more information.


16.11
=====

* Fax reception: the "log" backend type has been removed. You should remove references to it in your
  :file:`/etc/xivo/asterisk/xivo_fax.conf` if you were using it. Now, every time a fax is processed,
  a log line is added to :file:`/var/log/xivo-agid.log`.

Consult the `16.11 Roadmap <https://projects.wazo.community/versions/247>`_ for more information.


16.10
=====

* The config file ``/etc/xivo/xivo-confgend.conf`` has been replaced with
  ``/etc/xivo-confgend/config.yml`` and ``/etc/xivo-confgend/conf.d``. Custom modifications to this
  file are not migrated automatically, so manual intervention is required to migrate custom values
  to the ``conf.d`` directory. The file ``/etc/xivo/xivo-confgend/asterisk/contexts.conf`` has been
  moved to ``/etc/xivo-confgend/templates/contexts.conf``, but custom modification are left
  untouched. See also :ref:`configuration-files` for more details about configuration files in XiVO.

Consult the `16.10 Roadmap <https://projects.wazo.community/versions/246>`_ for more information.


16.09
=====

* The Wazo Client now uses xivo-ctid-ng to do transfers. Those new transfers cannot be cancelled
  with the ``*0`` DTMF sequence and there is no interface in the Wazo Client to cancel a transfer
  for profiles other than the switchboard (bug `#6321`_). This will be addressed in a later version.

* Transfers started from the Wazo Client do not respect the ``Dial timeout on transfer`` option
  anymore (bug `#6322`_). This feature will be reintroduced in a later version.

.. _#6321: http://projects.wazo.community/issues/6321
.. _#6322: http://projects.wazo.community/issues/6322

Consult the `16.09 Roadmap <https://projects.wazo.community/versions/245>`_ for more information.


16.08
=====

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

Consult the `16.08 Roadmap <https://projects.wazo.community/versions/244>`_ for more information.


16.07
=====

* If you were affected by the `bug #6213 <http://projects.wazo.community/issues/6213>`_, i.e. if your agent
  login time statistics were incorrect since your upgrade to XiVO 15.20 or later, and you want to
  fix your statistics for that period of time, you'll need to `manually apply a fix
  <http://projects.wazo.community/issues/6213#note-3>`_.

Consult the `16.07 Roadmap <https://projects.wazo.community/versions/243>`_ for more information.


16.06
=====

Consult the `16.06 Roadmap <https://projects.wazo.community/versions/242>`_ for more information.


16.05
=====

* The ``view``, ``add``, ``edit``, ``delete`` and ``deleteall`` actions of the "lines" web service
  provided by the web interface have been removed.  As a reminder, note that the web services
  provided by the web interface are deprecated.

Consult the `16.05 Roadmap <https://projects.wazo.community/versions/241>`_ for more information.


16.04
=====

* :ref:`cti-protocol` is now in version *2.1*
* The field :guilabel:`Rightcall Code` from :menuselection:`Services -> IPBX -> IPBX Settings ->
  Users` under :guilabel:`Services` tab  will overwrite all password call permissions for the user.
* Faxes stored on FTP servers are now converted to PDF by default. See :ref:`fax-ftp` if you want
  to keep the old behavior of storing faxes as TIFF files.

Consult the `16.04 Roadmap <https://projects.wazo.community/versions/240>`_ for more information.


16.03
=====

* The new section :menuselection:`Services --> Statistics --> Switchboard` in the web interface will
  only be visible by a non-root administrator after adding the corresponding permissions in the
  administrator configuration.
* Update the switchboard configuration page for the statistics in
  :ref:`switchboard_configuration_multi_queues`.
* The API for associating a line to a device has been replaced. Consult the :ref:`xivo-confd
  changelog <rest-api_changelog>` for further details
* The configuration parameters of *xivo_ldap_user* plugin of *xivo-auth* has been changed. See
  :ref:`xivo_ldap plugin <auth-backends-ldap>`.
* The user's email is now a unique constraint. Every duplicate email will be deleted during
  the migration. (This does not apply to the voicemail's email)

Consult the `16.03 Roadmap <https://projects.wazo.community/versions/239>`_ for more information.


16.02
=====

* The experimental *xivo_ldap_voicemail* plugin of *xivo-auth* has been removed. Use the new
  :ref:`xivo_ldap plugin <auth-backends-ldap>`.
* Bus messages in the *xivo* exchange are now sent with the content-type `application/json`.
  Some libraries already do the message conversion based the content-type. Kombu users will
  receive a python dictionnary instead of a string containing json when a message is received.
* :ref:`xivo-ctid encryption <ctid-encryption>` is automatically switched on for every XiVO server
  and Wazo Client >= 16.02. If you really don't want encryption, you must disable it manually on
  the server after the upgrade. In that case, Wazo Clients will ask whether to accept the connection
  the first time.

Consult the `16.02 Roadmap <https://projects.wazo.community/versions/238>`_ for more information.


16.01
=====

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

Consult the `16.01 Roadmap <https://projects.wazo.community/versions/237>`_ for more information.


Archives
========

.. toctree::
   :maxdepth: 2

   old_upgrade_notes
