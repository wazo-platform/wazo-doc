.. index:: interconnections

******************************
Interconnect two Wazo directly
******************************

.. figure:: images/two_xivo.png
   :align: center

   Situation diagram

Interconnecting two Wazo will allow you to send and receive calls between the
users configured on both sides.

The steps to configure the interconnections are:

* Establish the trunk between the two Wazo, that is the SIP connection
  between the two servers
* Configure outgoing calls on the server(s) used to emit calls
* Configure incoming calls on the server(s) used to receive calls

For now, only SIP interconnections have been tested.


Establish the trunk
-------------------

The settings below allow a trunk to be used in both directions, so it doesn't
matter which server is A and which is B.

Consider Wazo A wants to establish a trunk with Wazo B.

On Wazo B, go on page :menuselection:`Services --> IPBX --> Trunk management -->
SIP Protocol`, and create a SIP trunk::

    Name : wazo-trunk
    Username: wazo-trunk
    Password: pass
    Connection type: Friend
    IP addressing type: Dynamic
    Context: <see below>

.. note::

   For the moment, Name and Username need to be the same string.

The ``Context`` field will determine which extensions will be reachable by the
other side of the trunk:

* If ``Context`` is set to ``default``, then every user, group, conf room,
  queue, etc. that have an extension if the ``default`` context will be
  reachable directly by the other end of the trunk. This setting can ease
  configuration if you manage both ends of the trunk.
* If you are establishing a trunk with a provider, you probably don't want
  everything to be available to everyone else, so you can set the ``Context``
  field to ``Incalls``. By default, there is no extension available in this
  context, so we will be able to configure which extension are reachable by the
  other end. This is the role of the incoming calls: making bridges from the
  ``Incalls`` context to other contexts.

On Wazo A, create the other end of the SIP trunk on the :menuselection:`Services
--> IPBX --> Trunk management --> SIP Protocol`::

    Name: wazo-trunk
    Username: wazo-trunk
    Password: pass
    Identified by: Friend
    Connection type: Static
    Address: <Wazo B IP address or hostname>
    Context: Incalls

Register tab::

    Register: checked
    Transport: udp
    Username: wazo-trunk
    Password: pass
    Remote server: <Wazo B IP address or hostname>


On both Wazo, activate some codecs, :menuselection:`Services
--> IPBX --> General Settings --> SIP protocol`, tab ``Signaling``::

   Enabled codecs: at least GSM (audio)

At that point, the Asterisk command ``sip show registry`` on Wazo B should print
a line showing that Wazo A is registered, meaning your trunk is established.


Set the outgoing calls
----------------------

The outgoing calls configuration will allow Wazo to know which extensions will
be called through the trunk.

On the call emitting server(s), go on the page :menuselection:`Services
--> IPBX --> Call management --> Outgoing calls` and add an outgoing call.

Tab General::

   Trunks: wazo-trunk

Tab Exten::

    Exten: **99. (note the period at the end)
    Stripnum: 4

This will tell Wazo: if any extension begins with ``**99``, then try to dial it
on the trunk ``wazo-trunk``, after removing the 4 first characters (the ``**99``
prefix).

The most useful special characters to match extensions are::

   . (period): will match one or more characters
   X: will match only one character

You can find more details about pattern matching in Asterisk (hence in Wazo) on
`the Asterisk wiki <https://wiki.asterisk.org/wiki/display/AST/Pattern+Matching>`_.


Set the incoming calls
----------------------

Now that we have calls going out from a Wazo, we need to route incoming calls on
the Wazo destination.

.. note::

   This step is only necessary if the trunk is linked to an Incoming calls
   context.

To route an incoming call to the right destination in the right context, we will
create an incoming call in :menuselection:`Services --> IPBX --> Call management
--> Incoming calls`.

Tab General::

    DID: 101
    Context: Incalls
    Destination: User
    Redirect to: someone

This will tell Wazo: if you receive an incoming call to the extension ``101`` in
the context ``Incalls``, then route it to the user ``someone``. The destination
context will be found automatically, depending on the context of the line of the
given user.

So, with the outgoing call set earlier on Wazo A, and with the incoming call
above set on Wazo B, a user on Wazo A will dial ``**99101``, and the user
``someone`` will ring on Wazo B.
