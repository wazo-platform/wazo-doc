.. _cti-protocol:

************
CTI Protocol
************

Protocol Changelog
==================

The versions below indicate the xivo version followed by the protocol version.

.. warning:: The CTI server protocol is subject to change without any prior warning. If you are
   using this protocol in your own tools please be sure to check that the protocol did not change
   before upgrading XiVO


16.04 - 2.1
-----------

* the :ref:`cti_protocol_chitchat` command `to` and `from` fields are now a list of two strings,
  `xivo_uuid` and `user_uuid`.


16.01 - 2.0
-----------

* the `lastconnswins` field has been removed from the :ref:`cti_protocol_login_capas` command
* the `loginkind` field has been removed from the :ref:`cti_protocol_login_capas` command
* the `ipbxcommands` and `regcommands` capakinds have been removed from
  :ref:`cti_protocol_login_capas` command
* the :ref:`cti_protocol_login_pass` command has been modified. The `hashedpassword` has been
  replaced by the `password` field which is now sent verbatim.


15.20 - 1.2
-----------

* the :ref:`cti_protocol_starttls` command has been added


15.19 - 1.2
-----------

* the :ref:`cti_protocol_chitchat` command `to` field is now a list of two elements, `xivo_uuid` and
  `user_id`.
* the ``getlist`` command has been removed for the *channels* listname.
* many fields have been removed from the ``getlist`` command.

  * users list

    * enableclient
    * profileclient

  * phones

    * context
    * protocol
    * simultcalls
    * channels

  * voicemails

    * email
    * fullname
    * old
    * waiting

  * agents

    * phonenumber

* some ipbxcommands have been removed:

  * mailboxcount
  * atxfer
  * transfer
  * hangup
  * originate


15.18 - 1.2
-----------

* add the :ref:`cti_protocol-attended_transfer_voicemail` command
* add the :ref:`cti_protocol-blind_transfer_voicemail` command
* the :ref:`cti_protocol_fax_send` command now include the size and data field.
* the `filetransfer` command has been removed.


15.16 - 1.2
-----------

* the :ref:`cti_protocol_get_relations` command was added.
* the :ref:`cti_protocol_relations` message was added.


15.14 - 1.2
-----------

* the ``people_purge_personal_contacts`` message was added.
* the ``people_personal_contacts_purged`` message was added.
* the ``people_personal_contact_raw`` message was added.
* the ``people_personal_contact_raw_result`` message was added.
* the ``people_edit_personal_contact`` message was added.
* the ``people_personal_contact_raw_update`` message was added.
* the ``people_import_personal_contacts_csv`` message was added.
* the ``people_import_personal_contacts_csv_result`` message was added.
* the ``people_export_personal_contacts_csv`` message was added.
* the ``people_export_personal_contacts_csv_result`` message was added.
* for messages ``people_personal_contact_deleted`` and ``people_favorite_update`` there are no longer ``data`` sub-key.


15.13 - 1.2
-----------

* for ``channel status update`` message:

  * the value of ``commstatus`` have been changed from ``linked-caller`` and ``linked-called`` to
    ``linked``.
  * the key ``direction`` have been removed.
  * the key ``talkingto_kind`` have been removed.

* the ``people_personal_contacts`` message was added.
* the ``people_personal_contacts_result`` message was added.
* the ``people_create_personal_contact`` message was added.
* the ``people_personal_contact_created`` message was added.
* the ``people_delete_personal_contact`` message was added.
* the ``people_personal_contact_deleted`` message was added.


15.12 - 1.2
-----------

* ``people_search_result`` has a new key in ``relations``: ``source_entry_id``
* the ``people_favorites`` message was added.
* the ``people_favorites_result`` message was added.
* the ``people_set_favorite`` message was added.
* the ``people_favorite_update`` message was added.


15.11 - 1.2
-----------

* the ``fax_progress`` message was added.


15.09 - 1.2
-----------

* for messages of class ``history`` the client cannot request by mode anymore. The server returns
  all calls and the mode is now metadata for each call.


14.24 - 1.2
-----------

* for messages of class ``ipbxcommand``, the command ``record`` and ``sipnotify`` have been removed.
* the ``logfromclient`` message has been removed


14.22 - 1.2
-----------

* for messages of class ``faxsend``, the steps ``file_decoded`` and ``file_converted`` have been removed.


14.06 - 1.2
-----------

* the ``dial_success`` message was added


