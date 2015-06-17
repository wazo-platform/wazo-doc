*******************************
Asterisk 11 to 13 Upgrade Notes
*******************************

If you have *not* customized your asterisk installation in one of the following way:

* custom dialplan
* custom asterisk configuration
* custom application using AGI or AMI
* custom application exploiting CEL or queue_log
* custom asterisk modules (e.g. codec_g729a.so)

then you can safely skip this section. Otherwise, it is your responsibility to make sure
every customization still works with asterisk 13. See the `External Links`_ for more information.

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


List of Known Bugs And Limitations
==================================

List of known bugs and limitations that were not in XiVO 15.11 and appeared following the upgrade to
asterisk 13:

* when direct media is active and DTMF are sent using SIP INFO, features code (e.g. \*0 to hangup)
  are not working properly
* when using SCCP phones, the connected line information on the phones are not updated after a
  transfer


External Links
==============

* https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+12
* https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+13
* http://git.asterisk.org/gitweb/?p=asterisk/asterisk.git;a=blob;f=CHANGES;h=d0363f7c3b03cec5f71b3806535c4f9d2b2baa02;hb=refs/heads/13
