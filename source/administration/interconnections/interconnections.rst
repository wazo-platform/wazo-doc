Interconnections
================

.. toctree::
   :maxdepth: 1

   two_xivo
   xivo_with_voip_provider
   xivo_with_pbx


Create an interconnection
-------------------------

There are three types of interconnections :

* Customized
* SIP
* IAX

Customized interconnection
^^^^^^^^^^^^^^^^^^^^^^^^^^

Add an interconnection to the menu :menuselection:`Services --> IPBX --> Trunk management --> Customized` ::

     Name : interconnection name
     Interface : dahdi/g0
     Context : outgoing call (to-extern) 


.. figure:: images/interco_t2.png
   :scale: 85%


Debug
-----

Interesting Asterisk commands: ::

    sip show peers
    sip show registry
    sip set debug on

Caller ID
---------

When setting up an interconnection with the public network or another PBX, it is possible to set a
caller ID in different places. Each way to configure a caller ID has it's own use case.

The format for a caller ID is the following ``"My Name" <9999>`` If you don't set the number part of
the caller ID, the dialplan's number will be used instead. This might not be a good option in most
cases.


Outgoing call caller ID
-----------------------

When you create an outgoing call, it's possible to set the it to internal, using the check box in
the outgoing call configuration menu. When this option is activated, the caller's caller ID will be
forwarded to the trunk. This option is use full when the other side of the trunk can reach the user
with it's caller ID number.

.. figure:: images/outgoing_call_internal.png
   :scale: 85%

When the caller's caller ID is not usable to the called party, the outgoing call's caller id can
be fixed to a given value that is more use full to the outside world. Giving the public number here
might be a good idea.

.. figure:: images/outgoing_call_callerid.png
   :scale: 85%

A user can also have a forced caller ID for outgoing calls. This can be use full for someone who has
his own public number. This option can be set in the user's configuration page. The Outgoing
Caller ID id option must be set to Customize. The user can also set his outgoing caller ID to
anonymous.

.. figure:: images/user_custom_callerid.png
   :scale: 85%

The order of precedence when setting the caller ID in multiple place is the following.

#. Internal
#. User's outgoing caller ID
#. Outgoing call
#. Default caller ID
