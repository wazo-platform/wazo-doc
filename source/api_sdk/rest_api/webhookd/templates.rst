.. _webhookd_templates:

****************************
wazo-webhookd HTTP templates
****************************

Templates use the Jinja2 syntax. See `the Jinja documentation for more details <http://jinja.pocoo.org/docs/2.9/templates/>`_.

Example
=======

Given a subscription:

.. figure:: images/template-subscription.png

When an event is emitted:

.. figure:: images/template-event.png

Then a HTTP request is sent to https://example.com:

.. figure:: images/template-request.png


Reference
=========

Available variables:

* ``event_name``: the name of the event.
* ``wazo_uuid``: the UUID of the Wazo server who sent the event.
* ``event``: the body of the event. Details may be accessed like: ``event['detail']``. Further nested details may be accessed like: ``event['detail']['subdetail']``.
