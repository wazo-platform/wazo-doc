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
=====================

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

Search for the term "Bob"::

    GET /0.1/directories/lookup/default HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "headers": ["Firstname", "Lastname", "Phone number"],
      "values_type": [null, null, "office"]
    }


Lookup Representation
=====================

The `lookup` query will return a list of result matching the searched term. The
result will be retrieved from all configured directories for the given user.

Query
-----

::

    GET /0.1/directories/lookup/<profile>


Parameters
----------

Mandatory
^^^^^^^^^

profile
    The lookup profile. It determines which directories to search. The profile is the "Context"
    listed in :menuselection:`CTI Server --> Direct directories`.

Optional
^^^^^^^^

term
    the search term that we are looking for

user_id
    the ID of the user doing the search, the `user_id`. Used for searching personal directories.


Errors
------

+------------+---------------+-----------------------------------+
| Error code | Error message | Description                       |
+============+===============+===================================+
|        404 | Not found     | The lookup profile does not exist |
+------------+---------------+-----------------------------------+


Example requests
----------------

Search for the term "Bob"::

    GET /0.1/directories/lookup/default?term=Bob HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

::

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "term": "Bob",
      "column_headers": ["Firstname", "Lastname", "Phone number", "Mobile", "Fax", "Email", "Agent"],
      "column_types": [null, "name", "number_office", "number_mobile", "fax", "email", "agent_relation"],
      "results": [
        {
          "column_values": ["Bob", "Marley", "5555555", "5556666", "5553333", "mail@example.com", null],
          "relations": {
            "agent_id": null,
            "user_id": null,
            "endpoint_id": null
          },
          "source": "my_ldap_directory"
        }, {
          "column_values": ["Charlie", "Boblin", "5555556", "5554444", "5552222", "mail2@example.com", null],
          "relations": {
            "agent_id": 12,
            "user_id": 34,
            "endpoint_id": 56
          },
          "source": "internal"
        }
      ]
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
