.. _stock-plugins:

===========================
Stock Plugins Documentation
===========================

View Plugins
============

default_json
------------

View name: default_json

Purpose: present directory entries in JSON format. The format is detailed in http://api.xivo.io.

headers
-------

View name: headers

Purpose: List headers that will be available in results from ``default_json`` view.

privates_view
-------------

View name: privates_view

Purpose: Expose REST API to manage private contacts (create, delete, list).


Service Plugins
===============

lookup
------

Service name: lookup

Purpose: Search through multiple data sources, looking for entries matching a word.

Configuration
^^^^^^^^^^^^^

Example (excerpt from the main configuration file):

.. code-block:: yaml
   :linenos:

   services:
       lookup:
           default:
               sources:
                   - my_csv
               timeout: 0.5

The configuration is a dictionary whose keys are profile names and values are configuration specific
to that profile.

For each profile, the configuration keys are:

sources
   The list of source names that are to be used for the lookup

timeout
   The maximum waiting time for an answer from any source. Results from sources that take longer to
   answer are ignored. Default: no timeout.

favorites
---------

Service name: favorites

Purpose: Mark/unmark contacts as favorites and get the list of all favorites.

privates
--------

Service name: privates

Purpose: Add, delete, list private contacts of users.

The ``privates`` service needs a working Consul installation to store private contacts.


Configuration
^^^^^^^^^^^^^

Example (excerpt from the main configuration file):

.. code-block:: yaml
   :linenos:

   services:
       favorites:
           default:
               sources:
                   - my_csv
               timeout: 0.5

The configuration is a dictionary whose keys are profile names and values are configuration specific
to that profile.

For each profile, the configuration keys are:

sources
   The list of source names that are to be used for the lookup

timeout
   The maximum waiting time for an answer from any source. Results from sources that take longer to
   answer are ignored. Default: no timeout.


Back-end Configuration
======================

This sections completes the :ref:`sources_configuration` section.

csv
---

Back-end name: csv

Purpose: read directory entries from a CSV file.

Limitations:

* the CSV delimiter is not configurable (currently: ``,`` (comma)).

Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
   :linenos:

   type: csv
   name: my_csv
   file: /var/tmp/test.csv
   unique_column: id
   searched_columns:
       - fn
       - ln
   format_columns:
       lastname: "{ln}"
       firstname: "{fn}"
       number: "{num}"

With the CSV file:

.. code-block:: text
   :linenos:

   id,fn,ln,num
   1,Alice,Abrams,55553783147
   2,Bob,Benito,5551354958
   3,Charles,Curie,5553132479


file
   the absolute path to the CSV file

unique_column
   the column that contains a unique identifier of the entry. This is necessary for listing and
   identifying favorites.


CSV web service
---------------

Back-end name: csv_ws

Purpose: search using a web service that returns CSV formatted results.


Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
    :linenos:

    type: csv_ws
    name: a_csv_web_service
    lookup_url: "http://example.com:8000/ws-phonebook?search={term}"
    reverse_lookup_url: "http://example.com:8000/ws-phonebook?phonesearch={term}"
    list_url: "http://example.com:8000/ws-phonebook"
    delimiter: ","
    timeout: 16
    unique_column: id
    source_to_display_columns:
        exten: number

lookup_url
    the URL used for directory searches. Looked up columns are managed by the web service.

reverse_lookup_url
    the URL used for reverse searches. This URL usually does an exact match search on the phone number.

list_url (optional)
    the URL used to list all available entries. This URL is used to retrieve favorites.

delimiter
    the field delimiter in the CSV result.

timeout (optional)
    the number of seconds before the lookup on the web service is aborted, default is 10 seconds.


ldap
----

Back-end name: ldap

Purpose: search directory entries from an LDAP server.

Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
   :linenos:

   type: ldap
   name: my_ldap
   ldap_uri: ldap://example.org
   ldap_base_dn: ou=people,dc=example,dc=org
   ldap_username: cn=admin,dc=example,dc=org
   ldap_password: foobar
   unique_column: objectGUID  # Active Directory
   unique_column: entryUUID  # OpenLDAP
   searched_columns:
       - cn
   format_columns:
       firstname: "{givenName}"
       lastname: "{sn}"
       number: "{telephoneNumber}"


