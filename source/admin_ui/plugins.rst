*******
Plugins
*******

Wazo plugins can be installed from AdminUI in the plugin menu. Features can be installed here
to customize your Wazo installation.

.. figure:: images/plugins.png

Official plugins are developped by the Wazo development team, are tested and should not break
during an upgrade. None official plugins are developped by the comunity are are available in
the market for your convenience.  The default is to show only official plugins.

Installing plugins
==================

To install a plugin click on it's install button. This will install the plugin as well as all
of its dependencies. This process is done in background, meaning that the web interface will
not wait for the plugin installation to complete before being available to do other actions.


Upgrading plugins
=================

When a plugin is installed on you system and a new version of that plugin is available, an upgrade
button will be available to show you that the plugin can be upgraded.

.. figure:: images/plugin_upgrade.png


Dependencies
------------

Dependencies are not upgraded when upgrading a plugin.

For example, if the plugin user depends on the extension plugin and a newer version
of both plugins are available on the market, upgrading user will only upgrade user
since its extension dependency is already satisfied.

=================== ================== ===================
Before              Market             After
=================== ================== ===================
user(1.0.1-1)       user(1.2.0-0)      user(1.2.0-0)
extension(1.5.42-0) extension(2.0.0-4) extension(1.5.42-0)
=================== ================== ===================


Removing plugins
================

To remove a plugin simply click the "Remove" button. This will remove the plugin and
any other plugin depending on it.

For example, removing "extension" will remove "user" since user depends on extension.
