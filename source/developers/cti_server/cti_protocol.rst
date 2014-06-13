.. _cti-protocol:

************
CTI Protocol
************

Protocol Changelog
==================

.. warning::
   The CTI server protocol is subject to change without any prior warning. If you are using this protocol in your own tools please be sure
   to check that the protocol did not change before upgrading XiVO


14.06
-----

* the ``dial_success`` message was added

14.05
-----

* the ``unhold_switchboard`` command was renamed ``resume_switchboard``.

13.22
-----

* the ``actionfiche`` message was renamed ``call_form_result``.

13.17
-----

* for messages of class ``login_capas`` from server to client: the key ``presence`` has been removed.

13.14
-----

* for messages of class ``getlist``, list ``agents`` and function ``updatestatus``: the key ``availability`` in the ``status`` object/dictionary has changed values:

  * deleted values: ``on_call_non_acd_incoming`` and ``on_call_non_acd_outgoing``
  * added values:
    * ``on_call_non_acd_incoming_internal``
    * ``on_call_non_acd_incoming_external``
    * ``on_call_non_acd_outgoing_internal``
    * ``on_call_non_acd_outgoing_external``

13.12
-----

* for messages of class ``getlist``, list ``agents`` and function ``updatestatus``: the key ``availability`` in the ``status`` object/dictionary has changed values:

  * deleted value: ``on_call_non_acd``
  * added values: ``on_call_non_acd_incoming`` and ``on_call_non_acd_outgoing``


13.10
-----

* for messages of class ``getlist`` and function ``updateconfig``, the ``config`` object/dictionary
  does not have a ``rules_order`` key anymore.


Commands
========

Objects have the format: "<type>:<xivoid>/<typeid>"

* <type> can take any of the following values:  user, agent, queue, phone, group, meetme, ...
* <xivoid> indicates on which server the object is defined
* <typeid> is the object id, type dependant

e.g.
 user:xivo-test/5
 I'm looking for the user that has the ID 5 on the xivo-test server.

Here is a non exaustive list of types:

* exten
* user
* vm_consult
* voicemail


Class list
----------


people_headers
-------------

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_headers",
    "commandid": <commandid>
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_headers_result",
    "commandid": <commandid>,
    "column_headers": ["Status", "Name", "Number"],
    "column_types": [null, null, "number"],
  }


people_search
-------------

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_search",
    "pattern": <pattern>,
    "commandid": <commandid>
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_search_result",
    "commandid": <commandid>
    "term": "Bob",
    "column_headers": ["Firstname", "Lastname", "Phone number", "Mobile", "Fax", "Email", "Agent"],
    "column_types": [null, "name", "number_office", "number_mobile", "fax", "email", "relation_agent"],
    "results": [
      {
        "column_values": ["Bob", "Marley", "5555555", "5556666", "5553333", "mail@example.com", null],
        "relations": {
          "agent_id": null,
          "user_id": null,
          "endpoint_id": null
        },
        "source": "my_ldap_directory"
      }, {
        "column_values": ["Charlie", "Boblin", "5555556", "5554444", "5552222", "mail2@example.com", null],
        "relations": {
          "agent_id": 12,
          "user_id": 34,
          "endpoint_id": 56
        },
        "source": "internal"
      }
    ]
  }

.. _register_user_status_update_command:

register_user_status_update
---------------------------

The `register_user_status_update` command is used to register to the status
updates of a list of user. Once registered to a user's status, the client will
receive all :ref:`user_status_update_event` events for the registered users.

This command should be sent when a user is displayed in the people xlet to be
able to update the presence status icon.

The :ref:`unregister_user_status_update_command` command should be used to stop receiving updates.

``Client -> Server``

.. code-block:: javascript

  {
    "class": "register_user_status_update",
    "user_ids": [<user_id1>, <user_id2>, ..., <user_idn>],
    "commandid": <commandid>
  }


.. _unregister_user_status_update_command:

unregister_user_status_update
-----------------------------

The `unregister_user_status_update` command is used to unregister from the
status updates of a list of user.

Once unregistered, the client will stop receiving the :ref:`user_status_update_event`
events for the specified users.

``Client -> Server``

.. code-block:: javascript

  {
    "class": "unregister_user_status_update",
    "user_ids": [<user_id1>, <user_id2>, ..., <user_idn>],
    "commandid": <commandid>
  }

.. _user_status_update_event:

user_status_update
------------------

The `user_status_update` event is received when the presence of a user changes.

To receive this event, the user must first register to the event for a specified
user using the :ref:`register_user_status_update_command` command.

To stop receiving this event, the user must send the
:ref:`unregister_user_status_update_command` command.

* data, a dictionary containing 3 fields:

  * user_id, is an integer containing the ID of the user affected by this status change
  * color: a string representing the color to display for the new status
  * display: a string containing the displayed text

``Server -> Client``

