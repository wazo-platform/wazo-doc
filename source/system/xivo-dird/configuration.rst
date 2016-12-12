.. _dird-configuration-file:

=======================
xivo-dird configuration
=======================

There are three sources of configuration for xivo-dird:

* the :ref:`command line options <xivo-dird-usage>`
* the main configuration file
* the sources configuration directory

The command-line options have priority over the main configuration file options.


Main Configuration File
=======================

Default location: ``/etc/xivo-dird/config.yml``. Format: YAML

The default location may be overwritten by the command line options.

Here's an example of the main configuration file:

.. code-block:: yaml
   :linenos:

   debug: False
   foreground: False
   log_filename: /var/log/xivo-dird.log
   log_level: info
   pid_filename: /var/run/xivo-dird/xivo-dird.pid
   source_config_dir: /etc/xivo-dird/sources.d
   user: www-data

   rest_api:
       wsgi_socket: /var/run/xivo-dird/xivo-dird.sock

   enabled_plugins:
      backends:
          - csv
          - ldap
          - phonebook
      services:
          - lookup
      views:
          - cisco_view
          - default_json

   views:
       displays:
           switchboard_display:
               -
                   title: Firstname
                   default: Unknown
                   field: firstname
                   type: name
               -
                   title: Lastname
                   default: Unknown
                   field: lastname
                   type: name
           default_display:
               -
                   title: Firstname
                   field: fn
                   type: name
               -
                   title: Location
                   default: Canada
                   field: country
               -
                   title: Number
                   field: number
                   type: number
       displays_phone:
           default:
               name:
                   - display_name
               number:
                   -
                       field:
                           - phone
                   -
                       field:
                           - phone_mobile
                       name_format: "{name} (Mobile)"
        profile_to_display:
            default: default_display
            switchboard: switchboard_display
        profile_to_display_phone:
            default: default

   services:
       lookup:
           default:
               sources:
                   - my_csv
                   - ldap_quebec
               timeout: 0.5
           switchboard:
               sources:
                   - my_csv
                   - xivo_phonebook
                   - ldap_quebec
               timeout: 1

   sources:
       my_source:
           name: my_source
           type: ldap
           ldap_option1: value
           ldap_option2: value
           ...


Root section
------------

debug
   Enable log debug messages. Overrides ``log_level``. Default: ``False``.

foreground
   Foreground, don't daemonize. Default: ``False``.

log_filename
   File to write logs to. Default: ``/var/log/xivo-dird.log``.

log_level
   Logs messages with LOG_LEVEL details. Must be one of: ``critical``, ``error``, ``warning``,
   ``info``, ``debug``. Default: ``info``.

pid_filename
   File used as lock to avoid multiple xivo-dird instances. Default:
   ``/var/run/xivo-dird/xivo-dird.pid``.

source_config_dir
   The directory from which sources configuration are read. See
   :ref:`dird-sources_configuration`. Default: ``/etc/xivo-dird/sources.d``.

user
   The owner of the process. Default: ``www-data``.


enabled_plugins section
-----------------------

This sections controls which plugins are to be loaded at xivo-dird startup. All plugin types must
have at least one plugin enabled, or xivo-dird will not start. For back-end plugins, sources using a
back-end plugin that is not enabled will be ignored.


views section
-------------

displays
   A dictionary describing the content of each display. The key is the display's name, and the value
   are the display's content.

   The display content is a list of fields. Each field is a dictionary with the following keys:

   * title: The label of the field
   * default: The default value of the field
   * type: An arbitrary identifier of the field. May be used by consumers to identify the field
     without matching the label. For meaningful values inside Wazo, see
     :ref:`xivo-dird-integration`.
   * field: the key of the data from the source that will be used for this field.

   The display may be used by a plugin view to configure which fields are to be presented to the
   consumer.

.. _dird-config-displays_phone:

displays_phone
   A dictionary describing the content of phone-related displays. Like ``displays``, the key is the
   display's name and the value is the display's content. These displays are used by phone-related
   view plugins, like the ``cisco_view`` plugin.

   The display content contains 2 keys, ``name`` and ``number``.

   The value of the ``name`` key is a list of source result fields. For a given source result, the
   first field that will return a non-empty value will be used as the display name on the phone.
   For example, if ``name`` is configured with ``["display_name", "name"]`` and you have a source result
   with fields ``{"display_name": "", "name": "Bob"}``, then "Bob" will be displayed on the phone.

   The value of the ``number`` key is a list of number item. Each item is composed of a dictionary
   containing at least a ``field`` key, and optionally a ``name_format`` key. For example, if you
   have the following number configuration::

      name:
          - display_name
      number:
          -
              field:
                  - phone
          -
              field:
                  - phone_mobile
              name_format: "{name} (Mobile)"

   and you have a source result ``{"display_name": "Bob", "phone": "101", "phone_mobile": "102"}``,
   then 2 results will be displayed on your phone:

   #. "Bob", with number "101"
   #. "Bob (Mobile)", with number "102"

   The ``name_format`` value is a python format string. There's two substitution variables
   available, ``{name}`` and ``{number}``.

profile_to_display
   A dictionary associating a profile to a display. It allows xivo-dird to use the right display
   when a consumer makes a query with a profile. The key is the profile name and the value is the
   display name.

profile_to_display_phone:
   A dictionary associating a profile to a phone display. This is similar to ``profile_to_display``,
   but only used by phone-related view plugins.


services section
----------------

This section is a dictionary whose keys are the service plugin name and values are the configuration
of that service. Hence the content of the value is dependent of the service plugin. See the
documentation of the service plugin (:ref:`stock-plugins`).


sources section
---------------

This section is a dictionary whose keys are the source name and values are the configuration for that
source. See the :ref:`dird-sources_configuration` section for more details about source
configuration.


.. _dird-sources_configuration:

Sources Configuration
=====================

There are two ways to configure sources:

* in the sources section of the main configuration
* in files of a directory, one file for each source:

  * Default directory location ``/etc/xivo-dird/sources.d``
  * Files format: YAML
  * File names are ignored
  * Each file listed in this directory will be read and used to create a data source for xivo-dird.

Here is an example of a CSV source configuration in its own file:

.. code-block:: yaml
   :linenos:

   type: csv
   name: my_contacts_in_a_csv_file
   file: /usr/local/share/my_contacts.csv
   unique_column: id
   searched_columns:
       - fn
       - ln
   format_columns:
       name: "{fn} {ln}"
       number: "{num}"


This is strictly equivalent in the main configuration file:

.. code-block:: yaml
   :linenos:

   sources:
       my_contacts_in_a_csv_file:
           type: csv
           name: my_contacts_in_a_csv_file
           file: /usr/local/share/my_contacts.csv
           unique_column: id
           searched_columns:
               - fn
               - ln
           source_to_display_columns:
               ln: lastname
               fn: firstname
               num: number

type
   the type of the source. It must be the same than the name of one of the enabled back-end plugins.

name
   is the name of this given configuration. The name is used to associate the source to profiles.
   The value is arbitrary, but it must be unique across all sources.

.. warning:: Changing the name of the source will make all favorites in that source disappear. There
             is currently no tool to help you migrate favorites between source names, so choose your
             source names carefully.

The other options are dependent on the source type (the back-end used). See the documentation of the
back-end plugin (:ref:`stock-plugins`). However, the following keys should be present in all source
configurations:

first_matched_columns (optional)
   the columns used for the reverse lookup. Any column having the search term will be a reverse
   lookup result.

format_columns (optional)
   a mapping between result fields and a format string. The new key will be added to the result, if
   this name already exists in the result, it will be replaced with the new value. The syntax is a
   python format string. See https://docs.python.org/2/library/string.html#formatspec for a complete
   reference.

searched_columns (optional)
   the columns used for the lookup. Any column containing the search term substring will be a lookup
   result.

unique_column (optional)
   This column is what makes an entry unique in this source. The ``unique_column`` is used to build
   the ``uid`` that is passed to the list method to fetch a list of results by unique ids. This is
   necessary for listing and identifying favorites.