14.05 - 1.2
-----------

* the ``unhold_switchboard`` command was renamed ``resume_switchboard``.


13.22 - 1.2
-----------

* the ``actionfiche`` message was renamed ``call_form_result``.


13.17 - 1.2
-----------

* for messages of class ``login_capas`` from server to client: the key ``presence`` has been removed.


13.14 - 1.2
-----------

* for messages of class ``getlist``, list ``agents`` and function ``updatestatus``: the key ``availability`` in the ``status`` object/dictionary has changed values:

  * deleted values: ``on_call_non_acd_incoming`` and ``on_call_non_acd_outgoing``
  * added values:
    * ``on_call_non_acd_incoming_internal``
    * ``on_call_non_acd_incoming_external``
    * ``on_call_non_acd_outgoing_internal``
    * ``on_call_non_acd_outgoing_external``


13.12 - 1.2
-----------

* for messages of class ``getlist``, list ``agents`` and function ``updatestatus``: the key ``availability`` in the ``status`` object/dictionary has changed values:

  * deleted value: ``on_call_non_acd``
  * added values: ``on_call_non_acd_incoming`` and ``on_call_non_acd_outgoing``


13.10 - 1.2
-----------

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


Agent
-----

Login agent
^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

   {"agentphonenumber": "1000", "class": "ipbxcommand", "command": "agentlogin", "commandid": 733366597}

agentphonenumber is the physical phone set where the agent is going to log on.


``Server > Client``

* Login successfull :

.. code-block:: javascript

   {"function": "updateconfig",
    "listname": "queuemembers",
    "tipbxid": "xivo",
    "timenow": 1362664323.94,
    "tid": "Agent/2002,blue",
    "config": {"paused": "0",
               "penalty": "0",
               "membership": "static",
               "status": "1",
               "lastcall": "",
               "interface": "Agent/2002",
               "queue_name": "blue",
               "callstaken": "0"},
    "class": "getlist"}

   {"function": "updatestatus",
    "listname": "agents",
    "tipbxid": "xivo",
    "timenow": 1362664323.94,
    "status": {"availability_since": 1362664323.94,
               "queues": [],
               "on_call": false,
               "availability": "available",
               "channel": null},
      "tid": 7,
      "class": "getlist"}


* The phone number is already used by an other agent :

.. code-block:: javascript

   {"class": "ipbxcommand", "error_string": "agent_login_exten_in_use", "timenow": 1362664158.14}


Logout agent
^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "agentlogout", "commandid": 552759274}

Pause
^^^^^

On all queues

``Client -> Server``

.. code-block:: javascript

   {"class": "ipbxcommand", "command": "queuepause", "commandid": 859140432, "member": "agent:xivo/1", "queue": "queue:xivo/all"}

Un pause agent
^^^^^^^^^^^^^^

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


Configuration
-------------

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

Users configuration
^^^^^^^^^^^^^^^^^^^

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

User configuration
^^^^^^^^^^^^^^^^^^

Return a user configuration

* tid is the userid returned by `Users configuration`_ message

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
            "voicemailid": null, "incallfilter": 0,  "enablevoicemail": 0,   "agentid": 2, "linelist": ["7"], "mobilephonenumber": ""}
       }


Phones configuration
^^^^^^^^^^^^^^^^^^^^

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
      "config": {"allowtransfer": null, "identity": "SIP/ihvbur", "iduserfeatures": 1,
                     "initialized": null, "number": "1000"},
      "function": "updateconfig", "listname": "phones", "tid": "3", "timenow": 1364994093.43, "tipbxid": "xivo"}

Agents configuration
^^^^^^^^^^^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 1431355191, "function": "listid", "listname": "agents", "tipbxid": "xivo"}

Queues configuration
^^^^^^^^^^^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 719950939, "function": "listid", "listname": "queues", "tipbxid": "xivo"}

``Server -> Client``

.. code-block:: javascript

   {"function": "listid", "listname": "queues", "tipbxid": "xivo",
         "list": ["1", "10", "3", "2", "5", "4", "7", "6", "9", "8"], "timenow": 1382704649.64, "class": "getlist"}

Queue configuration
^^^^^^^^^^^^^^^^^^^
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


Voicemails configuration
^^^^^^^^^^^^^^^^^^^^^^^^
``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 1034160761, "function": "listid", "listname": "voicemails", "tipbxid": "xivo"}


Queue members configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^
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


