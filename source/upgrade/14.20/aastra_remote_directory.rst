*************************************
Aastra Remote Directory Upgrade Notes
*************************************

Starting from XiVO 14.20, it is not possible anymore to use SSL 3.0 when connecting to XiVO using HTTPS.

This has the unfortunate consequence of breaking the remote directory on Aastra phones
configured by the ``xivo-aastra`` provisioning plugins in version 1.2 and earlier.


Upgrade procedure
=================

To be able to use the remote directory on your Aastra phones on XiVO 14.20 or later,
you'll need to take one of the following actions:


Upgrade to the Latest Plugin
----------------------------

This is the recommended solution. This can be done either before or after the upgrade. You'll have to:

#. Upgrade your ``xivo-aastra`` plugin to version 1.3 or later
#. Restart/synchronize all your phones

The correction is only available for plugin ``xivo-aastra-3.3.1-SP2`` and later. If you are using an
older plugin (``xivo-aastra-3.2.2-SP3`` for example), then you'll need to install a newer plugin
and :ref:`update all your phones to use the new plugin <provd-changing-device-plugin>`.

If you were already using custom templates, make sure to update them so that the phones
access the remote directory via HTTP instead of HTTPS. This can be done using the following command::

   find /var/lib/xivo-provd/plugins/xivo-aastra* -name '*.tpl' -exec sed -i '/X_xivo_phonebook_ip/s/\bhttps:/http:/' {} \;


Update the Templates
--------------------

If you can't or don't want to update to a newer plugin, you can instead update the templates used by the
plugin. This can be done either before or after the upgrade. You'll have to:

#. Update the templates so that the directory is accessed via HTTP
#. Restart/synchronize all your phones

In this specific case, it is safe to directly modify the templates used by the plugin instead of
:ref:`creating custom templates <provd-custom-templates>`. To update the templates, you can use the
following command::

   find /var/lib/xivo-provd/plugins/xivo-aastra* -name '*.tpl' -exec sed -i '/X_xivo_phonebook_ip/s/\bhttps:/http:/' {} \;


Re-enable SSL 3.0
-----------------

If you can't restart/synchronize your phones, the last solution is to re-enable SSL 3.0 on your XiVO.
This should only be used as a temporary solution to give you more time to plan a firmware upgrade for
your phones. This can be done only after the upgrade. You'll have to:

#. Update nginx configuration
#. Reload nginx

This can be done using the following commands::

   sed -i 's/ssl_protocols .*/ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;/' /etc/nginx/sites-available/xivo
   service nginx reload
