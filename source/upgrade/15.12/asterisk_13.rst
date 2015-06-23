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

List of known bugs and limitations for asterisk 13:

* when direct media is active and DTMF are sent using SIP INFO, features code (e.g. \*0 to hangup)
  are not working properly
* when using SCCP phones, the connected line information on the phones are not updated after a
  transfer


Changes Between Asterisk 11 and 13
==================================

Some of the more common changes to look for:

* The SetMusicOnHold dialplan application was deprecated and has been removed. Users of the
  application should use the CHANNEL function's ``musicclass`` setting instead.
* The WaitMusicOnHold dialplan application was deprecated and has been removed. Users of the
  application should use MusicOnHold with a ``duration`` parameter instead.
* The SIPPEER dialplan function no longer supports using a colon as a delimiter for parameters. The
  parameters for the function should be delimited using a comma.
* The SIPCHANINFO dialplan function was deprecated and has been removed. Users of the function
  should use the CHANNEL function instead.
* For SIP, the codec preference order in an SDP during an offer is slightly different than
  previous releases.  Prior to Asterisk 13, the preference order of codecs used to be:

  #. Our preferred codec
  #. Our configured codecs
  #. Any non-audio joint codecs

  Now, in Asterisk 13, the preference order of codecs is:

  #. Our preferred codec
  #. Any joint codecs offered by the inbound offer
  #. All other codecs that are not the preferred codec and not a joint codec offered by the inbound
     offer
* Queue strategy ``rrmemory`` (Round robin memory) now has a predictable order. Members will be
  called in the order that they are added to the queue. For agents, this means they will be called
  in the order they are logged.

You can see the complete list of changes from the asterisk website:

* https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+12
* https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+13
* http://git.asterisk.org/gitweb/?p=asterisk/asterisk.git;a=blob;f=CHANGES;h=d0363f7c3b03cec5f71b3806535c4f9d2b2baa02;hb=refs/heads/13

The AGI protocol did not change between asterisk 11 and asterisk 13; if you have custom AGI
applications, you only need to make sure that the dialplan applications and functions you are using
from the AGI are still valid.
