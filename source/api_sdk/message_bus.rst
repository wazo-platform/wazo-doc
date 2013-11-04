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
supported operation.

Otherwise, the default connection information is:

* Virtual host: /
* User name: guest
* User password: guest
* Port: 5672


Example
-------

Here's an example of a simple client, in python, listening for the
:ref:`bus-call_form_result` CTI events::

   #!/usr/bin/python

   import pika

   connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
   channel = connection.channel()

   result = channel.queue_declare(exclusive=True)
   queue_name = result.method.queue

   channel.queue_bind(exchange='xivo-cti', queue=queue_name, routing_key='call_form_result')

   def callback(ch, method, props, body):
       print 'Received:', body
       ch.basic_ack(delivery_tag=method.delivery_tag)

   channel.basic_consume(callback, queue=queue_name)
   channel.start_consuming()

If you are new to AMQP, you might want to look at the
`RabbitMQ tutorial <http://previous.rabbitmq.com/v2_8_x/getstarted.html>`_.


Notes
-----

Things to be aware when writing a client/consumer:

* The ``xivo-service stop`` command stops the AMQP broker. This means that the client
  connections to the AMQP broker will be lost on:

  * a XiVO upgrade
  * an asterisk crash
* The published messages are not persistant. When the AMQP broker stops, the messages
  that are still in queues will be lost.


Events
======

Events that are sent to the bus use a JSON serialization format. For example,
the CTI call_form_result event looks like this::

    {"name": "call_form_result", "data": {...}}

All events have the same basic structure, namely, a JSON object with two keys:

name
    A string representing the name of the event. Each event type has a unique name.

data
    The data specific part of the event. This is documented on a per event type; if not
    this is assumed to be null.


CTI
---

CTI related events are sent to the ``xivo-cti`` exchange, which is an exchange of type direct.

To subscribe to event with name X, you must create a binding between the exchange
and your queue with the binding/routing key X.


.. _bus-call_form_result:

call_form_result
^^^^^^^^^^^^^^^^

The call_form_result event is sent when a :ref:`custom call form <custom-call-form>`
is submitted by a CTI client.

* routing key: call_form_result
* event specific data: a dictionary with 2 keys:

  * user_id: an integer corresponding to the user ID of the client who saved the call form
  * variables: a dictionary holding the content of the form

Example::

   {
       "name": "call_form_result",
       "data": {
           "user_id": 40,
           "variables": {
               "firstname": "John",
               "lastname": "Doe"
           }
       }
   }