.. code-block:: javascript

  {
    "class": "user_status_update",
    "data": {
      "user_id": 42,
      "color": "#001AFF",
      "display": "Out to lunch",
    }
  }

The `user_status_update` event contains the same data as the :ref:`bus-user_status_update`.
The latter should be prefered to the former for uses that do not require a
persistent connection to xivo-ctid.


LOGINCOMMANDS
-------------

Once the network is connected at the socket level, the login process requires three steps. If one of these steps is omitted, the connection is
reseted by the cti server.

* login_id, the username is sent as a login to the cti server, cti server answers by giving a sessionid
* login_pass, the password combined with the sessionid is sent to the cti server, cti server answers by giving a capaid
* login_capas, the capaid is returned to the server with the phone state, cti server answers with a list of info relevevant to the user

.. code-block:: javascript

   {
   "commandid": <commandid>,
   "class": "login_id",
   }

* class: defined what class of command use.
* commandid : a unique integer number.

login_id
^^^^^^^^

``Client -> Server``

.. code-block:: javascript

    {
    "class": "login_id",
    "commandid": 1092130023,
    "company": "default",
    "ident": "X11-LE-24079",
    "lastlogout-datetime": "2013-02-19T11:13:36",
    "lastlogout-stopper": "disconnect",
    "userlogin": <userlogin>,
    "version": "9999",
    "xivoversion": "1.2"
    }

``Server -> Client``

.. code-block:: javascript

   {
       "class": "login_id",
       "sessionid": "21UaGDfst7",
       "timenow": 1361268824.64,
       "xivoversion": "1.2"
   }

.. note::

   sessionid is used to calculate the hashed password in next step


login_pass
^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

    {
    "hashedpassword": "e5229ef45824333e0f8bbeed20dccfa2ddcb1c80",
    "class": "login_pass",
    "commandid": <commandid>
    }

.. note::

   hashed_password = sha1(self.sessionid + ':' + password).hexdigest()

``Server -> Client``

.. code-block:: javascript

   {
       "capalist": [
           2
       ],
       "class": "login_pass",
       "replyid": 1646064863,
       "timenow": 1361268824.68
   }

If no CTI profile is defined on XiVO for this user, the following message will be sent:

.. code-block:: javascript

   {
       "error_string": "capaid_undefined",
       "class": "login_pass",
       "replyid": 1646064863,
       "timenow": 1361268824.68
   }


.. note::
   the first element of the capalist is used in the next step login_capas

login_capas
^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

    {
    "loginkind": "user",
    "capaid": 3,
    "lastconnwins": False,
    "commandid": <commandid>,
    "state": "available",
    "class": "login_capas"
    }

loginkind can be 'user' or 'agent', if 'agent', the property 'agentphonenumber' can be added.

``Server -> Client``

First message, describes all the capabilities of the client, configured at the server level

* presence : actual presence of the user
* userid : the user id, can be used as a reference
* capas
   * userstatus : a list of available statuses
      * status name
      * color
      * selectionnable status from this status
      * default action to be done when this status is selected
      * long name
   * services : list of availble services
   * phonestatus : list of available phonestatuses with default colors and descriptive names
   * capaxlets : List of xlets configured for this profile
   * appliname

.. code-block:: javascript

   {
      "class": "login_capas"
      "presence": "available",
      "userid": "3",
      "ipbxid": "xivo",
      "timenow": 1361440830.99,
      "replyid": 3,
      "capas": {
               "regcommands": {},
               "preferences": false,
               "userstatus": {
                           "available": { "color": "#08FD20",
                                          "allowed": ["available", "away", "outtolunch", "donotdisturb", "berightback"],
                                          "actions": {"enablednd": "false"}, "longname": "Disponible"
                                         },
                           "berightback": {  "color": "#FFB545",
                                             "allowed": ["available", "away", "outtolunch", "donotdisturb", "berightback"],
                                             "actions": {"enablednd": "false"}, "longname": "Bient\u00f4t de retour"
                                           },
                           "disconnected": { "color": "#202020",
                                             "actions": {"agentlogoff": ""}, "longname": "D\u00e9connect\u00e9"
                                           },
                          /* a list of other status depends on the cti server configuration */
               },
            "services": ["fwdrna", "fwdbusy", "fwdunc", "enablednd"],
            "phonestatus": {
                              "16": {"color": "#F7FF05", "longname": "En Attente"},
                              "1":  {"color": "#FF032D", "longname": "En ligne OU appelle"},
                              "0":  {"color": "#0DFF25", "longname": "Disponible"},
                              "2":  {"color": "#FF0008", "longname": "Occup\u00e9"},
                              "-1": {"color": "#000000", "longname": "D\u00e9sactiv\u00e9"},
                              "4":  {"color": "#FFFFFF", "longname": "Indisponible"},
                              "-2": {"color": "#030303", "longname": "Inexistant"},
                              "9":  {"color": "#FF0526", "longname": "(En Ligne OU Appelle) ET Sonne"},
                              "8":  {"color": "#1B0AFF", "longname": "Sonne"}
                           },
            "ipbxcommands": {}
         },
      "capaxlets": [["identity", "grid"], ["search", "tab"], ["customerinfo", "tab", "1"], ["fax", "tab", "2"], ["dial", "grid", "2"], ["tabber", "grid", "3"], ["history", "tab", "3"], ["remotedirectory", "tab", "4"], ["features", "tab", "5"], ["mylocaldir", "tab", "6"], ["conference", "tab", "7"]],
      "appliname": "Client",
   }

