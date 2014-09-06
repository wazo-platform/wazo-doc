.. _ethernet:

**********************
Ethernet configuration
**********************

Discover interfaces
===================

Query
-----

::

    GET /discover_netifaces

Example request
---------------

::

   GET /discover_netifaces HTTP/1.1
   Host: xivoserver
   Accept: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json
    {
       "lo":
       {
           "hwaddress": "00:00:00:00:00:00",
           "typeid": 24,
           "alias-raw-device": null,
           "network": "127.0.0.0",
           "family": "inet",
           "physicalif": false,
           "vlan-raw-device": null,
           "vlanif": false,
           "dummyif": false,
           "mtu": 65536,
           "broadcast": "127.255.255.255",
           "hwtypeid": 772,
           "netmask": "255.0.0.0",
           "carrier": true,
           "flags": 9,
           "address": "127.0.0.1",
           "vlan-id": null,
           "type": "loopback",
           "options": null,
           "aliasif": false,
           "name": "lo"
       },
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




Get interface
=============

Query
-----

::

    POST /netiface

Example request
---------------

::

    POST /netiface HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
        "iface":   ["lo", "eth0"]
    }


Get interface from dst
======================

Query
-----

::

    POST /netiface_from_dst_address

Example request
---------------

::

    POST /netiface_from_dst_address HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
        "address":   ["192.168.0.1", "172.16.1.1"]
    }

Get interface from src 
=======================

Query
-----

::

    POST /netiface_from_src_address

Example request
---------------

::

    POST /netiface_from_src_address HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
        "address":   ["192.168.0.1", "172.16.1.1"]
    }


Modify interface
================

Query
-----

::

    POST /modify_physical_eth_ipv4/<interface>

Example request
---------------

::

    POST /modify_physical_eth_ipv4/eth0 HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
        'method': 'dhcp',
        'auto':   True
    }

Replace virtual interface
=========================

Query
-----

::

    POST /replace_virtual_eth_ipv4/<virtual_interface>

Example request
---------------

::

    POST /replace_physical_eth_ipv4/eth0:0 HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
        'ifname': 'eth0:0',
        'method': 'dhcp',
        'auto': True
    }

Modify interface
================

Query
-----

::

    POST /modify_eth_ipv4/<interface>

Example request
---------------

::

    POST /modify_eth_ipv4/eth0 HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
        'address': '192.168.0.1',
        'netmask': '255.255.255.0',
        'broadcast': '192.168.0.255',
        'gateway': '192.168.0.254',
        'mtu': 1500,
        'auto': True,
        'up': True,
        'options': [['dns-search', 'toto.tld tutu.tld'],
                   ['dns-nameservers', '127.0.0.1 192.168.0.254']]i
    }

Change state
============

Query
-----

::

    POST /change_state_eth_ipv4/<interface>

Example request
---------------

::

    POST /change_state_eth_ipv4/eth0 HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
    {
    }

Delete interface ipv4
=====================

Query
-----

::

    GET /delete_eth_ipv4

Example request
---------------

::

    GET /delete_eth_ipv4/eth0 HTTP/1.1
    Host: xivoserver
    Content-Type: application/json