Fax
---

.. _cti_protocol_fax_send:

Send fax
^^^^^^^^

``Client -> Server``

.. code-block:: javascript

   {"class": "faxsend",
    "filename": "contract.pdf",
    "destination", 41400,
    "size": 100000,
    "data": "<base64 of the fax content>"}


.. _cti_protocol_fax_status:

Fax status
^^^^^^^^^^

``Server -> Client``

* pages: number of pages sent (``NULL`` if FAILED)
* status

  * FAILED: Failed to send fax.
  * PRESENDFAX: Fax number exist and converting pdf->tiff has been done.
  * SUCCESS: Fax sent with success.

.. code-block:: javascript

   {"class": "fax_progress", "status": "SUCCESS", "pages": 2 }


Call control commands
---------------------

Dial
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


.. _cti_protocol-attended_transfer_voicemail:

Attended transfer to voicemail
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfer the current call to a given voicemail and listen to the message before
completing the transfer.

``Client -> Server``

.. code-block:: javascript

    {
        "class": "attended_transfer_voicemail",
        "voicemail": "<voicemail number>"
    }


.. _cti_protocol-blind_transfer_voicemail:

Blind transfer to voicemail
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfer the current call to a given voicemail.

``Client -> Server``

.. code-block:: javascript

    {
        "class": "blind_transfer_voicemail",
        "voicemail": "<voicemail number>"
    }


Login
-----

Once the network is connected at the socket level, the login process requires
three steps. If one of these steps is omitted, the connection is reset by the
cti server.

* login_id, the username is sent as a login to the cti server, cti server answers by giving a sessionid
* login_pass, the password is sent to the cti server, cti server answers by giving a capaid
* login_capas, the capaid is returned to the server with the user's
  availability, cti server answers with a list of info relevant to the user

.. code-block:: javascript

   {
   "commandid": <commandid>,
   "class": "login_id",
   }

* class: defined what class of command use.
* commandid : a unique integer number.

Login ID
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
    "xivoversion": "<cti protocol version>"
    }


``Server -> Client``

.. code-block:: javascript

   {
       "class": "login_id",
       "sessionid": "21UaGDfst7",
       "timenow": 1361268824.64,
       "xivoversion": "<cti protocol version>"
   }

.. note::

   sessionid is used to calculate the hashed password in next step


.. _cti_protocol_login_pass:

Login password
^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

    {
        "class": "login_pass",
        "password": "secret",
        "commandid": <commandid>
    }

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

.. _cti_protocol_login_capas:

Login capas
^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

    {
    "capaid": 3,
    "commandid": <commandid>,
    "state": "available",
    "class": "login_capas"
    }


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
                           }
         },
      "capaxlets": [["identity", "grid"], ["search", "tab"], ["customerinfo", "tab", "1"], ["fax", "tab", "2"], ["dial", "grid", "2"], ["tabber", "grid", "3"], ["history", "tab", "3"], ["remotedirectory", "tab", "4"], ["features", "tab", "5"], ["people", "tab", "6"], ["conference", "tab", "7"]],
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


Others
------

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


History
^^^^^^^

* size : Size of the list to be sent by the server

``Client -> Server``

.. code-block:: javascript

   {
      "class": "history",
      "commandid": <commandid>
      "size": "8",
      "xuserid": "<xivoid>/<userfeaturesid>",
   }

``Server > Client``

Send back a table of calls :

* duration in seconds
* extension: caller/destination extension
* fullname: caller ID name
* mode

  * 0 : sent calls
  * 1 : received calls
  * 2 : missed calls

.. code-block:: javascript


   {
      "class": "history",
      "history": [
         {"calldate": "2013-03-29T08:44:35.273998",
          "duration": 30.148765,
          "extension": "*844201",
          "fullname": "Alice Wonderland",
          "mode": 0},
         {"calldate": "2013-03-28T16:56:48.071213",
          "duration": 58.134744,
          "extension": "41400",
          "fullname": "41400"}
          "mode": 1},
      ],
      "replyid": 529422441,
      "timenow": 1364571477.33
   }


.. _cti_protocol_chitchat:

Chitchat
^^^^^^^^

``Client > Server``

.. code-block:: javascript

    {
       "class": "chitchat",
       "alias": "Alice",
       "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse venenatis velit nibh, ac condimentum felis rutrum id.",
       "to": [<xivo_uuid>, <user_uuid>],
       "commandid": <commandid>
    }


