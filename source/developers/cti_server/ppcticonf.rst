*********
ppcticonf
*********

`ppcticonf` is a small utility used to pretty print the CTI server configuration.

The utility is installed by default with XiVO. It comes with the pf-xivo-utils package.

In fact, `ppcticonf` can be used to pretty print any URL or file that contains a JSON document.

How-to
======

The simplest invocation is:

.. code-block:: javascript

   $ ppcticonf
   {
       "agentstatus": [], 
       "bench": 0.077938079833984, 
       "certfile": "/var/lib/pf-xivo/certificates/test2.crt", 
       "channelstatus": [], 
       "contexts": {
           "*": {
               "didextens": {
                   "*": [
                       "xivodir"
                   ]
               }
           }, 
           "default": {
               "directories": [
                   "xivodir", 
                   "internal"
               ], 
               "display": "Display"
           }
      },
    ......
   }

You can also pass a URL as an argument:


.. code-block:: javascript

   $ ppcticonf http://127.0.0.1/service/ipbx/json.php/private/pbx_settings/users
   [
       {
           "agentid": null, 
           "bsfilter": "no", 
           "callerid": "\"User 2\"", 
           "callrecord": false, 
           "commented": false, 
           "description": "", 
           "destbusy": "", 
           "destrna": "", 
           "destunc": "", 
           "enableautomon": false, 
           "enablebusy": false, 
           "enableclient": true, 
           "enablednd": false, 
           "enablehint": true, 
           "enablerna": false, 
           "enableunc": false, 
           "enablevoicemail": false, 
           "enablexfer": false, 
           "entityid": 1, 
           "firstname": "User", 
           "fullname": "User 2", 
           "id": 2, 
           "identity": "User 2", 
           "incallfilter": false,
    .....
   ]

Alternatively, you can pass a file path as an argument:



.. code-block:: javascript

   $ curl -s https://localhost/service/ipbx/json.php/private/ctiserver/configuration > cticonf
   $ ppcticonf cticonf 
   {
       "agentstatus": [], 
       "bench": 0.078904151916504003, 
       "certfile": "/var/lib/pf-xivo/certificates/test2.crt", 
       "channelstatus": [], 
       "contexts": {
           "*": {
               "didextens": {
                   "*": [
                       "xivodir"
                   ]
               }
           }, 
           "default": {
               "directories": [
                   "xivodir", 
                   "internal"
               ], 
               "display": "Display"
         }
   .....
   }

