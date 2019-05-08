.. _upgrade-notes:

*************
Upgrade notes
*************

19.07
=====

* Upgrade from version older than 15.01 are not supported anymore.
* If a group or queue was named ``general``, then it has been renamed with one or more suffix ``_``
  (e.i. ``general_``). The name ``general`` is no more allowed.
* xivo-sysconfd is now async by default. If you rely on Asterisk being reloaded when configuring resources.
  See :ref:`sysconfd-configuration` to set the `synchronous` option to `true`
* The configuration of ``rest_api`` section for ``xivo-confd`` configuration file has changed. See
  `xivo-confd changelog <https://github.com/wazo-pbx/xivo-confd/blob/master/CHANGELOG.md#1907>`_ for
  more information.
* xivo-ctid-ng was renamed to wazo-calld. All users that are logged in Wazo must logout and log back
  in, to apply the change of authorizations names (ACL).
* Skills are migrated to the tenant of the agent with whom they are associated. If a skill was not
  associated with an agent, is has been deleted.
* All the existing skill rules have been associated to the tenant of the first queue found in the
  database. If no queue was found, meaning there was no queue, the skill rules were deleted.
* The skill rules internal names have been changed to use the format ``skillrule-<id>``. If you were
  using custom dialplan with a preprocess subroutine to handle your skill rules, we recommend
  removing it and using the REST API (see :ref:`skill-apply`). If you really want to keep it, you
  must change the name used in the variable ``XIVO_QUEUESKILLRULESET`` to use the new format.

Consult the `19.07 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10022>`_ for more information


19.06
=====

* All administration interfaces ``xivo-web-interface`` and ``wazo-admin-ui``  have been removed
* Agents are now multi-tenant. Agents created using the rest API that were not logged into a queue
  and that were not associated to a user have been deleted.

Consult the `19.06 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10020>`_ for more information


19.05
=====

* ``xivo-provd-client`` is now deprecated. You must use ``wazo-provd-client`` instead.
* The ``tenant_name`` variable has been removed from the call recording templates in favor of the ``tenant_uuid``.
  If the ``tenant_name`` was used in the directory name, a symlink can be used to keep the same name.
* All chat messages will be deleted after the upgrade. There are now handled by ``wazo-chatd``
  instead of ``xivo-ctid-ng`` and ``MongooseIM``.

Consult the `19.05 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10017>`_ for more information


19.04
=====

* ``wazo-dird`` is now configured using its REST API. The previous configuration have been removed and
  a new configuration has been automatically generated based on the current tenants and internal contexts.

* ``xivo-provisioning`` and ``xivo-confd`` now implement multi-tenant devices.
  Existing devices are migrated automatically to the tenant of their first associated line. If a device is
  in autoprov mode, it will be migrated to the default tenant.

  See :ref:`intro-provisioning` for more information on how device tenants are handled.

* Call pickups that have been created using the REST API or wazo-admin-ui have the interceptors
  and targets mixed up. Since call pickups created using the "normal" web interface did not have
  that bug, we could not fix the existing configuration automatically. Faulty call pickups will
  have to be edited and users moved from interceptors to targets and vice versa.

* The provisioning option :ref:`dhcp-integration` is now enabled by default. There is no REST API to disable this feature.

* User and device presences are now handled by ``wazo-chatd`` instead of ``xivo-ctid-ng``.

* ``xivo-ctid`` has been removed, therefore the ``wazoclient`` will not connect anymore.

Consult the `19.04 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10014>`_ for more information


19.03
=====

* `xivo-provisioning` now uses YAML configuration. The defaults can be overriden in the `/etc/xivo-provd/conf.d/` directory. See :ref:`configuration-files`.

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   19.03/sounds

Consult the `19.03 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10013>`_ for more information


19.02
=====

* For wazo-auth backend developers: The API to implement a wazo-auth backend has been changed in
  18.02.
  The compatibility code that allowed old backends to keep working has been removed.

  * The `get_ids` method has been removed.

* ACL templating has been modified: when generating multiple ACLs with one template, ACL were
  separated with ``\n``. They are now separated with ``:`` (colon). ``\n`` is not interpreted
  anymore. You should hence replace any ``\n`` with ``:`` in your ACLs.
* `xivo-provisioning` now uses `wazo-auth` to authenticate all requests and uses HTTPS. It is no
  longer possible to deactivate authentication. Therefore, all calls to the REST API will need to
  be made using HTTPS and a token generated with `wazo-auth`.
* `xivo-provd-cli` has been updated to remove the username and password command line arguments since
  they are no longer used.

Consult the `19.02 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10009>`_ for more information


19.01
=====

* The `xivo` `wazo-dird` backend has been renamed `wazo`. Custom directory configuration files will have to be updated.
* The procedure for custom certificates, especially for Let's Encrypt certificates, has been simplified. See :ref:`https_certificate`.
* The `xivo_admin` backend in wazo-auth has been removed. All `xivo_admin` users have been
  migrated to `wazo_user` backend.

Consult the `19.01 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10007>`_ for more information.


18.14
=====

* The username for all SIP devices in autoprov mode has been changed. Devices in autoprov mode will
  have to be restarted before entering the provisioning code.
* All agents will have to log out and log back in to receive calls from queues
* People using the xivo-aastra-2.6.0.2019 will have to upgrade to version 1.9.2 or later
* The `xivo_service` backend in wazo-auth has been removed. All `xivo_service` users have been
  migrated to `wazo_user` backend.