``Server > Client``

The following message is received by the remote XiVO client

.. code-block:: javascript

    {
        "class": "chitchat",
        "from": [<xivo_uuid>, <user_uuid>],
        "to": [<xivo_uuid>, <user_uuid>]
        "alias": "Alice",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse venenatis velit nibh, ac condimentum felis rutrum id.",
    }


Directory
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

keepalive

availstate

getipbxlist

.. code-block:: javascript

    {
        "class": "getipbxlist",
        "commandid": <commandid>
    }


People
------

.. _cti_protocol_get_relations:

Get relations
^^^^^^^^^^^^^

This command will trigger a :ref:`cti_protocol_relations` message.

``Client -> Server``

.. code-block:: javascript

    {
        "class": "get_relations"
    }


People headers
^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_headers",
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_headers_result",
    "column_headers": ["Status", "Name", "Number"],
    "column_types": [null, null, "number"],
  }


People Search
^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_search",
    "pattern": <pattern>,
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_search_result",
    "term": "Bob",
    "column_headers": ["Firstname", "Lastname", "Phone number", "Mobile", "Fax", "Email", "Agent"],
    "column_types": [null, "name", "number_office", "number_mobile", "fax", "email", "relation_agent"],
    "results": [
      {
        "column_values": ["Bob", "Marley", "5555555", "5556666", "5553333", "mail@example.com", null],
        "relations": {
          "agent_id": null,
          "user_id": null,
          "endpoint_id": null,
          "source_entry_id": null
        },
        "source": "my_ldap_directory"
      }, {
        "column_values": ["Charlie", "Boblin", "5555556", "5554444", "5552222", "mail2@example.com", null],
        "relations": {
          "agent_id": 12,
          "user_id": 34,
          "endpoint_id": 56,
          "source_entry_id": "34"
        },
        "source": "internal"
      }
    ]
  }


.. _cti_protocol_relations:

Relations
^^^^^^^^^

This message can currently only be received as a response to the :ref:`cti_protocol_get_relations`
command.

* The *xivo_uuid* is the id of the server
* The *user_id* is the id of the current user.
* The *endpoint_id* is the id of the line of the current user or null.
* The *agent_id* is the id of the agent of the current user or null.

``Server -> Client``

.. code-block:: javascript

    {
        "class": "relations",
        "data": {"xivo_uuid": <the xivo uuid>,
                 "user_id": <the user id>,
                 "endpoint_id": <the endpoint id>,
                 "agent_id": <the agent id>}
    }


Favorites list
^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_favorites",
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_favorites_result",
    "column_headers": ["Firstname", "Lastname", "Phone number", "Mobile", "Fax", "Email", "Agent", "Favorites"],
    "column_types": [null, "name", "number_office", "number_mobile", "fax", "email", "relation_agent", "favorite"],
    "results": [
      {
        "column_values": ["Bob", "Marley", "5555555", "5556666", "5553333", "mail@example.com", null, true],
        "relations": {
          "agent_id": null,
          "user_id": null,
          "endpoint_id": null,
          "source_entry_id": "55"
        },
        "source": "my_ldap_directory"
      }, {
        "column_values": ["Charlie", "Boblin", "5555556", "5554444", "5552222", "mail2@example.com", null, true],
        "relations": {
          "agent_id": 12,
          "user_id": 34,
          "endpoint_id": 56,
          "source_entry_id": "34"
        },
        "source": "internal"
      }
    ]
  }


Set favorite
^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_set_favorite",
    "source": "my_ldap_directory"
    "source_entry_id": "55"
    "favorite": true
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_favorite_update",
    "source": "my_ldap_directory"
    "source_entry_id": "55"
    "favorite": true
  }


.. _cti_protocol_starttls:

STARTTLS
^^^^^^^^

The STARTTLS command is used to upgrade a connection to use SSL. Once connected,
the server send a starttls offer to the client which can reply with a starttls
message including the status field. The server will then send a starttls message
back to the client with the same status and start the handshake if the status is
true.

``Server -> Client``

.. code-block:: javascript

    {
        "class": "starttls"
    }


``Client -> Server -> Client``

.. code-block:: javascript

    {
        "class": "starttls",
        "status": true
    }


.. note:: a client which does not reply to the starttls offer will keep it's
    unencrypted connection.


