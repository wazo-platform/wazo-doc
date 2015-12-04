****************
Mass User Import
****************

Users and common related resources can be imported onto a XiVO server by sending a CSV file with a predefined set of fields.

This page only describes how to migrate CSV files from the legacy format used by the web interface to the new format. Consult the `API documentation <http://api.xivo.io>`_ for further details.


Uploading files
===============

Files may be uploaded using HTTP utilities. The Header `Content-Type: text/csv charset=utf-8` must be set and the CSV data must be sent in the body of the request. A file may be uploaded using `curl` as follows:

.. code-block:: bash

	curl -k -H "Content-Type: text/csv; charset=utf-8" -u username:password --data-binary "@file.csv" https://xivo:9486/1.1/users/import

The response can be reindented in a more readable format by piping the response through `python -m json.tool` in the following way:

.. code-block:: bash

	curl (...) | python -m json.tool


CSV Data
========

 * Only data encoded as UTF-8 will be accepted
 * The pipe delimiter (``|``) has been replaced by a comma (``,``)
 * Double-quotes (``"``) must be escaped by writing them twice (e.g ``"`` becomes ``""``)
 * Lines may be seperated by ``\r\n``, however only ``\n`` is recommended


Field names
===========

Fields have been renamed in the new API. Use the following table to rename fields in your CSV data

 +----------------------+---------------------------+
 | Webi name            | Confd name                |
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