ldap_uri
   the URI of the LDAP server. Can only contains the scheme, host and port part of an LDAP URL.

ldap_base_dn
   the DN of the entry at which to start the search

ldap_username (optional)
   the user's DN to use when performing a "simple" bind.

   Default to an empty string.

   When both ldap_username and ldap_password are empty, an anonymous bind is performed.

ldap_password (optional)
   the password to use when performing a "simple" bind.

   Default to an empty string.

ldap_custom_filter (optional)
   a custom LDAP filter to use when performing searches instead of searching in the column specified
   by the ``searched_columns`` option.

   This must be a valid `LDAP filter <https://tools.ietf.org/html/rfc4515>`_, where the string ``%Q`` will be replaced by the (escaped) search
   term when performing a search.

   Example: ``(&(o=ACME)(cn=*%Q*))``

ldap_network_timeout (optional)
   the maximum time, in second, that an LDAP network operation can take. If it takes more time than
   that, no result is returned.

   Defaults to 0.1.

ldap_timeout (optional)
   the maximum time, in second, that an LDAP operation can take.

   Defaults to 1.0.

unique_column (optional)
   the column that contains a unique identifier of the entry. This is necessary for listing and
   identifying favorites.


phonebook
---------

Back-end name: phonebook

Purpose: search directory entries from a XiVO :ref:`phone book <phonebook>`.

Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
   :linenos:

   type: phonebook
   name: my_phonebook
   phonebook_url: https://example.org/service/ipbx/json.php/restricted/pbx_services/phonebook
   phonebook_username: admin
   phonebook_password: foobar
   format_columns:
       firstname: "{phonebook.firstname}"
       lastname: "{phonebook.lastname}"
       number: "{phonebooknumber.office.number}"


phonebook_url (optional)
   the phonebook's URL.

   Default to ``http://localhost/service/ipbx/json.php/private/pbx_services/phonebook``.

   The URL to use differs depending on if you are accessing the phone book locally or remotely:

   * Local: ``http://localhost/service/ipbx/json.php/private/pbx_services/phonebook``
   * Remote: ``https://example.org/service/ipbx/json.php/restricted/pbx_services/phonebook``

phonebook_username (optional)
   the username to use in HTTP requests.

   No HTTP authentication is tried when phonebook_username or phonebook_password are empty.

phonebook_password (optional)
   the password to use in HTTP requests.

phonebook_timeout (optional)
   the HTTP request timeout, in seconds.

   Defaults to 1.0.

To be able to access the phone book of a remote XiVO, you must create a web services access user
(:menuselection:`Configuration -> Web Services Access`) on the remote XiVO.


privates
--------

Back-end name: privates

Purpose: search directory entries among users' private contacts

You should only have one source of type ``privates``, because only one will be used to list private
contacts. The ``privates`` backend needs a working Consul installation. This backend works with the
privates service, which allows users to add private contacts.

The complete list of fields is in :ref:`private-contact-attributes`.

Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
   :linenos:

   type: privates
   name: privates
   format_columns:
       firstname: "{firstname}"
       lastname: "{lastname}"
       number: "{number}"

``unique_column`` is not configurable, its value is always ``id``.


xivo
----

Back-end name: xivo

Purpose: add users from a XiVO (may be remote) as directory entries

Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
   :linenos:

   type: xivo
   name: my_xivo
   confd_config:
       https: True
       host: xivo.example.com
       port: 9486
       version: 1.1
       username: admin
       password: password
       timeout: 3
   unique_column: id
   searched_columns:
       - firstname
       - lastname
   format_columns:
       number: "{exten}"
       mobile: "{mobile_phone_number}"

confd_config:host
   the hostname of the XiVO (more precisely, of the xivo-confd service)

confd_config:port
   the port of the xivo-confd service (usually 9486)

confd_config:version
   the version of the xivo-confd API (should be 1.1)
