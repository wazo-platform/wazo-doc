.. _remote-directory:

****************
Remote directory
****************

If you have a phone provisioned with Wazo and its one of the supported ones, you'll be able to
search in your Wazo directory and place call directly from your phone.

See the list of :ref:`supported devices <supported-devices>` to know if a model supports the Wazo
directory or not.


Configuration
=============

For the remote directory to work on your phones, the first thing to do is to create a custom
xivo-dird-phoned configuration file :file:`/etc/xivo-dird-phoned/conf.d/custom.yml`

You then have to add the range of IP addresses that will be allowed to access the directory.
So if you know that your phone's IP addresses are all in the 192.168.1.0/24 subnet, add::

  rest_api:
    authorized_subnets: [192.168.1.0/24]


You must then restart ``xivo-dird-phoned``::

  systemctl restart xivo-dird-phoned

Once this is done, on your phone, just click on the "remote directory" function key and
you'll be able to do a search in the Wazo directory from it.
