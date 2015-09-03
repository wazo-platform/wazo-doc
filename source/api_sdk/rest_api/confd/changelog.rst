.. _confd_changelog:

*****************************
xivo-confd REST API changelog
*****************************

15.15
=====

 * The field ``enabled`` has been added to the voicemail model
 * A line is no longer required when associating a voicemail with a user
 * Voicemails can now be edited even when they are associated to a user

15.14
=====

 * All optional fields on a user are now always null (sometimes they were empty strings)
 * The caller id is no longer automatically updated when the firstname or lastname is modified. You must update the
   caller id yourself if you modify the user's name.
 * Caller id will be generated if and only if it does not exist when creating a user.

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
