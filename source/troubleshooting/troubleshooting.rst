.. _troubleshooting:

Troubleshooting
===============

The list of current bugs can be found on
`the official XiVO issue tracker <https://projects.xivo.io/issues?set_filter=1&tracker_id=1>`_.


Transfers using DTMF
--------------------

When transfering a call using DTMF (\*1) you get an *invalid extension* error when dialing the
extension.

The workaround to this problem is to create a preprocess subroutine and assign it to the destinations
where you have the problem.

Under :menuselection:`Services --> IPBX --> IPBX configuration --> Configuration files` add a new file
containing the following dialplan::

    [allow-transfer]
    exten = s,1,NoOp(## Setting transfer context ##)
    same = n,Set(__TRANSFER_CONTEXT=<internal-context>)
    same = n,Return()

Do not forget to substitute <internal-context> with your internal context.

Some places where you might want to add this preprocess subroutine is on queues and outgoing calls
to be able to transfer the called person to another extension.


.. _fax-detection:

Fax detection
-------------

XiVO **does not currently support Fax detection**. The following describe a workaround to use this
feature. The behavior is to answer all incoming (external) call, wait for a number of seconds (4 in
this example) : if a fax is detected, receive it otherwise route the call normally.

.. note:: This workaround works only :

    * on incoming calls towards an User (and an User only),
    * if the incoming trunk is a DAHDI or a SIP trunk,
    * if the user has a voicemail which is activated and with the email field filled
    * XiVO >= 13.08 (needs asterisk 11)

    Be aware that this workaround will probably not survive any upgrade.

#. In the Web Interface and under :menuselection:`Services --> IPBX --> IPBX configuration -->
   Configuration files` add a new file named *fax-detection.conf* containing the following
   dialplan::

    ;; Fax Detection
    [pre-user-global-faxdetection]
    exten = s,1,NoOp(Answer call to be able to detect fax if call is external AND user has an email configured)
    same  =   n,GotoIf($["${XIVO_CALLORIGIN}" = "extern"]?:return)
    same  =   n,GotoIf(${XIVO_USEREMAIL}?:return)
    same  =   n,Set(FAXOPT(faxdetect)=yes) ; Activate dynamically fax detection
    same  =   n,Answer()
    same  =   n,Wait(4) ; You can change the number of seconds it will wait for fax (4 to 6 is good)
    same  =   n,Set(FAXOPT(faxdetect)=no) ; If no fax was detected deactivate dyamically fax detection (needed if you want directmedia to work)
    same  =   n(return),Return()

    exten = fax,1,NoOp(Fax detected from ${CALLERID(num)} towards ${XIVO_DSTNUM} - will be sent upon reception to ${XIVO_USEREMAIL})
    same  =     n,GotoIf($["${CHANNEL(channeltype)}" = "DAHDI"]?changeechocan:continue)
    same  =     n(changeechocan),Set(CHANNEL(echocan_mode)=fax) ; if chan type is dahdi set echo canceller in fax mode
    same  =     n(continue),Gosub(faxtomail,s,1(${XIVO_USEREMAIL}))

#. In the file :file:`/etc/xivo/asterisk/xivo_globals.conf` set the global user subroutine to
   ``pre-user-global-faxdetection`` : this subroutine will be executed each time a user is called::

    XIVO_PRESUBR_GLOBAL_USER = pre-user-global-faxdetection

#. Reload asterisk configuration (both for dialplan and dahdi)::

    asterisk -rx 'core reload'


.. _berofos-integration-with-pbx:

Berofos Integration with PBX
----------------------------

You can use a Berofos failover switch to secure the ISDN provider lines
when installing a XiVO in front of an existing PBX.
The goal of this configuration is to mitigate the consequences of an outage of the XiVO : with this
equipment the ISDN provider links could be switched to the PBX directly if the XiVO goes down.

XiVO **does not offer natively** the possibility to configure Berofos in this failover mode.
This section describes a workaround.

Logical view::

                   +------+                            +-----+
   -- Provider ----| XiVO | -- ISDN Interconnection  --| PBX | -- Phones
                   +------+                            +-----+

Connection::

       +-------------Bero*fos---------------+
       | A        B        C        D       |
       | o o o o  o o o o  o o o o  o o o o |
       +-+-+------+-+------+-+------+-+-----+
         | |      | |      | |      | |
        / /       | |      | |      | |
       / /    +--------+   / /   +---------+
     2 T2     |  XiVO  |  / /    |   PBX   |
              +--------+ / /     +---------+
                  | |   / /
                  \ \__/ /
                   \____/


The following describes how to configure your XiVO and your Berofos.

#. Follow the Berofos general configuration (firmware, IP, login/password) described
   in the the :ref:`Berofos Installation and Configuration <berofos-installation-and-configuration>`
   page.

#. When done, apply these specific parameters to the berofos::

    bnfos --set scenario=1   -h 10.105.2.26 -u admin:berofos
    bnfos --set mode=1       -h 10.105.2.26 -u admin:berofos
    bnfos --set modedef=1    -h 10.105.2.26 -u admin:berofos
    bnfos --set wdog=1       -h 10.105.2.26 -u admin:berofos
    bnfos --set wdogdef=1    -h 10.105.2.26 -u admin:berofos
    bnfos --set wdogitime=60 -h 10.105.2.26 -u admin:berofos

#. Add the following script :file:`/usr/local/sbin/berofos-workaround`::

    #!/bin/bash
    # Script workaround for berofos integration with a XiVO in front of PABX

    res=$(service asterisk status)
    does_ast_run=$?
    if [ $does_ast_run -eq 0 ]; then
        /usr/bin/logger "$0 - Asterisk is running"
        # If asterisk is running, we (re)enable wdog and (re)set the mode
        /usr/bin/bnfos --set mode=1 -f fos1 -s
        /usr/bin/bnfos --set modedef=1 -f fos1 -s
        /usr/bin/bnfos --set wdog=1 -f fos1 -s

        # Now 'kick' berofos ten times each 5 seconds
        for ((i == 1; i <= 10; i += 1)); do
            /usr/bin/bnfos --kick -f fos1 -s
            /bin/sleep 5
        done
    else
        /usr/bin/logger "$0 - Asterisk is not running"
    fi


#. Add execution rights to script::

    chmod +x /usr/local/sbin/berofos-workaround

#. Create a cron to launch the script every minutes :file:`/etc/cron.d/berofos-cron-workaround`::

    # Workaround to berofos integration
    MAILTO=""

    */1 * * * * root /usr/local/sbin/berofos-workaround


Upgrading from XiVO 1.2.3
--------------------------

#. There is an issue with ``xivo-libsccp`` and ``pf-xivo-base-config`` during an upgrade from 1.2.3::

    dpkg: error processing /var/cache/apt/archives/pf-xivo-base-config_13%3a1.2.4-1_all.deb (--unpack):
    trying to overwrite '/etc/asterisk/sccp.conf', which is also in package xivo-libsccp 1.2.3.1-1
    ...
    Errors were encountered while processing:
    /var/cache/apt/archives/pf-xivo-base-config_13%3a1.2.4-1_all.deb
    E: Sub-process /usr/bin/dpkg returned an error code (1)


#. You have to remove :file:`/var/lib/dpkg/info/xivo-libsccp.conffiles`::

    rm /var/lib/dpkg/info/xivo-libsccp.conffiles

#. You have to edit :file:`/var/lib/dpkg/info/xivo-libsccp.list` and remove the following line::

    /etc/asterisk/sccp.conf

#. and remove :file:`/etc/asterisk/sccp.conf`::

    rm /etc/asterisk/sccp.conf

#. Now, you can launch ``xivo-upgrade`` to finish the upgrade process


.. _cti-ami-proxy:

CTI server is unexpectedly terminating
--------------------------------------

If you observes that your CTI server is sometimes unexpectedly terminating with the following
message in :file:`/var/log/xivo-ctid.log`::

    (WARNING) (main): AMI: CLOSING

Then you might be in the case where asterisk generates lots of data in a short period of time on the
AMI while the CTI server is busy processing other thing and is not actively reading from its AMI
connection. If the CTI server takes too much time before consuming some data from the AMI
connection, asterisk will close the AMI connection. The CTI server will terminate itself once it
detects the connection to the AMI has been lost.

There's a workaround to this problem called the ami-proxy, which is a process which buffers the AMI
connection between the CTI server and asterisk. This should only be used as a last resort solution,
since this increases the latency between the processes and does not fix the root issue.

To enable the ami-proxy, you must:

#. Add a file :file:`/etc/systemd/system/xivo-ctid.service.d/ami-proxy.conf`:

   .. code-block:: sh

      mkdir -p /etc/systemd/system/xivo-ctid.service.d
      cat >/etc/systemd/system/xivo-ctid.service.d/ami-proxy.conf <<EOF
      [Service]
      Environment=XIVO_CTID_AMI_PROXY=1
      EOF
      systemctl daemon-reload

#. Restart the CTI server::

      systemctl restart xivo-ctid.service

If you are on a XiVO cluster, you must do the same procedure on the slave if you want the ami-proxy
to also be enabled on the slave.

To disable the ami-proxy::

   rm /etc/systemd/system/xivo-ctid.service.d/ami-proxy.conf
   systemctl daemon-reload
   systemctl restart xivo-ctid.service


Agents receiving two ACD calls
------------------------------

An agent can sometimes receive more than 1 ACD call at the same time, even if the queues
he's in have the "ringinuse" parameter set to no (default).

This behaviour is caused by a bug in asterisk: https://issues.asterisk.org/jira/browse/ASTERISK-16115

It's possible to workaround this bug in XiVO by adding an agent :ref:`subroutine <subroutine>`.
The subroutine can be either set globally or per agent::

   [pre-limit-agentcallback]
   exten = s,1,NoOp()
   same  =   n,Set(LOCKED=${LOCK(agentcallback-${XIVO_AGENT_ID})})
   same  =   n,GotoIf(${LOCKED}?:not-locked,1)
   same  =   n,Set(GROUP(agentcallback)=${XIVO_AGENT_ID})
   same  =   n,Set(COUNT=${GROUP_COUNT(${XIVO_AGENT_ID}@agentcallback)})
   same  =   n,NoOp(${UNLOCK(agentcallback-${XIVO_AGENT_ID})})
   same  =   n,GotoIf($[ ${COUNT} <= 1 ]?:too-many-calls,1)
   same  =   n,Return()

   exten = not-locked,1,NoOp()
   same  =   n,Log(ERROR,Could not obtain lock)
   same  =   n,Wait(0.5)
   same  =   n,Hangup()

   exten = too-many-calls,1,NoOp()
   same  =   n,Log(WARNING,Not calling agent ID/${XIVO_AGENT_ID} because already in use)
   same  =   n,Wait(0.5)
   same  =   n,Hangup()

This workaround only applies to queues with agent members; it won't work for queues
with user members.

Also, the subroutine prevent asterisk from calling an agent twice by hanguping the second
call. In the agent statistics, this will be shown as a non-answered call by the agent.


.. _postgresql_localization_errors:

PostgreSQL localization errors
------------------------------

The database and the underlying `database cluster`_ used by XiVO is sensitive to the system locale
configuration. The locale used by the database and the database cluster is set when XiVO is
installed. If you change your system locale without particular attention to PostgreSQL, you might
make the database and database cluster temporarily unusable.

.. _database cluster: http://www.postgresql.org/docs/9.4/interactive/creating-cluster.html

When working with locale and PostgreSQL, there's a few useful commands and things to know:

* ``locale -a`` to see the list of currently available locales on your system
* ``locale`` to display information about the current locale of your shell
* ``grep ^lc_ /etc/postgresql/9.4/main/postgresql.conf`` to see the locale configuration of your
  database cluster
* ``sudo -u postgres psql -l`` to see the locale of your databases
* the :file:`/etc/locale.gen` file and the associated ``locale-gen`` command to configure the
  available system locales
* ``systemctl restart postgresql.service`` to restart your database cluster
* the PostgreSQL log file located at :file:`/var/log/postgresql/postgresql-9.4-main.log`

.. note:: You can use any locale with XiVO as long as it uses an UTF-8 encoding.


Database cluster is not starting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the database cluster doesn't start and you have the following errors in your log file::

   LOG:  invalid value for parameter "lc_messages": "en_US.UTF-8"
   LOG:  invalid value for parameter "lc_monetary": "en_US.UTF-8"
   LOG:  invalid value for parameter "lc_numeric": "en_US.UTF-8"
   LOG:  invalid value for parameter "lc_time": "en_US.UTF-8"
   FATAL:  configuration file "/etc/postgresql/9.4/main/postgresql.conf" contains errors

Then this usually means that the locale that is configured in :file:`postgresql.conf` (here ``en_US.UTF-8``)
is not currently available on your system, i.e. does not show up the output of ``locale -a``. You
have two choices to fix this issue:

* either make the locale available by uncommenting it in the :file:`/etc/locale.gen` file and running
  ``locale-gen``
* or modify the :file:`/etc/postgresql/9.4/main/postgresql.conf` file to set the various ``lc_*``
  options to a locale that is available on your system

Once this is done, restart your database cluster.


Can't connect to the database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the database cluster is up but you get the following error when trying to connect to the
``asterisk`` database::

   FATAL:  database locale is incompatible with operating system
   DETAIL:  The database was initialized with LC_COLLATE "en_US.UTF-8",  which is not recognized by setlocale().
   HINT:  Recreate the database with another locale or install the missing locale.

Then this usually means that the database locale is not currently available on your system. You have
two choices to fix this issue:

* either make the locale available by uncommenting it in the :file:`/etc/locale.gen` file, running
  ``locale-gen`` and restarting your database cluster
* or :ref:`recreate the database using a different locale <postgres-change-locale>`


Error during the upgrade
^^^^^^^^^^^^^^^^^^^^^^^^

Then you are mostly in one of the cases described above. Check your log file.


Error while restoring a database backup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If during a database restore, you get the following error::

   pg_restore: [archiver (db)] Error while PROCESSING TOC:
   pg_restore: [archiver (db)] Error from TOC entry 4203; 1262 24745 DATABASE asterisk asterisk
   pg_restore: [archiver (db)] could not execute query: ERROR:  invalid locale name: "en_US.UTF-8"
       Command was: CREATE DATABASE asterisk WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';

Then this usually means that your database backup has a locale that is not currently available on
your system. You have two choices to fix this issue:

* either make the locale available by uncommenting it in the :file:`/etc/locale.gen` file, running
  ``locale-gen`` and restarting your database cluster
* or if you want to restore your backup using a different locale (for example ``fr_FR.UTF-8``),
  then restore your backup using the following commands instead::

     sudo -u postgres dropdb asterisk
     sudo -u postgres createdb -l fr_FR.UTF-8 -O asterisk -T template0 asterisk
     sudo -u postgres pg_restore -d asterisk asterisk-*.dump


Error during master-slave replication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Then the slave database is most likely not using an UTF-8 encoding. You'll need to
:ref:`recreate the database using a different locale <postgres-change-locale>`


.. _postgres-change-locale:

Changing the locale (LC_COLLATE and LC_CTYPE) of the database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have decided to change the locale of your database, you must:

* make sure that you have enough space on your hard drive, more precisely in the file system holding
  the :file:`/var/lib/postgresql` directory. You'll have, for a moment, two copies of the
  ``asterisk`` database.
* prepare for a service interruption. The procedure requires the services to be restarted twice,
  and the system performance will be degraded while the database with the new locale is being
  created, which can take a few hours if you have a really large database.
* make sure the new locale is available on your system, i.e. shows up in the output of ``locale -a``

Then use the following commands (replacing ``fr_FR.UTF-8`` by your locale)::

   xivo-service restart all
   sudo -u postgres createdb -l fr_FR.UTF-8 -O asterisk -T template0 asterisk_newlocale
   sudo -u postgres pg_dump asterisk | sudo -u postgres psql -d asterisk_newlocale
   xivo-service stop
   sudo -u postgres psql <<'EOF'
   DROP DATABASE asterisk;
   ALTER DATABASE asterisk_newlocale RENAME TO asterisk;
   EOF
   xivo-service start

You should also modify the :file:`/etc/postgresql/9.4/main/postgresql.conf` file to set the various
``lc_*`` options to the new locale value.

For more information, consult the `official documentation on PostgreSQL localization support
<http://www.postgresql.org/docs/9.4/interactive/charset.html>`_.
