.. _confd_changelog:

*****************************
xivo-confd REST API changelog
*****************************

16.16
=====

* A new API for editing fallbacks for a group has been added:

  * GET ``/1.1/groups/<group_id>/fallbacks``
  * PUT ``/1.1/groups/<group_id>/fallbacks``

* A new API for editing fallbacks for a user has been added:

  * GET ``/1.1/users/<user_id>/fallbacks``
  * PUT ``/1.1/users/<user_id>/fallbacks``


16.15
=====

* New readonly parameters have been added to the voicemail resource:

  * ``users``

* A new API for associating trunks with an group has been added:

  * PUT ``/1.1/groups/<group_id>/members/users``

* A new API for associating an extension with a group has been added:

  * DELETE ``/1.1/groups/<group_id>/extensions/<extension_id>``
  * PUT ``/1.1/groups/<group_id>/extensions/<extension_id>``

* Added groups endpoints:

  * GET ``/1.1/groups``
  * POST ``/1.1/groups``
  * DELETE ``/1.1/groups/<group_id>``
  * GET ``/1.1/groups/<group_id>``
  * PUT ``/1.1/groups/<group_id>``


* New readonly parameters have been added to the ivr resource:

  * ``incalls``

* New readonly parameters have been added to the incall resource:

  * For destinations of type `ivr`:

      * ``ivr_name``

  * For destinations of type `user`:

      * ``user_firstname``
      * ``user_lastname``

  * For destinations of type `voicemail`:

      * ``voicemail_name``

* New readonly parameters have been added to the user resource:

  * ``voicemail``
  * ``incalls``

* Added contexts endpoints:

  * GET ``/1.1/contexts``
  * POST ``/1.1/contexts``
  * DELETE ``/1.1/contexts/<context_id>``
  * GET ``/1.1/contexts/<context_id>``
  * PUT ``/1.1/contexts/<context_id>``


16.14
=====

* Added users endpoints in REST API:

  * GET ``/1.1/users/<user_uuid>/lines/<line_id>/associated/endpoints/sip``

* New readonly parameters have been added to the line resource:

  * ``endpoint_sip``
  * ``endpoint_sccp``
  * ``endpoint_custom``
  * ``extensions``
  * ``users``

* New readonly parameters have been added to the extension resource:

  * ``lines``

* New readonly parameters have been added to the user resource:

  * ``lines``

* A new readonly parameter have been added to the endpoint_sip, endpoint_sccp and endpoint_custom
  resource:

  * ``line``

* Added outcalls endpoints:

  * GET ``/1.1/outcalls``
  * POST ``/1.1/outcalls``
  * DELETE ``/1.1/outcalls/<outcall_id>``
  * GET ``/1.1/outcalls/<outcall_id>``
  * PUT ``/1.1/outcalls/<outcall_id>``

* Added IVR endpoints:

  * GET ``/1.1/ivr``
  * POST ``/1.1/ivr``
  * DELETE ``/1.1/ivr/<ivr_id>``
  * GET ``/1.1/ivr/<ivr_id>``
  * PUT ``/1.1/ivr/<ivr_id>``

* A new API for associating trunks with an outcall has been added:

  * PUT ``/1.1/outcalls/<outcall_id>/trunks``

* A new API for associating an extension with an outcall has been added:

  * DELETE ``/1.1/outcalls/<outcall_id>/extensions/<extension_id>``
  * PUT ``/1.1/outcalls/<outcall_id>/extensions/<extension_id>``


16.13
=====

* New readonly parameters have been added to the trunks resource:

  * ``endpoint_sip``
  * ``endpoint_custom``

* A new readonly parameter have been added to the endpoint_sip and endpoint_custom resource:

  * ``trunk``

* A new API for associating an extension with an incall has been added:

  * DELETE ``/1.1/incalls/<incall_id>/extensions/<extension_id>``
  * PUT ``/1.1/incalls/<incall_id>/extensions/<extension_id>``

* Added incalls endpoints:

  * GET ``/1.1/incalls``
  * POST ``/1.1/incalls``
  * DELETE ``/1.1/incalls/<incall_id>``
  * GET ``/1.1/incalls/<incall_id>``
  * PUT ``/1.1/incalls/<incall_id>``


