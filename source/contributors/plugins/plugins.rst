*******
Plugins
*******

This section cover the preferred way to extend the functionnalities of a
Wazo server. There are many extension point in Wazo, all of them can be used
in combination to add complete features to you favorite PBX.


What is a plugin
================

A plugin is a set of additions made to a custom Wazo installation to add a new
functionnality.


What can be done with a plugin
==============================

Wazo plugins allow a third party to add almost anything to Wazo. Most of our services
have extension points that can be used togeter to create a complete feature as a plugin.

Here's a non exaustive list of what can be done with plugins

* Add configuration files to wazo services in `/etc/*/conf.d/`
* Add configuration files and dialplan files to Asterisk
* Reload services to complete the installation
* Extend wazo services using the available extension points

    * xivo-auth
    * xivo-confd
    * xivo-confgend
    * xivo-ctid-ng
    * xivo-dird


Creating a plugin
=================

A plugin has the following structure:

* package.yml
* Makefile


plugin.yml
----------

The `package.yml` file contains all the metadata of plugin. It should contains
the following fields:

* description: The description of the plugin
* name: The name of the plugin
* version: The version of the plugin


rules
-----

The `Makefile` file is a standard makefile.

The following targets should be present in the Makefile:

* install
* uninstall


Hello World
-----------

This example will create a plugin that adds an extension `***42` that
says `Hello World` when called.


package.yml:

.. code-block::yml

    name: helloworld
    description: Adds the extension "***42" to you dialplan to greet users
    version: 0.0.1


Makefile:

.. code-block::Makefile

    .PHONY: install uninstall

    install:
        cp helloworld.conf /etc/asterisk/extensions_extra.d/
        asterisk -x 'dialplan reload'

    uninstall:
        rm -f /etc/asterisk/extensions_extra.d/helloworld.conf
        asterisk -x 'dialplan reload'

.. warning:: Tabs should be used in the makefile


helloworkd.conf:

.. code-block::ini

    [xivo-extrafeatures]
    exten = ***42,1,Playback(hello-world)
    same = n,Return()