Second message describes the current user configuration

.. code-block:: javascript

   {
      "function": "updateconfig",
      "listname": "users",
      "tipbxid": "xivo",
      "timenow": 1361440830.99,
      "tid": "3",
      "config": {"enablednd": false},
      "class": "getlist"
   }

Third message describes the current user status

.. code-block:: javascript

   {
      "function": "updatestatus",
      "listname": "users",
      "status": {"availstate": "available"},
      "tipbxid": "xivo",
      "tid": "3",
      "class": "getlist",
      "timenow": 1361440830.99
   }

Unsolicited Messages
--------------------

These messages are received whenever one of the following corresponding event occurs: sheet message on incoming calls, or updatestatus when a phone status changes.

sheet
^^^^^
This message is received to display customer information if configured at the server side

.. code-block:: javascript

   {
      "timenow": 1361444639.61,
      "class": "sheet",
      "compressed": true,
      "serial": "xml",
      "payload": "AAADnnicndPBToNAEAbgV1n3XgFN1AP...................",
      "channel": "SIP/e6fhff-00000007"
   }

How to decode payload :

.. code-block:: python

   >>> b64content = base64.b64decode(<payload content>)
   >>> # 4 first cars are the encoded lenght of the xml string (in Big Endian format)
   >>> xmllen = struck.unpack('>I',b64content[0:4])
   >>> # the rest is a compressed xml string
   >>> xmlcontent = zlib.decompress(toto[4:])
   >>> print xmlcontent

   <?xml version="1.0" encoding="utf-8"?>
      <profile>
         <user>
            <internal name="ipbxid"><![CDATA[xivo]]></internal>
            <internal name="where"><![CDATA[dial]]></internal>
            <internal name="channel"><![CDATA[SIP/barometrix_jyldev-00000009]]></internal>
            <internal name="focus"><![CDATA[no]]></internal>
            <internal name="zip"><![CDATA[1]]></internal>
            <sheet_qtui order="0010" name="qtui" type="None"><![CDATA[]]></sheet_qtui>
            <sheet_info order="0010" name="Nom" type="title"><![CDATA[0230210083]]></sheet_info>
            <sheet_info order="0030" name="Origine" type="text"><![CDATA[extern]]></sheet_info>
            <sheet_info order="0020" name="Num\xc3\xa9ro" type="text"><![CDATA[0230210083]]></sheet_info>
            <systray_info order="0010" name="Nom" type="title"><![CDATA[Maric\xc3\xa9 Sapr\xc3\xaftch\xc3\xa0]]></systray_info>
            <systray_info order="0030" name="Origine" type="body"><![CDATA[extern]]></systray_info>
            <systray_info order="0020" name="Num\xc3\xa9ro" type="body"><![CDATA[0230210083]]></systray_info>
         </user>
      </profile>

The xml file content is defined by the following xsd file:
:file:`xivo-javactilib/src/main/xsd/sheet.xsd`
(`online version <https://www.gitorious.org/xivo/xivo-javactilib/blobs/master/src/main/xsd/sheet.xsd>`_)

phone status update
^^^^^^^^^^^^^^^^^^^

Received when a phone status change

* class : getlist
* function : updatestatus
* listname : phones


.. code-block:: javascript

   {
      "class": "getlist",
      "function": "updatestatus",
      "listname": "phones",
      "tipbxid": "xivo",
      "timenow": 1361447017.29,
      .........
   }

tid is the the object identification

Example of phone messages received when a phone is ringing :

.. code-block:: javascript

   { ... "status": {"channels": ["SIP/x2gjtw-0000000b"]}, "tid": "3",}
   {.... "status": {"channels": ["SIP/x2gjtw-0000000b"], "queues": [], "hintstatus": "0", "groups": []}, "tid": "3"}
   {.... "status": {"hintstatus": "8"}, "tid": "3"}

channel status update
^^^^^^^^^^^^^^^^^^^^^
* class : getlist
* function : updatestatus
* listname : channels
* status

  * direction : (in,out ...)
  * state : (Down, Ring, Unknown ...)
  * commstatus : (ready, calling, ringing ...)

.. code-block:: javascript

   {
      "class": "getlist",
      "function": "updatestatus",
      "listname": "channels",
      "tipbxid": "xivo",
      "timenow": 1361447017.29,
      .........
   }

