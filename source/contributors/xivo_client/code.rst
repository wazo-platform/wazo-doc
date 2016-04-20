**********************
Coding the XiVO Client
**********************

Project folder map
==================

baselib
-------

The folder `baselib` contains all files necessary to build the baselib. It contains the necessary
code and data structures to communicate with the XiVO CTI server.

This library is designed to be reusable by other XiVO CTI clients. If you want to build it
without the rest of the XiVO Client, go in its folder and type::

   $ qmake && make

The library will be available in the new bin folder.

xivoclient
----------

The folder `xivoclient` contains all other source files included in the XiVO Client.

`src` contains the source code files, `images` contains the images, `i18n` contains the
translation files and `qtaddons` contains some Qt addons used by the XiVO Client.

src
---

The source files are separated in three categories :

* the XiVO Client itself, the source files are directly in `src`.
* the XLet library (`xletlib`) contains the code common to multiple XLets (plugins),
  like the XLet base class and mainly GUI stuff.
* the XLets themselves (`xlets`), each one is in a `xlets/something` subfolder.

Each XLet is compiled into a dynamic library, but some XLets are still compiled within the
xivoclient executable instead of in a separated library. They are marked with a `*-builtin`
subfolder name.

delivery
--------

This folder contains all license informations necessary for the XiVO Client to be redistributed,
i.e. the GNU GPLv3 and the additional requirements.

Configuration access
====================

The settings of the application are stored in BaseEngine for runtime and in files when the client is closed :

* `~/.config/XiVO` on GNU/Linux systems
* (what about other platforms?)

There are now 3 sets of functions from BaseEngine that you can use to read/store settings :

getConfig() / setConfig()
-------------------------

They are proxy methods to use the BaseConfig object inside BaseEngine. They use QVariantMap to store
the settings values. They are currently used to store/retrieve options used in the ConfigWidget.

You can find the available keys to access data in the detailed Doxygen documentation of BaseEngine,
 or in `baseengine.h`.

Note that the settings stored in BaseConfig won't be written in the configuration file if BaseEngine
is not aware of their existence (loaded in `loadSettings` and saved in `saveSettings`).

getSettings()
-------------

Through this function, you can access the lowest level of configuration storage, QSettings.
It also contains the options stored in BaseConfig, but is less easy to use.

This direct access is used for purely graphical settings, only used to remember the appearance of
the GUI until the next launch. These settings don't have to be shared with other widgets, and storing
them directly in QSettings avoids writing code to import/export to/from BaseConfig.

getProfileSetting() / setProfileSetting()
-----------------------------------------

This pair of methods allow you to read/write settings directly in QSettings, but specifically for
the current configuration profile.

Configuration profiles
======================

When starting XiVO Client with an argument, this argument is interpreted as a profile name.
This profile name allows you to separate different profiles, with different configuration options.

For example, configuration profile "profileA" will auto-connect with user A and password B and "profileB"
will not auto-connect, but is set to connect with user C, no password remembered. To invoke these profiles, use :

.. code-block:: javascript

   $ xivoclient profileA
   $ xivoclient profileB

The default configuration profile is default-user.

Recognizing / extracting phone numbers
======================================

Of course, working on XiVO Client implies working with phone numbers. But how to interpret them easily,
when we are not sure of the format they're in?

You can use the PhoneNumber namespace (`baselib/src/phonenumber.h`) to do that, it contains routines
for recognition/extraction of phone numbers, that way you don't have to parse manually.

These subroutines are pretty basic for the moment, if you need/want to improve them, feel free to do it.

Retrieving CTI server infos
===========================

Informations are synchronized from the server to the BaseEngine when the client connects.

It is stored in BaseEngine in "lists". It is stored in a format close to the one used to transmit it,
so you can see the CTI protocol definition for further documentation.

Each list contains objects of different type. These types are :

* channel
* user
* phone
* trunk
* agent
* queue
* group
* meetme
* voicemail
* queuemember
* parking

Each type corresponds to a class derived from XInfo, e.g. channel infos are stored in ChannelInfo objects.

The basic attributes of all objects are 3 strings: the IPBX ID, the XiVO object ID and the extended
ID of the object, which is the two previous attributes linked with a "/".

Listen to IPBX events
---------------------

If you want your XLet to receive IPBX/CTI events, you can do so by inheriting the IPBXListener interface.

You must specify which type of events you want to listen. This depends of the implemented functions in the CTI server.
You can register to listen these events by calling the IPBXListener method :

 registerListener(xxx);

For now, `xxx`, the event type, can take take the values :
* chitchat
* history
* records_campaign
* queuestats

On reception of the specified type of event, BaseEngine will call the `IPBXListener` method `parseCommand(QVariantMap)`.

You should then reimplement this method to make it process the event data, stored in the `QVariantMap` parameter.

The parking XLet
================

There are two concepts here :
* Parked calls: These calls have been parked by a switchboard or an operator.
They are waiting to be answered by a specific person, unlike a queue, where calls will be
answered by one of the agents of the group associated to the queue. Each parked call is given
a phone number so that the call can be answered by everyone.

* Parking lots: They are containers for parked calls. Each parking lot has a phone number,
  used to identify where to send the call we want to park.

ParkingWidget represents a parking lot and contains a table that stores all parked calls.

Adding new XLets
================

When you want to add a new XLet, you can use the basic XLetNull, that only prints "Hello World".
Here is a little script to accelerate the copy from XLetNull.

