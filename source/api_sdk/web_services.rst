***********
WebServices
***********

**Using web services XiVO to develop applications around XiVO.**



HTTP status codes
=================

- 200: Success
- 204: No data (only for list and search queries)
- 304: Document not changed (only for requests list, search and see)
- 400: Incorrect syntax (only for requests to add)
- 401: Authentication required
- 403: Authentication refused
- 404: Resource not found (for queries only view and delete)
- 500: Internal error

Configuration
=============

Manage
------

Entity
^^^^^^

List::

   https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=list

Search::

   https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=search&search=[string]

Search Attributes:
 * name
 * displayname
 * phonenumber
 * faxnumber
 * email
 * url
 * address1
 * address2
 * city
 * state
 * zipcode
 * country
 * description

View::

   https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=view&id=[entity_id] 

Add::
   
   https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=add

Example content

.. code-block:: javascript

   {
      "name": "proformatique",
      "displayname": "Proformatique",
      "phonenumber": "0033141389960",
      "faxnumber": "0033141389970",
      "email": "contact@proformatique.com",
      "url": "http://www.proformatique.com",
      "address1": "10 bis, rue Lucien VOILIN",
      "address2": "",
      "city": "Puteaux",
      "state": "Hauts de Seine",
      "zipcode": "92800",
      "country": "FR",
      "description": ""
   }


Network
-------

Mail
^^^^

View::

   https://[ip_xivo]/xivo/configuration/json.php/restricted/network/mail/?act=view

``Return code example``

.. code-block:: javascript

   {
       "id": "1",
       "mydomain": "proformatique.com",
       "origin": "devel.proformatique.com",
       "relayhost": "smtp.free.fr",
       "fallback_relayhost": "smtp.orange.fr",
       "canonical": [
           {
               "pattern": "@proformatique.com",
               "result": "support@proformatique.com"
           }
       ]
   }


Description des champs:
 * id: identifiant de la ressource (toujours égal à 1)
 * mydomain: nom de domaine mail du serveur
 * origin: adresse d"envoi des mails générés par le système
 * relayhost: serveur de relai principal des mails
 * fallback_relayhost: serveur de relai secondaire des mails
 * canonical: règles de réécriture des adresses email

Edit::

   https://[ip_xivo]/xivo/configuration/json.php/restricted/network/mail/?act=edit

Example content

.. code-block:: javascript

   {
       "mydomain": "proformatique.com",
       "origin": "devel.proformatique.com",
       "relayhost": "smtp.free.fr",
       "fallback_relayhost": "smtp.orange.fr",
       "canonical": [
           {
               "pattern": "@proformatique.com",
               "result": "support@proformatique.com"
           }
       ]
   }


IPBX
====

IPBX Settings
-------------

Lines
^^^^^

List:

* return all lines::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list

* return all free lines::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list&free=1

* return all no free lines::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list&free=0

* return all lines with protocol <xxx> `(sip, iax, sccp)`::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list&protocol=sip

* Example possible::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list&free=1&protocol=sip



Search::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]
   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]&context=default

Attributes:
 * number
 * name (peer)


* To search free lines::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]&free=1


* To search no free lines::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]&free=0


* To search a line with specific protocol::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]&protocol=sip


View::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=view&id=[linefeatures_id]

Delete::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=delete&id=[linefeatures_id]

Add:: 

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=add

Edit:: 

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=edit&id=[linefeatures_id]


``Example of content``

