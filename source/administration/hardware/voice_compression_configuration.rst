************************************
Voice Compression Card configuration
************************************

Verifications
=============

Verify that the ``wctc4xxp`` module is uncommented in :file:`/etc/dahdi/modules`.

If it wasn't, do again the step :ref:`load_dahdi_modules`.

Configure
=========

To configure the card you have to:

#. Install the card firmware::

    xivo-fetchfw install digium-tc400m

#. Comment out the following line in :file:`/etc/asterisk/modules.conf`::

    noload = codec_dahdi.so

#. Restart asterisk::

    service asterisk restart


Next step
=========

Now that you have configured your Voice Compression card:

#. you must check if you need to follow one of the :ref:`vc_card_specific_conf` sections below,
#. then, if you have another type of card to configure, you can go back to the :ref:`configure your card <card_configuration>` section.


.. _vc_card_specific_conf:

Specific configuration
======================


Select the transcoding mode
---------------------------

The Digium TC400 card can be used to transcode:

* 120 G.729a channels,
* 92 G.723.1 channels,
* or 92 G.729a/G.723.1 channels.

Depending on the codec you want to transcode, you can modify the ``mode`` parameter which can take the following value:

* mode = mixed : this the default value which activates transcoding for 92 channels
  in G.729a or G.723.1 (5.3 Kbit and 6.3 Kbit)
* mode = g729 : this option activates transcoding for 120 channels in G.729a
* mode = g723 : this option activates transcoding for 92 channels in G.723.1 (5.3 Kbit et 6.3 Kbit)

#. Create the file :file:`/etc/modprobe.d/xivo-transcode.conf`::

    touch /etc/modprobe.d/xivo-transcode.conf

#. And insert the following lines::

    options wctc4xxp mode=g729

#. Apply the configuration by restarting the services::

    xivo-service restart

#. Verify that the card is correctly seen by asterisk with the ``transcoder show`` CLI command
   - this command should show the encoders/decoders registered by the TC400 card::

    *CLI> transcoder show
    0/0 encoders/decoders of 120 channels are in use.
