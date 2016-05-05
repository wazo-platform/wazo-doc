.. index:: interconnections/simonics

*****************
Simon Telephonics
*****************

The following configuration is based on the example found `here <http://support.simonics.com/support/solutions/articles/3000033840-asterisk-sip-conf>`_

* username: ``GV18005551212``
* password: ``password``
* exten: ``18005551212``
* host: ``gvgw.simonics.com``


General SIP configuration
=========================

Under :menuselection:`Services --> IPBX --> General settings --> SIP Protocol`.

* General

  * Match users with 'username' field: *checked*

.. figure:: images/simonics_sip_general.png
    :scale: 85%


Trunk settings
==============

Under :menuselection:`Services --> IPBX --> Trunk management --> SIP Protocol`.

* General

  * Name: ``GV18005551212``
  * Authentication username: ``GV18005551212``
  * Password: ``password``
  * Caller ID: ``18005551212``
  * Connection type: ``Friend``
  * IP Addressing type: ``static``

    * ``gvgw.simonics.com``

  * Context: ``<your incoming call context>``

.. figure:: images/simonics_trunk_general.png
    :scale: 85%


* Register

  * Register: ``checked``
  * Transport: ``UDP``
  * Name: ``GV18005551212``
  * Password: ``password``
  * Remote Server: ``GV18005551212``
  * Contact: ``18005551212``

.. figure:: images/simonics_trunk_register.png
    :scale: 85%


* Signaling

  * Monitoring: ``Yes``

.. figure:: images/simonics_trunk_signaling.png
    :scale: 85%


Outgoing calls
==============

See the :ref:`voip_provider_outcall` section.


Incoming calls
==============

See the :ref:`voip_provider_incall` section.
