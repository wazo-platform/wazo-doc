****************
Call Permissions
****************

You can manage call permissions via the
:menuselection:`Services --> IPBX --> Call management --> Call permissions`
page.

Call permissions can be used for:

* denying a user from calling a specific extension
* denying a user of a group from calling a specific extension
* denying a specific extension on a specific outgoing call from being called

More than one extension can match a given call permission, either by specifying more
than one extension for that permission or by using extension patterns.

You can also create permissions that allow a specific extension to be called
instead of being denied. This make it possible to create a general "deny all"
permission and then an "allow for some" one.

Finally, instead of unconditionally denying calling a specific extension,
call permissions can instead challenge the user for a password to be able
to call that extension.

As you can see, you can do a lot of things with Wazo's call permissions. They
can be used to create fairly complex rules. That said, it is probably
*not* a good idea to so because it's pretty sure you'll get it somehow wrong.


Examples
========

Note that when creating or editing a call permission, you must at least:

* fill the :guilabel:`Name` field
* have one extension / extension pattern in the :guilabel:`Extensions` field


Denying a user from calling a specific extension
------------------------------------------------

* Add the extension in the extensions list
* In the :guilabel:`Users` tab, select the user

.. note::
    User's :guilabel:`Rightcall Code` (:menuselection:`Services -> IPBX -> IPBX Settings -> Users` under
    :guilabel:`Services` tab) overwrite all password call permissions for the user.

.. warning::
   The extension can be anything but it will only work if it's the extension of a user or
   an extension that pass through an outgoing call. It does *not* work, for example, if
   the extension is the number of a conference room.


Denying a user of a group from calling a specific extension
-----------------------------------------------------------

First, you must create a group and add the user to this group. Note that groups
aren't required to have a number.

Then,

* Add the extension in the extensions list
* In the :guilabel:`Groups` tab, select the group


Denying users from calling a specific extension on a specific outgoing call
---------------------------------------------------------------------------

* Add the extension in the extensions list
* In the :guilabel:`Outgoing calls` tab, select the outgoing call

Note that selecting both a user and an outgoing call for the same call permission
doesn't mean the call permission applies only to that user. In fact, it means that the
user can't call that extension and that the extension can't be called on the specific
outgoing call. This in redundant and you will get the same result by not
selecting the user.
