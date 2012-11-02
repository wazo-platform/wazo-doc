****************
Managing Plugins
****************

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


Before updating a plugin, it must be passed through the testing phase.
Once it has been approved it can be uploaded to the production server

To upload the modified plugin in the testing repo on `provd.xivo.fr`,
you can execute the following command::

   $ make upload

Afterwards, in the web-interface, you must modify the URL in section
:menuselection:`Configuration --> Provisioning --> General` to::

   `http://provd.xivo.fr/plugins/1/testing/`

You can then update the list of plugins and check the version number for the plugin that you modified.
Don't forget to install the plugin to test it.

Once checked, you must synchronize the plugin from `dev` to `stable`

To download the stable plugins::

   $ make download-stable

Go to the `plugins/_build/stable` directory and delete the file that need to be replaced::

   $ rm -fi xivo-cisco-spa*

Copy the files from the directory `dev` to `stable`::

   $ cp ../dev/xivo-cisco-spa* .

Go back to the `plugins` directory and upload the files to the stable repo::

   $ make upload-stable

The file are now up to date and you can test by putting back the `stable`
url in the web-interface's configuration::

   `http://provd.xivo.fr/plugins/1/stable/`
