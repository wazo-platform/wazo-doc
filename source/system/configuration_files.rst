*******************
Configuration Files
*******************

This section describes some of the configuration files present in XiVO.


xivo_ring.conf
==============

File :file:`/etc/pf-xivo/asterisk/xivo_ring.conf`.

This file can be used to change the ringtone used by the phone depending on the 
origin of the call.

.. warning:: Note that this features has not been tested for all phones and all call flows.
  This page describes how you can customize this file but does not intend to 

This file consists of :

* profiles of configuration (profiles examples by brands are already included (``[aastra]``,
  ``[snom]`` etc.))
* one section named ``[number]`` where you apply the profile to an extension or a context etc.

Here is the process you should follow if you want to use/customize this feature :

#. Create a new profile, e.g.::
  
    [myprofile-aastra]

#. Change the phonetype accordingly, in our example::

    [myprofile-aastra]
    phonetype = aastra

#. Chose the ringtone for the different type of calls (note that the ringtone names is brand
   specific)::

    [myprofile-aastra]
    phonetype = aastra
    intern = <Bellcore-dr1>
    group = <Bellcore-dr2>

#. Apply your profile, in the section ``[number]``

  * to a given list of extensions (e.g. 1001 and 1002)::
  
      1001@default = myprofile-aastra
      1002@default = myprofile-aastra

  * or to a whole context (e.g. default)::
  
     @default = myprofile-aastra

5. Restart ``xivo-agid`` service::

    service xivo-agid restart