16.12
=====

* A new API for associating an endpoint with a trunk has been added:

  * DELETE ``/1.1/trunks/<trunk_id>/endpoints/sip/<endpoint_id>``
  * PUT ``/1.1/trunks/<trunk_id>/endpoints/sip/<endpoint_id>``
  * GET ``/1.1/trunks/<trunk_id>/endpoints/sip``
  * GET ``/1.1/endpoints/sip/<endpoint_id>/trunks``

  * DELETE ``/1.1/trunks/<trunk_id>/endpoints/custom/<endpoint_id>``
  * PUT ``/1.1/trunks/<trunk_id>/endpoints/custom/<endpoint_id>``
  * GET ``/1.1/trunks/<trunk_id>/endpoints/custom``
  * GET ``/1.1/endpoints/custom/<endpoint_id>/trunks``

* Added trunks endpoints:

  * GET ``/1.1/trunks``
  * POST ``/1.1/trunks``
  * DELETE ``/1.1/trunks/<trunk_id>``
  * GET ``/1.1/trunks/<trunk_id>``
  * PUT ``/1.1/trunks/<trunk_id>``

* Added SIP general endpoints:

  * GET ``/1.1/asterisk/sip/general``
  * PUT ``/1.1/asterisk/sip/general``


16.11
=====

* A new API for associating a user with an agent has been added:

  * DELETE ``/1.1/users/<user_id>/agents``
  * GET ``/1.1/users/<user_id>/agents``
  * PUT ``/1.1/users/<user_id>/agents/<agent_id>``

* A new API to list lines associated to an extension

  * GET ``/1.1/extensions/<extension_id>/lines``


* The following URLs have been deprecated. Please use the new API instead:

  * GET ``/1.1/extensions/<extension_id>/line``


16.10
=====

* Add possibility to associate many lines to the same user.
* Add possibility to associate many extensions to the same line (only if these lines are
  associated to the same user).
* A new API for associating a user with a voicemail has been added:

  * DELETE ``/1.1/users/<user_id>/voicemails``
  * GET ``/1.1/users/<user_id>/voicemails``
  * PUT ``/1.1/users/<user_id>/voicemails``

* A new API for associating a line with an extension has been added:

  * PUT ``/1.1/lines/<line_id>/extensions/<extension_id>``

* A new API for associating a user with a line has been added:

  * PUT ``/1.1/users/<user_id>/lines/<line_id>``

* The following URLs have been deprecated. Please use the new API instead:

  * DELETE ``/1.1/users/<user_id>/voicemail``
  * GET ``/1.1/users/<user_id>/voicemail``
  * POST ``/1.1/users/<user_id>/voicemail``
  * POST ``/1.1/users/<user_id>/lines``
  * POST ``/1.1/lines/<line_id>/extensions``


16.09
=====

* Added entities endpoints:

  * GET ``/1.1/entities``
  * POST ``/1.1/entities``
  * GET ``/1.1/entities/<entity_id>``
  * DELETE ``/1.1/entities/<entity_id>``

* A new API for updating all user's funckeys

  * PUT ``/1.1/users/<user_id>/funckeys``

* A new parameter have been added to the users resource:

  * ``dtmf_hangup_enabled``


16.06
=====

* A new API for initializing a XiVO (passing the wizard):

  * GET ``/1.1/wizard``
  * POST ``/1.1/wizard``
  * GET ``/1.1/wizard/discover``

* A new API for associating a user with an entity has been added:

  * GET ``/1.1/users/<user_id>/entities``
  * PUT ``/1.1/users/<user_id>/entities/<entity_id>``


16.05
=====

* A new API for associating a user with a call permission has been added:

  * GET ``/1.1/users/<user_id>/callpermissions``
  * PUT ``/1.1/users/<user_id>/callpermissions/<call_permission_id>``
  * DELETE ``/1.1/users/<user_id>/callpermissions/<call_permission_id>``
  * GET ``/1.1/callpermissions/<call_permission_id>/users``

* Two new parameters have been added to the users resource:

  * ``call_permission_password``
  * ``enabled``

