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

personal_view
-------------

View name: personal_view

Purpose: Expose REST API to manage personal contacts (create, delete, list).

aastra_view
-----------

View name: aastra_view

Purpose: Expose REST API to search in configured directories for Aastra phone.

cisco_view
----------

View name: cisco_view

Purpose: Expose REST API to search in configured directories for Cisco phone (see CiscoIPPhone_XML_Objects_).

.. _CiscoIPPhone_XML_Objects: http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/8_5_1/xsi_dev_guide/xmlobjects.html

polycom_view
-------------

View name: polycom_view

Purpose: Expose REST API to search in configured directories for Polycom phone.

snom_view
---------

View name: snom_view

Purpose: Expose REST API to search in configured directories for Snom phone.

thomson_view
------------

View name: thomson_view

Purpose: Expose REST API to search in configured directories for Thomson phone.

yealink_view
------------

View name: yealink_view

Purpose: Expose REST API to search in configured directories for Yealink phone.


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

sort
   The list of columns to sort the results. Multiple columns can be set and the order is important.
   If is not defined, the lookup paging will not work properly.

favorites
---------

Service name: favorites

Purpose: Mark/unmark contacts as favorites and get the list of all favorites.


.. _dird_services_personal:

personal
--------

Service name: personal

Purpose: Add, delete, list personal contacts of users.

The ``personal`` service needs a working Consul installation to store personal contacts.


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

.. _dird-backend-csv:

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


.. _dird-backend-csv_ws:

CSV web service
---------------

Back-end name: csv_ws

Purpose: search using a web service that returns CSV formatted results.

Given the following configuration, *xivo-dird* would call
"http://example.com:8000/ws-phonebook?firstname=alice&lastname=alice" for a
lookup for the term "alice".


Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
    :linenos:

    type: csv_ws
    name: a_csv_web_service
    lookup_url: "http://example.com:8000/ws-phonebook"
    reverse_lookup_url: "http://example.com:8000/ws-phonebook"
    list_url: "http://example.com:8000/ws-phonebook"
    searched_columns:
      - firstname
      - lastname
    delimiter: ","
    timeout: 16
    unique_column: id
    format_columns:
        number: "{exten}"

lookup_url
    the URL used for directory searches.

reverse_lookup_url
    the URL used for reverse searches. This URL usually does an exact match search on the phone number.

list_url (optional)
    the URL used to list all available entries. This URL is used to retrieve favorites.

searched_columns
    the columns to use for the search.

delimiter
    the field delimiter in the CSV result.

timeout (optional)
    the number of seconds before the lookup on the web service is aborted, default is 10 seconds.


.. _dird-backend-ldap:

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
   ldap_custom_filter: (l=québec)
   unique_column: entryUUID
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
   the custom filter is used to add more criteria to the filter generated by the back end.

   Example:

   * ldap_custom_filter: (l=québec)
   * searched_columns: [cn,st]

   will result in the following filter being used for searches. ``(&(l=québec)(|(cn=*%Q*)(st=*%Q*)))``

   If only the custom filter is to be used, leave the ``searched_columns`` field
   empty.

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

   For OpenLDAP, you should set this option to "entryUUID".

   For Active Directory, you should set this option to "objectGUID" and also set the
   "unique_column_format" option to "binary_uuid".

unique_column_format (optional)
   the unique column's type returned by the queried LDAP server. Valid values are "string" or
   "binary_uuid".

   Defaults to "string".


.. _dird-backend-phonebook:

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


personal
--------

Back-end name: personal

Purpose: search directory entries among users' personal contacts

You should only have one source of type ``personal``, because only one will be used to list personal
contacts. The ``personal`` backend needs a working Consul installation. This backend works with the
personal service, which allows users to add personal contacts.

The complete list of fields is in :ref:`personal-contact-attributes`.

Configuration
^^^^^^^^^^^^^

Example (a file inside ``source_config_dir``):

.. code-block:: yaml
   :linenos:

   type: personal
   name: personal
   format_columns:
       firstname: "{firstname}"
       lastname: "{lastname}"
       number: "{number}"

``unique_column`` is not configurable, its value is always ``id``.


.. _dird-backend-xivo:

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
