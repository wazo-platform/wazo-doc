********
Asterisk
********

Asterisk 1.8 to Asterisk 11
===========================

Table of modules that were availble in the asterisk 1.8 package but that are not available anymore in the asterisk 11 package:

+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| Name            | Description                           | Loaded in AST1.8 | Asterisk Status | Replaced By        |
+=================+=======================================+==================+=================+====================+
| app_dahdibarge  | Barge in on DAHDI channel application | Yes              | Deprecated      | app_chanspy        |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| app_readfile    | Stores output of file into a variable | Yes              | Deprecated      | func_env (FILE())  |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| app_saycountpl  | Say polish counting words             | Yes              | Deprecated      | say.conf           |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| app_setcallerid | Set CallerID Presentation Application | Yes              | Deprecated      | func_callerid      |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| cdr_sqlite      | SQLite CDR Backend                    | No               | Removed         | cdr_sqlite3_custom |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| chan_gtalk      | Gtalk Channel Driver                  | No               | Deprecated      | chan_motif         |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| chan_jingle     | Jingle Channel Driver                 | No               | Deprecated      | chan_motif         |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| chan_vpb        | Voicetronix API driver                | No               | Supported       |                    |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| format_sln16    | Raw Signed Linear 16KHz Audio support | Yes              | Removed         | format_sln         |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| res_ais         | SAForum AIS                           | No               | Removed         | res_corosync       |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+
| res_jabber      | AJI - Asterisk Jabber Interface       | No               | Deprecated      | res_xmpp           |
+-----------------+---------------------------------------+------------------+-----------------+--------------------+


External Links
**************

* https://wiki.asterisk.org/wiki/display/AST/New+in+10
* https://wiki.asterisk.org/wiki/display/AST/New+in+11
