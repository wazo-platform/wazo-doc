.. _asterisk_voicemail:

******************
Asterisk Voicemail
******************

Delete voicemail
================

Query
-----

::

    GET /delete_voicemail

Parameters
----------

Mandatory
^^^^^^^^^

name
    the voicemail name

Optional
^^^^^^^^

context
    the voicemail context (default is 'default')


Errors
------

+------------+---------------+------------------------------+
| Error code | Error message | Description                  |
+============+===============+==============================+
|        404 | Not found     | The voicemail does not exist |
+------------+---------------+------------------------------+

Example requests
----------------

::

    GET /delete_voicemail HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        nothing
    }