Personal contacts list
^^^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_personal_contacts"
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_personal_contacts_result",
    "column_headers": ["Firstname", "Lastname", "Phone number", "Mobile", "Fax", "Email", "Agent", "Favorites", "Personal"],
    "column_types": [null, "name", "number_office", "number_mobile", "fax", "email", "relation_agent", "favorite", "personal"],
    "results": [
      {
        "column_values": ["Bob", "Marley", "5555555", "5556666", "5553333", "mail@example.com", null, false, true],
        "relations": {
          "agent_id": null,
          "user_id": null,
          "endpoint_id": null,
          "source_entry_id": "abcd-12"
        },
        "source": "personal"
      }, {
        "column_values": ["Charlie", "Boblin", "5555556", "5554444", "5552222", "mail2@example.com", null, false, true],
        "relations": {
          "agent_id": null,
          "user_id": null,
          "endpoint_id": null,
          "source_entry_id": "efgh-34"
        },
        "source": "personal"
      }
    ]
  }


Personal contact purge
^^^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_purge_personal_contacts",
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_personal_contacts_purged",
  }


Personal contact raw
^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_personal_contact_raw",
    "source": "personal",
    "source_entry_id": "abcd-1234"
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_personal_contact_raw_result",
    "source": "personal",
    "source_entry_id": "abcd-1234",
    "contact_infos": {
        "firstname": "Bob",
        "lastname": "Wonderland"
        ...
    }
  }


Create personal contact
^^^^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_create_personal_contact",
    "contact_infos": {
        "firstname": "Bob",
        "lastname": "Wonderland",
        ...
    }
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_personal_contact_created"
  }


Delete personal contact
^^^^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_delete_personal_contact",
    "source": "personal",
    "source_entry_id": "abcd-1234"
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_personal_contact_deleted",
    "source": "personal",
    "source_entry_id": "abcd-1234"
  }


Edit personal contact
^^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_edit_personal_contact",
    "source": "personal",
    "source_entry_id": "abcd-1234",
    "contact_infos": {
        "firstname": "Bob",
        "lastname": "Wonderland",
        ...
    }
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_personal_contact_raw_update",
    "source": "personal",
    "source_entry_id": "abcd-1234"
  }


Import personal contacts
^^^^^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_import_personal_contacts_csv",
    "csv_contacts": "firstname,lastname\r\nBob,the Builder\r\n,Alice,Wonderland\r\n,BobMissingFields\r\n"
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_import_personal_contacts_csv_result",
    "created_count": 2,
    "failed": [
        {
            "line": 3,
            "errors": [
                "missing fields"
                ]
        }

    ]
  }


Export personal contacts
^^^^^^^^^^^^^^^^^^^^^^^^

``Client -> Server``

.. code-block:: javascript

  {
    "class": "people_export_personal_contacts_csv",
  }

``Server -> Client``

.. code-block:: javascript

  {
    "class": "people_export_personal_contacts_csv_result",
    "csv_contacts": "firstname,lastname\r\nBob,the Builder\r\n,Alice,Wonderland\r\n"
  }


Service
-------

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


Statistics
----------

Subscribe to queues stats
^^^^^^^^^^^^^^^^^^^^^^^^^

This message can be sent from the client to enable statitics update on queues

``Client -> Server``

.. code-block:: javascript

   {"commandid":36,"class":"subscribetoqueuesstats"}

 ``Server > Client``

Get queues stats
^^^^^^^^^^^^^^^^

When statistic update is enable by sending message `Subscribe to queues stats`_.

The first element of the message is the queue id

.. code-block:: javascript

   {"stats": {"10": {"Xivo-LoggedAgents": 0}},
      "class": "getqueuesstats", "timenow": 1384509582.88}
   {"stats": {"1": {"Xivo-WaitingCalls": 0}},
      "class": "getqueuesstats", "timenow": 1384509582.89}
   {"stats": {"1": {"Xivo-TalkingAgents": "0", "Xivo-AvailableAgents": "1", "Xivo-EWT": "6"}},
      "class": "getqueuesstats", "timenow": 1384512350.25}


Status
------

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
* tid is the line id, found in linelist from message `User configuration`_

``Client -> Server``

.. code-block:: javascript

   {"class": "getlist", "commandid": 107712156,
      "function": "updatestatus",
      "listname": "phones", "tid": "8", "tipbxid": "xivo"}

``Server > Client``