* A new API for user's forwards has been added:

  * PUT ``/1.1/users/<user_id>/forwards``

* SIP endpoint: ``allow`` and ``disallow`` options are not split into multiple options anymore.
* SCCP endpoint: ``allow`` and ``disallow`` options are not split into multiple options anymore.


16.04
=====

* The ``summary`` view has been added to ``/users`` (GET ``/users?view=summary``)

* A new API for user's services has been added:

  * GET ``/1.1/users/<user_id>/services``
  * GET ``/1.1/users/<user_id>/services/<service_name>``
  * PUT ``/1.1/users/<user_id>/services/<service_name>``

* A new API for user's forwards has been added:

  * GET ``/1.1/users/<user_id>/forwards``
  * GET ``/1.1/users/<user_id>/forwards/<forward_name>``
  * PUT ``/1.1/users/<user_id>/forwards/<forward_name>``

* GET ``/1.1/users/export`` now requires the following header for CSV output::

   Accept: text/csv; charset=utf-8

* Added call permissions endpoints:

  * GET ``/1.1/callpermissions``
  * POST ``/1.1/callpermissions``
  * GET ``/1.1/callpermissions/<callpermission_id>``
  * PUT ``/1.1/callpermissions/<callpermission_id>``
  * DELETE ``/1.1/callpermissions/<callpermission_id>``


16.03
=====

* Added switchboard endpoints:

  * GET ``/1.1/switchboards``
  * GET ``/1.1/switchboards/<switchboard_id>/stats``

* A new API for associating a line with a device has been added:

  * PUT ``/1.1/lines/<line_id>/devices/<device_id>``
  * DELETE ``/1.1/lines/<line_id>/devices/<device_id>``

* The following URLs have been deleted. Please use the new API instead:

  * GET ``/1.1/devices/<device_id>/associate_line/<line_id>``
  * GET ``/1.1/devices/<device_id>/dissociate_line/<line_id>``


16.02
=====

* Added users endpoints in REST API:

  * GET ``/1.1/users/<user_uuid>/lines/main/associated/endpoints/sip``


16.01
=====

* The SIP API has been improved. ``options`` now accepts any extra parameter.  However, due to
  certain database limitations, parameters that appear in :ref:`sip-endpoint-parameters` may only
  appear once in the list. This limitation will be removed in future versions.
* A new API for custom endpoints has been added: ``/1.1/endpoints/custom``
* A new API for associating custom endpoints has been added: ``/1.1/lines/<line_id>/endpoints/custom/<endpoint_id>``


15.20
=====

* A new API for mass updating users has been added: PUT ``/1.1/users/import``
* A new API for exporting users has been added: GET ``/1.1/users/export``


15.19
=====

* A new API for mass importing users has been added: POST ``/1.1/users/import``
* The following fields have been added to the ``/users`` API:

  * supervision_enabled
  * call_tranfer_enabled
  * ring_seconds
  * simultaneous_calls


15.18
=====

* Ports 50050 and 50051 have been removed. Please use 9486 and 9487 instead
* Added sccp endpoints in REST API:

  * GET ``/1.1/endpoints/sccp``
  * POST ``/1.1/endpoints/sccp``
  * DELETE ``/1.1/endpoints/sccp/<sccp_id>``
  * GET ``/1.1/endpoints/sccp/<sccp_id>``
  * PUT ``/1.1/endpoints/sccp/<sccp_id>``
  * GET ``/1.1/endpoints/sccp/<sccp_id>/lines``
  * GET ``/1.1/lines/<line_id>/endpoints/sccp``
  * DELETE ``/1.1/lines/<line_id>/endpoints/sccp/<sccp_id>``
  * PUT ``/1.1/lines/<line_id>/endpoints/sccp/<sccp_id>``

* Added lines endpoints in REST API:

  * GET ``/1.1/lines/<line_id>/users``


15.17
=====

* A new API for SIP endpoints has been added. Consult the documentation
  on http://api.wazo.community for further details.
