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

* The ``xivo-service stop`` command stops the AMQP broker. This means that the client
  connections to the AMQP broker will be lost on:

  * a XiVO upgrade
  * an asterisk crash
* The published messages are not persistent. When the AMQP broker stops, the messages
  that are still in queues will be lost.


Events
======

Events that are sent to the bus use a JSON serialization format. For example,
the CTI call_form_result event looks like this::

    {"name": "call_form_result",
     "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
     "data": {...}}

All events have the same basic structure, namely, a JSON object with three keys:

name
    A string representing the name of the event. Each event type has a unique name.

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
* event specific data: a dictionary with 3 keys:

  * agent_id: an integer corresponding to the agent ID of the agent who's status changed
  * status: a string identifying the status
  * xivo_id: the uuid of the xivo

Example::

   {
       "name": "agent_status_update",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "agent_id": 42,
           "xivo_id": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
           "status": "logged_in"
       }
   }

.. _bus-chat_message_event:

chat_message_event
------------------

This message is used to send a chat message to a user

* routing key: chat.message.<xivo-uuid>.<user_id>
* event specific data:

  * alice: The nickname of the chatter
  * to: The destination's XiVO UUID and user ID
  * from: The chatter's XiVO UUID and user ID
  * msg: The message

Example::

  {
      "name": "chat_message_event",
      "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
      "data": {
          "alias": "Alice"
          "to": ["ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", 42],
          "from": ["ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3", 22],
          "msg": "Hi!"
      }
  }

.. _bus-endpoint_status_update:

endpoint_status_update
----------------------

The endpoint_status_update is sent when an end point status changes. This information is
based on asterisk hints.

* routing key: status.endpoint
* event specific data: a dictionary with 3 keys

  * xivo_id: the uuid of the xivo
  * endpoint_id: an integer corresponding to the endpoint ID
  * status: an integer corresponding to the asterisk device state

Example::

   {
       "name": "endpoint_status_update",
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
* event specific data: a dictionary with 3 keys

  * xivo_id: the uuid of the xivo
  * user_id: an integer corresponding to the user ID of the user who changed its status
  * status: a string identifying the status

Example::

   {
       "name": "user_status_update",
       "origin_uuid": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
       "data": {
           "user_id": 42,
           "xivo_id": "ca7f87e9-c2c8-5fad-ba1b-c3140ebb9be3",
           "status": "busy"
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