.. code-block:: javascript

   "protocol": {
      "name": "reh58f",
      "secret": "FV4S9W",
      "protocol": "sip",
      "context": "default",
      "language": "fr_FR",
      "nat": "",
      "subscribemwi": "1",
      "buggymwi": "0",
      "progressinband": "",
      "dtmfmode": "",
      "rfc2833compensate": "",
      "qualify": "",
      "rtptimeout": "",
      "rtpholdtimeout": "",
      "rtpkeepalive": "",
      "allowtransfer": "",
      "autoframing": "",
      "videosupport": "",
      "maxcallbitrate": "",
      "g726nonstandard": "",
      "disallow": "all",
      "allow": [
            "alaw",
            "ulaw"
      ],
      "t38pt_udptl": "",
      "t38pt_rtp": "",
      "t38pt_tcp": "",
      "t38pt_usertpsource": "",
      "callerid": "\"John Doe\" <666>",
      "insecure": "",
      "host-type": "dynamic",
      "permit": "",
      "deny": "",
      "trustrpid": "",
      "sendrpid": "",
      "allowsubscribe": "",
      "allowoverlap": "",
      "promiscredir": "",
      "usereqphone": "",
      "canreinvite": "",
      "fromuser": "",
      "fromdomain": "",
      "amaflags": "default",
      "accountcode": "",
      "useclientcode": ""
   }

Devices
^^^^^^^

List::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=list

``Return code example``

.. code-block:: javascript

   [
      {
         id: 2,
         deviceid: "43dafbd0cb8d447a85ebd02b2639861d",
         config: "43dafbd0cb8d447a85ebd02b2639861d",
         plugin: "xivo-aastra-3.2.2.1136",
         ip: "10.0.0.13",
         mac: "00:08:5d:2a:4f:b1",
         sn: "",
         vendor: "Aastra",
         model: "6731i",
         version: "3.2.2.1136",
         proto: "",
         internal: "0",
         configured: true,
         commented: false,
         description: "",
         provdexist: true,
         capabilities: false
      },
      ...
   ]


Search::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=search&search=[value]

search is done either on *ip address* or *mac address* field (with exact match)

.. code-block:: javascript

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=search&search=00:0e:50:4e:57:b7

   [
      {
         id: 4,
         deviceid: "396fa65e837c40d3a78a4424e32a1df7",
         config: "396fa65e837c40d3a78a4424e32a1df7",
         plugin: "xivo-technicolor-ST2030-2.74",
         ip: "10.0.0.12",
         mac: "00:0e:50:4e:57:b7",
         sn: "",
         vendor: "Technicolor",
         model: "ST2030",
         version: "2.74",
         proto: "",
         internal: "0",
         configured: true,
         commented: false,
         description: "",
         provdexist: true,
         capabilities: false
      }
   ]


View::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=view&id=[deviceid]

``Return code example``

.. code-block:: javascript

   [
      {
         id: 2,
         deviceid: "43dafbd0cb8d447a85ebd02b2639861d",
         config: "43dafbd0cb8d447a85ebd02b2639861d",
         plugin: "xivo-aastra-3.2.2.1136",
         ip: "10.0.0.13",
         mac: "00:08:5d:2a:4f:b1",
         sn: "",
         vendor: "Aastra",
         model: "6731i",
         version: "3.2.2.1136",
         proto: "",
         internal: "0",
         configured: true,
         commented: false,
         description: "",
         provdexist: true,
         capabilities: false
      },
      ...
   ]


Users
^^^^^

List::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/users/?act=list


Search::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/users/?act=search&search=[string]

search is done either on *firstname* or *lastname* field (lazy match) or *userfield*
field (exact match).


View::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/users/?act=view&id=[userfeatures_id]

Delete::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/users/?act=delete&id=[userfeatures_id]

Add::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/users/?act=add

Edit::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/users/?act=edit&id=[userfeatures_id]


Miminum set of data for user creation or edition:

.. code-block:: javascript

   {
       "userfeatures": {
           "entityid": "2",
           "firstname": "John"
       },
       "dialaction": {
           "noanswer": {
               "actiontype": "none"
           },
           "busy": {
               "actiontype": "none"
           },
           "congestion": {
               "actiontype": "none"
           },
           "chanunavail": {
               "actiontype": "none"
           }
       }
   }


Full example:

