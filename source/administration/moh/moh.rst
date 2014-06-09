.. _moh:

*************
Music on Hold
*************

The menu :menuselection:`Services --> IPBX --> IPBX services --> On-hold Music` leads to the list of
available on-hold musics.


Categories
==========

Available categories are:

* files: play sound files. Formats supported:

  +------------------+--------------------------------------------------------------------+
  | Format Name      | Filename Extension                                                 |
  +==================+====================================================================+
  | G.719            | .g719                                                              |
  +------------------+--------------------------------------------------------------------+
  | G.723            | .g723 .g723sf                                                      |
  +------------------+--------------------------------------------------------------------+
  | G.726            | .g726-40 .g726-32 .g726-24 .g726-16                                |
  +------------------+--------------------------------------------------------------------+
  | G.729            | .g729                                                              |
  +------------------+--------------------------------------------------------------------+
  | GSM              | .gsm                                                               |
  +------------------+--------------------------------------------------------------------+
  | iLBC             | .ilbc                                                              |
  +------------------+--------------------------------------------------------------------+
  | Ogg Vorbis       | .ogg                                                               |
  +------------------+--------------------------------------------------------------------+
  | G.711 A-law      | .alaw .al .alw                                                     |
  +------------------+--------------------------------------------------------------------+
  | G.711 μ-law      | .pcm .ulaw .ul .mu .ulw                                            |
  +------------------+--------------------------------------------------------------------+
  | G.722            | .g722                                                              |
  +------------------+--------------------------------------------------------------------+
  | Au               | .au                                                                |
  +------------------+--------------------------------------------------------------------+
  | Siren7           | .siren7                                                            |
  +------------------+--------------------------------------------------------------------+
  | Siren14          | .siren14                                                           |
  +------------------+--------------------------------------------------------------------+
  | SLN              | .raw .sln .sln12 .sln16 .sln24 .sln32 .sln44 .sln48 .sln96 .sln192 |
  +------------------+--------------------------------------------------------------------+
  | VOX              | .vox                                                               |
  +------------------+--------------------------------------------------------------------+
  | WAV              | .wav .wav16                                                        |
  +------------------+--------------------------------------------------------------------+
  | WAV GSM          | .WAV .wav49                                                        |
  +------------------+--------------------------------------------------------------------+

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