* The ``/lines_sip`` API has been deprecated. Please use ``/lines`` and ``/endpoints/sip`` instead.
* Due to certain limitations in the database, only a limited number of
  optional parameters can be configured. This limitation will be removed
  in future releases. Supported parameters are listed further down.
* Certain fields in the ``/lines`` API have been modified. List
  of fields are further down


Fields modified in the ``/lines`` API
-------------------------------------

+------------------------+-------------------+------------+------------+
| Name                   | Replaced by       | Editable ? | Required ? |
+========================+===================+============+============+
| id                     |                   | no         |            |
+------------------------+-------------------+------------+------------+
| device_id              |                   | no         |            |
+------------------------+-------------------+------------+------------+
| name                   |                   | no         |            |
+------------------------+-------------------+------------+------------+
| protocol               |                   | no         |            |
+------------------------+-------------------+------------+------------+
| device_slot            | position          | no         |            |
+------------------------+-------------------+------------+------------+
| provisioning_extension | provisioning_code | no         |            |
+------------------------+-------------------+------------+------------+
| context                |                   | yes        | yes        |
+------------------------+-------------------+------------+------------+
| provisioning_code      |                   | yes        |            |
+------------------------+-------------------+------------+------------+
| position               |                   | yes        |            |
+------------------------+-------------------+------------+------------+
| caller_id_name         |                   | yes        |            |
+------------------------+-------------------+------------+------------+
| caller_id_num          |                   | yes        |            |
+------------------------+-------------------+------------+------------+


.. _sip-endpoint-parameters:

Supported parameters on SIP endpoints
-------------------------------------

 * md5secret
 * language
 * accountcode
 * amaflags
 * allowtransfer
 * fromuser
 * fromdomain
 * subscribemwi
 * buggymwi
 * call-limit
 * callerid
 * fullname
 * cid-number
 * maxcallbitrate
 * insecure
 * nat
 * promiscredir
 * usereqphone
 * videosupport
 * trustrpid
 * sendrpid
 * allowsubscribe
 * allowoverlap
 * dtmfmode
 * rfc2833compensate
 * qualify
 * g726nonstandard
 * disallow
 * allow
 * autoframing
 * mohinterpret
 * useclientcode
 * progressinband
 * t38pt-udptl
 * t38pt-usertpsource
 * rtptimeout
 * rtpholdtimeout
 * rtpkeepalive
 * deny
 * permit
 * defaultip
 * setvar
 * port
 * regexten
 * subscribecontext
 * vmexten
 * callingpres
 * parkinglot
 * protocol
 * outboundproxy
 * transport
 * remotesecret
 * directmedia
 * callcounter
 * busylevel
 * ignoresdpversion
 * session-timers
 * session-expires
 * session-minse
 * session-refresher
 * callbackextension
 * timert1
 * timerb
 * qualifyfreq
 * contactpermit
 * contactdeny
 * unsolicited_mailbox
 * use-q850-reason
 * encryption
 * snom-aoc-enabled
 * maxforwards
 * disallowed-methods
 * textsupport


15.16
=====

* The parameter ``skip`` is now deprecated. Use ``offset`` instead for:

  * ``GET /1.1/devices``
  * ``GET /1.1/extensions``
  * ``GET /1.1/voicemails``
  * ``GET /1.1/users``

* The users resource can be referred to by ``uuid``

  * ``GET /1.1/users/<uuid>``
  * ``PUT /1.1/users/<uuid>``
  * ``DELETE /1.1/users/<uuid>``


15.15
=====

 * The field ``enabled`` has been added to the voicemail model
 * A line is no longer required when associating a voicemail with a user
 * Voicemails can now be edited even when they are associated to a user


15.14
=====

 * All optional fields on a user are now always null (sometimes they were empty strings)
 * The caller id is no longer automatically updated when the firstname or lastname is modified. You must update the
   caller id yourself if you modify the user's name.
 * Caller id will be generated if and only if it does not exist when creating a user.


14.16
=====

* Association user-voicemail, when associating a voicemail whose id does not exist:

  * before: error 404
  * after: error 400


14.14
=====

* Association line-extension, a same extension can not be associated to multiple lines


14.13
=====

* Resource line, field ``provisioning_extension``: type changed from ``int`` to ``string``
