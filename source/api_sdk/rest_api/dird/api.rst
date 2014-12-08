.. _dird-api:

********************
XiVO directories API
********************

Contacts and directories in XiVO are managed by the xivo-dird daemon. This
service provides a public API that can be used to query the directories that are
configured on a XiVO.

.. warning:: The 0.1 API is currently in development. Major changes could still
   happen and new resources will be added over time.


Lookup
======

The `lookup` query will return a list of result matching the searched term. The
result will be retrieved from all configured directories for the given profile.

This route is provided by the `default_json_view` plugin using the `lookup`
plugin and all configured sources for the given profile.


Query
-----

::

    GET /0.1/directories/lookup/<profile>


Parameters
----------

Mandatory
^^^^^^^^^

profile
    The lookup profile. It determines which directories to search. See
    :ref:`configuration-file`.


Optional
^^^^^^^^

term
    the search term that we are looking for

`*`
    any other arguments will be forwarded to the configured source and may be
    interpreted or ignored. Extra arguments can also be used by other plugins
    to add other functionalities.


Errors
------

+------------+---------------+-----------------------------------+
| Error code | Error message | Description                       |
+============+===============+===================================+
|        404 | Not found     | The lookup profile does not exist |
+------------+---------------+-----------------------------------+


Example requests
----------------

Search for the term ``Bob``

.. code-block:: http

    GET /0.1/directories/lookup/default?term=Bob HTTP/1.1
    Host: xivoserver
    Accept: application/json


Example response
----------------

Header
^^^^^^

.. code-block:: http

    HTTP/1.1 200 OK
    Content-Type: application/json


Content
^^^^^^^

.. code-block:: javascript
   :linenos:
   :emphasize-lines: 7, 15

    {
      "term": "Bob",
      "column_headers": ["Firstname", "Lastname", "Phone number", "Mobile", "Fax", "Email", "Agent"],
      "column_types": [null, "name", "number_office", "number_mobile", "fax", "email", "relation_agent"],
      "results": [
        {
          "column_values": ["Bob", "Marley", "5555555", "5556666", "5553333", "mail@example.com", null],
          "relations": {
            "agent": null,
            "user": null,
            "endpoint": null
          },
          "source": "my_ldap_directory"
        }, {
          "column_values": ["Charlie", "Boblin", "5555556", "5554444", "5552222", "mail2@example.com", null],
          "relations": {
            "agent": {
              "id": 12,
              "xivo_id": "ad2f36c7-b0f3-48da-a63c-37434fed479b"
            },
            "user": {
              "id": 34,
              "xivo_id": "ad2f36c7-b0f3-48da-a63c-37434fed479b"
            },
            "endpoint": {
              "id": 56,
              "xivo_id": "ad2f36c7-b0f3-48da-a63c-37434fed479b"
            },
          },
          "source": "internal"
        }
      ]
    }


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
