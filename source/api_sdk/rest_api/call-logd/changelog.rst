.. _call_logd_changelog:

*********************************
xivo-call-logd REST API changelog
*********************************

17.08
=====

* ``GET /users/me/cdr`` and ``GET /users/<user_uuid>/cdr`` accept new query string arguments:

  * ``call_direction``
  * ``number``

* ``GET /cdr`` accepts new query string arguments:

  * ``call_direction``
  * ``number``
  * ``tags``

* ``GET /cdr`` has new attribute:

  * ``id``
  * ``answer``
  * ``call_direction``
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
