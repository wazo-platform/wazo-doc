*******************
xivo-provd REST API
*******************

This section describes the REST API provided by the xivo-provd application.

If you want to interact with the REST API of the xivo-provd daemon that is executing as part of Wazo,
you should be careful on which operation you are doing as to not cause stability problem to other parts
of the Wazo ecosystem. Mostly, this means being careful when editing or deleting devices and configs.

By default, the REST API of xivo-provd is accessible only from localhost on port 8666. No authentication
is required.

.. warning:: Major changes could happen to this API.


API
===

The description of the API has been split into these sections:

.. toctree::
   :maxdepth: 1

   provd
   devices
   configs
   plugins
   general
