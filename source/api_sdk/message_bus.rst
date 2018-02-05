.. _message-bus:

***********
Message Bus
***********

The message bus is used to receive events from Wazo. It is provided by
an `AMQP <http://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol>`_ 0-9-1
broker (namely, `RabbitMQ <http://previous.rabbitmq.com/v2_8_x/documentation.html>`_)
that is integrated in Wazo.


Usage
=====

Websocket
---------

The easiest way to listen for events is to use the :ref:`Wazo WebSocket <wazo-websocketd>`.

Direct AMQP connection
----------------------

At the moment, the AMQP broker only listen on the 127.0.0.1 address. This means
that if you want to connect to the AMQP broker from a distant machine, you
must modify the RabbitMQ server configuration, which is not yet an officially
supported operation. All events are sent to the *xivo* exchange.

Otherwise, the default connection information is:

* Virtual host: /
* User name: guest
* User password: guest
* Port: 5672
* Exchange name: xivo
* Exchange type: topic


Example
-------

Here's an example of a simple client, in python, listening for the
:ref:`bus-call_form_result` CTI events::

    import kombu

    from kombu.mixins import ConsumerMixin

    EXCHANGE = kombu.Exchange('xivo', type='topic')
    ROUTING_KEY = 'call_form_result'


    class C(ConsumerMixin):

        def __init__(self, connection):
            self.connection = connection

        def get_consumers(self, Consumer, channel):
            return [Consumer(kombu.Queue(exchange=EXCHANGE, routing_key=ROUTING_KEY),
                    callbacks=[self.on_message])]

        def on_message(self, body, message):
            print('Received:', body)
            message.ack()


    def main():
        with kombu.Connection('amqp://guest:guest@localhost:5672//') as conn:
            try:
                C(conn).run()
            except KeyboardInterrupt:
                return


    main()

If you are new to AMQP, you might want to look at the
`RabbitMQ tutorial <http://previous.rabbitmq.com/v2_8_x/getstarted.html>`_.


Notes
-----

Things to be aware when writing a client/consumer:

* The published messages are not persistent. When the AMQP broker stops, the messages
  that are still in queues will be lost.


.. _bus-changelog:

Changelog
=========

18.02
-----

* The following message has been added:

  * :ref:`auth_user_external_auth_authorized <bus-external-auth-authorized>`


17.17
-----

* The following messages have been added:

  * :ref:`auth_user_external_auth_added <bus-external-auth-added>`
  * :ref:`auth_user_external_auth_deleted <bus-external-auth-deleted>`


17.16
-----

* The following messages have been added:

  * :ref:`relocate_initiated <bus-relocate_initiated>`
  * :ref:`relocate_answered <bus-relocate_answered>`
  * :ref:`relocate_completed <bus-relocate_completed>`
  * :ref:`relocate_ended <bus-relocate_ended>`


17.14
-----

* The :ref:`chat_message_sent <bus-chat_message>` bus message has been added.
* The :ref:`chat_message_received <bus-chat_message>` bus message has been added.
* The :ref:`chat_message_event <bus-chat_message>` bus message has been deprecated.


17.08
-----

* The :ref:`bus-plugin_install_progress` bus message has been added.
* The :ref:`bus-plugin_uninstall_progress` bus message has been added.


17.01
-----

* The :ref:`bus-favorite_added` bus message has been added.
* The :ref:`bus-favorite_deleted` bus message has been added.


16.08
-----

* The :ref:`bus-call_held_event` bus message has been added.
* The :ref:`bus-call_resumed_event` bus message has been added.
* The :ref:`bus-user_status_update` bus message now uses the user's UUID instead of the user's ID.


16.07
-----

* The :ref:`bus-user_created` bus message has been added.
* The :ref:`bus-user_edited` bus message has been added.
* The :ref:`bus-user_deleted` bus message has been added.


15.20
-----

* The :ref:`chat_message_event <bus-chat_message>` bus message has been added.


15.17
-----

* The :ref:`bus-service_registered_event` and :ref:`bus-service_deregistered_event` bus messages have
  been added.


.. _bus-events:

Events
======

Events that are sent to the bus use a JSON serialization format with the content-type
`application/json`. For example, the CTI call_form_result event looks like this::

    {"name": "call_form_result",
     "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
     "data": {...}}