.. code-block:: none

   #!/usr/bin/env sh

   newname="newname" # Replaces xletnull
   NewName="NewName" # Replaces XLetNull & XletNull
   NEWNAME="NEWNAME" # Replaces XLETNULL  
   
   if [ ! -d xletnull ] ; then
   
       echo "Please execute this script in XIVO_CLIENT/plugins"
       echo $newname
       exit 1
   fi
   
   cp -r xletnull $newname
   cd $newname
   rm -f moc* *.o Makefile
   
   for f in $(find . -type f -print) ; do
       mv $f `echo $f | sed s/xletnull/$newname/`
   done
   
   find . -type f -exec sed -i "s/xletnull/$newname/g;s/X[Ll]etNull/$NewName/g;s/XLETNULL/$NEWNAME/g" {} \;</nowiki>

Before executing the script, just replace the first three variables with the name of the new XLet.

Then, you must add a line in xivoclient/xlets.pro to add your new directory to the SUBDIRS variable.

Then you can start implementing your new class. The <xletname>Plugin class is only an interface between the main app and your XLet.

Translations
------------

If you want to localize your XLet, there are four steps.

Modify the sources
------------------

In the <xletname>Plugin constructor, add the line :

 b_engine->registerTranslation(":/<xletname>_%1");

before the return instruction.

Modify the project file
-----------------------

Add these lines in the .pro file in your XLet directory :

 TRANSLATIONS = <xletname>_fr.ts
 TRANSLATIONS += <xletname>_nl.ts

 RESOURCES = res.qrc

Replace fr and nl with the languages you want.

Create the resource file
------------------------

In a file res.qrc in your XLet directory, put these lines :

.. code-block:: xml

    <!DOCTYPE RCC><RCC version="1.0">
        <qresource>
            <file><xletname>_fr.qm</file>
            <file><xletname>_nl.qm</file>
        </qresource>
    </RCC>

These files will be embedded in the Xlet library binary.

Create the translation files
----------------------------

In your XLet directory, run :

 lupdate <xletname>.pro

This creates as much .ts translation files as specified in the .pro file. You can now translate strings in these file.

The XLet will now be compiled and translated.

Add a new XLet
==============

For now, it is not possible to add easily an XLet without changing the CTI server configuration files.

If you just want to test your new XLet, you can add the following line in baseengine.cpp :

 m_capaxlets.push_back(QVariantList() << QVariant("<xletname>") << QVariant("tab"));

right after the line

 m_capaxlets = datamap.value("capaxlets").toList();

You can replace "tab" with "grid" or "dock".

Add a translation
=================

This is definitely not something funny and not easy to automatize.

You have to add, in every .pro file of the project (except xlets.pro and all those that don't need translations), a line

 TRANSLATIONS += <project>_<lang>.ts

Replace <project> with the project name (xivoclient, baselib, xlet) and <lang> by the identifier of your language (en, fr, nl, ...)
Then you have to add, in every .qrc file, the .qm files corresponding to the ones you added in the .pro files, such as :

 <file><project>_<lang>.qm</file>

in the <qresource> section of these XML .qrc files.

After that, you have to run, in the XiVO Client root directory, something like :

 find . -name \*.pro -exec lupdate {} \;

This will create or update all .ts translation files registered in the .pro files.

You can then start translating the strings in these files, in the `xivoclient/i18n` folder.

Code modification
=================

If you want to be able to select your new language from within the XiVO Client, you have to add it in the interface.

For that, you can add your new language in the `m_locale_cbox` QCombobox in ConfigWidget.

CTI debugging tool
==================

If you have a problem and you want to see what is going on between the CTI server and client,
you can use a specific script, designed specifically for XiVO, instead of using something like
Wireshark to listen network communications.

Profiling
=========

To get profiling informations on the XiVO Client:

* Compile the XiVO Client with debugging symbols
* Run the command::

    LD_LIBRARY_PATH=bin valgrind --tool=callgrind bin/xivoclient

* Quit the client
* Open the generated file :file:`callgrind.out.<pid>` with KCacheGrind

Automatic checking tools
========================

We use two tools to check the source code of the XiVO Client: CppCheck et Valgrind.

CppCheck
--------

Usage::

    cppcheck -I baselib/src -I xivoclient/src .

Valgrind (Memcheck)
-------------------

Usage::

    LD_LIBRARY_PATH=bin valgrind --leak-check=full --suppressions=valgrind.supp --num-callers=30 --gen-suppressions=yes bin/xivoclient

You need to fill a file :file:`valgrind.supp` with Valgrind suppressions, to avoid displaying errors in code you have no control over.

Here is a template :file:`valgrind.supp` you can use. All memory in the XiVO Client is allocated using the new operator, so all calls to ``malloc`` and co. must come from libraries::

    {
       malloc
       Memcheck:Leak
       fun:malloc
       ...
    }
    
    {
       calloc
       Memcheck:Leak
       fun:calloc
       ...
    }
    
    {
       realloc
       Memcheck:Leak
       fun:realloc
       ...
    }
    
    {
       memalign
       Memcheck:Leak
       fun:memalign
       ...
    }

Figures
=======

Here's a call graph for the presence features. Not complete, but gives a good global view of the internal mechanism.

.. figure:: /cti_client/images/Xivoclient-presence.png
   :scale: 50%
   
   Xivo Client presence call graph
   
Here's a call graph describing the chaining of calls when the XiVO Client connects to the server.

.. figure:: /cti_client/images/Xivoclient-login.png
   :scale: 50%
   
   Xivo Client login call graph

