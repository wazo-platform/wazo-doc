.. _confd_changelog:

*****************************
xivo-confd REST API changelog
*****************************

16.06
=====

* A new API for initializing a XiVO (passing the wizard):

  * GET ``/1.1/wizard``
  * POST ``/1.1/wizard``
  * GET ``/1.1/wizard/discover``


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
  on http://api.xivo.io for further details.
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
 * fullcontact
 * vmexten
 * callingpres
 * ipaddr
 * regseconds
 * regserver
 * lastms
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
 * registertrying
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
