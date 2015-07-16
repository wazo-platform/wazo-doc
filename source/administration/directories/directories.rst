.. _directories:

***********
Directories
***********

This page documents how to add and configure directories from custom sources. Directories added from
custom sources can be used for lookup via the :ref:`CTI Client <remote_directory_xlet>` or for
:ref:`reverse lookup <reverse_lookup>` on incoming calls. The directory feature of phones do not use
these data sources.

.. note:: This page describes how to add custom sources of contacts. For other sources of contacts,
          see :ref:`phonebook`, and :ref:`ldap`.


Add a data source
=================

You can add new data sources via the :menuselection:`Configuration --> Management --> Directories` page.


XiVO directories
----------------

This type of directory is used to query the users of a XiVO. On a fresh install,
the local XiVO is already configured. The URI field for this type of directory
should be the base URL of a `xivo-confd` server.

This directory type matches the `xivo` backend in `xivo-dird`.

Example:

* `Directory name`: xivo-montreal
* `Type`: xivo
* `URI`: ``https://<remote-ip>:<port>``


File directories
----------------

The source file of the directory must be in CSV format. You will be able to choose the headers and the separator in the next steps. For example, the file will look like::

    title|firstname|lastname|displayname|society|mobilenumber|email
    mr|Emmett|Brown|Brown Emmett|DMC|5555551234|emmet.brown@dmc.example.com

Example:

* `Directory name`: csv-phonebook
* `Type`: File
* `URI`: ``/data/csv-phonebook.csv``


Web service directories
-----------------------

The data returned by the Web service must have the same format than the file directory. In the same way, you will be able to choose the headers and the separator in the next step.

Example:

* `Directory name`: ws-phonebook
* `Type`: Webservices
* `URI`: ``http://example.org:8000/ws-phonebook``


Configure the access to the data source
=======================================

Go in :menuselection:`Services --> CTI Server --> Directories --> Definitions` and add a new directory definition.

* `URI`: your data source
* `Delimiter`: the field delimiter in your data source
* `Direct match`: the key used to match entries for direct lookup
* `Match reverse directories`: idem, but for reverse lookup
* `Mapped field`:

  * the `fieldname` is the identifier of the field. It will be used in the display filter, so look there if you want to use an existing one, or make it up if you want a custom display filter.
  * the `value` is the corresponding header of your data source.


File directories
----------------

For file directories, the `Direct match` and the `Match reverse directories` must be filled with
the name of the column used to match entries.

For example, given you have the following CSV::

   name|phone
   John|5551234

And you want to do direct lookup on the ``name`` column and reverse lookup on the ``phone`` column,
then you'll use:

* `Direct match`: name
* `Match reverse directories`: phone


Web service directories
-----------------------

For web service directories, the `Direct match` and the `Match reverse directories` must be filled
with the name of the HTTP query parameter that will be used when doing the HTTP requests.

For example, given you have the following directory definition:

* `Direct match`: search
* `Match reverse directories`: phonesearch

When a direct lookup for "John" is performed, then the following HTTP request::

   GET /ws-phonebook?search=John HTTP/1.1

is emitted. When a reverse lookup for "5551234" is performed, then the following HTTP request::

   GET /ws-phonebook?phonesearch=5551234 HTTP/1.1

is emitted.

Note that the CSV returned by the Web service is not further processed.


Reverse lookup
--------------

To enable reverse lookup, you need to add an entry in `Mapped fields`:

* `Fieldname`: reverse
* `Value`: the header of your data source that you want to see as the caller ID on your phone on incoming calls


Configure the display of the data
=================================

Edit the default display filter or create your own in :menuselection:`Services --> CTI Server --> Directories --> Display filters`.

Each line in the display filter will result in a header in your XiVO Client.

* `Field title` will be the text displayed in the header
* `Display format` is a format string, for example ``{db-firstname} {db-lastname}``, where ``{db-***}`` will be replaced with the value from the data source. ``***`` is the identifier of the field configured in the directory definition, ```not``` the header of your data source.


Make your directory available
=============================

Go in :menuselection:`Services --> CTI Server --> Directories --> Reverse/Direct directories`, select your display filter if needed and add the directory you just created.

You may have to restart the CTI Server or the AGI daemon to apply the change::

    service xivo-ctid restart
    service xivo-agid restart
