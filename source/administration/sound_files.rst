Sound Files
***********

Asterisk will read natively WAV files encoded in wav 8kHz, 16 bits, mono.

The following command will return the encoding format of the <file>

::

   $ file <file>
   RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz

The following command will re-encode the <input file> with the correct parameters for asterisk and write into the <output file>

::

   $ sox <input file> -b 16 -c 1 -r 8000 -t wavpcm <output file>
