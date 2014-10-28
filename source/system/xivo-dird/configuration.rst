.. _configuration-file:

=======================
XiVO dird configuration
=======================

There are three sources of configuration for xivo-dird:

* the :ref:`command line options <xivo-dird-usage>`
* the main configuration file
* the sources configuration directory

The command-line options have priority over the main configuration file options.


Main Configuration File
=======================

Default location: ``/etc/xivo/xivo-dird/xivo-dird.yml``.
Format: YAML

The default location may be overwritten by the command line options.

Here's an example of the main configuration file:

.. code-block:: yaml
   :linenos:

   debug: False
   foreground: False
   log_filename: /var/log/xivo-dird.log
   log_level: info
   pid_filename: /var/run/xivo-dird/xivo-dird.pid
   source_config_dir: /etc/xivo/xivo-dird/sources.d
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
          - aastra_xml
          - default_json

   views:
       displays:
           switchboard_display:
               -
                   title: Firstname
                   default: Unknown
                   field: firstname
               -
                   title: Lastname
                   default: Unknown
                   field: lastname
           default_display:
               -
                   title: Firstname
                   field: fn
               -
                   title: Location
                   default: Canada
                   field: country
               -
                   title: Number
                   field: number
        profile_to_display:
            default: default_display
            switchboard: switchboard_display

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
   :ref:`sources_configuration_directory`. Default: ``/etc/xivo/xivo-dird/sources.d``.

user
   The owner of the process. Default: ``www-data``.


rest_api section
----------------

wsgi_socket
   The socket used for WSGI communications (between nginx and xivo-dird). Default:
   ``/var/run/xivo-dird/xivo-dird.sock``.


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
   * field: An arbitrary identifier of the field. May be used by consumers to identify the field
     without matching the label.

   The display may be used by a plugin view to configure which fields are to be presented to the
   consumer.

profile_to_display
   A dictionary associating a profile to a display. It allows xivo-dird to use the right display
   when a consumer makes a query with a profile. The key is the profile name and the value is the
   display name.


services section
----------------

This section is a dictionary whose keys are the service plugin name and values are the configuration
of that service. Hence the content of the value is dependent of the service plugin. See the
documentation of the service plugin.


.. _sources_configuration_directory:

Sources Configuration Directory
===============================

Default location: ``/etc/xivo/xivo-dird/sources.d``
File format: YAML

Here is an example of a CSV source configuration:

.. code-block:: yaml
   :linenos:

   type: csv
   name: my_contacts_in_a_csv_file
   file: /usr/local/share/my_contacts.csv
   searched_columns: ['Firstname', 'Lastname', ..., 'E-mail']

type
   The type of the source. It must be the same than the name of one of the enabled back-end plugins.

name
   The name of the source. The value is arbitrary, but it must be unique across all sources.

The other options are dependent on the source type (the back-end used). See the documentation of the
back-end plugin.
