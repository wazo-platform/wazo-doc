.. _15_20_csv_import_upgrade_notes:

*************
CSV Migration
*************

This page describes how to migrate CSV files from the legacy format to the new format. Consult the `API documentation <http://api.wazo.community>`_ on user imports for further details.


CSV Data
========

 * Only data encoded as UTF-8 will be accepted
 * The pipe delimiter (``|``) has been replaced by a comma (``,``)
 * Double-quotes (``"``) must be escaped by writing them twice (e.g ``Robert ""Bob"" Jenkins``)


Field names
===========

Fields have been renamed in the new CSV format. Use the following table to rename your fields. Fields marked as **N/A** are no longer supported.

 +----------------------+---------------------------+
 | Old name             | New name                  |
 +======================+===========================+
 | entityid             | entity_id                 |
 +----------------------+---------------------------+
 | firstname            | firstname                 |
 +----------------------+---------------------------+
 | lastname             | lastname                  |
 +----------------------+---------------------------+
 | language             | language                  |
 +----------------------+---------------------------+
 | outcallerid          | outgoing_caller_id        |
 +----------------------+---------------------------+
 | mobilephonenumber    | mobile_phone_number       |
 +----------------------+---------------------------+
 | agentnumber          | **N/A**                   |
 +----------------------+---------------------------+
 | bosssecretary        | **N/A**                   |
 +----------------------+---------------------------+
 | callerid             | **N/A**                   |
 +----------------------+---------------------------+
 | enablehint           | supervision_enabled       |
 +----------------------+---------------------------+
 | enablexfer           | call_transfer_enabled     |
 +----------------------+---------------------------+
 | enableclient         | cti_profile_enabled       |
 +----------------------+---------------------------+
 | profileclient        | cti_profile_name          |
 +----------------------+---------------------------+
 | username             | username                  |
 +----------------------+---------------------------+
 | password             | password                  |
 +----------------------+---------------------------+
 | phonenumber          | exten                     |
 +----------------------+---------------------------+
 | context              | context                   |
 +----------------------+---------------------------+
 | protocol             | line_protocol             |
 +----------------------+---------------------------+
 | linename             | sip_username              |
 +----------------------+---------------------------+
 | linesecret           | sip_secret                |
 +----------------------+---------------------------+
 | incallexten          | incall_exten              |
 +----------------------+---------------------------+
 | incallcontext        | incall_context            |
 +----------------------+---------------------------+
 | incallringseconds    | incall_ring_seconds       |
 +----------------------+---------------------------+
 | voicemailname        | voicemail_name            |
 +----------------------+---------------------------+
 | voicemailnumber      | voicemail_number          |
 +----------------------+---------------------------+
 | voicemailcontext     | voicemail_context         |
 +----------------------+---------------------------+
 | voicemailpassword    | voicemail_password        |
 +----------------------+---------------------------+
 | voicemailemail       | voicemail_email           |
 +----------------------+---------------------------+
 | voicemailattach      | voicemail_attach_audio    |
 +----------------------+---------------------------+
 | voicemaildelete      | voicemail_delete_messages |
 +----------------------+---------------------------+
 | voicemailaskpassword | voicemail_ask_password    |
 +----------------------+---------------------------+
