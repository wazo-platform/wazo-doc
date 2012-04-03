****************
Remote directory
****************

If you have a phone provisioned with XiVO and its one of the supported ones, you'll be able to search in your XiVO directory and place call directly
from your phone.


Supported devices
=================

Tested

* Aastra 6700 series using the **3.2** or later firmware (does not work on firmware 2.6)

Untested

* Cisco SPA series (SPA500 and SPA900)
* Snom
* Thomson
* Yealink


Configuration
=============

For the remote directory to work on your phones, the first thing to do is to go to the
:menuselection:`Services --> IPBX --> (General settings) Phonebook` page.

You then have to add the range of IP addresses that will be allowed to access the directory.
So if you know that your phone's IP addresses are all in the 192.168.1.0/24 subnet, just
click on the small "+" icon and enter "192.168.1.0/24", then save.

Once this is done, on your phone, just click on the "remote directory" function key and
you'll be able to do a search in the XiVO directory from it.
