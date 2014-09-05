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



Get interface from dst
======================

Query
-----

::

    GET /netiface_from_dst_address

Get interface from src 
=======================

Query
-----

::

    GET /netiface_from_src_address

Modify interface
================

Query
-----

::

    POST /modify_physical_eth_ipv4

Replace virtual interface
=========================

Query
-----

::

    POST /replace_virtual_eth_ipv4

Modify interface
================

Query
-----

::

    POST /modify_eth_ipv4

Change state
============

Query
-----

::

    POST /change_state_eth_ipv4

Delete interface ipv4
=====================

Query
-----

::

    GET /delete_eth_ipv4