All events have the same basic structure, namely, a JSON object with 4 keys:

name
    A string representing the name of the event. Each event type has a unique name.

required_acl (optional)
    Either a string or null. Currently used by xivo-websocketd to determine if
    a client can receive the event or not. See the :ref:`ws-events-acl` section for
    more information.

origin_uuid
    The uuid to identify the message producer.

data
    The data specific part of the event. This is documented on a per event type; if not
    this is assumed to be null.


.. _bus-ami_events:

AMI events
----------

All AMI events are broadcasted on the bus.

* routing key: ami.<event name>
* event specific data: a dictionary with the content of the AMI event

Example event with binding key QueueMemberStatus::

   {
       "name": "QueueMemberStatus",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "Status": "1",
           "Penalty": "0",
           "CallsTaken": "0",
           "Skills": "",
           "MemberName": "sip\/m3ylhs",
           "Queue": "petak",
           "LastCall": "0",
           "Membership": "static",
           "Location": "sip\/m3ylhs",
           "Privilege": "agent,all",
           "Paused": "0",
           "StateInterface": "sip\/m4ylhs"
       }
   }


.. _bus-external-auth-added:

auth_user_external_auth_added
-----------------------------

This event is sent when a user adds an external authentification to its account.

* routing_key: auth.users.{user_uuid}.external.{external_auth_name}.created
* event specific data:

  * user_uuid: The user's UUID
  * external_auth_name: The name of the external service

Example::

  {
    "name": "auth_user_external_auth_added",
    "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
    "data": {
      "user_uuid": "a1e05585-1421-4397-bd59-9cf9725888e9",
      "external_auth_name": "zoho"
    }
  }


.. _bus-external-auth-authorized:

auth_user_external_auth_authorized
----------------------------------

This event is sent when a user authorizes an oauth2 request on an external authentification plugin.

* routing_key: auth.users.{user_uuid}.external.{external_auth_name}.authorized
* event specific data:

  * user_uuid: The user's UUID
  * external_auth_name: The name of the external service

Example::

  {
    "name": "auth_user_external_auth_authorized",
    "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
    "data": {
      "user_uuid": "a1e05585-1421-4397-bd59-9cf9725888e9",
      "external_auth_name": "zoho"
    }
  }


.. _bus-external-auth-deleted:

auth_user_external_auth_deleted
-------------------------------

This event is sent when a user removes an external authentification from its account.

* routing_key: auth.users.{user_uuid}.external.{external_auth_name}.deleted
* event specific data:

  * user_uuid: The user's UUID
  * external_auth_name: The name of the external service

Example::

  {
    "name": "auth_user_external_auth_deleted",
    "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
    "data": {
      "user_uuid": "a1e05585-1421-4397-bd59-9cf9725888e9",
      "external_auth_name": "zoho"
    }
  }


.. _bus-call_form_result:

call_form_result
----------------

The call_form_result event is sent when a :ref:`custom call form <custom-call-form>`
is submitted by a CTI client.

* routing key: call_form_result
* event specific data: a dictionary with 2 keys:

  * user_id: an integer corresponding to the user ID of the client who saved the call form
  * variables: a dictionary holding the content of the form

Example::

   {
       "name": "call_form_result",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "user_id": 40,
           "variables": {
               "firstname": "John",
               "lastname": "Doe"
           }
       }
   }


.. _bus-agent_status_update:

agent_status_update
-------------------

The agent_status_update is sent when an agent is logged in or logged out.

* routing key: status.agent
* required ACL: events.statuses.agents
* event specific data: a dictionary with 3 keys:

  * agent_id: an integer corresponding to the agent ID of the agent who's status changed
  * status: a string identifying the status
  * xivo_id: the uuid of the xivo

Example::

   {
       "name": "agent_status_update",
       "required_acl": "events.statuses.agents",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "agent_id": 42,
           "xivo_id": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
           "status": "logged_in"
       }
   }


.. _bus-call_created:

call_created, call_updated, call_ended
--------------------------------------

The events ``call_created``, ``call_updated``, ``call_ended`` are sent when a call handled by
xivo-ctid-ng is received, connected or hung up.

