****************
Fax Transmission
****************

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

Starting with XiVO 1.1.15, more advanced features have been added, like the 
ability of sending a PDF copy of a fax via FTP, printing it, changing the email body, 
or doing more than one action at the same time. These advanced features are unfortunately 
not available from the web-interface but only by editing the `/etc/asterisk/xivo_fax.conf` 
configuration file.


*************
Fax Reception
*************

Adding a fax reception DID
==========================

If you want to receive faxes from XiVO, you need to add incoming calls definition with the 
`Application` destination and the `FaxToMail` application for every DID you want to receive faxes from.

This apply even if you want the action to be different from sending an email, like putting it 
on a FTP server. You'll still need to enter an email address in these cases even though it won't be used.

Note that, as usual when adding incoming call definitions,, you must first define the incoming 
call range in the used context.

[[File:fax_recv_adding.png]]

Changing the email body
=======================

You can change the body of the email sent upon fax reception by editing the `/etc/pf-xivo/mail.txt` file.

The following variable can be included in the mail body:
* %(dstnum)s -- the DID that received the fax

If you want to include a regular percent character, i.e. "%", you must write it has "%%" in mail.txt 
or an error will occur when trying to do the variables substitution.

Changing the email subject
==========================

You can change the subject of the email sent upon fax reception by editing the `etc/asterisk/xivo_fax.conf` file.

Look for the "[mail]" section, and in this section, modify the value of the "subject" option.

The available variable substitution are the same as for the email body.

Using the advanced features
===========================

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

Here's an example of a valid `xivo_fax.conf` configuration file:

::
  
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

After editing the `xivo_fax.conf` file, you need to restart the agid server for the changes to be applied:


::

   $ /etc/init.d/pf-xivo-agid restart

Using the FTP backend
---------------------

The FTP backend is used to send a PDF version of the received fax to an FTP server.

An FTP backend is always defined in a section beginning with the "ftp" prefix. Here's an example for 
a backend named "ftp_example_org":

::

   [ftp_example_org]
   host = example.org
   username = foo
   password = bar
   directory = /foobar


The "directory" option is optional and if not specified, the document will be put in the user's root directory.

The uploaded file are named like "${XIVO_SRCNUM}-${EPOCH}.pdf".

Using the printer backend
-------------------------

To use the printer backend, you must have the "cups-client" package installed on your XiVO:

::

   $ apt-get install cups-client


The printer backend use the "lp" command to print fax.

A printer backend is always defined in a section beginning with the "printer" prefix. 
Here's an example for a backend named "printer_office":

::

   [printer_office]
   name = office


When a fax will be received, the system command "lp -d office <faxfile>" will be executed.

.. warning:: You need to have cups server somewhere in you network.

Using the mail backend
----------------------

By default, a mail backend named "mail" is defined.

You can define more mail backends if you want. Just look what the default mail backend looks like.

Using the log backend
---------------------

There's also a log backend available, which can be used to write a line to a file every time a fax is received.

