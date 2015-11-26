.. _auth_changelog:

*******************
xivo-auth changelog
*******************

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
