*****************************
Contributing to localize XiVO
*****************************

Edit an existing locale
=======================

Update the translation files
----------------------------

Run the following command on the wanted project file :
::

   $ lupdate xivoclient/xivoclient.pro

Edit the translation files
--------------------------

Translation files are located in ``baselib`` and ``xivoclient/i18n``.

Add a new XiVO Client locale
============================

Localizing the XiVO Client goes through four steps :

* Generate the translation files
* Translating the files
* Embedding the translation in the binaries
* Display the new locale to be chosen

Generate translation files
--------------------------

The translation files will be automatically generated from the source code.

For the command to create files for your locale, you need to ensure it is listed in the project file.

There are a few project files you should edit, each one will translate a module of the XiVO Client :

* ``baselib/baselib.pro``
* ``xivoclient/xivoclient.pro``
* ``xivoclient/xletlib.pro``
* ``xivoclient/src/xlets/*/*.pro``

In these files, you should add a line like this one :
::

   TRANSLATIONS += $$ROOT_DIR/i18n/xivoclient_fr.ts

This line adds a translation file for french. Please replace fr by the code of your locale.

For each project file modified, you should run the following command :
::

   $ lupdate xivoclient/xivoclient.pro

This will create the referenced file. The ``$$ROOT_DIR`` variable references either xivoclient or baselib.

Translate the files
-------------------

You can edit the files with extension .ts generated in ``baselib`` or in ``xivoclient/i18n``. For each entry, fill the ``<translation>`` tag with the translation of the ``<source>`` tag.

You can submit your translated files to the xivo-dev@lists.proformatique.com mailing list.

Embed the translation files
---------------------------

For each project previously edited, you should have a corresponding .qrc file. This lists all files that will be embedded in the XiVO Client binaries.
You should then add the corresponding translation files like below :
::

   <file>obj/xivoclient_fr.qm</file>

This embeds the French translation of the ``xivoclient`` module, corresponding to the translation file above. The path is changed to ``obj/`` because the ``.qm`` file will be generated from the ``.ts`` file.

Display the new locale
----------------------

You have to edit the source file ``xivoclient/src/configwidget.cpp`` and add the entry corresponding to your locale in the locale-choosing combobox.
