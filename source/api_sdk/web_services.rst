.. _web-services-api:

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

In order to use web services, a special user must be created with the correct
ACLs. In order to do so :

- Visit the :menuselection:`Configuration > Web Services Access` section
- Create a new web service user with the username, password OR host of allowed
  remote machine (the client that is about to use XiVO web services). Edit
  access rights of given web services user to allow access for needed sections.

If a username/password was given, then those credentials will be needed to
connect to the web services. If a host was given, only connections from this
host will be allowed. It is possible to specify a username/password pair AND a
host on the same web services user.

How to use this page
====================

This page lists Web Services available in XiVO. Data sent or received is
described either in unit-tests (see the section below) or on this page. This
data must be sent via POST, in JSON format.

Where do I find Web Services usage examples?
--------------------------------------------

Listing data here would is inefficient, as this documentation can not be always
up-to-date. So we're moving it out of the documentation.

Instead, we will use unit-tests as documentation. We are developping a Python
library to access Web Services, named ``xivo-ws``.

* If you plan to use WS in Python scripts, we recommand you use this library,
  available from PyPI. You can find examples of usage in its source code.
* If you are developping with another language, you can read our unit-tests for
  ``xivo-ws``, and find the appropriate data format there.

``xivo-ws`` source code is available in the ``xivo-ws`` `Git repository on
Gitorious <http://gitorious.org/xivo/xivo-ws>`_.

If you want information about the users Web Services, for example, go look at
the file :file:`xivo_ws/objects/tests/test_user.py` (`online version
<http://gitorious.org/xivo/xivo-ws/blobs/master/xivo_ws/objects/tests/test_user.py>`_).

The function ``test_from_obj_dict`` tests the conversion of data received from
``view`` action into the ``xivo-ws`` format. So the ``obj_dict`` variable in
that test is the type of data the Web Service will send upon a ``view``
action. The only difference is that it is expressed in Python format, rather
than the JSON format that WS use, but they are very similar.

The reverse function is ``test_to_obj_dict``, that expects data in a format that
will be accepted by Web Services for ``add`` or ``edit`` actions. So the
``expected_obj_dict`` variable will be the format accepted by Web Services.

Another information you might need is which attributes are required for Web
Services. For this, you can open the file :file:`xivo_ws/objects/user.py` and
look at the ``_ATTRIBUTES`` variable. Each attribute marked with
``required=True`` is in fact required.

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

* return all associated lines::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list&free=0

* return all lines with protocol <xxx> `(sip, iax, sccp)`::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list&protocol=sip

* Example::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=list&free=1&protocol=sip



Search::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]
   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]&context=default

Attributes:
 * number
 * name (peer)


* To search free lines::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/lines/?act=search&search=[string]&free=1


* To search associated lines::

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


``Example of sent data to edit a SCCP line``

.. code-block:: javascript

    {
        "protocol": {
            "context": "default",
            "protocol": "sccp"
        },
        "linefeatures": {
            "id": 150,
            "name": "101",
            "context": "default",
            "commented": false,
            "protocol": "sccp",
            "protocolid": 3,
            "iduserfeatures": 37,
            "config": "",
            "device": "11",
            "configregistrar": "default",
            "number": "101",
            "provisioningid": 0,
            "rules_type": "",
            "rules_time": "30",
            "rules_order": 1,
            "rules_group": "",
            "num": 1,
            "line_num": 0,
            "ipfrom": "10.32.0.1",
            "internal": false,
            "encryption": false,
            "description": ""
        }
    }

Devices
^^^^^^^

List::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=list

Search::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=search&search=[value]

search is done either on *ip address* or *mac address* field (with exact match)

Example::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=search&search=00:0e:50:4e:57:b7

View::

   https://[ip_xivo]/service/ipbx/json.php/restricted/pbx_settings/devices/?act=view&id=[deviceid]


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

To associate an available line with created/edited user, use following code
(number is optional, but must exist and be free if used):

.. code-block:: javascript

   "linefeatures": {
      "id": ["2"],
      "number": ["4000"]
   }

To automatically create a new line associated with created/edited user, don"t
set *id* key (or set it to "0" value):

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

Once again, line number is optional. You can also create or associate several
lines at once. Here is different possible combinations:

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
            "preprocess_subroutine": ""
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

.. warning:: The list returned is limited to 5000, you can set it with argument ``limit=100`` in the url


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


IPBX Services
-------------

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

IPBX Configuration
------------------

Backup Files
^^^^^^^^^^^^

Configuration Files
^^^^^^^^^^^^^^^^^^^

Contexts
^^^^^^^^

View::

    https://[ip_xivo]/service/ipbx/json.php/restricted/system_management/context/?act=view&id=[context_name]

List::

    https://[ip_xivo]/service/ipbx/json.php/restricted/system_management/context/?act=list

Add::

    https://[ip_xivo]/service/ipbx/json.php/restricted/system_management/context/?act=add

``Example of content to send to add``

.. code-block:: javascript

    {
        "context": {
            "name": "default",
            "displayname": "Appels internes",
            "entity": "skaro",
            "contexttype":"internal",
            "description": ""
        },
        "contextinclude": [
            "to-extern"
        ],
        "contextnumbers": {
            "user": [
                  {
                          "numberbeg": "100",
                          "numberend": "199"
                  }
                    ],
            "group": [
                  {
                          "numberbeg": "200",
                          "numberend": "210"
                  }
                     ]
    }

LDAP Filters
^^^^^^^^^^^^


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
