.. _dird-api:

********************
XiVO directories API
********************

Contacts and directories in XiVO are managed by the xivo-dird daemon. This
service provides a public API that can be used to query the directories that are
configured on a XiVO.

.. warning:: The 0.1 API is currently in development. Major changes could still
   happen and new resources will be added over time.


Lookup Representation
=====================

The `lookup` query will return a list of result matching the searched term. The
result will be retrieved from all configured directories for the given user.

Query
-----

::

    GET /0.1/directories/lookup


Parameters
----------

order
    Sort results using the specified field

direction
    'asc' or 'desc'. Sort list in ascending or descending order

limit
    number of result to show in the list

skip
    number of result to skip before starting the list

term
    the search term that we are looking for

user_id
    the ID of the user doing the search, the `user_id`


Errors
------


Example requests
----------------


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
      "display": "James Bond",
      "source": <directory_name>
    }


Errors
------

+------------+---------------+-------------------------------------+
| Error code | Error message | Description                         |
+============+===============+=====================================+
|        404 | Not found     | No contact matches the given number |
+------------+---------------+-------------------------------------+
