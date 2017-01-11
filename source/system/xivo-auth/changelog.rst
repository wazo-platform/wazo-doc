.. _auth_changelog:

****************************
xivo-auth HTTP API Changelog
****************************

17.02
=====

* A new resource has been added to manage ACL policies

    * POST ``/0.1/policy``


16.16
=====

* The token data in the response of POST and GET on ``/0.1/token`` now include the following new fields
    * utc_expires_at
    * utc_issued_at
    * xivo_uuid


16.02
=====

* POST ``/0.1/token``, field ``expiration``: only integers are accepted, floats are now invalid.
* Experimental backend ``ldap_user_voicemail`` has been removed.
* New backend ``ldap_user`` has been added.


15.19
=====

* POST ``/0.1/token`` do not accept anymore argument ``backend_args``


15.17
=====

* New backend ``ldap_user_voicemail`` has been added. **WARNING** this backend is **EXPERIMENTAL**.


15.16
=====

* HEAD and GET now take a new ``scope`` query string argument to check ACLs
* Backend interface method ``get_acls`` is now named ``get_consul_acls``
* Backend interface method ``get_acls`` now returns a list of ACLs
* HEAD and GET can now return a ``403`` if an ACL access is denied


15.15
=====

* POST ``/0.1/token`` accept new argument ``backend_args``
* Signature of backend method ``get_ids()`` has a new argument ``args``
* New method ``get_acls`` for backend has been added
* New backend ``service`` has been added