Example of phone messages received when a phone is ringing :

.. code-block:: javascript

   {"status": {"timestamp": 1361447017.22, "holded": false, "commstatus": "ready", "parked": false, "state": "Down"}, "tid": "SIP/barometrix_jyldev-0000000a"}
   {"status": {"timestamp": 1361447017.29, "holded": false, "commstatus": "ready", "parked": false, "state": "Unknown"}, "tid": "SIP/x2gjtw-0000000b"}
   {"status": {"talkingto_kind": "channel", "direction": "out", "timestamp": 1361447017.29, "holded": false, "talkingto_id": "SIP/x2gjtw-0000000b", "state": "Ring", "parked": false, "commstatus": "calling"}, "tid": "SIP/barometrix_jyldev-0000000a", "class": "getlist"}
   {"status": {"direction": "in", "timestamp": 1361447017.29, "holded": false, "talkingto_id": "SIP/barometrix_jyldev-0000000a", "state": "Down", "parked": false, "commstatus": "ringing"}, "tid": "SIP/x2gjtw-0000000b", "class": "getlist"}


Configuration Messages
----------------------

The following messages are used to retrieve XiVO configuration.

Common fields
^^^^^^^^^^^^^
* class : getlist
* function : listid
* commandid
* tipbxid
* listname : Name of the list to be retreived : users, phones, agents, queues, voicemails, queuemembers


.. code-block:: javascript

   {
      "class": "getlist",
      "commandid": 489035169,
      "function": "listid",
      "tipbxid": "xivo",
      "listname": "........."
   }

users
^^^^^

Return a list of configured user id's

``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 489035169, "function": "listid", "listname": "users", "tipbxid": "xivo"}

``Server -> Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "function": "listid", "listname": "users",
      "list": ["11", "12", "14", "17", "1", "3", "2", "4", "9"],
      "tipbxid": "xivo","timenow": 1362735061.17
      }

user
^^^^

Return a user configuration

* tid is the userid returned by users_ message

``Client -> Server``

.. code-block:: javascript

    {
      "class": "getlist",
      "function": "updateconfig",
      "listname": "users",
      "tid": "17",
      "tpbxid": "xivo",  "commandid": 5}

``Server -> Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "function": "updateconfig",
      "listname": "users",
      "tid": "17",
      "tipbxid": "xivo",
      "timenow": 1362741166.4,
      "config": {
            "enablednd": 0, "destrna": "", "enablerna": 0,  "enableunc": 0, "destunc": "", "destbusy": "", "enablebusy": 0, "enablexfer": 1,
            "firstname": "Alice",  "lastname": "Bouzat", "fullname": "Alice Bouzat",
            "voicemailid": null, "incallfilter": 0,  "enablevoicemail": 0,   "profileclient": null, "agentid": 2, "enableclient": 1, "linelist": ["7"], "mobilephonenumber": ""}
       }


phones
^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 495252308, "function": "listid", "listname": "phones", "tipbxid": "xivo"}

``Server > Client``

.. code-block:: javascript

   {"class": "getlist", "function": "listid", "list": ["1", "3", "2", "5", "14", "7", "6", "9", "8"],
      "listname": "phones", "timenow": 1364994093.38, "tipbxid": "xivo"}

Individual phone configuration request:

.. code-block:: javascript

   {"class": "getlist", "commandid": 704096693, "function": "updateconfig", "listname": "phones", "tid": "3", "tipbxid": "xivo"}

``Server > Client``

.. code-block:: javascript

   {"class": "getlist",
      "config": {"allowtransfer": null, "context": "default", "identity": "SIP/ihvbur", "iduserfeatures": 1,
                     "initialized": null, "number": "1000", "protocol": "sip"},
      "function": "updateconfig", "listname": "phones", "tid": "3", "timenow": 1364994093.43, "tipbxid": "xivo"}

agents
^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 1431355191, "function": "listid", "listname": "agents", "tipbxid": "xivo"}

queues
^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 719950939, "function": "listid", "listname": "queues", "tipbxid": "xivo"}

``Server -> Client``

.. code-block:: javascript

   {"function": "listid", "listname": "queues", "tipbxid": "xivo",
         "list": ["1", "10", "3", "2", "5", "4", "7", "6", "9", "8"], "timenow": 1382704649.64, "class": "getlist"}

queue
^^^^^
tid is the id returned in the list field of the getlist response message

``Client -> Server``

.. code-block:: javascript

   {"commandid":7,"class":"getlist","tid":"3","tipbxid":"xivo","function":"updateconfig","listname":"queues"}

``Server -> Client``

.. code-block:: javascript

   {
    "function": "updateconfig", "listname": "queues", "tipbxid": "xivo", "timenow": 1382704649.69, "tid": "3",
      "config":
         {"displayname": "red", "name": "red", "context": "default", "number": "3002"},
    "class": "getlist"}

