*******************************
Asterisk 11 to 13 Upgrade Notes
*******************************

You might be impacted by the upgrade to asterisk 13 if you have:

* custom dialplan
* custom asterisk configuration
* custom application using AGI, AMI or any other asterisk interface
* custom application exploiting CEL or queue_log
* custom asterisk modules (e.g. codec_g729a.so)
* customized asterisk in some other way

If you find yourself in one of these cases, you should make sure that your customizations still work
with asterisk 13.

If you are upgrading from asterisk 1.8, you should also check the :ref:`asterisk 1.8 to 11 upgrade notes
<asterisk-1.8-to-11>`.


List of Known Bugs And Limitations
==================================

List of known bugs and limitations that comes with the upgrade to asterisk 13:

* when direct media is active and DTMF are sent using SIP INFO, features code (e.g. \*0 to hangup)
  are not working properly
* when using SCCP phones, the connected line information on the phones are not updated after a
  transfer

These bugs and limitations will eventually be fixed.


Changes Between Asterisk 11 and 13
==================================

Table of asterisk modules that were available in the asterisk 11 package but that are not available
anymore in the asterisk 13 package:

+---------------------+-----------------------------------------+-----------------+-----------------+--------------------+
| Name                | Description                             | Loaded in AST11 | Asterisk Status | Replaced By        |
+=====================+=========================================+=================+=================+====================+
| app_parkandannounce | Call Parking and Announce Application   | Yes             | Removed         | res_parking        |
+---------------------+-----------------------------------------+-----------------+-----------------+--------------------+
| bridge_multiplexed  | Multiplexed two channel bridging module | Yes             | Removed         | bridge_*           |
+---------------------+-----------------------------------------+-----------------+-----------------+--------------------+
| chan_agent          | Agent Proxy Channel                     | Yes             | Removed         | app_agent_pool     |
+---------------------+-----------------------------------------+-----------------+-----------------+--------------------+
| chan_bridge         | Bridge Interaction Channel              | Yes             | Removed         | app_confbridge     |
+---------------------+-----------------------------------------+-----------------+-----------------+--------------------+
| chan_local          | Local Proxy Channel                     | Yes             | Removed         | system core        |
+---------------------+-----------------------------------------+-----------------+-----------------+--------------------+

Local channels are always available in asterisk 13 since they are now part of the system core.


External Links
--------------

* https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+12
* https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+13
* http://git.asterisk.org/gitweb/?p=asterisk/asterisk.git;a=blob;f=CHANGES;h=d0363f7c3b03cec5f71b3806535c4f9d2b2baa02;hb=refs/heads/13
