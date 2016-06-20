.. _ctid_ng_changelog:

*******************************
xivo-ctid-ng HTTP API changelog
*******************************

16.08
=====

* A new API for making calls from the authenticated user:

    * POST ``/1.0/users/me/calls``

* A new API for sending chat messages:

    * POST ``/1.0/chats``
    * POST ``/1.0/users/me/chats``

* A new API for updating presences:

    * PUT ``/1.0/presences``
    * PUT ``/1.0/users/me/presences``