.. code-block:: javascript

   {"class": "getlist",
    "function": "updatestatus",
    "listname": "phones",
    "status": {"hintstatus": "0"},
    "tid": "1",
    "timenow": 1364994093.48,
    "tipbxid": "xivo"}


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


Switchboard
-----------

Answer
^^^^^^

This allows the switchboard operator to answer an incoming call or unhold a call on-hold.

.. code-block:: javascript

   {"class": "answer", "uniqueid": "12345667.89"}

Unsolicited Messages
--------------------

These messages are received whenever one of the following corresponding event occurs: sheet message on incoming calls, or updatestatus when a phone status changes.

Sheet
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

Phone status update
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

   {.... "status": {"hintstatus": "0"}, "tid": "3"}
   {.... "status": {"hintstatus": "8"}, "tid": "3"}


Update notification
-------------------

.. _register_agent_status_update_command:

Register agent status update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `register_agent_status_update` command is used to register to the status
updates of a list of agent. Once registered to a agent's status, the client will
receive all :ref:`agent_status_update_event` events for the registered agents.

This command should be sent when an agent is displayed in the people xlet to be
able to update the agent status icon.

The :ref:`unregister_agent_status_update_command` command should be used to stop receiving updates.

``Client -> Server``

.. code-block:: javascript

  {
    "class": "register_agent_status_update",
    "agent_ids": [["<xivo-uuid>", "<agent-id1>"],
                  ["<xivo-uuid>", "<agent-id2>"],
                  ...,
                  ["<xivo-uuid>", "<agent-idn>"]],
    "commandid": <commandid>
  }


.. _unregister_agent_status_update_command:

Unregister agent status update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `unregister_agent_status_update` command is used to unregister from the
status updates of a list of agent.

Once unregistered, the client will stop receiving the :ref:`agent_status_update_event`
events for the specified agents.

``Client -> Server``

.. code-block:: javascript

  {
    "class": "unregister_agent_status_update",
    "agent_ids": [["<xivo-uuid>", "<agent-id1>"],
                  ["<xivo-uuid>", "<agent-id2>"],
                  ...,
                  ["<xivo-uuid>", "<agent-idn>"]],
    "commandid": <commandid>
  }

.. _agent_status_update_event:

Agent status update
^^^^^^^^^^^^^^^^^^^

The `agent_status_update` event is received when the presence of an agent changes.

To receive this event, the user must first register to the event for a specified
agent using the :ref:`register_agent_status_update_command` command.

To stop receiving this event, the user must send the
:ref:`unregister_agent_status_update_command` command.

* data, a dictionary containing 3 fields:

  * agent_id, is an integer containing the ID of the user affected by this status change
  * xivo_uuid: a string containing the UUID of the XiVO that sent the status update
  * status: a string containing the new status, "logged_in" or "logged_out"

``Server -> Client``

.. code-block:: javascript

  {
    "class": "agent_status_update",
    "data": {
      "agent_id": 42,
      "xivo_uuid": "<the-xivo-uuid>",
      "status": "<status-name>"
    }
  }

The `agent_status_update` event contains the same data as the :ref:`bus-agent_status_update`.
The latter should be preferred to the former for uses that do not require a
persistent connection to xivo-ctid.


.. _register_endpoint_status_update_command:

Register endpoint status update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `register_endpoint_status_update` command is used to register to the status
updates of a list of lines. Once registered to a endpoint's status, the client will
receive all :ref:`endpoint_status_update_event` events for the registered agents.

This command should be sent when a endpoint is displayed in the people xlet to be
able to update the agent status icon.

The :ref:`unregister_endpoint_status_update_command` command should be used to stop receiving updates.

``Client -> Server``

.. code-block:: javascript

  {
    "class": "register_endpoint_status_update",
    "endpoint_ids": [["<xivo-uuid>", "<endpoint-id1>"],
                     ["<xivo-uuid>", "<endpoint-id2>"],
                     ...,
                     ["<xivo-uuid>", "<endpoint-idn>"]],
    "commandid": <commandid>
  }


.. _unregister_endpoint_status_update_command:

Unregister endpoint status update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `unregister_endpoint_status_update` command is used to unregister from the
status updates of a list of agent.

Once unregistered, the client will stop receiving the :ref:`endpoint_status_update_event`
events for the specified agents.

``Client -> Server``

