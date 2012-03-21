.. index:: interconnections

*********************
Interconnect Two XiVO
*********************

.. figure:: images/two_xivo.png
   :align: center

   Situation diagram

Establish the trunk
-------------------

The settings below allow a trunk to be used in both directions.

Consider XiVO A wants to establish a trunk with XiVO B.

On XiVO B, create a SIP trunk: ::

    Name : xivo-trunk
    Username : xivo-trunk
    Password : pass
    Identified by : Username
    Connection type : Static
    Address : <XiVO A IP address>
    Context : Incalls
    Language : something

.. note::

   For the moment, Name and Username need to be the same string.

On XiVO A, create a SIP trunk: ::

    Name : xivo-trunk
    Username : xivo-trunk
    Password : pass
    Identified by : Username
    Connection type : Static
    Address : <XiVO B IP address>
    Context : Incalls
    Language : something

Register tab: ::

    Register : On
    Transport : UDP
    Username : xivo-b
    Password : xivo-b
    Remote server : <XiVO B IP address>



On both XiVO, activate some codecs, General Settings > SIP protocol, Signaling tab: ::

   Enabled codecs : at least GSM (audio)

Set the routes
^^^^^^^^^^^^^^

On XiVO A, Outgoing Calls: ::

   Trunks : xivo-trunk

Tab Exten: ::

    Exten : 0101
    Stripnum : 1

.. note::

   On XiVO B, you need a range of DID for Incalls context.

Incoming calls: ::

    DID : 101
    Context : Incalls
    Destination : User
    Redirect to : someone

.. note::

   Do the same with roles reversed to have a route in the other direction.

Call
^^^^

User A on XiVO A dials 0101 and rings someone on XiVO B.