voicemails
^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 1034160761, "function": "listid", "listname": "voicemails", "tipbxid": "xivo"}

queuemembers
^^^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 964899043, "function": "listid", "listname": "queuemembers", "tipbxid": "xivo"}

``Server -> Client``

.. code-block:: javascript

   {"function": "listid", "listname": "queuemembers", "tipbxid": "xivo",
      "list": ["Agent/2501,blue", "Agent/2500,yellow", "Agent/2002,yellow", "Agent/2003,__switchboard",
               "Agent/2003,blue", "Agent/108,blue", "Agent/2002,blue"],
      "timenow": 1382717016.23,
      "class": "getlist"}

Status messages
---------------

These messages can also be received without any request as unsolicited messages.

User status
^^^^^^^^^^^
User status is to manage user presence

- Request user status update

``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 107712156,
      "function": "updatestatus",
      "listname": "users",
      "tid": "14", "tipbxid": "xivo"}

``Server > Client``

.. code-block:: javascript

   {"class": "getlist",
      "function": "updatestatus",
      "listname": "users",
      "status": {"availstate": "outtolunch", "connection": "yes"},
            "tid": "1", "timenow": 1364994093.48, "tipbxid": "xivo"}

- Change User status

``Client -> Server``

.. code-block:: javascript

    {"availstate": "away",
        "class": "availstate",
        "commandid": 1946092392,
        "ipbxid": "xivo",
            "userid": "1"}

``Server > Client``

.. code-block:: javascript

    {"class": "getlist",
        "function": "updatestatus",
        "listname": "users",
        "status": {"availstate": "away"},
        "tid": "1", "timenow": 1370523352.6, "tipbxid": "xivo"}


Phone status
^^^^^^^^^^^^
* tid is the line id, found in linelist from message `user`_

``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 107712156,
      "function": "updatestatus",
      "listname": "phones", "tid": "8", "tipbxid": "xivo"}

``Server > Client``

.. code-block:: javascript

   {"class": "getlist", "function": "updatestatus", "listname": "phones",
      "status": {"channels": [], "groups": [], "hintstatus": "0", "queues": []},
      "tid": "1", "timenow": 1364994093.48, "tipbxid": "xivo"}

Queue status
^^^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"commandid":17,"class":"getlist","tid":"8","tipbxid":"xivo","function":"updatestatus","listname":"queues"}

``Server > Client``

.. code-block:: javascript

   {"function": "updatestatus", "listname": "queues", "tipbxid": "xivo", "timenow": 1382710430.54,
      "status": {"agentmembers": ["1","5"], "phonemembers": ["8"]},
      "tid": "8", "class": "getlist"}

Agent status
^^^^^^^^^^^^

* tid is the agent id.

``Client -> Server``

.. code-block:: javascript

   {"class": "getlist",
    "commandid": <random_integer>,
    "function": "updatestatus",
    "listname": "agents",
    "tid": "635",
    "tipbxid": "xivo"}

``Server > Client``

.. code-block:: javascript

   {"class": "getlist",
    "listname": "agents",
    "function": "updatestatus",
    "tipbxid": "xivo",
    "tid": 635,
    "status": {
        "availability": "logged_out",
         "availability_since": 1370868774.74,
         "channel": null,
         "groups": [],
         "on_call_acd": false,
         "on_call_nonacd": false,
         "on_wrapup": false,
         "phonenumber": null,
         "queues": [
             "113"
         ]
     }}

* availability can take the values:

    * logged_out
    * available
    * unavailable
    * on_call_nonacd_incoming_internal
    * on_call_nonacd_incoming_external
    * on_call_nonacd_outgoing_internal
    * on_call_nonacd_outgoing_external

* availability_since is the timestamp of the last availability change
* queues is the list of queue ids from which the agent receives calls

Agent messages
--------------

login
^^^^^

``Client -> Server``

.. code-block:: javascript

   {"agentphonenumber": "1000", "class": "ipbxcommand", "command": "agentlogin", "commandid": 733366597}

agentphonenumber is the physical phone set where the agent is going to log on.


``Server > Client``

* Login successfull :

.. code-block:: javascript

   {"function": "updateconfig", "listname": "queuemembers", "tipbxid": "xivo",
      "timenow": 1362664323.94, "tid": "Agent/2002,blue",
      "config": {"paused": "0", "penalty": "0", "membership": "static", "status": "1", "lastcall": "",
                  "interface": "Agent/2002", "queue_name": "blue", "callstaken": "0"},
    "class": "getlist"
      }

   {"function": "updatestatus", "listname": "agents", "tipbxid": "xivo",
      "timenow": 1362664323.94,
      "status": {"availability_since": 1362664323.94,
                  "queues": [], "phonenumber": "1001", "on_call": false, "groups": [],
                  "availability": "available", "channel": null},
      "tid": 7, "class": "getlist"
         }


