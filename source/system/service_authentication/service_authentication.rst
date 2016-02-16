.. _service-authentication:

**********************
Service Authentication
**********************

In our system, there are :ref:`permissions<rest-api-acl>` on every REST resource and sometime, a
service need to access it. To do this, we use service authentication with the backend
:ref:`xivo-service<auth-backends-service>`.


Workflow
========

In XiVO, we use the following workflow to access a REST resource from a XiVO service:

1. Create a username/password (service_id/service_key) with the right :ref:`ACL<rest-api-acl>`, via
   :menuselection:`Configuration --> Management --> Web Services Access` (See
   :ref:`web_services_access`).
2. Create a token with this credential and the backend :ref:`xivo-service<auth-backends-service>`.
3. Use this token to access the REST resource defined by the :ref:`ACL<rest-api-acl>`.

.. figure:: images/service_authentication_workflow.png

   Workflow of service authentication


Service
    Service that want access a REST resource.

xivo-{daemon}
    Server that expose a REST resources. Implement a required acl on each resource.

xivo-auth
    Server that authenticate the `Service` and validate the required acl with the token.

To see which XiVO service use this system, see :menuselection:`Configuration --> Management --> Web
Services Access` with the prefix ``xivo-``.
