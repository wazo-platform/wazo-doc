***********
Directories
***********

This page documents how to add directories from custom sources. The menu is accessible in :menuselection:`Configuration --> Management --> Directories`.

Directories can be used for lookup via the :ref:`CTI Client <remote_directory_xlet>`, via the :ref:`directory feature of phones <remote-directory>` or for :ref:`reverse lookup <reverse_lookup>` on incoming calls.


Add a data source
=================

File directories
----------------

The source file of the directory must be in CSV format. You will be able to choose the headers and the separator in the next steps. For example, the file will look like::

    title|firstname|lastname|displayname|society|mobilenumber|email|
    mr|Emmett|Brown|Brown Emmett|DMC|5555551234|emmet.brown@dmc.example.com|


Webservice directories
----------------------

The data returned by the Web service must have the same format than the file directory. In the same way, you will be able to choose the headers and the separator in the next step.


Configure the access to the data source
=======================================

Go in :menuselection:`Services --> CTI Server --> Directories --> Definitions` and add a new directory.

* `URI`: your data source
* `Delimiter`: the field delimiter in your data source
* `Direct match`: the headers of your data source used to match entries for direct lookup
* `Match reverse directories`: idem, but for reverse lookup
* `Mapped field`:

  * the `fieldname` is the identifier of the field. It will be used in the display filter, so look there if you want to use an existing one, or make it up if you want a custom display filter.
  * the `value` is the corresponding header of your data source.

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