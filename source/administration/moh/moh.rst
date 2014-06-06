.. _moh:

*************
Music on hold
*************

The menu :menuselection:`Services --> IPBX --> IPBX services --> On-hold Music` leads to the list of
available on-hold musics.


Categories
==========

Available categories are:

* files: play sound files. Formats supported:

  * G.719
  * G.723
  * G.726
  * G.729
  * GSM
  * H.263
  * H.264
  * iLBC
  * Ogg Vorbis
  * PCM
  * Siren14
  * Siren7
  * SLN
  * VOX
  * WAV (see :ref:`wav_files`)
  * WAV GSM

  See :code:`asterisk -rx 'module show like format'`.
  The on-hold music will always play from the start.

* mp3: play MP3 files.

  The on-hold music will play from an arbitrary position on the track, it will not play from the start.

* custom: do not play sound files. Instead, run an external process. That process must send on
  stdout the same binary format than WAV files.

  Example process: :code:`/usr/bin/mpg123 -s --mono -y -f 8192 -r 8000 http://streaming.example.com/stream.mp3`

.. note:: Processes run by custom categories are started as soon as the category is created and will
          only stop when the category is deleted. This means that on-hold music fed from online
          streaming will constantly be receiving network traffic, even when there are no calls.
