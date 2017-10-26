**********
Voicemails
**********

Voicemail Configuration.


.. _voicemail_general_configuration:

General Configuration
=====================

The global voicemail configuration is located under :menuselection:`Services --> IPBX --> General Settings --> Voicemails`.

To customize the email sent when a voicemail is received, you can use a few variables. The complete list is available on the `Asterisk wiki <https://wiki.asterisk.org/wiki/display/AST/VoiceMail+Channel+Variables>`_.


Adding voicemails
=================

There are 2 ways to add a voicemail:

* :ref:`voicemail_add_1`
* :ref:`voicemail_add_2`


.. _voicemail_add_1:

Using :menuselection:`Services --> IPBX --> IPBX settings --> Voicemails`
-------------------------------------------------------------------------

New voicemails can be added using the ``+`` button.


.. figure:: images/Voicemail_add_ipbx_settings.png
   :scale: 85%
   :alt: Add voicemail from voicemails menu

   Add voicemails from voicemail menu


Once your voicemail is configured, you have to edit the user configuration and
search the voicemail previously created and then associate it to your user.

.. figure:: images/Voicemail_search_engine.png
   :scale: 80%
   :alt: Search for a voicemail in the user's configuration

   Search for a voicemail in the user's configuration


.. _voicemail_add_2:

Using the user's configuration
------------------------------

The other way is to add the voicemail from user's configuration in the 'voicemail' tab by

#. Clicking the ``+`` button
#. Filling the voicemail form
#. Saving

.. figure:: images/Voicemail_add_from_user.png
   :scale: 80%
   :alt: Add a voicemail from the user's configuration

   Add a voicemail from the user's configuration

.. note:: The user's language *must* be set in the `general` tab



Disabling a voicemail
=====================

You can disable a user's voicemail by un-checking the 'Enable voicemail' option
on the Voicemail tab from user's configuration.


.. figure:: images/Deactivate_user_voicemail.png
   :scale: 80%
   :alt: Deactivate user's voicemail

   Deactivate user's voicemail


Deleting a voicemail
====================

Delete voicemail is done on :menuselection:`Services --> IBX --> IPBX settings --> Voicemails`
or from the user's `voicemail` tab.

.. note::

   * Deleting a voicemail is irreversible. It deletes all messages associated with that voicemail.
   * If the voicemail contains messages, the message waiting indication on the phone will not be deactivated until the next phone reboot.


Disable password checking
=========================

Unchecking the option ``Ask password`` allows you to skip password checking for the voicemail only
when it is consulted from an internal context.

* when calling the voicemail with \*98
* when calling the voicemail with \*99<voicemail number>

.. warning::

   If the the \*99 extension is enabled and a user does not have a password on its voicemail, anyone from the same context will be able
   to listen to its messages, change its password and greeting messages.

However, the password will be asked when the voicemail is consulted through an incoming call. For
instance, let's consider the following incoming call:

.. figure:: images/Incoming_call_voicemail.png
   :scale: 80%
   :alt: Incoming call for voicemails

With such a configuration, when calling this incoming call from the outside, we will be asked for:

* the voicemail number we want to consult
* the voicemail password, **even if the "Disable password checking option" is activated**

And then, we will be granted access to the voicemail.

Take note that the second "context" field contains the context of the voicemail. Voicemails of other contexts
will not be accessible through this incoming call.

.. warning::

   For security reasons, such an incoming call should be avoided if a voicemail in the given context
   has no password.


Advanced configuration
======================

Remote *xivo-confd*
-------------------

If *xivo-confd* is on a remote host, *xivo-confd-client* configuration will be
required to be able to change the voicemail passwords using a phone.

This configuration should be done:

.. code-block:: sh

    mkdir -p /etc/systemd/system/asterisk.service.d
    cat >/etc/systemd/system/asterisk.service.d/remote-confd-voicemail.conf <<EOF
    [Service]
    Environment=CONFD_HOST=localhost
    Environment=CONFD_PORT=9486
    Environment=CONFD_HTTPS=true
    Environment=CONFD_USERNAME=<username>
    Environment=CONFD_PASSWORD=<password>
    EOF
    systemctl daemon-reload
