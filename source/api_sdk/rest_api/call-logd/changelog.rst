.. _call_logd_changelog:

*********************************
xivo-call-logd REST API changelog
*********************************

17.08
=====

* ``GET /cdr`` has new attribute:

  * ``id``
  * ``answer``
  * ``direction``
  * ``tags``


17.07
=====

* New endpoints for listing call logs:

  * ``GET /users/<user_uuid>/cdr``
  * ``GET /users/me/cdr``

17.06
=====

* Call logs objects now have a new attribute ``end``
* ``GET /cdr`` has new parameters:

  * ``from``
  * ``until``
  * ``order``
  * ``direction``
  * ``limit``
  * ``offset``

* ``GET /cdr`` has new attributes:

  * ``total``
  * ``filtered``

17.05
=====

* New endpoint for listing call logs:

  * ``GET /cdr``

17.04
=====

* Creation of the HTTP daemon
