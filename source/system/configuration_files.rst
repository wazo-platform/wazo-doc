*******************
Configuration Files
*******************

This section describes some of the XiVO configuration files.


xivo_ring.conf
==============

* Path: :file:`/etc/pf-xivo/asterisk/xivo_ring.conf`
* Purpose: This file can be used to change the ringtone played by the phone depending on the 
  origin of the call.

.. warning:: Note that this feature has not been tested for all phones and all call flows.
  This page describes how you can customize this file but does not intend to list all validated
  call flows or phones.
  

This file :file:`xivo_ring.conf` consists of :

* profiles of configuration (some examples for different brands are already included: ``[aastra]``,
  ``[snom]`` etc.)
* one section named ``[number]`` where you apply the profile to an extension or a context etc.

Here is the process you should follow if you want to use/customize this feature :

#. Create a new profile, e.g.::
  
    [myprofile-aastra]

#. Change the ``phonetype`` accordingly, in our example::

    [myprofile-aastra]
    phonetype = aastra

#. Chose the ringtone for the different type of calls (note that the ringtone names are 
   brand-specific)::

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


ipbx.ini
==============

* Path: :file:`/etc/pf-xivo/xivo-web-interface/ipbx.ini`
* Purpose: This file specifies various configuration options and paths related 
  to Asterisk and used by the web interface.

Here is a partial glimpse of what can be configured in file :file:`ipbx.ini` :

#. Enable/Disable modification of SIP line username and password::

      [user]
      readonly-idpwd = "true"

  When editing a SIP line, the username and password fields cannot be modified 
  via the web interface. Set this option to false to enable the modification of 
  both fields. This option is set to "true" by default.

.. warning:: This feature is not fully tested. It should be used only when 
  absolutely necessary and with great care.


