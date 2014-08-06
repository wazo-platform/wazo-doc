*************************
DAHDI 2.9.2 Upgrade Notes
*************************

These notes only apply to:

* Digium TE133/TE131 cards that are in firmware version 780017 or earlier
* Digium TE435/TE235 cards that are in firmware version e0017 or ealier

.. warning::

   The system will need to be power cycled after the upgrade. Your cards will not be usable until then.


After the upgrade
=================

First, you need to install the latest firmware for your TE133/TE131 or TE435/TE235 cards::

   xivo-fetchfw install digium-te133
   xivo-fetchfw install digium-te435

Then stop all the services and reload the DAHDI modules. Reloading the DAHDI module might take up to 30 seconds::

   xivo-service stop
   service dahdi stop
   service dahdi start

Following this manipulation, you should see something similar at the end of the :file:`/var/log/messages` file::

   dahdi: Telephony Interface Unloaded
   dahdi: Version: 2.9.2
   dahdi: Telephony Interface Registered on major 196
   wcte13xp 0000:03:0c.0: Firmware version 780017 is running, but we require version 780019.
   wcte13xp 0000:03:0c.0: firmware: agent loaded dahdi-fw-te133.bin into memory
   wcte13xp 0000:03:0c.0: Found dahdi-fw-te133.bin (version: 780019) Preparing for flash
   wcte13xp 0000:03:0c.0: Uploading dahdi-fw-te133.bin. This can take up to 30 seconds.
   wcte13xp 0000:03:0c.0: Delaying reset. Firmware load requires a power cycle
   wcte13xp 0000:03:0c.0: Running firmware version: 780017
   wcte13xp 0000:03:0c.0: Loaded firmware version: 780019 (Will load after next power cycle)
   wcte13xp 0000:03:0c.0: FALC version: 5
   wcte13xp 0000:03:0c.0: Setting up global serial parameters for T1
   wcte13xp 0000:03:0c.0: VPM450: firmware dahdi-fw-oct6114-032.bin not available from userspace

For the firmware update to complete, you **must halt** the machine (a reboot won't be enough) before restarting it.
