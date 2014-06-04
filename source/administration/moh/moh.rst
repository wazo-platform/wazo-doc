.. _moh:

*************
Music on hold
*************

The menu :menuselection:`Services --> IPBX --> IPBX services --> On-hold Music` leads to the list of
available on-hold musics.


Categories
==========

Available categories are:

* files: accept WAV files. See :ref:`wav_files`.
* mp3: accept MP3 files.
* custom: does not accept files. Instead, it runs an external process. That process must send on
  stdout the same binary format than WAV files.

.. note:: Processes run by custom categories are started as soon as the category is created and will
          only stop when the category is deleted. This means that on-hold music fed from online
          streaming will constantly be receiving network traffic, even when there are no calls.