* routing key: calls.call.created, calls.call.updated, calls.call.ended
* required ACL: events.calls.<user_uuid>
* event specific data: a dictionary with the same fields as the REST API model of Call (See
  http://api.wazo.community, section xivo-ctid-ng)

Example::

   {
       "name": "call_created",
       "required_acl": "events.calls.2e752722-0864-4665-887d-a78a024cf7c7",
       "origin_uuid": "08c56466-8f29-45c7-9856-92bf1ba89b82",
       "data": {
           "bridges": [],
           "call_id": "1455123422.8",
           "caller_id_name": "Some One",
           "caller_id_number": "1001",
           "creation_time": "2016-02-10T11:57:02.592-0500",
           "status": "Ring",
           "talking_to": {},
           "user_uuid": "2e752722-0864-4665-887d-a78a024cf7c7"
       }
   }


.. _bus-call_held_event:

call_held
---------

This message is sent when a call is placed on hold

* routing key: calls.hold.created
* event specific data:

  * call_id: The asterisk channel unique ID

Example:

.. code-block:: javascript

   {"name": "call_held",
    "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
    "data": {"call_id": "1465572129.31"}}


.. _bus-call_resumed_event:

call_resumed
------------

This message is sent when a call is resumed from hold

* routing key: calls.hold.deleted
* event specific data:

  * call_id: The asterisk channel unique ID

Example:

.. code-block:: javascript

   {"name": "call_resumed",
    "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
    "data": {"call_id": "1465572129.31"}}


.. _bus-chat_message:

chat_message_received, chat_message_sent
----------------------------------------

* routing key: ``chat.message.<wazo-uuid>.<user_id>``. The ``wazo-uuid`` and ``user-uuid`` are the sender for ``chat_message_sent`` and the recipient for ``chat_message_received``.
* event specific data:

  * alias: The nickname of the chatter
  * to: The destination's Wazo UUID and user UUID
  * from: The chatter's Wazo UUID and user UUID
  * msg: The message

Example:

.. code-block:: javascript

  {
      "name": "chat_message_received",
      "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
      "data": {
          "alias": "Alice"
          "to": ["ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", "fcb36731-c50a-453e-92c7-571297d41616"],
          "from": ["ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", "4f2e2249-ae2b-4bc2-b5fc-ad42ee01ddaf"],
          "msg": "Hi!"
      }
  }

.. note:: The message named ``chat_message_event`` is deprecated since Wazo 17.14. You should not use it anymore. If you want to send a new chat message, you should use the :ref:`xivo-ctid-ng REST API <rest-api_changelog>` instead.


.. _bus-endpoint_status_update:

endpoint_status_update
----------------------

The endpoint_status_update is sent when an end point status changes. This information is
based on asterisk hints.

* routing key: status.endpoint
* required ACL: events.statuses.endpoints
* event specific data: a dictionary with 3 keys

  * xivo_id: the uuid of the xivo
  * endpoint_id: an integer corresponding to the endpoint ID
  * status: an integer corresponding to the asterisk device state

Example::

   {
       "name": "endpoint_status_update",
       "required_acl": "events.statuses.endpoints",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "endpoint_id": 67,
           "xivo_id": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
           "status": 0
       }
   }


.. _bus-favorite_added:

favorite_added
--------------

The `favorite_added` event is published when a contact is marked as a favorite by a user.

* routing key: directory.<user_uuid>.favorite.created
* required ACL: events.directory.<user_uuid>.favorite.created
* event specific data:

    * xivo_id: The user's Wazo server UUID
    * user_uuid: The user's UUID
    * source: The source in which this contact can be found
    * source_entry_id: The ID of the contact within this source

Example:

.. code-block:: javascript

    {
        "name": "favorite_added",
        "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
        "data": {
            "xivo_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
            "user_uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2",
            "source": "internal",
            "source_entry_id": 42
        }
    }

.. _bus-favorite_deleted:

favorite_deleted
----------------

The `favorite_deleted` event is published when a favorited contact is marked a not
favorite by a user

* routing key: directory.<user_uuid>.favorite.deleted
* required ACL: events.directory.<user_uuid>.favorite.deleted
* event specific data:

    * xivo_id: The user's Wazo server UUID
    * user_uuid: The user's UUID
    * source: The source in which this contact can be found
    * source_entry_id: The ID of the contact within this source

Example:

