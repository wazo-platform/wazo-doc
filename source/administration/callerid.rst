================
CallerID in Wazo
================

The CallerID is what users see on their phones when they emit or receive a call, e.g. ``Rick Sanchez 963-555-9296``.

The CallerID is composed of two parts: the CallerID name and the CallerID number.

In Wazo, the format is: ``"Rick Sanchez" <9635559296>``.


CallerID for internal calls
---------------------------

Users calling each other will see the CallerID configured in the `Caller ID` field of each user.


CallerID for outgoing calls (through a trunk)
---------------------------------------------

There are multiple settings coming into play:

* The calling user's `Outgoing Caller ID`
* The outgoing call's `Callerid` (one for each `Exten`)

The current logic for outgoing calls is:

* If the call is not emitted by a user: use the outgoing call's CallerID
* If the call is emitted by a user:

  * If the `Outgoing Caller ID` is Default, use the outgoing call's CallerID
  * If the `Outgoing Caller ID` is Anonymous, remove the CallerID
  * If the `Outgoing Caller ID` is set, use it


CallerID for incoming calls (from a trunk)
------------------------------------------

There are multiple settings coming into play, in order of priority:

#. SIP trusting remote-party CallerID
#. The trunk's `CallerID`
#. CallerID number normalization
#. The Incoming Call's `CallerID mode`
#. Reverse lookup


SIP CallerID
^^^^^^^^^^^^

To accept the CallerID sent via all SIP trunks, enable the option :menuselection:`Services --> IPBX
--> General settings --> SIP Protocol --> Default`:

    * Trust the Remote-Party-ID: yes

This option may also be enabled on specific SIP trunks, instead of globally.


Trunk CallerID
^^^^^^^^^^^^^^
    
The trunk's `CallerID` option overwrites the incoming CallerID. Usually, this options is left blank
to leave the incoming CallerID untouched.


CallerID number normalization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`callerid_num_normalization` for details.


Incoming Call CallerID
^^^^^^^^^^^^^^^^^^^^^^

The Incoming Call's `CallerID mode` can prepend, append or overwrite the incoming CallerID.


Reverse Lookup
^^^^^^^^^^^^^^

Reverse lookup is the operation of finding the CallerID name from the CallerID number. Wazo can lookup this information in multiple sources, see :ref:`directories` for more details.

This operation is only triggered when the incoming CallerID has no CallerID name or when the CallerID name equals the CallerID number.