* The fail2ban jail was renamed from ``asterisk-xivo`` to ``asterisk-wazo``.
* Wazo now uses res_pjsip instead of chan_sip.

  * All custom lines with interface ``SIP/something`` must be changed to ``PJSIP/something``
  * All custom dialplan using the ``SIP_HEADER`` dialplan function must be changed to ``PJSIP_HEADER`` function
  * The ``SIPAddHeader`` and ``SIPRemoveHeader`` dialplan application must be changed to ``PJSIP_HEADER`` function

Consult the `18.14 Roadmap <https://wazo-dev.atlassian.net/secure/ReleaseNote.jspa?projectId=10011&version=10003>`_ for more information.


18.13
=====

* The following daemons have been updated to Python 3. If you have written or installed a custom
  plugin for those daemons, you must ensure that the plugins are compatible with Python 3.

  * wazo-auth
  * wazo-dird
  * xivo-ctid-ng

Consult the `18.13 Roadmap <https://projects.wazo.community/versions/285>`_ for more information.


18.12
=====

Please consult the following detailed upgrade notes for more information:

.. toctree::
   :maxdepth: 1

   18.12/asterisk_16

Consult the `18.12 Roadmap <https://projects.wazo.community/versions/283>`_ for more information.


18.11
=====

* Asterisk logs (``/var/log/asterisk/full``) now contain milliseconds

Consult the `18.11 Roadmap <https://projects.wazo.community/versions/282>`_ for more information.


18.10
=====

Consult the `18.10 Roadmap <https://projects.wazo.community/versions/281>`_ for more information.


18.09
=====

Consult the `18.09 Roadmap <https://projects.wazo.community/versions/280>`_ for more information.


18.08
=====

Consult the `18.08 Roadmap <https://projects.wazo.community/versions/279>`_ for more information.


18.07
=====

* Upgrade from version older than 14.01 are not supported anymore.

Consult the `18.07 Roadmap <https://projects.wazo.community/versions/278>`_ for more information.


18.06
=====

Consult the `18.06 Roadmap <https://projects.wazo.community/versions/276>`_ for more information.


18.05
=====

* ``xivo-dird`` has been renamed ``wazo-dird``

  * The custom configuration has been moved to ``/etc/wazo-dird/conf.d/``.
  * The log file has been renamed to ``wazo-dird.log``.
  * The NGINX proxy has been recreated in ``/etc/nginx/locations/https-enabled/wazo-dird``
  * Entrypoint for custom plugin has been renamed to ``wazo_dird.*``.

* ``xivo-dird-client`` has been renamed ``wazo-dird-client``

  * If you were using the xivo-dird-client in your python code you should use the wazo-dird-client which
    has the same interface at the moment.

* wazo-dird now uses a token to authenticate when doing searches on xivo-confd

  * See :ref:`dird-backend-wazo` if you have customized configuration files in
    `/etc/wazo-dird/sources.d` or `/etc/wazo-dird/conf.d` for a source of type `xivo`
  * If you are using custom certificates you will have to modify your directory configuration to add
    your certificate. See :ref:`https_certificate` for more information in the `Use your own
    certificate` section.

* Authentication policies now have a `tenant_uuid` and the relationship between tenants and policies
  has been removed. If you did use policies with tenant association, the policy is now associated to
  one of its tenant. This feature is not used yet in Wazo, so most likely you are not affected.

Consult the `18.05 Roadmap <https://projects.wazo.community/versions/275>`_ for more information.


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
  * Time to import users (import CSV) has been increased significatively if the field password is
    provided.
  * Fields `username` and `password` in xivo-confd API `/users` don't have impact anymore on
    authentication and must be considered as invalid. To change these values, use wazo-auth API
    instead.
  * Fields `enabled` for xivo-confd API `/users/<user_id>/cti` don't have impact anymore on
    authentication and must be considered as invalid. To change this value, use wazo-auth API
    instead.
  * In wazo-auth, the backend `xivo_user` has been removed.
  * In xivo-ctid, the default authentication backend is now `wazo_user`.

* Default phone passwords are now auto-generated. Switchboard users with a Snom device will now have
  to add a configuration file to store the username and password.
* Creating user using the REST API now requires the Wazo-Tenant HTTP header when the created user is
  not in the same tenant has its creator.
* Tenants have been automatically created to match configured entities.

Consult the `18.04 Roadmap <https://projects.wazo.community/versions/274>`_ for more information.


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

Consult the `18.03 Roadmap <https://projects.wazo.community/versions/272>`_ for more information.


18.02
=====

* For wazo-auth backend developers: The API to implement a wazo-auth backend has changed.
  Old implementations have to be updated. If the BaseAuthenticationBackend class was used
  as a base class for the backend the `get_metadata` method from the base class will use
  `get_ids` to generate the result of `get_metadata`.

  * The `get_ids` method has been removed.
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

* The web interface no longer validates the queue skill rules fields added in
  :menuselection:`Services --> Call Center --> Configuration --> Skill rules`. If a rule is wrong,
  it will appear in the Asterisk console.

Consult the `18.01 Roadmap <https://projects.wazo.community/versions/271>`_ for more information.


Archives
========

.. toctree::
   :maxdepth: 2

   old_upgrade_notes