.. code-block:: javascript

    {
        "name": "favorite_deleted",
        "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
        "data": {
            "xivo_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
            "user_uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2",
            "source": "internal",
            "source_entry_id": 42
        }
    }


.. _bus-plugin_install_progress:

plugin_install_progress
-----------------------

The `plugin_install_progress` event is published during the installation of a plugin.

* routing key: `plugin.install.<uuid>.<status>`
* required ACL: `events.plugin.install.<uuid>.<status>`
* event specific data:

  * uuid: The installation task UUID
  * status: The status of the installation

Example:

.. code-block:: javascript

   {
       "name": "plugin_install_progress",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2",
           "status": "completed"
       }
   }


.. _bus-plugin_uninstall_progress:

plugin_uninstall_progress
-------------------------

The `plugin_uninstall_progress` event is published during the removal of a plugin.

* routing key: `plugin.uninstall.<uuid>.<status>`
* required ACL: `events.plugin.uninstall.<uuid>.<status>`
* event specific data:

  * uuid: The removal task UUID
  * status: The status of the removal

Example:

.. code-block:: javascript

   {
       "name": "plugin_uninstall_progress",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2",
           "status": "removing"
       }
   }


.. _bus-relocate_initiated:
.. _bus-relocate_answered:
.. _bus-relocate_completed:
.. _bus-relocate_ended:

relocate_initiated, relocate_answered, relocate_completed, relocate_ended
-------------------------------------------------------------------------

Those events are published during the different steps of a relocate operation.

* routing key: ``calls.relocate.XXX`` where ``XXX`` is the event, e.g. ``calls.relocate.completed``
* headers:

  * ``"user_uuid:XXX": True`` where ``XXX`` is the initiator's user UUID

* required ACL: ``events.relocates.XXX`` where XXX is the initiator's user UUID
* event specific data: a relocate object, see http://api.wazo.community, section ``xivo-ctid-ng``.

Example:

.. code-block:: javascript

    {
        "name": "relocate_completed",
        "origin_uuid": "cc5d0d76-687e-40a7-81cf-75e0540d1787",
        "data": {
            "uuid": "2fb9efc0-95d3-463b-9042-e2cf2183a303",
            "completions": [
              "answer"
            ],
            "relocated_call": "132456789.1",
            "initiator_call": "132456789.2",
            "recipient_call": "132456789.3",
            "initiator": "b459e3c9-b0a9-43a6-86ff-b4f7d00f6737",
        }
    }


.. _bus-user_created:

user_created
------------

The `user_created` event is published when a new user is created.

* routing key: `config.user.created`
* event specific data: a dictionary with 2 keys

  * id: the ID of the created user
  * uuid: the UUID of the created user

Example:

.. code-block:: javascript

    {
        "name": "user_created",
        "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
        "data": {
            "id": 42,
            "uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2"
        }
    }


.. _bus-user_deleted:

user_deleted
------------

The `user_deleted` event is published when a user is deleted.

* routing key: `config.user.deleted`
* event specific data: a dictionary with 2 keys

  * id: the ID of the deleted user
  * uuid: the UUID of the deleted user

Example:

.. code-block:: javascript

    {
        "name": "user_deleted",
        "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
        "data": {
            "id": 42,
            "uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2"
        }
    }


.. _bus-user_edited:

user_edited
-----------

The `user_edited` event is published when a user is modified.

* routing key: `config.user.edited`
* event specific data: a dictionary with 2 keys

  * id: the ID of the modified user
  * uuid: the UUID of the modified user

Example:

.. code-block:: javascript

    {
        "name": "user_edited",
        "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
        "data": {
            "id": 42,
            "uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2"
        }
    }


.. _bus-user_status_update:

user_status_update
------------------

The user_status_update is sent when a user changes his CTI presence using the Wazo Client.

* routing key: status.user
* required ACL: events.statuses.users
* event specific data: a dictionary with 3 keys

  * xivo_id: the uuid of the xivo
  * user_uuid: the user's UUID
  * status: a string identifying the status

Example::

   {
       "name": "user_status_update",
       "required_acl": "events.statuses.users",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "user_uuid": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2",
           "xivo_id": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
           "status": "busy"
       }
   }


.. _bus-users_forwards_forward_updated:

users_forwards_<forward_name>_updated
-------------------------------------

The users_forwards_<forward_name>_updated is sent when a user changes his forward using REST API.

