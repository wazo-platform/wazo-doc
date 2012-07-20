***
Fax
***

Fax transmission
================

It's possible to send faxes from XiVO using the fax Xlet in the XiVO client.
Sending and receiving a fax on the same XiVO

It's possible to send a fax to the same XiVO you use to receive it.
This is mostly useful for testing purpose.

* create a new context named fax-context of type "external".
* add an incoming call number to the fax-context context which will be used as the fax extension.
* modify the default context so that it includes the fax-context context
* add an incoming call using the following information::

   DID: the fax extension
   Context: fax-context
   Destination: Application
   Application: FaxToMail
   Email: as you wish 

You'll then be able to use your fax extension from your XiVO client
to send a fax to the same XiVO that you use to receive it.


When a fax is received, the default behaviour is to send an email to a
user-specified address with the incoming fax attached as a PDF document.

.. figure:: images/xivoclient-fax.png

   The fax Xlet in the XiVO Client

Starting with XiVO 1.1.15, more advanced features have been added, like the
ability of sending a PDF copy of a fax via FTP, printing it, changing the email body,
or doing more than one action at the same time. These advanced features are unfortunately
not available from the web-interface but only by editing the `/etc/asterisk/xivo_fax.conf`
configuration file.


Fax reception
=============

Adding a fax reception DID
--------------------------

If you want to receive faxes from XiVO, you need to add incoming calls definition with the
`Application` destination and the `FaxToMail` application for every DID you want to receive faxes from.

This apply even if you want the action to be different from sending an email, like putting it
on a FTP server. You'll still need to enter an email address in these cases even though it won't be used.

Note that, as usual when adding incoming call definitions,, you must first define the incoming
call range in the used context.

.. figure:: images/Fax_recv_adding.png


Changing the email body
-----------------------

You can change the body of the email sent upon fax reception by editing the `/etc/pf-xivo/mail.txt` file.

The following variable can be included in the mail body:
* %(dstnum)s -- the DID that received the fax

If you want to include a regular percent character, i.e. "%", you must write it has "%%" in mail.txt
or an error will occur when trying to do the variables substitution.


Changing the email subject
--------------------------

You can change the subject of the email sent upon fax reception by editing the `etc/asterisk/xivo_fax.conf` file.

Look for the "[mail]" section, and in this section, modify the value of the "subject" option.

The available variable substitution are the same as for the email body.


Using the advanced features
---------------------------

The following features are only available via the `/etc/asterisk/xivo_fax.conf` configuration file.
They are not available from the web-interface.

The configuration file has documentation embedded in it in the form of comments, with some examples
included, so if you want to use the advanced features, you might also want to take a look at the
configuration file comments.

The way it works is the following:

* you first declare some "backends", i.e. actions to be taken when a fax is received. A backend
  name looks like "mail", "ftp_example_org" or "printer_office".
* once your backends are defined, you can use them in your destination numbers. For example,
  when someone calls the 100 DID, you might want the "ftp_example_org" and "mail" backend to be run,
  but otherwise, you only want the "mail" backend to be run.

Here's an example of a valid :file:`xivo_fax.conf` configuration file::

   [general]
   tiff2pdf = /usr/bin/tiff2pdf
   mutt = /usr/bin/mutt
   lp = /usr/bin/lp
   
   [mail]
   subject = FAX reception to %(dstnum)s
   content_file = /etc/pf-xivo/mail.txt
   
   [ftp_example_org]
   host = example.org
   username = foo
   password = bar
   directory = /foobar
   
   [dstnum_default]
   dest = mail
   
   [dstnum_100]
   dest = mail, ftp_example_org

There's destination named "dstnum_default" is special because it represent the default actions to be
taken when no DID-specific action are defined.

After editing the :file:`xivo_fax.conf` file, you need to restart the agid server for the changes to be applied::

   $ /etc/init.d/pf-xivo-agid restart


Using the FTP backend
^^^^^^^^^^^^^^^^^^^^^

The FTP backend is used to send a PDF version of the received fax to an FTP server.

An FTP backend is always defined in a section beginning with the "ftp" prefix. Here's an example for
a backend named "ftp_example_org"::

   [ftp_example_org]
   host = example.org
   username = foo
   password = bar
   directory = /foobar


The "directory" option is optional and if not specified, the document will be put in the user's root directory.

The uploaded file are named like "${XIVO_SRCNUM}-${EPOCH}.pdf".


Using the printer backend
^^^^^^^^^^^^^^^^^^^^^^^^^

To use the printer backend, you must have the "cups-client" package installed on your XiVO::

   $ apt-get install cups-client

The printer backend use the "lp" command to print fax.

A printer backend is always defined in a section beginning with the "printer" prefix.
Here's an example for a backend named "printer_office"::

   [printer_office]
   name = office
   convert_to_pdf = 1

When a fax will be received, the system command ``lp -d office <faxfile>`` will be executed.

The "convert_to_pdf" option is optional and defaults to 1. If it is set to 0, the TIFF file will not
be converted to PDF before being printed.

.. warning:: You need to have cups server somewhere in you network.


Using the mail backend
^^^^^^^^^^^^^^^^^^^^^^

By default, a mail backend named "mail" is defined.

You can define more mail backends if you want. Just look what the default mail backend looks like.


Using the log backend
^^^^^^^^^^^^^^^^^^^^^