* The phone number is already used by an other agent :

.. code-block:: javascript

   {"class": "ipbxcommand", "error_string": "agent_login_exten_in_use", "timenow": 1362664158.14}

Logout
^^^^^^

``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "agentlogout", "commandid": 552759274}

Pause
^^^^^
On all queues

``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "queuepause", "commandid": 859140432, "member": "agent:xivo/1", "queue": "queue:xivo/all"}

Un pause
^^^^^^^^
On all queues

``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "queueunpause", "commandid": 822604987, "member": "agent:xivo/1", "queue": "queue:xivo/all"}

Add an agent in a queue
^^^^^^^^^^^^^^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "queueadd", "commandid": 542766213, "member": "agent:xivo/3", "queue": "queue:xivo/2"}

Remove an agent from a queue
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "queueremove", "commandid": 742480296, "member": "agent:xivo/3", "queue": "queue:xivo/2"}

Listen to an agent
^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "listen", "commandid": 1423579492, "destination": "xivo/1", "subcommand": "start"}


Service Messages
----------------
* class : featuresput

Call Filtering
^^^^^^^^^^^^^^
* function : incallfilter
* value : true, false activate deactivate filtering

``Client -> Server``

.. code-block:: javascript

   {"class": "featuresput", "commandid": 1326845972, "function": "incallfilter", "value": true}

``Server > Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "config": {"incallfilter": true},
      "function": "updateconfig",
      "listname": "users",
      "tid": "2",
      "timenow": 1361456398.52, "tipbxid": "xivo"  }

DND
^^^
* function : enablednd
* value : true, false activate deactivate DND

``Client -> Server``

.. code-block:: javascript

   {"class": "featuresput", "commandid": 1088978942, "function": "enablednd", "value": true}

``Server > Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "config": {"enablednd": true},
      "function": "updateconfig",
      "listname": "users",
      "tid": "2",
      "timenow": 1361456614.55, "tipbxid": "xivo"}

Recording
^^^^^^^^^
* function : enablerecording
* value : true, false

Activate / deactivate recording for a user, extension call recording has to be activated : :menuselection:`Services->IPBX->IPBX services->Extension`

``Client -> Server``

.. code-block:: javascript

   {"class": "featuresput", "commandid": 1088978942, "function": "enablerecording", "value": true, "target" : "7" }

``Server > Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "config": {"enablerecording": true},
      "function": "updateconfig",
      "listname": "users",
      "tid": "7",
      "timenow": 1361456614.55, "tipbxid": "xivo"}

Unconditional Forward
^^^^^^^^^^^^^^^^^^^^^
Forward the call at any time, call does not reach the user

* function : fwd

``Client -> Server``

.. code-block:: javascript

   {
      "class": "featuresput", "commandid": 2082138822, "function": "fwd",
      "value": {"destunc": "1002", "enableunc": true}
   }

``Server > Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "config": {"destunc": "1002", "enableunc": true},
      "function": "updateconfig",
      "listname": "users",
      "tid": "2",
      "timenow": 1361456777.98, "tipbxid": "xivo"}

Forward On No Answer
^^^^^^^^^^^^^^^^^^^^
Forward the call to another destination if the user does not answer

* function : fwd


``Client -> Server``

.. code-block:: javascript

   {
      "class": "featuresput", "commandid": 1705419982, "function": "fwd",
      "value": {"destrna": "1003", "enablerna": true}
      }

``Server > Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "config": {"destrna": "1003", "enablerna": true},
      "function": "updateconfig",
      "listname": "users",
      "tid": "2",
      "timenow": 1361456966.89, "tipbxid": "xivo" }

Forward On Busy
^^^^^^^^^^^^^^^
Forward the call to another destination when the user is busy

* function : fwd

``Client -> Server``

.. code-block:: javascript

   {
      "class": "featuresput", "commandid": 568274890, "function": "fwd",
      "value": {"destbusy": "1009", "enablebusy": true}
      }

``Server > Client``

.. code-block:: javascript

   {
      "class": "getlist",
      "config": {"destbusy": "1009", "enablebusy": true},
      "function": "updateconfig",
      "listname": "users",
      "tid": "2",
      "timenow": 1361457163.77, "tipbxid": "xivo"
      }


IPBX Commands
-------------


dial
^^^^


* destination can be any number
* destination can be a pseudo URL of the form "type:ibpx/id"

``Client -> Server``

.. code-block:: javascript

    {
       "class": "ipbxcommand",
       "command": "dial",
       "commandid": <commandid>,
       "destination": "exten:xivo/<extension>"
    }

For example :

.. code-block:: javascript

    {
        "class": "ipbxcommand",
        "command": "dial",
        "commandid": 1683305913,
        "destination": "exten:xivo/1202"
    }

The server will answer with either an error or a success:

