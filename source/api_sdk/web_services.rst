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

Return code example

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


Example of content

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

Return code example

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

Return code example

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

Call pickups
^^^^^^^^^^^^

List::

   https://[ip_xivo]/service/ipbx/json.php/restricted/call_management/pickup/?act=list


Return code example

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

Return code example

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

Return code example

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
  
Return code example

.. code-block:: javascript

   [101,102,104,105,106,109,110,210]