.. code-block:: javascript

   {
       "userfeatures": {
           "entityid": "[entityid]",
           "firstname": "John",
           "lastname": "Doe",
           "callerid": "John Doe",
           "loginclient": "jdoe",
           "passwdclient": "8888",
           "mobilephonenumber": "",
           "ringseconds": "30",
           "simultcalls": "5",
           "musiconhold": "default",
           "voicemailid": "0",
           "enableclient": "1",
           "profileclient": "client",
           "enablehint": "1",
           "enablevoicemail": "1",
           "enablexfer": "1",
           "enableautomon": "0",
           "callrecord": "0",
           "callfilter": "0",
           "enablednd": "0",
           "bsfilter": "no",
           "agentid": "",
           "enablerna": "0",
           "destrna": "0033141389960",
           "enablebusy": "0",
           "destbusy": "0033141389960",
           "enableunc": "0",
           "destunc": "0033141389960",
           "outcallerid": "default",
           "preprocess_subroutine": "",
           "language": "fr_FR",
           "timezone": "America/Montreal",
           "ringintern": "",
           "ringextern": "",
           "ringgroup": "",
           "ringforward": "",
           "rightcallcode": "",
           "alarmclock": "00:00",
           "pitchdirection": "",
           "pitch": "",
           "description": ""
       },
       "linefeatures": {
           "id": [
               ""
           ],
           "protocol": [
               ""
           ],
           "name": [
               ""
           ],
           "context": [
               ""
           ],
           "number": [
               ""
           ],
           "rules_type": [
               ""
           ],
           "rules_time": [
               ""
           ],
           "rules_order": [
               ""
           ],
           "rules_group": [
               ""
           ]
       },
       "voicemail": {
           "fullname": "John Doe",
           "mailbox": "666",
           "password": "0000",
           "email": "jdoe@proformatique.com",
           "tz": "eu-fr",
           "attach": "1",
           "deletevoicemail": "1"
       },
       "vmfeatures": {
           "skipcheckpass": "1"
       },
       "dialaction": {
           "noanswer": {
               "actiontype": "group",
               "actionarg1": "2",
               "actionarg2": "15"
           },
           "busy": {
               "actiontype": "queue",
               "actionarg1": "1",
               "actionarg2": ""
           },
           "congestion": {
               "actiontype": "voicemenu",
               "actionarg1": "1"
           },
           "chanunavail": {
               "actiontype": "application",
               "action": "faxtomail",
               "actionarg1": "fax@proformatique.com"
           }
       },
       "group-select": [
           "tous"
       ],
       "group": {
           "accueil": {
               "chantype": "default",
               "call-limit": "0"
           },
           "tous": {
               "chantype": "default",
               "call-limit": "3"
           }
       },
       "queue-select": [
           "technique"
       ],
       "queue": {
           "commerciale": {
               "chantype": "default",
               "penalty": "0",
               "call-limit": "0"
           },
           "technique": {
               "chantype": "default",
               "penalty": "4",
               "call-limit": "10"
           }
       },
       "phonefunckey": {
           "fknum": [
               "13",
               "14",
               "15",
               "17",
               "18"
           ],
           "type": [
               "user",
               "extension",
               "meetme",
               "group",
               "queue"
           ],
           "typeval": [
               "41",
               "extenfeatures-vmusermsg",
               "3",
               "2",
               "1"
           ],
           "supervision": [
               "1",
               "0",
               "0",
               "0",
               "0"
           ]
       },
       "queueskills": [
           {
               "id": 5,
               "weight": 22
           },
           {
               "id": 2,
               "weight": 97
           }
       ]
   }


Here is "linefeatures" complete options list:

.. code-block:: javascript

   "linefeatures": {
      "id": [""],
      "protocol": [""],
      "name": [""],
      "context": [""],
      "number": [""],
      "rules_type": [""],
      "rules_time": [""],
      "rules_order": [""],
      "rules_group": [""]
   }

To associate an available line with created/edited user, use following code (number is optional, but must exist and be free if used):

.. code-block:: javascript

   "linefeatures": {
      "id": ["2"],
      "number": ["4000"]
   }

To automatically create a new line associated with created/edited user, don"t set *id* key (or set it to "0" value):

.. code-block:: javascript

   "linefeatures": {
      "protocol": ["sip"],
      "context": ["default"],
      "number": [""],
      "rules_type": [""],
      "rules_time": [""],
      "rules_order": [""],
      "rules_group": [""]
   }

Once again, line number is optional.
You can also create or associate several lines at once. Here is different possible combinations:

