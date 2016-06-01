.. _embedded_swagger:

***********************************************************
How to use the embedded REST API web interface (Swagger UI)
***********************************************************

Every XiVO server embeds its own copy of the Swagger UI exposed on http://api.xivo.io.
The instance embedded in the XiVO allows you to directly try the requests with the in-page buttons.

For the rest of this article, we will consider that your XiVO is accessible under the hostname
``MY_XIVO``.

The instance is available at: http://MY_XIVO/api

Before using the Swagger UI, there are a few prerequisites:

* Accept the HTTPS certificate for each service of the XiVO
* Add the permissions to use the REST API to a Web Services Access user
* Obtain an authentication token

HTTPS certificates
------------------

**For each** service on the left menu that you want to try, you need to accept the HTTPS certificate for
this service. To that end:

#. click on the service in the menu on the left
#. copy the URL you see in the text box at the top of the page, something like:
   ``https://MY_XIVO:9497/0.1/api/api.json`` and paste it in your browser
#. accept the HTTPS certificate validation exception
#. go back to http://MY_XIVO/api and select the service again (or click on the top-right "Explore"
   button)

You should now be able to see the different sections for the REST API of that service.

REST API permissions
--------------------

You must create a Web Services Access with the right permissions before using the REST API. See
:ref:`web_services_access`.

Each endpoint has its own ACL, but you may add wildcard ACLs, like:

* ``auth.#`` to gain access to all ``xivo-auth`` REST API endpoints
* ``confd.#`` to gain access to all ``xivo-confd`` REST API endpoints
* ``#`` to gain access to every endpoint of every service.

.. warning:: Only use wildcards when doing tests, not with a production REST API access. You should
             always restrict the permissions to the bare minimum.

Obtain an authentication token
------------------------------

The quick and easy way is to use http://auth.xivo.io. You may log-in with the following parameters:

* Host = https://MY_XIVO:9497  (you must have accepted the HTTPS certificate of ``xivo-auth`` first)
* Backend = XIVO Service
* Login = username of your Web Services Access
* Password = the associated password

Then click "Sign in!", and you can get see the token. This token will expire after one hour, and you
will need to re-authenticate to get a new token.

The other way you can get a token is via Swagger UI (what else?). Choose the ``xivo-auth`` service
in the list of REST API. Under ``tokens``, choose ``POST /tokens``.

#. In the top-right text box of the page (left to the "Explore" button), fill "token" with the
   string ``username:password`` where those credentials come from the Web Services Access you
   created earlier.
#. Go back to the ``POST /tokens`` section and click on the yellow box to the right of the ``body``
   parameter. This will pre-fill the ``body`` parameter.
#. In the ``body`` parameter, set:

   * ``backend`` to ``xivo-service``
   * ``expiration`` to the number of seconds for the token to be valid (e.g. 60 for one hour). After
     the expiration time, you will need to re-authenticate to get a new token.

#. Click "Try it out" at the end of the section
#. In the response, you should see a ``token`` attribute.

For more informations about the backends of xivo-auth, see :ref:`xivo-auth plugins <auth-stock-plugins>`.


Use the authentication token
----------------------------

To use the authentication token, choose the service for which you want to try the REST API, then
paste the token in the top-right text box. You do not need to click "Explore" to apply the token
change, the new token will be used automatically at the next request you send.

You can now choose a REST API endpoint and "Try it out".
