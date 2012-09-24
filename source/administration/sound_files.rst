***********
Sound Files
***********

Add Sounds Files
================

On a fresh install, only en_US and fr_Fr sounds are installed. Canadian French and German are available too.

To install Canadian French sounds you have to execute the following command in the cli::

    root@xivo:~# apt-get install asterisk-sounds-wav-fr-ca xivo-sounds-fr-ca

To install German sounds you have to execute the following command in the cli::

    root@xivo:~# apt-get install asterisk-sounds-wav-de-de xivo-sounds-de-de

Now you may select the newly installed language for yours users.


Convert Your Wav File
=====================

Asterisk will read natively WAV files encoded in wav 8kHz, 16 bits, mono.

The following command will return the encoding format of the <file>

::

   $ file <file>
   RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz

The following command will re-encode the <input file> with the correct parameters for asterisk and write into the <output file>

::

   $ sox <input file> -b 16 -c 1 -r 8000 -t wavpcm <output file>
