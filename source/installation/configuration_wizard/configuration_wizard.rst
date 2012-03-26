******************
Running the Wizard
******************

After the system installation, you must go through the wizard before being able to use your XiVO.


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


Components Checks
=================

After this step, the wizard displays the status of the system and of several components. When ready, click on ``Next``.


Configuration
=============

.. figure:: images/wizard_step4_configuration.png
   :scale: 75%
   :alt: Basic configuration

   Basic configuration

#. Enter the hostname [1]_,
#. Enter the domain name [2]_,
#. Enter the password for the ``root`` user of the web interface,
#. Configure the IP address and gateway used by your XiVO (by default it pre-fills the fields with the current IP and gateway of the network interface on which you are connected to complete the wizard steps).

   .. note:: The network configuration will be applied at the end of the wizard

#. Finally verify and modify if needed the DNS servers information.


Entities and Contexts
=====================

.. figure:: images/wizard_step5_entities_contexts.png
   :scale: 75%
   :alt: Entities and Contexts

   Entities and Contexts

#. Enter the entity name (e.g. your organization name) [2]_,
#. You may change your internal context name and you must pick a number range. This will define the internal users's phone number of your sytem (you can change it afterward),
#. You may change your incoming calls context name and you may also give the DID range you have,
#. You may change your outgoing calls context name.


Validation
==========

Finally you have to validate your configuration by clicking on the ``Validate`` button.
Note that if you want to change one of the chosen settings you can go backward in the wizard with the ``Previous`` button.

.. warning:: This is the last time the ``root`` password will be displayed. Take care to note it up.

Congratulation, you now have a fully functional XiVO server.


.. [1] Allowed characters are : "``A-Z a-z 0-9 -``"
.. [2] Allowed characters are : "``A-Z a-z 0-9 - .``"
