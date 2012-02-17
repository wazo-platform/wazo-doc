************
CTI protocol
************


Then, under `xivo_ctid/`

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
  * the group and queue members and shall be handled in a special way each
  * most statuses of the calls should be set inside the channel structure

The purpose of the 'relations' field, in the various structures, is to keep track of relations 
and cross-relations between different objects (a phone logged in as an agent, itself in a queue, 
itself called by some channels belonging to phones ...).


Message flow
============

Received messages from the CTI clients to the server are received by the CTIServer class. 
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


Commands
========

Objects have the format: "<type>:<xivoid>/<typeid>"

* <type> can take values in user, agent, queue, phone, group, meetme, ...
* <xivoid> indicates on which server the object is defined
* <typeid> is the object id, type dependant

e.g.
 user:xivo-test/5
 I'm looking for the user that has the ID 5 on the xivo-test server.


Class list
----------


LOGINCOMMANDS
-------------

.. code-block:: javascript

   {
   "commandid": <commandid>, 
   "class": "login_id", 
   }

* class: defined what class of command use.
* command: used to build the method called e.g. regcommand_login_id()

login_id

.. code-block:: javascript

    {
    "ident": "X11-LE-27333", 
    "version": "9999", 
    "userlogin": "<loginclient>", 
    "company": "default", 
    "commandid": <commandid>, 
    "lastlogout-stopper": "disconnect", 
    "git_date": "to_fill", 
    "lastlogout-datetime": "2011-09-06T13:30:49", 
    "git_hash": "to_fill", 
    "class": "login_id", 
    "xivoversion": "1.2"
    }

   
login_pass 

.. code-block:: javascript

    {
    "hashedpassword": "e5229ef45824333e0f8bbeed20dccfa2ddcb1c80", 
    "class": "login_pass", 
    "commandid": <commandid>
    }


login_capas 

.. code-block:: javascript

    {
    "loginkind": "user", 
    "capaid": "test", 
    "lastconnwins": False, 
    "commandid": <commandid>, 
    "state": "available", 
    "class": "login_capas"
    }

REGCOMMANDS
-----------

logout

callcampaign

chitchat

.. code-block:: javascript

    {
       "class": "chitchat", 
       "text": "message envoye", 
       "to": "<xivoid>/<userfeaturesid>",
       "commandid": <commandid>
    }

actionfiche

featuresget

featuresput

directory

history

.. code-block:: javascript

   {
      "mode": "0", 
      "size": "8", 
      "class": "history", 
      "xuserid": "<xivoid>/<userfeaturesid>", 
      "commandid": <commandid>
   }
 
parking

logfromclient

getqueuesstats

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

getlist

.. code-block:: javascript

    {
       "function": "updatestatus", 
       "listname": "channels", 
       "tipbxid": "<xivoid>", 
       "commandid": <commandid>, 
       "tid": "SIP/6d29u5-00000003", 
       "class": "getlist"
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

IPBXCOMMANDS
------------

hangupme

dial

.. code-block:: javascript

    {
       "destination": "<type>:<xivoid>/<typeid>", 
       "command": "dial", 
       "class": "ipbxcommand", 
       "commandid": <commandid>
    }

originate

.. code-block:: javascript

    {
       "amicommand": "originate", 
       "amiargs": ("<protocol>", "<callerpeer>", "<callerext>", "<callername> ", "<calledext>", "<calledname>", "<context>"), 
       "request": 
       {
           "ipbxcommand": "dial", 
           "commandid": <commandid>, 
           "requester": <xivo_ctiservers.interface_cti.CTI instance at 0x8997fec>
       }
    }

meetme

sipnotify

mailboxcount

parking

transfer

atxfer

transfercancel

intercept

hangup

answer

cancel

refuse

agentlogin

agentlogout

queueadd

queueremove

queuepause

queueunpause

queuepause_all

queueunpause_all

queueremove_all

record

listen

