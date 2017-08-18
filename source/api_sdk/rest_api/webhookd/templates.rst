.. _webhookd_templates:

****************************
wazo-webhookd HTTP templates
****************************

Templates use the Jinja2 syntax. See `the Jinja documentation for more details <http://jinja.pocoo.org/docs/2.9/templates/>`_.

Example
=======

Given a subscription::

   {
     "name": "Hello subscription",
     "service": "http",
     "events": [
       "hello"
     ],
     "config": {
       "content_type": "text/plain",
       "method": "POST",
       "url": "https://example.com/event_handler?v=1.0",
       "verify_certificate": "true",
       "body": "I just received an event named {{ event_name }}, from the Wazo server {{ wazo_uuid }}. The event contained the following data: hello = \"{{ event['hello'] }}\", bye = \"{{ event['bye'] }}\"."
     }
   }

When an event is emitted::

   {
     "name": "hello_event",
     "origin_uuid": "my-wazo",
     "data": {
       "hello": "world",
       "bye": "bye"
     }
   }

Then a HTTP request is sent to https://example.com::

   POST /event_handler?v=1.0
   Content-Type: text/plain
   
   I just received an event named hello_event, from the Wazo server my-wazo. The event contained the following data: hello = "world", bye = "bye".


Reference
=========

Available variables:

* ``event_name``: the name of the event.
* ``wazo_uuid``: the UUID of the Wazo server who sent the event.
* ``event``: the body of the event. Details may be accessed like: ``event['detail']``. Further nested details may be accessed like: ``event['detail']['subdetail']``.
