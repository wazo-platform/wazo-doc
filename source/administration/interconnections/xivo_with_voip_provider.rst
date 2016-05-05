.. index:: interconnections

**************************************
Interconnect a XiVO to a VoIP provider
**************************************

When you want to send and receive calls to the global telephony network, one
option is to subscribe to a VoIP provider. To receive calls, your XiVO needs to
tell your provider that it is ready and to which IP the calls must be sent. To
send calls, your XiVO needs to authenticate itself, so that the provider knows
that your XiVO is authorized to send calls and whose account must be credited
with the call fare.

The steps to configure the interconnections are:

* Establish the trunk between the two XiVO, that is the SIP connection
  between the two servers
* Configure outgoing calls on the server(s) used to emit calls
* Configure incoming calls on the server(s) used to receive calls


Establish the trunk
-------------------

You need the following information from your provider:

* a username
* a password
* the name of the provider VoIP server
* a public phone number

On your XiVO, go on page :menuselection:`Services --> IPBX --> Trunk management -->
SIP Protocol`, and create a SIP/IAX trunk::

    Name : provider_username
    Username: provider_username
    Password: provider_password
    Connection type: Peer
    IP addressing type: voip.provider.example.com
    Context: Incalls (or another incoming call context)

Register tab::

    Register: checked
    Transport: udp
    Name: provider_username
    Username: provider_username
    Password: provider_password
    Remote server: voip.provider.example.com

.. note::

   For the moment, Name and Username need to be the same value.

If your XiVO is behind a NAT device or a firewall, you should set the
following::

    Monitoring: 2000 milliseconds

This option will make Asterisk send a signal to the VoIP provider server every 2
seconds, so that NATs and firewall know the connection is still alive.

At that point, the Asterisk command ``sip show registry`` should print a line
showing that you are registered, meaning your trunk is established.


.. _voip_provider_outcall:

Set the outgoing calls
----------------------

The outgoing calls configuration will allow XiVO to know which extensions will
be called through the trunk.

Go on the page :menuselection:`Services --> IPBX --> Call management -->
Outgoing calls` and add an outgoing call.

Tab General::

   Trunks: provider_username

Tab Exten::

    Exten: 418. (note the period at the end)

This will tell XiVO: if an internal user dials a number beginning with ``418``,
then try to dial it on the trunk ``provider_username``.

The most useful special characters to match extensions are::

   . (period): will match one or more characters
   X: will match only one character

You can find more details about pattern matching in Asterisk (hence in XiVO) on
`the Asterisk wiki <https://wiki.asterisk.org/wiki/display/AST/Pattern+Matching>`_.


.. _voip_provider_incall:

Set the incoming calls
----------------------

Now that we have calls going out, we need to route incoming calls.

To route an incoming call to the right destination in the right context, we will
create an incoming call in :menuselection:`Services --> IPBX --> Call management
--> Incoming calls`.

Tab General::

    DID: your_public_phone_number
    Context: Incalls (the same than configured in the trunk)
    Destination: User
    Redirect to: the_front_desk_guy

This will tell XiVO: if you receive an incoming call to the public phone number
in the context ``Incalls``, then route it to the user
``the_front_desk_guy``. The destination context will be found automatically,
depending on the context of the line of the given user.
