.. _asterisk-1.8-to-11:

********************************
Asterisk 1.8 to 11 Upgrade Notes
********************************

Table of modules that were available in the asterisk 1.8 package but that are not available anymore in the asterisk 11 package:

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

List of modules that were loaded in asterisk 1.8 but that are not loaded anymore in asterisk 11 (see modules.conf):

* res_calendar.so
* res_calendar_caldav.so
* res_calendar_ews.so
* res_calendar_exchange.so
* res_calendar_icalendar.so
* res_config_sqlite.so
* res_stun_monitor.so

List of debian packages that are not available anymore for asterisk 11:

* asterisk-config
* asterisk-mysql
* asterisk-web-vmail

.. note::  These packages were not installed by default for asterisk 1.8.

If you are using some custom dialplan or AGIs, it is your responsibility to make sure it still
works with asterisk 11. See the `External Links`_ for more information.


External Links
**************

* http://svnview.digium.com/svn/asterisk/branches/11/UPGRADE-10.txt
* http://svnview.digium.com/svn/asterisk/branches/11/UPGRADE.txt
* https://wiki.asterisk.org/wiki/display/AST/New+in+10
* https://wiki.asterisk.org/wiki/display/AST/New+in+11
