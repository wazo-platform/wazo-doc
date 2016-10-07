.. _asterisk-13-to-14:

*******************************
Asterisk 13 to 14 Upgrade Notes
*******************************

You might be impacted by the upgrade to Asterisk 14 if you have:

* custom dialplan
* custom Asterisk configuration
* custom application using AMI or ARI
* custom Asterisk modules (e.g. codec_g729a.so)
* customized Asterisk in some other way

If you find yourself in one of these cases, you should make sure that your customizations still work
with Asterisk 14.

If you are upgrading from Asterisk 11, you should also check the :ref:`Asterisk 11 to 13 upgrade notes
<asterisk-11-to-13>`.


Changes Between Asterisk 13 and 14
==================================

Some of the more common changes to look for:

* AMI: The Command action now sends the output from the CLI command as a series of Output headers
  for each line instead of as a block of text with the ``--END COMMAND--`` delimiter to match the
  output from other actions.

You can see the complete list of changes from the Asterisk website:

* https://wiki.asterisk.org/wiki/display/AST/Upgrading+to+Asterisk+14
* https://github.com/asterisk/asterisk/blob/14/CHANGES

The AGI protocol did not change between Asterisk 13 and Asterisk 14; if you have custom AGI
applications, you only need to make sure that the dialplan applications and functions you are using
from the AGI are still valid.