* forward_name:

  * busy
  * noanswer
  * unconditional

* routing key: config.users.<user_uuid>.forwards.<forward_name>.updated
* required ACL: events.config.users.<user_uuid>.forwards.<forward_name>.updated
* event specific data: a dictionary with 3 keys

  * user_uuid: the user uuid
  * enabled: the state of the forward
  * destination: the destination of the forward

Example::

   {
       "name": "users_forwards_busy_updated",
       "required_acl": "events.config.users.a1223fe6-bff8-4fb6-a982-f9157dea5094.forwards.busy.updated",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "user_uuid": "a1223fe6-bff8-4fb6-a982-f9157dea5094",
           "enabled": true
           "destination": "1234"
       }
   }


.. _bus-users_services_service_updated:

users_services_<service_name>_updated
-------------------------------------

The users_services_<service_name>_updated is sent when a user changes his service using REST API.

* service_name:

  * dnd
  * incallfilter

* routing key: config.users.<user_uuid>.services.<service_name>.updated
* required ACL: events.config.users.<user_uuid>.services.<service_name>.updated
* event specific data: a dictionary with 2 keys

  * user_uuid: the user uuid
  * enabled: the state of the service

Example::

   {
       "name": "users_services_dnd_updated",
       "required_acl": "events.config.users.a1223fe6-bff8-4fb6-a982-f9157dea5094.services.dnd.updated",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "user_uuid": "a1223fe6-bff8-4fb6-a982-f9157dea5094",
           "enabled": true
       }
   }


.. _bus-service_registered_event:

service_registered_event
------------------------

The service_registered_event is sent when a service is started.

* routing key: service.registered.<service_name>
* event specific data: a dictionary with 5 keys

  * service_name: The name of the started service
  * service_id: The consul ID of the started service
  * address: The advertised address of the started service
  * port: The advertised port of the started service
  * tags: The advertised Consul tags of the started service

Example:

.. code-block:: javascript

    {
        "name": "service_registered_event",
        "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
        "data": {
            "service_name": "xivo-ctid",
            "service_id": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2",
            "address": "192.168.1.42",
            "port": 9495,
            "tags": ["xivo-ctid", "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", "Québec"]
        }
    }


.. _bus-service_deregistered_event:

service_deregistered_event
--------------------------

The service_deregistered_event is sent when a service is stopped.

* routing key: service.deregistered.<service_name>
* event specific data: a dictionary with 3 keys

  * service_name: The name of the stopped service
  * service_id: The consul ID of the stopped service
  * tags: The advertised Consul tags of the stopped service


Example:

.. code-block:: javascript

    {
        "name": "service_deregistered_event",
        "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
        "data": {
            "service_name": "xivo-ctid",
            "service_id": "8e58d2a7-cfed-4c2e-ac72-14e0b5c26dc2",
            "tags": ["xivo-ctid", "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", "Québec"]
        }
    }


user_voicemail_message_created
------------------------------

The events ``user_voicemail_message_created``, ``user_voicemail_message_updated``,
``user_voicemail_message_deleted`` are sent when a message is left, updated or deleted from a
voicemail. A distinct message is generated for each user associated to the voicemail: if the
voicemail is not associated to any user, no message is generated.

* routing key: voicemails.messages.created, voicemails.messages.updated, voicemails.messages.deleted
* required ACL: events.users.<user_uuid>.voicemails
* event specific data: a dictionary with the same fields as the REST API model of VoicemailMessage (See
  http://api.wazo.community, section xivo-ctid-ng)

Example::

   {
       "name": "user_voicemail_message_created",
       "required_acl": "events.users.8a709eb7-897f-4183-aa3b-ffa2a74e7e37.voicemails",
       "origin_uuid": "3b13295f-9f93-4c19-bd52-015a928a8a2a",
       "data": {
           "voicemail_id": 1,
           "message": {
               "timestamp": 1479226725,
               "caller_id_num": "1001",
               "caller_id_name": "Alice",
               "duration": 0,
               "folder": {
                   "type": "new",
                   "id": 1,
                   "name": "inbox"
               },
               "id": "1479226725-00000003"
           },
           "user_uuid": "8a709eb7-897f-4183-aa3b-ffa2a74e7e37",
           "message_id": "1479226725-00000003"
       }
   }
