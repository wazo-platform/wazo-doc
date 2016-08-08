.. _ctid_ng_changelog:

*******************************
xivo-ctid-ng HTTP API changelog
*******************************

16.10
=====

* A new API for checking the status of the daemon:

    * GET ``/1.0/status``

16.09
=====

* A new API for updating user presences:

    * GET ``/1.0/users/{uuid}/presences``
    * PUT ``/1.0/users/{uuid}/presences``
    * GET ``/1.0/users/me/presences``
    * PUT ``/1.0/users/me/presences``

* New APIs for listing and hanging up calls of a user:

    * GET ``/1.0/users/me/calls``
    * DELETE ``/1.0/users/me/calls/{id}``

* New APIs for listing, cancelling and completing transfers of a user:

    * GET ``/1.0/users/me/transfers``
    * DELETE ``/1.0/users/me/transfers/{transfer_id}``
    * PUT ``/1.0/users/me/transfers/{transfer_id}/complete``

* POST ``/1.0/users/me/transfers`` may now return 403 status code.
* Originates (POST ``/*/calls``) now return 400 if an invalid extension is given.


16.08
=====

* A new API for making calls from the authenticated user:

    * POST ``/1.0/users/me/calls``

* A new API for sending chat messages:

    * POST ``/1.0/chats``
    * POST ``/1.0/users/me/chats``

* A new parameter for transfer creation (POST ``/1.0/transfers``):

    * ``variables``

* A new API for making transfers from the authenticated user:

    * POST ``/1.0/users/me/transfers``
