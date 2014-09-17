Voice Compression Card configuration
====================================

Here's how to install a Digium TC400M card (used for G.729a and/or G.723.1 codecs) :

* Verify that the ``wctc4xxp`` module is uncommented in :file:`/etc/dahdi/modules`.
  If it wasn't, do again the step :ref:`load_dahdi_modules`.

* install the card firmware::

    xivo-fetchfw install digium-tc400m

* comment out the following line in :file:`/etc/asterisk/modules.conf`::

    noload = codec_dahdi.so

* restart asterisk::

    /etc/init.d/asterisk restart

* depending on the codec you want to transcode, you can modify the ``mode`` parameter of the module by
  creating a file in :file:`/etc/modprobe.d/`. This parameter can take the following value :

 * mode = mixed : this the default value which activates transcoding for 92 channels
   in G.729a or G.723.1 (5.3 Kbit and 6.3 Kbit)
 * mode = g729 : this option activates transcoding for 120 channels in G.729a
 * mode = g723 : this option activates transcoding for 92 channels in G.723.1 (5.3 Kbit et 6.3 Kbit)

Example::

   cat << EOF > /etc/modprobe.d/xivo-transcode.conf
   options wctc4xxp mode=g729
   EOF

After having applied the configuration (see `Apply configuration`_ section) you can verify that the
card is correctly seen by asterisk with the ``transcoder show`` CLI command - this command should show
the encoders/decoders registered by the TC400 card::

   *CLI> transcoder show
   0/0 encoders/decoders of 120 channels are in use.
