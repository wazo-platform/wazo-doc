**************************************
Manage Translations of the XiVO Client
**************************************

This sections describes how to manage XiVO Client translations from a developer
point of view. If you want to help translate the XiVO Client, see
:doc:`Translating XiVO <../translate>`

You need to install these tools::

   pip install transifex-client
   apt-get install qt4-dev-tools


How to Add a New Translated String
==================================

String to be translated is marked using the tr macro in the source code.


Example::

   tr("Number");


Updating translations on transifex
----------------------------------

Run the following commands from the root of the xivo-client-qt project::

    make pushtr

After this command, you can visit `Transifex`_, and check that the xivo-client is 100% translated
for your language. Once all the translations have been checked, run the 3 following commands::

    make pulltr
    git commit
    git push

.. _Transifex: https://www.transifex.com/proformatique/xivo/

.. warning:: Under Arch Linux, you must have qt5 installed and prepend ``QT_PATH=/usr/bin`` before
             ``make {pull,push}tr``.


Add a new XiVO Client locale
============================

Localizing the XiVO Client goes through four steps :

* Creating the new translation in Transifex
* Generatint the translation files
* Embedding the translation in the binaries
* Displaying the new locale to be chosen


Creating the new translation in Transifex
-----------------------------------------

Log into Transifex and click the ``Create language`` option.


Generate translation files
--------------------------

The translation files will be automatically generated from the source code.

For the command to create files for your locale, you need to ensure it is listed
in the project file.

There are a few project files you should edit, each one will translate a module
of the XiVO Client :

* :file:`baselib/baselib.pro`
* :file:`xivoclient/xivoclient.pro`
* :file:`xivoclient/xletlib.pro`
* :file:`xivoclient/src/xlets/*/*.pro`

In these files, you should add a line like this one::

   TRANSLATIONS += $$ROOT_DIR/i18n/xivoclient_fr.ts

This line adds a translation file for french. Please replace fr by the code of
your locale. The ``$$ROOT_DIR`` variable references either xivoclient or
baselib.

You can use a command like the following to automate this ($LANG is the new language)::

   find . -name '*.pro' -exec sed -i -e 's|^TRANSLATIONS += $${\?ROOT_DIR}\?/i18n/\(.*\)_en.ts|\0\nTRANSLATIONS += $$ROOT_DIR/i18n/\1_$LANG.ts|' {} \;

To actually create the files, you will have to use the translation managing
script. But first, you must tell the script about your new locale. Edit the
:file:`utils/translations.sh` file and add your locale to the ``LOCALES``
variable. Then, you can run the script::

   $ make pulltr

Embed the translation files
---------------------------

For each project previously edited, you should have a corresponding ``.qrc``
file. These resource files list all files that will be embedded in the XiVO
Client binaries.  You should then add the corresponding translation files like
below::

   <file>obj/xivoclient_fr.qm</file>

This embeds the French translation of the ``xivoclient`` module, corresponding
to the translation file above. The path is changed to ``obj/`` because the
``.qm`` file will be generated from the ``.ts`` file.

You can use a command like the following to automate this ($LANG is the new language)::

   find . -name '*.qrc' -exec sed -i -e 's|^\( *\)<file>\(.*\)obj/\(.*\)_fr.qm</file>|\0\n\1<file>\2obj/\3_$LANG.qm</file>|' {} \;


Display the new locale
----------------------

You have to edit the source file :file:`xivoclient/src/configwidget.cpp` and add
the entry corresponding to your locale in the locale-choosing combobox.
