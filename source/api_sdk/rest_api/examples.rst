.. _rest-api-examples:

*****************
REST API Examples
*****************

CURL Examples (xivo-confd)
==========================

::

   # Get the list of users
   curl --insecure \
   -H 'Accept: application/json' \
   -H 'X-Auth-Token: 17496bfa-4653-9d9d-92aa-17def0fa9826' \
   https://xivo:9486/1.1/users

   # Create a user
   # When sending data, you need the Content-Type header.
   curl --insecure \
   -X POST \
   -d '{"firstname": "hello-world"} \
   -H 'Accept: application/json' \
   -H 'Content-Type: application/json' \
   -H 'X-Auth-Token: 17496bfa-4653-9d9d-92aa-17def0fa9826' \
   https://xivo:9486/1.1/users


Create a user with a phone and a voicemail (xivo-confd)
=======================================================

.. figure:: images/rest-api-example-user-voicemail.png

1. Create a line::

    POST /lines/sip
    {
      "context": "default"
    }

   Response::

    {
      "id": 11
      ...
    }

2. Create an extension::

    POST /extensions
    {
      "exten": "1234",
      "context": "default"
    }

   Response::

    {
      "id": 22
      ...
    }

3. Associate the line-extension::

    PUT /lines/11/extensions/22

4. Create a user::

    POST /users
    {
      "firstname": "Alice"
    }

   Response::

    {
      "uuid": "44444444-4444-4444-4444-444444444444"
      ...
    }

5. Associate the user-line::

    PUT /users/44444444-4444-4444-4444-444444444444/lines/11

6. Create the SIP endpoint::

    POST /endpoints/sip
    {
    }

   Response::

    {
      "id": 66
      ...
    }

7. Associate the line-endpoint::

    PUT /lines/11/endpoints/sip/66

8. Create the device. This is usually done automatically when the device is plugged in and put in
   autoprov mode. However, you need to get the device ID::

    GET /devices?search=88:88:88:88:88:88  or  GET /devices?search=192.168.88.88
    {
      "id": "88888888888888888888888888888888",
      ...
    }

9. Associate the line-device::

    PUT /lines/11/devices/88888888888888888888888888888888

   You may also want to re-synchronize the device::

    PUT /devices/88888888888888888888888888888888/synchronize

10. Create the voicemail::

     POST /voicemails
     {
       "name": "Alice's voicemail",
       "number": "1234"
       "context": "default"
     }

    Response::

     {
       "id": 1010
       ...
     }

11. Associate the user-voicemail::

     PUT /users/44444444-4444-4444-4444-444444444444/voicemails/1010
