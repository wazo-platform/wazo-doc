.. _message-bus:

***********
Message Bus
***********

The message bus is used to receive events from XiVO. It is provided by
an `AMQP <http://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol>`_ 0-9-1
broker (namely, `RabbitMQ <http://previous.rabbitmq.com/v2_8_x/documentation.html>`_)
that is integrated in XiVO.

.. warning:: Interaction with the bus is presently experimental and
   some things might change in the next XiVO versions.


Usage
=====

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

* routing key: calls.call.created, calls.call.updated, call.call.ended
* required ACL: events.calls.<user_uuid>
* event specific data: a dictionary with the same fields as the REST API model of Call (See
  http://api.xivo.io, section xivo-ctid-ng)

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


.. _bus-chat_message_event:

chat_message_event
------------------

This message is used to send a chat message to a user

* routing key: chat.message.<xivo-uuid>.<user_id>
* event specific data:

  * alice: The nickname of the chatter
  * to: The destination's XiVO UUID and user UUID
  * from: The chatter's XiVO UUID and user UUID
  * msg: The message

Example:

.. code-block:: javascript

  {
      "name": "chat_message_event",
      "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
      "data": {
          "alias": "Alice"
          "to": ["ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", "fcb36731-c50a-453e-92c7-571297d41616"],
          "from": ["ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", "4f2e2249-ae2b-4bc2-b5fc-ad42ee01ddaf"],
          "msg": "Hi!"
      }
  }


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


.. _bus-user_status_update:

user_status_update
------------------

The user_status_update is sent when a user changes his CTI presence using the XiVO client.

* routing key: status.user
* required ACL: events.statuses.users
* event specific data: a dictionary with 3 keys

  * xivo_id: the uuid of the xivo
  * user_id: an integer corresponding to the user ID of the user who changed its status
  * status: a string identifying the status

Example::

   {
       "name": "user_status_update",
       "required_acl": "events.statuses.users",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "user_id": 42,
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
