*****
Users
*****

Users Configuration.


.. index:: users

Importing Users
===============

You may import your users using a csv comma separated file. Users and lines are automatically created.


How to import users
-------------------

Once you have saved your file, you can import your users via
the :menuselection:`Services --> IPBX --> IPBX settings --> Users` page by clicking on the plus button.

.. figure:: images/Import_user_menu.png
   :scale: 80%
   :alt: Import users

   Import Users


Supported fields
----------------

+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| Field                   | Values                                               | Description                                                             |
|                         |                                                      |                                                                         |
+=========================+======================================================+=========================================================================+
|                         |                                                      |                                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| **[section user]**      | **For just add a user**                              |                                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| entityid                | int                                                  | entity id (configuration menu) ``Must be a valid entityid``             |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| firstname *             | string                                               | User first name                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| lastname                | string                                               | User last name                                                          |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| language **             | enum `['de_DE', 'en_US', 'es_ES', 'fr_FR', 'fr_CA']` | Locale ``Must be set if you add a voicemail``                           |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| enableclient            | bool `[0, 1]`                                        | username and password have to be set                                    |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| username                | string                                               | xivo client username                                                    |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| password                | string                                               | xivo client password                                                    |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| profileclient           | string                                               | xivo client profile define in menus: `Services > CTI server > Profiles` |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| outcallerid             | string                                               | Customize outgoing caller id for this user                              |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| agentnumber             | string                                               | Associated agent number                                                 |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| mobilephonenumber       | string                                               | Mobile phone number                                                     |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| bosssecretary           | enum `['no','boss','secretary']`                     | Filter: Boss - Secretary                                                |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| enablehint              | bool `[0, 1]`                                        | Enable/Disable supervision                                              |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
|                         |                                                      |                                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| **[section line]**      | **For add an line to a user**                        |                                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| phonenumber *           | string                                               | User phone number create a line ``Must be exist in context <context>``  |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| context *               | string                                               | context name ``internal context must be exist e.g. default``            |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| protocol *              | enum `['sip', 'sccp']`                               | Protocol for the line                                                   |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
|                         |                                                      |                                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| **[section incall]**    | **For add an incall to a user**                      |                                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| incallexten *           | string                                               | DID number ``incallexten must be exist in context <incallcontext>``     |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| incallcontext *         | string                                               | context name ``incall context must be exist e.g. from-extern``          |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| incallringseconds       | int                                                  | ring time in seconds                                                    |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
|                         |                                                      |                                                                         |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| **[section voicemail]** | **For add an voicemail to a user**                   | You must set a language is use this section                             |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| voicemailname *         | string                                               | voicemail fullname                                                      |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| voicemailmailbox *      | string                                               | mailbox number                                                          |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| voicemailpassword *     | string                                               | password voicemail                                                      |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| voicemailemail          | string                                               | mail for send a notification to have a receive a message                |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| voicemailattach         | bool `[0, 1]`                                        | Enable/Disable attach the audio file to your mail                       |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| voicemaildelete         | bool `[0, 1]`                                        | Enable/Disable delete message after notification                        |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+
| voicemailskippass       | bool `[0, 1]`                                        | Enable/Disable password checking                                        |
+-------------------------+------------------------------------------------------+-------------------------------------------------------------------------+

.. warning::
   "*", this field is required - valid by section

.. warning::
   "**", this field is required if you add a voicemail


Examples
--------

First step is to create a text file containing the users you want to create. Here's a basic example::

   entityid|firstname|lastname|phonenumber|context|protocol|mobilephonenumber
   1|John|Doe|1000|default|sip|00123456789
   1|George|Clinton|1001|default|sip|00123456789
   1|Bill|Bush|1002|default|sip|00123456789

This example defines 3 users:

 * John Doe with one SIP line with number 1000
 * George Clinton with one SIP line with number 1001
 * Bill Bush with one SIP line with number 1002

.. note::

   Note that the number you use must all be in the range you defined for your default context.


Text file for add a simple user with a line and voicemail::

   entityid|firstname|lastname|language|phonenumber|context|protocol|voicemailname|voicemailmailbox|voicemailpassword
   1|John|Doe|en_US|1000|default|sip|John Doe|1000|1234
   


Text file for add a simple user with a line and incall::

   entityid|firstname|lastname|phonenumber|context|protocol|incallexten|incallcontext
   1|John|Doe|1000|default|sip|2050|from-extern
   



Function keys
=============

Function keys can be configured to customize the user's phone keys. Key types are pre-defined and can be browsed through the Type drop-down list. The Supervision field allow the key to be supervised. A supervised key will light up when enabled.

.. image:: images/funckeys.png

Call forwards keys should have a destination, it's use without a destination is experimental at the moment.