1st line create, 2d associated with id 45

.. code-block:: javascript

   "linefeatures": {
      "id": ["0","45"],
      "protocol": ["sip",""],
      "context": ["default",""],
      "number": ["","4000"],
      "rules_type": ["",""],
      "rules_time": ["",""],
      "rules_order": ["",""],
      "rules_group": ["",""]
   }


1st & last lines created, 2d associated with id 45

.. code-block:: javascript

   "linefeatures": {
      "id": ["0","45","0"],
      "protocol": [{"sip","","sip"],
      "context": ["default","","default"],
      "number": ["","4000","4001"],
      "rules_type": ["simul","simul",""],
      "rules_time": ["10","10","20"],
      "rules_order": ["1","2","1"],
      "rules_group": ["1","1","2"]
   }


Call Management
---------------

Incalls
^^^^^^^

List::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/incall/?act=list


Search::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/incall/?act=search&search=[string]


View::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/incall/users/?act=view&id=[incall_id]

Delete::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/incall/?act=delete&id=[incall_id]

Add::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/incall/?act=add

Edit::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/incall/?act=edit&id=[incall_id]


``Sample JSON for add or edit action``

.. code-block:: javascript

  {
     "incall": {
          "exten": "9970",
          "context": "from-extern",
          "preprocess_subroutine": "",
     },
     "dialaction": {
           "answer": {
                "actiontype": "user",
                "actionarg1": "2",
                "actionarg2": ""
           }
     },
     "rightcall": [
          "1"
     ]
  }



Call pickups
^^^^^^^^^^^^

List::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/pickup/?act=list


``Return code example``

.. code-block:: javascript

   [
       {
           "commented": 0,
           "description": "sample unittest pickup group",
           "id": 0,
           "name": "unittest"
       }
   ]

.. note:: if no group exists, the web service returns HTTP code 204


View::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/pickup/?act=view&id=ID
 
where ID is the identifier of the target group

``Return code example``

.. code-block:: javascript

   {
       "members": [
           {
               "category": "member",
               "memberid": 1,
               "membertype": "group",
               "pickupid": 0
           },
           {
               "category": "member",
               "memberid": 1,
               "membertype": "queue",
               "pickupid": 0
           },
           {
               "category": "member",
               "memberid": 1,
               "membertype": "user",
               "pickupid": 0
           },
           {
               "category": "member",
               "memberid": 3,
               "membertype": "user",
               "pickupid": 0
           },
           {
               "category": "member",
               "memberid": 2,
               "membertype": "user",
               "pickupid": 0
           }
       ],
       "pickup": {
           "commented": 0,
           "description": "sample unittest pickup group",
           "id": 0,
           "name": "unittest"
       },
       "pickups": [
           {
               "category": "pickup",
               "memberid": 1,
               "membertype": "group",
               "pickupid": 0
           }
       ]
   }



.. note:: the web service returns HTTP code 404 if no group corresponding to the specified id is found

Delete::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/pickup/?act=delete&id=ID
 
where ID is the identifier of the target group

.. note:: the web service returns HTTP code 404 if no group corresponding to the specified id is found

Add::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/pickup/?act=add

.. note:: This web service must be called with the HTTP POST method with a JSON object describing the group.

``Return code example``

.. code-block:: javascript

   {
       "name": "unittest",
       "description": "sample unittest pickup group",
       "members": [
           {
               "category": "member",
               "membertype": "group",
               "memberid": 1
           },
           {
               "category": "member",
               "membertype": "queue",
               "memberid": 1
           },
           {
               "category": "member",
               "membertype": "user",
               "memberid": 1
           },
           {
               "category": "member",
               "membertype": "user",
               "memberid": 3
           },
           {
               "category": "pickup",
               "membertype": "group",
               "memberid": 1
           },
           {
               "category": "member",
               "membertype": "queue",
               "memberid": 1
           },
           {
               "category": "member",
               "membertype": "user",
               "memberid": 1
           },
           {
               "category": "member",
               "membertype": "user",
               "memberid": 2
           }
       ]
   }

.. note:: returns the HTTP code 400 if the creation fails


Calls Records
^^^^^^^^^^^^^

.. warning:: The list returned is limit to 5000, you can set it with argument ``limit=100`` in the url


Search by id:

Example to return Calls Records with id begining 200 (limit to 5000 by default)::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/cel/?act=searchid&idbeg=200

``return code example``

.. code-block:: javascript
   
   [
       {
           "id": "201",
           "eventtype": "CHAN_START",
           "eventtime": "2012-01-27 03:12:33.175832",
           "userdeftype": "",
           "cid_name": "Sup - 0472445668",
           "cid_num": "0472445668",
           "cid_ani": "",
           "cid_rdnis": "",
           "cid_dnid": "",
           "exten": "42803",
           "context": "default",
           "channame": "IAX2/assurancetourisk-durallo-3431",
           "appname": "",
           "appdata": "",
           "amaflags": "3",
           "accountcode": "",
           "peeraccount": "",
           "uniqueid": "1327651953.51",
           "linkedid": "1327651953.51",
           "userfield": "",
           "peer": ""
       },
       {
           "id": "202",
               ...
           "peer": ""
       },
       {
           "id": "203",
               ...
           "peer": ""
       },
       ...
       {
          "id": "5200",
          "eventtype": "CHAN_END",
          "eventtime": "2012-02-03 14:11:53.859392",
          "userdeftype": "",
          "cid_name": "",
          "cid_num": "dial",
          "cid_ani": "",
          "cid_rdnis": "",
          "cid_dnid": "",
          "exten": "",
          "context": "outcall",
          "channame": "IAX2/assurancetourisk-proforhosting-324",
          "appname": "AppDial",
          "appdata": "(Outgoing Line)",
          "amaflags": "3",
          "accountcode": "",
          "peeraccount": "",
          "uniqueid": "1328296281.20",
          "linkedid": "1328296281.19",
          "userfield": "",
          "peer": ""
      
      }
   ]


Search:

Search Attributes:
 * dbeg
 * dend

.. note:: format accepted to date search: *Y* or *Y-m* or *Y-m-d* or *Y-m-d H:i:s*

Example to return all Calls Records from 2012-02-28 to now::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/cel/?dbeg=2012-02-28

``return code example``

.. code-block:: javascript

   [
       {
           "id": "21074",
           "eventtype": "CHAN_START",
           "eventtime": "2012-02-27 03:27:21.017623",
           "userdeftype": "",
           "cid_name": "Sup - asterisk",
           "cid_num": "asterisk",
           "cid_ani": "",
           "cid_rdnis": "",
           "cid_dnid": "",
           "exten": "42803",
           "context": "default",
           "channame": "IAX2/assurancetourisk-durallo-16052",
           "appname": "",
           "appdata": "",
           "amaflags": "3",
           "accountcode": "",
           "peeraccount": "",
           "uniqueid": "1330331241.287",
           "linkedid": "1330331241.287",
           "userfield": "",
           "peer": "",
           "amaflagsmeta": "documentation"
       },
       {
           "id": "21075",
           "eventtype": "APP_START",
           "eventtime": "2012-02-27 03:27:21.0437",
           "userdeftype": "",
           "cid_name": "Sup - Sup - asterisk",
           "cid_num": "asterisk",
           "cid_ani": "asterisk",
           "cid_rdnis": "",
           "cid_dnid": "",
           "exten": "s",
           "context": "group",
           "channame": "IAX2/assurancetourisk-durallo-16052",
           "appname": "Queue",
           "appdata": "support,,,,",
           "amaflags": "3",
           "accountcode": "",
           "peeraccount": "",
           "uniqueid": "1330331241.287",
           "linkedid": "1330331241.287",
           "userfield": "",
           "peer": "",
           "amaflagsmeta": "documentation"
       },
       ...
   ]


IPBX Services
-------------

Parkings
^^^^^^^^

Liste::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_services/parkinglot?act=list

View::
 
   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_services/parkinglot?act=view&id=[parkinglot_id]


Delete::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_services/parkinglot?act=delete&id=[parkinglot_id]

Add::
 
   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_services/parkinglot?act=add

Edit::
 
   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_services/parkinglot?act=edit


``Example of content to send to add``

.. code-block:: javascript

   {
       "name": "myparkinglot",
       "context": "default",
       "extension": 700,
       "positions": 10,
       "next": 1,
       "commented": 0
   }


Trunk management
----------------

Protocole SIP
^^^^^^^^^^^^^

View::
 
   https://[ip_xivo]/service/ipbx/json.php/restricted/trunk_management/sip?act=view&id=[trunk_id]

``Return code example``

.. code-block:: javascript

   {
       "protocol": {
           "name": "unittest",
           "username": "XiVO",
           "secret": "secretpassword",
           "callerid": "",
           "call-limit": "0",
           "host": "0.0.0.0",
           "type": "peer",
           "context": "from-extern",
           "language": "",
           "nat": "yes",
           "progressinband": "",
           "dtmfmode": "rfc2833",
           "rfc2833compensate": "",
           "qualify": "",
           "qualifyfreq": "",
           "rtptimeout": "",
           "rtpholdtimeout": "",
           "rtpkeepalive": "",
           "allowtransfer": "",
           "autoframing": "",
           "videosupport": "",
           "outboundproxy": "",
           "maxcallbitrate": "",
           "g726nonstandard": "",
           "timert1": "",
           "timerb": "",
           "registrertrying": "",
           "ignoresdpversion": "",
           "session-timers": "",
           "session-expires": "",
           "session-minse": "",
           "session-refresher": "",
           "disallow": "all",
           "allow": [
               "alaw",
               "ulaw",
               "gsm"
           ],
           "insecure": "port,invite",
           "port": "5060",
           "permit": "",
           "deny": "",
           "trustrpid": "",
           "sendrpid": "",
           "allowsubscribe": "",
           "allowoverlap": "",
           "promiscredir": "",
           "usereqphone": "",
           "directmedia": "",
           "fromuser": "",
           "fromdomain": "",
           "amaflags": "default",
           "accountcode": "",
           "useclientcode": "",
           "transport": "udp",
           "remotesecret": "",
           "callcounter": "",
           "busylevel": "",
           "callbackextension": "",
           "contactpermit": "",
           "contactdeny": ""
       },
       "register": {
           "transport": "udp",
           "username": "XiVO",
           "password": "secretpassword",
           "authuser": "",
           "host": "0.0.0.0",
           "port": "5060",
           "contact": "",
           "expiry": ""
       },
       "trunkfeatures": {
           "description": ""
       }
   }


IPBX Configuration
------------------

Extensions
^^^^^^^^^^

Get all free extensions for given context, object type and matching partial value::

   https://[ip_xivo]/service/ipbx/json.php/restricted/system_management/extensions/?act=search&context=[context]&obj=[objname]&number=[number]

Arguments:
 * **context** is one of xivo contexts name (i.e "*default*"),
 * **objname** is one of *user*, *group*, *queue*, *meetme* or *incall*,
 * **number** is part of search extensions (**optional argument**)


Return free user extensions (from "default" context) including "10"

Example::

   https://[ip_xivo]/service/ipbx/json.php/restricted/system_management/extensions/?act=search&context=default&obj=user&number=10

``Return code example``

.. code-block:: javascript

   [101,102,104,105,106,109,110,210]



Call Center
===========

Settings
--------

Agents
^^^^^^

View::

   https://[ip_xivo]/callcenter/json.php/restricted/settings/agents?act=view&id=[id]

List::
 
   https://[ip_xivo]/callcenter/json.php/restricted/settings/agents?act=list

Add::
 
   https://[ip_xivo]/callcenter/json.php/restricted/settings/agents?act=add
   
``Example of content to send to add``

.. code-block:: javascript

   {
      "agentfeatures": {
          "firstname": "Jack",
          "lastname": "Amand",
          "number": "99543",
          "acceptdtmf": "#",
          "ackcall": "no",
          "autologoff": "0",
          "context": "default",
          "enddtmf": "*",
          "language": "de_DE",
          "numgroup": "1",
          "passwd": "7789",
          "silent": "no",
          "wrapuptime": "0",
          "description": "working in services",
      },
      "agentoptions": {
          "maxlogintries": "3",
          "musiconhold": "default"
      },
      "queueskills": [
         {
            "id": "10", "weight": "87"
         },
         {
            "id": "12", "weight": "50"
         }
      ],
      "user-select": [
         "26"
      ]
    }

Arguments:
 * **wrapuptime** is one of 0,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000


Skills
^^^^^^

View::

   https://[ip_xivo]/callcenter/json.php/restricted/settings/queuesskills?act=view&id=[id]

``Return code example``

.. code-block:: javascript

   {

    "id": "1",
    "name": "english",
    "description": "English",
    "printscreen": "Eng",
    "category_name": "langs"
    }

List::

   https://[ip_xivo]/callcenter/json.php/restricted/settings/queueskills?act=list

``Return code example``

.. code-block:: javascript

   [
       {
           "id": "1",
           "name": "english",
           "description": "English",
           "printscreen": "Eng",
           "category_name": "langs"
       },
       {
           "id": "2",
           "name": "french",
           "description": "French",
           "printscreen": "Fr",
           "category_name": "langs"
       }
   ]

Add::

   https://[ip_xivo]/callcenter/json.php/restricted/settings/queueskills?act=add

``Example of content to send to add``

.. code-block:: javascript

   {
      "name": "service",
      "printscreen": "svc",
      "category_name": "business"
      "description": "answer to customer service"
   }


Category is created if not exists, printscreen should be less than 5 car long

Delete::

   https://[ip_xivo]/callcenter/json.php/restricted/settings/queueskills?act=delete&id=[kill_id]

*Category is not removed*

Queue
^^^^^

View::

   https://[ip_xivo]/callcenter/json.php/restricted/settings/queues?act=view&id=[id]

List::

   https://[ip_xivo]/callcenter/json.php/restricted/settings/queues?act=list
 
``Return code example``

.. code-block:: javascript
   
   [
       {
           "id": "7",
           "name": "epicerie",
           "displayname": "Épicerie",
           "number": "301",
           "context": "default",
           "data_quality": "0",
           "hitting_callee": "0",
           "hitting_caller": "0",
           "retries": "0",
           "ring": "0",
           "transfer_user": "0",
           "transfer_call": "0",
           "write_caller": "0",
           "write_calling": "0",
           "url": "",
           "announceoverride": "",
           "timeout": "0",
           "preprocess_subroutine": null,
           "announce_holdtime": "0",
           "ctipresence": null,
           "nonctipresence": null,
           "waittime": null,
           "waitratio": null,
           "commented": false,
           "category": "queue",
           "nb_qmember": "1",
           "identity": "Épicerie (301@default)"
       }
   ]

Add::
 
   https://[ip_xivo]/callcenter/json.php/restricted/settings/queues?act=add
   
``Example of content to send to add``

.. code-block:: javascript

   {
       "queuefeatures": {
           "name": "unittest",
           "number": "310",
           "context": "default",
           "preprocess_subroutine": "",
           "timeout": "0",
           "hitting_caller": "1",
           "transfer_user": "1",
           "write_caller": "1"
       },
       "queue": {
           "strategy": "ringall",
           "musiconhold": "default",
           "context": "default",
           "servicelevel": "",
           "timeout": "15",
           "retry": "5",
           "weight": "0",
           "wrapuptime": "0",
           "maxlen": "0",
           "monitor-type": "",
           "monitor-format": "",
           "joinempty": "no",
           "leavewhenempty": "no",
           "memberdelay": "0",
           "timeoutpriority": "app",
           "min-announce-frequency": 60,
           "announce-position": "yes",
           "announce-position-limit": 5
       },
       "user": [
           "1"
       ],
       "agent": [],
       "dialaction": {
           "noanswer": {
               "actiontype": "extension",
               "actionarg1": "0141389960",
               "actionarg2": "to-extern"
           },
           "busy": {
               "actiontype": "none"
           },
           "congestion": {
               "actiontype": "none"
           },
           "chanunavail": {
               "actiontype": "none"
           }
       }
   }
