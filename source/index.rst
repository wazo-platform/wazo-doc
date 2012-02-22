.. XiVO-doc Documentation master file.

****************************
XiVO |version| documentation
****************************

XiVO is an application suite developed by
Avencall_ Group, based on several free existing components including Asterisk_, and our own developments
to provide communication services (IPBX, Unified Messaging ....) to businesses.

.. _Avencall: http://www.avencall.com/ 
.. _Asterisk: http://www.asterisk.org/ 

XiVO is `free software`_. Most of its distinctive components, and XiVO as a whole, are distributed under the *GPLv3 license*.
We are also working on a fully `Open XiVO Hardware`_.

.. _free software: http://www.gnu.org/philosophy/free-sw.html
.. _Open Xivo Hardware: http://hardware.xivo.fr

.. warning::
   
   Upgrading from 1.2.0 or 1.2.1 require a special procedure before executing xivo-upgrade script::
      
       $ aptitude update
       $ aptitude install xivo-upgrade
       $ xivo-upgrade


.. toctree::
   :maxdepth: 2

   Introduction <introduction/introduction>
   installation/installation
   getting_started/getting_started
   cti_client/cti_client
   system_admin/system_admin
   api_sdk/api_sdk
   developers/developers


You may also check `XiVO blog`_ and `XiVO wiki`_ for more information.
XiVO documentation is also available as `an epub file <http://documentation.xivo.fr/epub/>`_ 
or as `a pdf file <http://documentation.xivo.fr/pdf/>`_ 

.. _XiVO blog: http://blog.xivo.fr/
.. _XiVO wiki: http://wiki.xivo.fr/

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
