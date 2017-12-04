.. _wazo-webhookd:

=============
wazo-webhookd
=============

wazo-webhookd is the microservice responsible for webhooks: it manages the list of webhooks and
triggers them when an event occurs.


How to add a new webhookd type (a.k.a service)
==============================================

Here is an example of a webhook type that does nothing. Actually, it is very busy and sleeps for N seconds ``:)`` You may of course change this behaviour for something more suited to your needs.

Files::

  setup.py
  example_service/plugin.py

``setup.py``:

.. code-block:: python

    from setuptools import setup
    from setuptools import find_packages

    setup(
        name='wazo-webhookd-service-example',
        version='1.0',
        packages=find_packages(),
        entry_points={
        'wazo_webhookd.services': [
                # * "example" is the name of the service.
                #   It will be used when creating a subscription.
                # * "example_service" is the name of the directory above,
                #   the one that contains plugin.py
                # * "plugin" is the name of the above file "plugin.py"
                # * "Service" is the name of the class shown below
                'example = example_service.plugin:Service',
            ]
        }
    )

``example_service/plugin.py``:

.. code-block:: python

    import time

    class Service:

        def load(self, dependencies):
            celery_app = dependencies['celery']

            @celery_app.task
            def example_callback(options, event):
                '''
                * "options" contains the options configured by the subscription,
                  e.g. for http: the url, the method, the body, etc.
                * "event" contains the Wazo event that triggered the webhook.
                  "event" is of the form:
                  {
                      "name": "user_created",
                      "origin_uuid": "the UUID of the Wazo server that sent the event",
                      "data": {
                        "id": 12,  # the ID of the user that was created
                      }
                  }
                '''
                tired = options['sleep_time']
                time.sleep(tired)

            self._callback = example_callback

        def callback(self):
            return self._callback


To install this Python plugin, run::

    python setup.py install

Once installed, you may create subscriptions with the type ``example``::

  POST /subscriptions
  {
    "name": "Example webhook",
    "service": "example",
    "config": {
      "time_sleep": 10
    },
    "events": ["user_created"],
  }
