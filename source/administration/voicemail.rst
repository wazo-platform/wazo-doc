*********
Voicemail
*********

Voicemail Configuration.


General Configuration
=====================

You can configure general settings for your voicemail service in :menuselection:`Services --> IPBX --> General Settings --> Voicemails` page.


Adding voicemail
================

There are 2 ways to add a voicemail. First is with :menuselection:`Services --> IPBX --> IPBX settings --> Voicemails` page, 2nd is editing user's configuration.


1 - Via :menuselection:`Services --> IPBX --> IPBX settings --> Voicemails`
---------------------------------------------------------------------------

In here you can add some voicemails and configure them by clicking on the plus button.


.. figure:: images/Voicemail_add_ipbx_settings.png
   :scale: 85%
   :alt: Add voicemail from voicemails menu

   Add voicemail from voicemails menu


Once your voicemails are configured, you have to edit the users configuration to search the voicemails previously created and then associate them to your users.

.. figure:: images/Voicemail_search_engine.png
   :scale: 80%
   :alt: Search voicemail for specific user

   Search voicemail for specific user


2 - On user's configuration
---------------------------

The other way is to directly add the voicemail from user's configuration in the 'voicemail' tab :

.. figure:: images/Voicemail_add_from_user.png
   :scale: 80%
   :alt: Add voicemail from user configuration

   Add voicemail from user configuration

.. warning::

   In this way, the language has to be set in user's general configuration


Deactivating voicemail
=======================

You can deactivate user's voicemail by un-checking 'Enable voicemail' option on the Voicemail tab from user's configuration:


.. figure:: images/Deactivate_user_voicemail.png
   :scale: 80%
   :alt: Deactivate user's voicemail

   Deactivate user's voicemail


Disassociating voicemail
========================

You can disassociate a voicemail from a user by selecting the 'None' option on 'Voice Mail' select box, from user's configuration:


.. figure:: images/Disassociate_voicemail.png
   :scale: 80%
   :alt: Disassociate voicemail

   Disassociate voicemail


.. warning::

   Note that disassociating a voicemail from its user don't delete that voicemail.


Deleting voicemail
==================

Delete voicemail is done on :menuselection:`Services --> IBX --> IPBX settings --> Voicemails`


.. warning::

   * Deleting a voicemail is irreversible. It deletes all messages associated with that voicemail.
   * If concerned user still have messages waiting for him, you have to manually reboot the phone.


