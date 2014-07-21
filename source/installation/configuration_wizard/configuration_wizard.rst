.. _configuration_wizard:

******************
Running the Wizard
******************

After the system installation, you must go through the wizard before being able to use your XiVO.
Browse to your server's IP address to start the configuration wizard (For example: http://192.168.1.10)

.. index:: wizard

Language
========

You first have to select the language you want to use for the wizard.

.. figure:: images/wizard_step1_lang.png
   :scale: 75%
   :alt: Base configuration

   Select the language


License
=======

You then have to accept the *GPLv3 License* under which XiVO is distributed.

.. figure:: images/wizard_step2_license.png
   :scale: 75%
   :alt: Accept the license

   Accept the license


Configuration
=============

.. figure:: images/wizard_step4_configuration.png
   :scale: 75%
   :alt: Basic configuration

   Basic configuration

#. Enter the hostname  (Allowed characters are : ``A-Z a-z 0-9 -``)
#. Enter the domain name (Allowed characters are : ``A-Z a-z 0-9 - .``)
#. Enter the password for the ``root`` user of the web interface,
#. Configure the IP address and gateway used by your XiVO (by default it pre-fills the fields with the current IP
   and gateway of the network interface on which you are connected if and only if network interface has a default
   gateway).

   .. note:: The network configuration will be applied at the end of the wizard

#. Finally, modify the DNS server information if needed.


Entities and Contexts
=====================

Contexts are used for managing various phone numbers that are used by your system.

* The Interal calls context is used for managing phone numbers for devices that are connected to your system.
* The Incalls context will intercept all incoming calls from the exterior
* The Outcalls context is used for managing ougoing calls to the exterior

.. figure:: images/wizard_step5_entities_contexts.png
   :scale: 75%
   :alt: Entities and Contexts

   Entities and Contexts

#. Enter the entity name (e.g. your organization name) (Allowed characters are : ``A-Z a-z 0-9 - .``)
#. Enter the number interval for you internal context. The interval will define the users's phone numbers for your system (you can change it afterwards)
#. Enter the DID range and DID length for your system.
#. You may change the name of your outgoing calls context.


Validation
==========

Finally, you can validate your configuration by clicking on the ``Validate`` button.
Note that if you want to change one of the settings you can go backwards in the wizard by clicking on the ``Previous`` button.

.. warning:: This is the last time the ``root`` password will be displayed. Take care to note it.

Congratulations, you now have a fully functional XiVO server.

You can subscribe to the `xivo-announce list <https://lists.proformatique.com/listinfo/xivo-announce>`_
to always stay informed on the latest upgrades for XiVO.

To start configuring XiVO, see :ref:`getting_started`.