.. code-block:: javascript

  {
    "class": "unregister_endpoint_status_update",
    "endpoint_ids": [["<xivo-uuid>", "<endpoint-id1>"],
                     ["<xivo-uuid>", "<endpoint-id2>"],
                     ...,
                     ["<xivo-uuid>", "<endpoint-idn>"]],
    "commandid": <commandid>
  }


.. _endpoint_status_update_event:

Endpoint status update
^^^^^^^^^^^^^^^^^^^^^^

The `endpoint_status_update` event is received when the status of a line changes.

To receive this event, the user must first register to the event for a specified
endpoint using the :ref:`register_endpoint_status_update_command` command.

To stop receiving this event, the user must send the
:ref:`unregister_endpoint_status_update_command` command.

* data, a dictionary containing 3 fields:

  * endpoint_id, is an integer containing the ID of the line affected by this status change
  * xivo_uuid: a string containing the UUID of the XiVO that sent the status update
  * status: an integer matching an entry in the cti hint configuration

``Server -> Client``

.. code-block:: javascript

  {
    "class": "endpoint_status_update",
    "data": {
      "endpoint_id": 42,
      "xivo_uuid": "<the-xivo-uuid>",
      "status": <hint-status>
    }
  }

The `endpoint_status_update` event contains the same data as the :ref:`bus-endpoint_status_update`.
The latter should be preferred to the former for uses that do not require a
persistent connection to xivo-ctid.


.. _register_user_status_update_command:

Register user status update
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    "user_ids": [["<xivo-uuid>", "<user-id1>"],
                 ["<xivo-uuid>", "<user-id2>"],
                 ...,
                 ["<xivo-uuid>", "<user-idn>"]],
    "commandid": <commandid>
  }


.. _unregister_user_status_update_command:

Unregister user status update
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `unregister_user_status_update` command is used to unregister from the
status updates of a list of user.

Once unregistered, the client will stop receiving the :ref:`user_status_update_event`
events for the specified users.

``Client -> Server``

.. code-block:: javascript

  {
    "class": "unregister_user_status_update",
    "user_ids": [["<xivo-uuid>", "<agent-id1>"],
                 ["<xivo-uuid>", "<agent-id2>"],
                 ...,
                 ["<xivo-uuid>", "<agent-idn>"]],
    "commandid": <commandid>
  }


.. _user_status_update_event:

User status update
^^^^^^^^^^^^^^^^^^

The `user_status_update` event is received when the presence of a user changes.

To receive this event, the user must first register to the event for a specified
user using the :ref:`register_user_status_update_command` command.

To stop receiving this event, the user must send the
:ref:`unregister_user_status_update_command` command.

* data, a dictionary containing 3 fields:

  * user_id, is an integer containing the ID of the user affected by this status change
  * xivo_uuid: a string containing the UUID of the XiVO that sent the status update
  * status: a string containing the new status of the user based on the cti profile configuration

.. note:: When multiple XiVO share user statuses, the cti profile configuration for presences and phone statuses
   should match on all XiVO to be displayed properly

``Server -> Client``

.. code-block:: javascript

  {
    "class": "user_status_update",
    "data": {
      "user_id": 42,
      "xivo_uuid": "<the-xivo-uuid>",
      "status": "<status-name>"
    }
  }

The `user_status_update` event contains the same data as the :ref:`bus-user_status_update`.
The latter should be preferred to the former for uses that do not require a
persistent connection to xivo-ctid.


CTI server implementation
=========================

In the git repository ``git://github.com/xivo-pbx/xivo-ctid.git``

* `cti_config` handles the configuration coming from the WEBI
* `interfaces/interface_ami`, together with `asterisk_ami_definitions`, `amiinterpret` and `xivo_ami` handle the AMI connections (asterisk)
* `interfaces/interface_info` handles the CLI-like connections
* `interfaces/interface_webi` handles the requests and signals coming from the WEBI
* `interfaces/interface_cti` handles the clients' connections, with the help of `client_connection`, and it often involves `cti_command` too
* `innerdata` is meant to be the place where all statuses are computed and stored

The main loop uses `select()` syscall to dispatch the tasks according to miscellaneous incoming requests.

Requirements for `innerdata`:

* the properties fetched from the WEBI configuration shall be stored in the relevant `xod_config` structure
* the properties fetched from elsewhere shall be stored in the relevant `xod_status` structure
* at least two kinds of objects are not "predefined" (as are the phones or the queues, for instance)

  * the channels (in the asterisk SIP/345-0x12345678 meaning)
  * the group and queue members shall be handled in a special way each

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
