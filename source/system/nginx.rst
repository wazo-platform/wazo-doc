.. _nginx:

*****
Nginx
*****

Wazo use nginx as a web server and reverse proxy.

In its default configuration, the nginx server listens on port TCP/80 and TCP/443 and allows these
services to be used:

* The agent management server (xivo-agentd)
* The authentication server (xivo-auth)
* The telephony service interface (xivo-ctid-ng)
* The directory service (xivo-dird)
* The AMI HTTP interface (xivo-amid)
* web interface (xivo-web-interface)
* API documentation (xivo-swagger-doc)
* The websocket interface (xivo-websocketd)
* Asterisk (xivo-config)

An administrator can easily modify the configuration to allow or disallow some services.

To do so, an administrator only has to create a symbolic link inside the
:file:`/etc/nginx/locations/http-enabled` directory to the corresponding file in the
:file:`/etc/nginx/locations/http-available` directory, and then reload nginx with
``systemctl reload nginx``. A similar operation must be done for HTTPS.

For example, to enable all the available services::

   ln -sf /etc/nginx/locations/http-available/* /etc/nginx/locations/http-enabled
   ln -sf /etc/nginx/locations/https-available/* /etc/nginx/locations/https-enabled
   systemctl reload nginx

To disable all the services other than the web interface::

   rm /etc/nginx/locations/http-enabled/* /etc/nginx/locations/https-enabled/*
   ln -s /etc/nginx/locations/http-available/xivo-web-interface /etc/nginx/locations/http-enabled
   ln -s /etc/nginx/locations/https-available/xivo-web-interface /etc/nginx/locations/https-enabled
   systemctl reload nginx
