.. _confd_changelog:

*****************************
xivo-confd REST API changelog
*****************************

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

* Association :ref:`user-voicemail <user-voicemail-association>`, when associating a voicemail whose
  id does not exist:

  * before: error 404
  * after: error 400

14.14
=====

* Association :ref:`line-extension <line-extension-associations>`, a same extension can not be
  associated to multiple lines

14.13
=====

* Resource :ref:`line <confd_lines>`, field ``provisioning_extension``: type changed from ``int`` to ``string``