There's also a log backend available, which can be used to write a line to a file every time a fax is 
received.


Fax detection
=============

XiVO **does not currently support Fax Detection**. A workaround is describe in the 
`Known bugs and limitations`_ section.


Using analog gateways
=====================

XiVO is able to provision Linksys SPA2102, SPA3102 and SPA8000 analog gateways which can be used to 
connect Fax equipments.
This type of equipments can handle Fax streams quite successfully if you configure them with the
correct parameters. This section describes the creation of custom template *for SPA3102* which modifies several parameters

.. note:: Be aware that most of the parameters are or could be country specific, i.e. :

   * Preferred Codec,
   * FAX Passthru Codec,
   * RTP Packet Size,
   * RTP-Start-Loopback_Codec,
   * Ring_Waveform, 
   * Ring_Frequency, 
   * Ring_Voltage, 
   * FXS_Port_Impedance

#. Create a custom template for the SPA3102 base template::

    cd /var/lib/pf-xivo-provd/plugins/xivo-cisco-spa3102-5.1.10/var/templates/
    cp ../../templates/base.tpl .

#. Add the following content before the ``</flat-profile>`` tag::

    <!-- CUSTOM TPL - for faxes - START -->
    
    {% for line_no, line in sip_lines.iteritems() %}
    <!-- Dial Plan: L{{ line_no }} -->
    <Dial_Plan_{{ line_no }}_ ua="na">([x*#].)</Dial_Plan_{{ line_no }}_>
    
    <Call_Waiting_Serv_{{ line_no }}_ ua="na">No</Call_Waiting_Serv_{{ line_no }}_>
    <Three_Way_Call_Serv_{{ line_no }}_ ua="na">No</Three_Way_Call_Serv_{{ line_no }}_>
    
    <Preferred_Codec_{{ line_no }}_ ua="na">G711a</Preferred_Codec_{{ line_no }}_>
    <Silence_Supp_Enable_{{ line_no }}_ ua="na">No</Silence_Supp_Enable_{{ line_no }}_>
    <Echo_Canc_Adapt_Enable_{{ line_no }}_ ua="na">No</Echo_Canc_Adapt_Enable_{{ line_no }}_>
    <Echo_Supp_Enable_{{ line_no }}_ ua="na">No</Echo_Supp_Enable_{{ line_no }}_>
    <Echo_Canc_Enable_{{ line_no }}_ ua="na">No</Echo_Canc_Enable_{{ line_no }}_>
    <Use_Pref_Codec_Only_{{ line_no }}_ ua="na">yes</Use_Pref_Codec_Only_{{ line_no }}_>
    <DTMF_Tx_Mode_{{ line_no }}_ ua="na">Normal</DTMF_Tx_Mode_{{ line_no }}_>
    
    <FAX_Enable_T38_{{ line_no }}_ ua="na">Yes</FAX_Enable_T38_{{ line_no }}_>
    <FAX_T38_Redundancy_{{ line_no }}_ ua="na">1</FAX_T38_Redundancy_{{ line_no }}_>
    <FAX_Passthru_Method_{{ line_no }}_ ua="na">ReINVITE</FAX_Passthru_Method_{{ line_no }}_>
    <FAX_Passthru_Codec_{{ line_no }}_ ua="na">G711a</FAX_Passthru_Codec_{{ line_no }}_>
    <FAX_Disable_ECAN_{{ line_no }}_ ua="na">yes</FAX_Disable_ECAN_{{ line_no }}_>
    <FAX_Tone_Detect_Mode_{{ line_no }}_ ua="na">caller or callee</FAX_Tone_Detect_Mode_{{ line_no }}_>
    
    <Network_Jitter_Level_{{ line_no }}_ ua="na">very high</Network_Jitter_Level_{{ line_no }}_>
    <Jitter_Buffer_Adjustment_{{ line_no }}_ ua="na">disable</Jitter_Buffer_Adjustment_{{ line_no }}_>
    {% endfor %}
    
    <!-- SIP Parameters -->
    <RTP_Packet_Size ua="na">0.020</RTP_Packet_Size>
    <RTP-Start-Loopback_Codec ua="na">G711a</RTP-Start-Loopback_Codec>
    
    <!-- Regional parameters -->
    <Ring_Waveform ua="rw">Sinusoid</Ring_Waveform> <!-- options: Sinusoid/Trapezoid -->
    <Ring_Frequency ua="rw">50</Ring_Frequency>
    <Ring_Voltage ua="rw">85</Ring_Voltage>
    
    <FXS_Port_Impedance ua="na">600+2.16uF</FXS_Port_Impedance>
    <Caller_ID_Method ua="na">Bellcore(N.Amer,China)</Caller_ID_Method>
    <Caller_ID_FSK_Standard ua="na">bell 202</Caller_ID_FSK_Standard>
    
    <!-- CUSTOM TPL - for faxes - END -->

#. Reconfigure the devices with::

    provd_pycli -c 'devices.using_plugin("xivo-cisco-spa3102-5.1.10").reconfigure()

#. Then reboot the devices::

    provd_pycli -c 'devices.using_plugin("xivo-cisco-spa3102-5.1.10").synchronize()


Most of this template can be copy/paste for a SP2102 or SPA8000.

.. _Known bugs and limitations: http://documentation.xivo.fr/production/introduction/introduction.html#fax-detection

