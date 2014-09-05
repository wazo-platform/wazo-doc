.. _confd_changelog:

******************
REST API changelog
******************

14.16
=====

* Association :ref:`user-voicemail <user-voicemail-association>`, when associating a voicemail whose
  id does not exist:

  * before: error 404
  * after: error 400

14.14
=====

* Association :ref:`line-extension <line-extension-associations>`, a same extension can not be
  associated to multiple lines

14.13
=====

* Resource :ref:`line <confd_lines>`, field ``provisioning_extension``: type changed from ``int`` to ``string``
