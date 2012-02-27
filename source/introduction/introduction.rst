************
Introduction
************

XiVO History
============

XiVO has been created in 2005 by Proformatique.


XiVO Releases
=============

The latest release of XiVO is |version|.
https://projects.xivo.fr/projects
`XiVO 1.2 was released <https://projects.xivo.fr/news/49>`_ on February 3, 2012.


Known Problems and limitations
==============================

Please note following problems and restrictions that apply to release 1.2.2


Installation with more than 250 users
-------------------------------------

Confgen is not able to generate sip configuration for installations with more than 300 users. If you want to overcome this limitation
you may apply the following procedure :

* create a gen_sip_conf file::

     #!/bin/bash
     netcat 127.0.0.1 8669 <<< "asterisk/sip.conf"

* change permission to gen_sip.conf to allow file execution ``chmod +x gen_sip_conf``
* edit /etc/asterisk/sip.conf and replace the line by ``#exec <path_to_file>/gen_sip_conf``


Known bugs
----------

You may find last bug updates in  `XiVO redmine <https://projects.xivo.fr/projects/xivo-software/issues?set_filter=1&tracker_id=1>`_.