.. code-block:: javascript

    {
        "class": "ipbxcommand",
        "error_string": "unreachable_extension:1202",
    }

    {
        "class": "dial_success",
        "exten": "1202"
    }

originate
^^^^^^^^^

Same message than the dial_ message with a source fied. The source field is ``user:xivo/<userid``,
userid is replaced by a user identifer returned by the message getting users_ list

Example:

.. code-block:: javascript

    {
        "class": "ipbxcommand",
        "command": "originate",
        "commandid": 1683305913,
        "source":"user:xivo/34",
        "destination": "exten:xivo/1202"
    }

record
^^^^^^

``Client -> Server``

* subcommand : ``start`` or ``stop``


.. code-block:: javascript

   {
            "class": "ipbxcommand",
            "command": "record",
            "subcommand": "start",
            "channel": "SIP/x2gjtw-0000000d",
            "commandid": 1423579492
   }

 ``Server > Client``

* response : ``ok`` request was correctly processed, ``ko`` unable to process the request

.. code-block:: javascript

   {"command": "record", "replyid": 1423579492, "class": "ipbxcommand", "ipbxreply": true, "timenow": 1361801751.87}
   {"replyid": 1423579492, "command": "record", "class": "ipbxcommand", "timenow": 1361798879.13, "response": "ok"}

hangup
^^^^^^

``Client -> Server``

.. code-block:: javascript

   {
       "class": "ipbxcommand",
       "command": "hangup",
       "channelids": "chan:xivo/<channel_id>",
       "commandid": <command_id>
   }

For example:

.. code-block:: javascript

   {
       "class": "ipbxcommand",
       "command": "hangup",
       "channelids": "chan:xivo/SIP/im2p7kzr-00000003",
       "commandid": 177773016
   }

``Server -> Client``

.. code-block:: javascript

   {
       "class": "ipbxcommand",
       "command": "hangup",
       "ipbxreply": 1,
       "replyid": 177773016,
       "timenow": 1395756534.64
   }


Statistics
----------

subscribetoqueuesstats
^^^^^^^^^^^^^^^^^^^^^^
This message can be sent from the client to enable statitics update on queues

``Client -> Server``

.. code-block:: javascript

   {"commandid":36,"class":"subscribetoqueuesstats"}

 ``Server > Client``

getqueuesstats
^^^^^^^^^^^^^^
When statistic update is enable by sending message `subscribetoqueuesstats`_.

The first element of the message is the queue id

.. code-block:: javascript

   {"stats": {"10": {"Xivo-LoggedAgents": 0}},
      "class": "getqueuesstats", "timenow": 1384509582.88}
   {"stats": {"1": {"Xivo-WaitingCalls": 0}},
      "class": "getqueuesstats", "timenow": 1384509582.89}
   {"stats": {"1": {"Xivo-TalkingAgents": "0", "Xivo-AvailableAgents": "1", "Xivo-EWT": "6"}},
      "class": "getqueuesstats", "timenow": 1384512350.25}

Switchboard
-----------

answer
^^^^^^

This allows the switchboard operator to answer an incoming call or unhold a call on-hold.

.. code-block:: javascript

   {"class": "answer", "uniqueid": "12345667.89"}

REGCOMMANDS
-----------

call_form_result
^^^^^^^^^^^^^^^^

This message is received when a `call form` is submitted from a client to the XiVO.

``Client -> Server``

.. code-block:: javascript

    {
        "class": "call_form_result",
        "commandid": <commandid>,
        "infos": {"buttonname": "saveandclose",
                  "variables": {"XIVOFORM_varname1": "value1",
                                "XIVOFORM_varname2": "value2"}}
    }


history
^^^^^^^
* mode
   * 0 : sent calls
   * 1 : received calls
   * 2 : missed calls
* size : Size of the list to be sent by the server

``Client -> Server``

.. code-block:: javascript

   {
      "mode": "0",
      "size": "8",
      "class": "history",
      "xuserid": "<xivoid>/<userfeaturesid>",
      "commandid": <commandid>
   }

``Server > Client``

Send back a table of calls :

* duration in seconds

.. code-block:: javascript


   {
      "class": "history",
      "history": [
         {"calldate": "2013-03-29T08:44:35.273998", "duration": 0.148765, "fullname": "*844201"},
         {"calldate": "2013-03-28T16:56:48.071213", "duration": 58.134744, "fullname": "41400"}
      ],
      "mode": 0, "replyid": 529422441, "timenow": 1364571477.33
   }


chitchat
^^^^^^^^

.. code-block:: javascript

    {
       "class": "chitchat",
       "text": "message envoye",
       "to": "<xivoid>/<userfeaturesid>",
       "commandid": <commandid>
    }

featuresget

featuresput

directory
^^^^^^^^^
Request directory information, names matching pattern ignore case.

``Client -> Server``

.. code-block:: javascript

   {
      "class": "directory",
      "commandid": 1079140548,
      "pattern": "pau"
   }

