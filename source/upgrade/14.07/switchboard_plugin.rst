*********************************************
Switchboard Phone Configuration Upgrade Notes
*********************************************

The xivo-aastra-switchboard and xivo-snom-switchboard plugins have been removed
and their functionalities are now provided by the generic xivo-aastra and xivo-snom
plugins respectively.

The upgrade is not done automatically, so please follow the `Upgrade Procedure`_
section below.

Although you are strongly advised to upgrade your switchboard phone configuration,
backwards compatibility with the old system will be maintained.

Note that if you need to install a switchboard for a previous version of XiVO, the old
xivo-aastra-switchboard and xivo-snom-switchboard plugins can be found in
:ref:`the archive repository <alternative-plugins-repo>`.


Upgrade Procedure
=================

The following upgrade procedure suppose that you are using an Aastra phone as your
switchboard phone. The same upgrade procedure apply for Snom phones, with
the only difference being the different plugin name.

#. Update the list of installable plugins.
#. Install the latest xivo-aastra plugin, or upgrade it to the latest version if it is already installed.
#. Install the needed language files and firmware files.
#. For each phone used for the switchboard, :ref:`change the plugin and activate the switchboard option <switchboard_device_option>`:

   * Select the generic xivo-aastra plugin.
   * Check the "switchboard" checkbox.
   * Synchronize the phone.
#. Once this is completed, you can uninstall the xivo-aastra-switchboard plugin.
