.. _stock-plugins:

===========================
Stock Plugins Documentation
===========================

View Plugins
============

default_json
------------

Purpose: present directory entries in JSON format. The format is detailed in :ref:`dird-api`.

Service Plugins
===============

lookup
------

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
   answer are ignored.


Back-end Configuration
======================

This sections completes the :ref:`sources_configuration_directory` section.

csv
---

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
   unique_columns:
       - fn
       - ln
   searched_columns:
       - fn
       - ln
   source_to_display:
       ln: lastname
       fn: firstname
       num: number

With the CSV file:

.. code-block:: text
   :linenos:

   fn,ln,num
   Alice,Abrams,55553783147
   Bob,Benito,5551354958
   Charles,Curie,5553132479


file
   the absolute path to the CSV file

unique_columns
   the list of columns that form a unique identifier of the entry. This is necessary for listing and
   identifying favorites.