``Server > Client``

.. code-block:: javascript

   {
      "class": "directory",
      "headers": ["Nom", "Num\u00e9ro", "Mobile", "Autre num\u00e9ro", "E-mail", "Fonction", "Site", "Source"],
      "replyid": 1079140548,
      "resultlist": ["Claire Mapaurtal;;+33644558899;31256;cmapaurtal@societe.com;;;",
                     "Paul Salvadier;+33445236988;+33678521430;31406;psalvadier@societe.com;;;"],
      "status": "ok",
      "timenow": 1378798928.26
   }

parking

logfromclient

keepalive

availstate

filetransfer

faxsend

getipbxlist

.. code-block:: javascript

    {
        "class": "getipbxlist",
        "commandid": <commandid>
    }

ipbxcommand

.. code-block:: javascript

    {
       "class": "ipbxcommand",
       "command": "originate",
       "commandid": <commandid>,
       "destination": "user:special:myvoicemail",
       "source": "user:special:me"
    }


CTI server implementation
=========================

In the git repository ``git://github.com/xivo-pbx/xivo-ctid.git``, under `xivo_ctid/`

* `cti_config` handles the configuration coming from the WEBI
* `interfaces/interface_ami`, together with `asterisk_ami_definitions`, `amiinterpret` and `xivo_ami` handle the AMI connections (asterisk)
* `interfaces/interface_fagi` handles the FAGI connections (still asterisk)
* `interfaces/interface_info` handles the CLI-like connections
* `interfaces/interface_webi` handles the requests and signals coming from the WEBI
* `interfaces/interface_cti` handles the clients' connections, with the help of `client_connection`, and it often involves `cti_command` too
* `interfaces/interface_rcti` handles the connections from the CTI server to other ones in the multi-xivo framework
* `innerdata` is meant to be the place where all statuses are computed and stored

The main loop uses `select()` syscall to dispatch the tasks according to miscellaneous incoming requests.

Requirements for `innerdata`:

* the properties fetched from the WEBI configuration shall be stored in the relevant `xod_config` structure
* the properties fetched from elsewhere shall be stored in the relevant `xod_status` structure
* at least two kinds of objects are not "predefined" (as are the phones or the queues, for instance)

  * the channels (in the asterisk SIP/345-0x12345678 meaning)
  * the group and queue members shall be handled in a special way each
  * most statuses of the calls should be set inside the channel structure

The purpose of the 'relations' field, in the various structures is to keep track of relations
and cross-relations between different objects (a phone logged in as an agent, itself in a queue,
itself called by some channels belonging to phones ...).

CTI server Message flow
=======================

Messages sent from the CTI clients to the server are received by the CTIServer class.
The CTIServer then calls ``interface_cti.CTI`` class ``manage_connection`` method.
The ``interface_cti`` uses his ``_cti_command_handler`` member to parse and run the command.
The ``CTICommandHandler`` get a list of classes that handle this message from the ``CTICommandFactory``.
Then the the ``interface_cti.CTI`` calls ``run_commands`` on the handler, which returns a list of all commands replies.

To implement a new message in the protocol you have to create a new class that inherits the ``CTICommand`` class.
Your new class should have a static member caller ``required_fields`` which is a list of required fields for this class.
Your class should also have a ``conditions`` static member which is a list of tupples of conditions to detect that
an incoming message matches this class. The ``__init__`` of your class is responsible for the initialization of
it's fields and should call ``super(<ClassName>, self).__init__(msg)``. Your class should register itself to the ``CTICommandFactory``.

.. code-block:: python

    from xivo_cti.cti.cti_command import CTICommand
    from xivo_cti.cti.cti_command_factory import CTICommandFactory

    class InviteConfroom(CTICommand):
        required_fields = ['class', 'invitee']
        conditions = [('class', 'invite_confroom')]
        def __init__(self):
            super(InviteConfroom, self).__init__(msg)
            self._invitee = msg['invitee']

    CTICommandFactory.register_class(InviteConfroom)

Each CTI commands has a callback list that you can register to from anywhere. Each callback function will be called when
this message is received with the command as parameter.

Refer to ``MeetmeList.__init__`` for a callback registration example and to ``MeetmeList.invite`` for the implementation of a callback.

.. code-block:: python

    from xivo_cti.cti.commands.invite_confroom import InviteConfroom

    class MySuperClass(object):
        def __init__(self):
            InviteConfroom.register_callback(self.invite_confroom_handler)

        def invite_confroom_handler(self, invite_confroom_command):
            # Do your stuff here.
            if ok:
                return invite_confroom_command.get_message('Everything is fine')
            else:
                return invite_confroom_command.get_warning('I don't know you, go away', True)

.. note:: The client's connection is injected in the command instance before calling callbacks functions.
   The client's connection is an ``interface_cti.CTI`` instance.
