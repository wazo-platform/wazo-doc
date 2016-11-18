*****************
REST API Examples
*****************

Examples (xivo-confd)
=====================

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
