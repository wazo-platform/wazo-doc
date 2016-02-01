*****
Users
*****

Users Configuration.

.. index:: users

.. toctree::
    :maxdepth: 1

    csv_import


Function keys
=============

Function keys can be configured to customize the user's phone keys. Key types are pre-defined and
can be browsed through the Type drop-down list. The Supervision field allows the key to be
supervised. A supervised key will light up when enabled. In most cases, a user cannot add multiple
times exactly the same function key (example : two user function keys pointing to the same user).
Adding the same function key multiple times can lead to undefined behavior and
generally will delete one of the two function keys.

.. warning::

   SCCP device only supports type "Customized".

.. image:: images/funckeys.png

For User keys, start to key in the user name in destination, XiVO will try to complete with the corresponding user.

If the forward unconditional function key is used with no destination the user will be prompted when the user
presses the function key and the BLF will monitor *ALL* unconditional forward for this user.


Extensions
==========

`*3` (online call recording)
----------------------------

To enable online call recording, you must check the "Enable online call recording" box in the user form.

.. figure:: images/user-services.png
   :alt: Users Services

   Users Services

When this option is activated, the user can press ``*3`` during a conversation to start/stop online
call recording. The recorded file will be available in the :file:`monitor` directory of the
:menuselection:`Services --> IPBX --> Audio files` menu.


`*26` (call recording)
----------------------

You can enable/disable the recording of all calls for a user in 2 different way:

1. By checking the "Call recording" box of the user form.

.. figure:: images/user-services.png
   :alt: Users Services

   Users Services

2. By using the extension `*26` from your phone (the "call recording" option must be activated
   in :menuselection:`Services --> IPBX --> Extensions`).

When this option is activated, all calls made to or made by the user will be recorded in the :file:`monitor`
directory of the :menuselection:`Services --> IPBX --> Audio files` menu.
