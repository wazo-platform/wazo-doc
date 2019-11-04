.. _ethernet:

**********************
Ethernet configuration
**********************

Get interface
=============

Query
-----

::

    GET /netiface/<interface>

Example request
---------------

::

    GET /netiface/eth0 HTTP/1.1
    Host: wazoserver
    Content-Type: application/json

Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json
    {
       "eth0":
       {
           "alias-raw-device": null,
           "family": "inet",
           "hwaddress": "36:76:70:29:69:c2",
           "vlan-id": null,
           "network": "172.17.0.0",
           "physicalif": false,
           "vlan-raw-device": null,
           "vlanif": false,
           "type": "eth",
           "aliasif": false,
           "broadcast": "172.17.255.255",
           "netmask": "255.255.0.0",
           "address": "172.17.0.101",
           "typeid": 6,
           "name": "eth0",
           "hwtypeid": 1,
           "dummyif": false,
           "mtu": 1500,
           "carrier": true,
           "flags": 3,
           "options": null
       }
    }
