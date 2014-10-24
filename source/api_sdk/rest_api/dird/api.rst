.. _dird-api:

********************
XiVO directories API
********************

Contacts and directories in XiVO are managed by the xivo-dird daemon. This
service provides a public API that can be used to query the directories that are
configured on a XiVO.

.. warning:: The 0.1 API is currently in development. Major changes could still
   happen and new resources will be added over time.


Lookup Headers
==============

Query
-----

::

    GET /0.1/directories/lookup/<profile>/headers

Parameters
----------

Mandatory
^^^^^^^^^

profile
    The lookup profile. It determines which directories to search. The profile is the "Context"
    listed in :menuselection:`CTI Server --> Direct directories`.


Errors
------

+------------+---------------+-----------------------------------+
| Error code | Error message | Description                       |
+============+===============+===================================+
|        404 | Not found     | The lookup profile does not exist |
+------------+---------------+-----------------------------------+

Example requests
----------------

::

    GET /0.1/directories/lookup/default/headers HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "column_headers": ["Firstname", "Lastname", "Phone number"],
      "column_types": [null, null, "office"]
    }


Reverse lookup
==============

The `reverse_lookup` query will return the first result matching the term in all
of the configured directories.


Query
-----

::

    GET /0.1/directories/reverse_lookup


Parameters
----------

term
    the search term that we are looking for


Example requests
----------------

Search for the term "5555555007"::

    GET /0.1/directories/reverse_lookup?term=5555555007 HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "name": "James Bond",
      "number": "5555555007",
      "source": <directory_name>
    }


Errors
------

+------------+---------------+-------------------------------------+
| Error code | Error message | Description                         |
+============+===============+=====================================+
|        404 | Not found     | No contact matches the given number |
+------------+---------------+-------------------------------------+
