****************
Managing Plugins
****************

Git Repository
==============

Most plugin-related files are available in the
`xivo-provd-plugins repository <https://github.com/wazo-pbx/xivo-provd-plugins.git>`_.
Following examples are relative to the repository directory tree. Any modifications
should be preceeded by a `git pull`.


Updating a Plugin
=================

We will be using  the `xivo-cisco-spa` plugins family as an example on this page

There is one directory per family. Here is the directory structure for :file:`xivo-cisco-spa`:

.. code-block:: javascript

   plugins/xivo-cisco-spa/
   +-- model_name_xxx
   +-- model_name_xxx
   +-- common
   +-- build.py


Every plugin has a folder called :file:`common` which regoups common ressources for each model.
Every model has its own folder with its version number.

After modifying a plugin, you must increment the version number.
You can modifiy the file :file:`plugin-info` to change the version number:

.. code-block:: javascript

   plugins/xivo-cisco-spa/
   +-- model_name_xxx
       +-- plugin-info


.. important::

   If ever you modify the folder :file:`common`, you must increment the version number of all the models.


Use Case: Update Firmwares for a given plugin
---------------------------------------------

Let us suppose we want to update firmwares for xivo-snom from 8.7.3.25 to
8.7.3.25 5. Here are the steps to follow :

1. Copy folder plugins/xivo-snom/8.7.3.25 to plugins/xivo-snom/8.7.3.25.5
#. Update VERSION number in plugins/xivo-snom/8.7.3.25.5/entry.py
#. Update VERSION number in plugins/xivo-snom/8.7.3.25.5/plugin-info
#. Download new firmwares (.bin files from `snom website <http://wiki.snom.com/Firmware/V8/Patch>`_)
#. Update VERSION number and URIs in plugins/xivo-snom/8.7.3.25.5/pkgs/pkgs.db
   (with uris of downloaded files from snom website)
#. Update sizes and sha1sums in plugins/xivo-snom/8.7.3.25.5/pkgs/pkgs.db (using
   helper script xivo-tools/dev-tools/check_fw)
#. Update plugins/xivo-snom/build.py (duplicate and update section 8.7.3.25 > 8.7.3.25.5)


Test your changes
-----------------

You have three different methods to test your changes on your development machine.


Always increase plugin version (easiest)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the production version is 0.4, change the plugin version to 0.4.01, make your
changes and upload to testing (see below).

Next modification will change the plugin version to 0.4.02, etc. When you are
finished making changes, change the version to 0.5 and upload one last time.


Edit directly on XiVO
^^^^^^^^^^^^^^^^^^^^^

Edit the files in :file:`/var/lib/xivo-provd/plugins`.

To apply your changes, go in ``xivo-provd-cli`` and run::

    plugins.reload('xivo-cisco-spa-7.5.4')


Disable plugin caching
^^^^^^^^^^^^^^^^^^^^^^

Edit :file:`/etc/xivo/provd/provd.conf` and add the line::

    cache_plugin: True

Empty :file:`/var/cache/xivo-provd` and restart provd.

Make your changes in provd-plugins, update the plugin version to the new one and upload to testing (see below). Now, every time you uninstall/install the plugin, the new plugin will be fetched from testing, instead of being cached, even without changing the version.

Uploading to testing
^^^^^^^^^^^^^^^^^^^^

Before updating a plugin, it must be passed through the testing phase.
Once it has been approved it can be uploaded to the production server

.. important::

  Before uploading a plugin in the testing provd repository, make sure to git pull the xivo-provd-plugins git repository.

To upload the modified plugin in the testing repo on `provd.xivo.io`,
you can execute the following command::

   $ make upload

Afterwards, in the web-interface, you must modify the URL in section
:menuselection:`Configuration --> Provisioning --> General` to::

   `http://provd.xivo.io/plugins/1/testing/`

You can then update the list of plugins and check the version number for the plugin that you modified.
Don't forget to install the plugin to test it.


Mass-install all firmwares related to a given plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using xivo-provd-cli on a xivo server, one can mass-install firmwares. Following
example installs all firmwares for xivo-snom 8.7.3.25.5 plugin
(note the auto-completion)::

    xivo-provd-cli> plugins.installed().keys()
    [u'xivo-snom-8.7.3.15',
     u'xivo-cisco-sccp-legacy',
     u'xivo-snom-8.4.35',
     u'xivo-snom-8.7.3.25',
     u'xivo-aastra-switchboard',
     u'xivo-aastra-3.2.2-SP3',
     u'xivo-aastra-3.2.2.1136',
     u'xivo-cisco-sccp-9.0.3',
     u'null',
     u'xivo-snom-8.7.3.25.5']
    xivo-provd-cli> p = plugins['xivo-snom-8.7.3.25.5']
    xivo-provd-cli> p.install_all()


Uploading to stable
^^^^^^^^^^^^^^^^^^^

Once checked, you must synchronize the plugin from `testing` to `stable`. If applicable, you
should also update the archive repo.

To download the stable and archive plugins::

   $ make download-stable
   $ make download-archive

Go to the `plugins/_build` directory and delete the plugins that are going to be updated. Note
that if you are not updating a plugin but you are instead removing it "once and for all", you
should instead move it to the archive directory::

   $ rm -fi stable/xivo-cisco-spa*

Copy the files from the directory `testing` to `stable`::

   $ cp testing/xivo-cisco-spa* stable

Go back to the `plugins` directory and upload the files to the stable and archive repo::

   $ make upload-stable
   $ make upload-archive

The file are now up to date and you can test by putting back the `stable`
url in the web-interface's configuration::

   `http://provd.xivo.io/plugins/1/stable/`
