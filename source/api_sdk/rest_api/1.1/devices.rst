.. _restapi-device:

*******
Devices
*******

Device Representation
=====================

Description
-----------

+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Values                                                | Description                                                                                                                                 |
+=============+=======================================================+=============================================================================================================================================+
| id          | string                                                | (Read-only)                                                                                                                                 |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| ip          | string formatted as an IP address (10.0.0.0)          | IP address                                                                                                                                  |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| mac         | string formatted as a MAC address (AA:BB:CC:DD:EE:FF) | MAC address                                                                                                                                 |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| vendor      | string                                                | Vendor name                                                                                                                                 |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| model       | string                                                | Device model                                                                                                                                |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| version     | string                                                | Firmware version                                                                                                                            |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| plugin      | string                                                | Provisioning plugin to be used by the device                                                                                                |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| description | string                                                |                                                                                                                                             |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| status      | - configured                                          | - configured: Device is configured and ready to be used                                                                                     |
|             | - autoprov                                            | - autoprov : Device can be provisionned using a provisioning code                                                                           |
|             | - not_configured                                      | - not_configured : Device has not been completely configured                                                                                |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| template_id | string                                                | ID of the device template. All devices using a device template will have a certain number of common parameters preconfigured for the device |
+-------------+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+


Example
-------

::

   {
       "id": "412c212cff500cc158f373ff00e078f7",
       "ip": "10.0.0.1",
       "mac": "00:00:5e:00:00:01",
       "vendor": "Aastra",
       "model": "6731i",
       "version": "3.2.2",
       "plugin": "xivo-aastra-3.2.2-SP3"
       "status": "configured",
       "template_id": "defaultconfigdevice",
       "links" : [
           {
               "rel": "devices",
               "href": "https://xivoserver/1.1/devices/412c212cff500cc158f373ff00e078f7"
           }
       ]
   }


Device list
===========

Query
-----

::

   GET /1.1/devices

Parameters
----------

order
    Sort devices using the specified field (e.g. "mac"). Allowed fields: ip, mac, plugin, model,
    vendor, version.

direction
    'asc' or 'desc'. Sort list in ascending (asc) or descending (desc) order

limit
    total number of devices to show in the list

skip
    number of devices to skip over before starting the list

search
    Search devices. Only devices with a field containing the search term
    will be listed.


Errors
------


+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| Error code | Error message                                                        | Description                                                              |
+============+======================================================================+==========================================================================+
| 400        | Invalid parameters: limit must be a positive number                  | the 'limit' parameter must be a number                                   |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: skip must be a positive number                   | the 'skip' parameter must be a number                                    |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: ordering parameter '<field>' does not exist      | you must use one of the fields available in a device when sorting a list |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+
| 400        | Invalid parameters: direction parameter '<direction>' does not exist | use either 'asc' or 'desc' as a direction when sorting a list            |
+------------+----------------------------------------------------------------------+--------------------------------------------------------------------------+


Example requests
----------------

List all devices::

   GET /1.1/devices HTTP/1.1
   Host: xivoserver
   Accept: application/json

List 10 devices, sorted by mac address::

   GET /1.1/devices?limit=10&order=mac HTTP/1.1
   Host: xivoserver
   Accept: application/json

Search for devices containing the term "aastra"::

   GET /1.1/devices?search=aastra HTTP/1.1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "total": 2,
       "items": [
           {
               "id": "412c212cff500cc158f373ff00e078f7",
               "ip": "10.0.0.1",
               "mac": "00:00:5e:00:00:01",
               "vendor": "Aastra",
               "model": "6731i",
               "version": "3.2.2",
               "plugin": "xivo-aastra-3.2.2-SP3"
               "status": "configured",
               "template_id": "defaultconfigdevice",
               "links" : [
                   {
                       "rel": "devices",
                       "href": "https://xivoserver/1.1/devices/412c212cff500cc158f373ff00e078f7"
                   }
               ]
           },
           {
               "id": "6ff76e09a7ab51ec3afe152a63324ff9",
               "ip": "10.0.0.2",
               "mac": "00:00:5e:00:00:02",
               "vendor": "Snom",
               "model": "720",
               "version": "8.7.3.19",
               "plugin": "xivo-snom-8.7.3.19",
               "status": "configured",
               "template_id": "defaultconfigdevice",
               "links" : [
                   {
                       "rel": "devices",
                       "href": "https://xivoserver/1.1/devices/6ff76e09a7ab51ec3afe152a63324ff9"
                   }
               ]
           }
       ]
   }


Get Device
==========

Query
-----

::

   GET /1.1/devices/<id>

Parameters
----------

id
    Device's id

Errors
------

+------------+-----------------------------------------------+------------------------------------------------------------------+
| Error code | Error message                                 | Description                                                      |
+============+===============================================+==================================================================+
| 404        | Not found                                     | The requested device was not found                               |
+------------+-----------------------------------------------+------------------------------------------------------------------+

Example request
---------------

::

   GET /1.1/devices/412c212cff500cc158f373ff00e078f7 HTTP/1.1
   Host: xivoserver
   Accept: application/json

Example response
----------------

::

   HTTP/1.1 200 OK
   Content-Type: application/json

   {
       "id": "412c212cff500cc158f373ff00e078f7",
       "ip": "10.0.0.1",
       "mac": "00:00:5e:00:00:01",
       "vendor": "Aastra",
       "model": "6731i",
       "version": "3.2.2",
       "plugin": "xivo-aastra-3.2.2-SP3"
       "status": "configured",
       "template_id": "defaultconfigdevice",
       "links" : [
           {
               "rel": "devices",
               "href": "https://xivoserver/1.1/devices/412c212cff500cc158f373ff00e078f7"
           }
       ]
   }


Create a Device
===============

Query
-----

::

   POST /1.1/devices

Input
-----

+-------------+----------+--------+-------------+
| Field       | Required | Values | Description |
+=============+==========+========+=============+
| ip          | no       | string | (see above) |
+-------------+----------+--------+-------------+
| mac         | no       | string | (see above) |
+-------------+----------+--------+-------------+
| sn          | no       | string | (see above) |
+-------------+----------+--------+-------------+
| vendor      | no       | string | (see above) |
+-------------+----------+--------+-------------+
| model       | no       | string | (see above) |
+-------------+----------+--------+-------------+
| version     | no       | string | (see above) |
+-------------+----------+--------+-------------+
| description | no       | string | (see above) |
+-------------+----------+--------+-------------+
| template_id | no       | string | (see above) |
+-------------+----------+--------+-------------+

Errors
------

+------------+------------------------------------------------------------------+--------------------------------------------------------------+
| Error code | Error message                                                    | Description                                                  |
+============+==================================================================+==============================================================+
| 400        | error while creating Device: <explanation>                       | See explanation for more details                             |
+------------+------------------------------------------------------------------+--------------------------------------------------------------+
| 400        | Invalid parameters: ip                                           | ip address is not formatted correctly                        |
+------------+------------------------------------------------------------------+--------------------------------------------------------------+
| 400        | Invalid parameters: mac                                          | mac address is not formatted correctly                       |
+------------+------------------------------------------------------------------+--------------------------------------------------------------+
| 400        | device <mac> already exists                                      | a device using the same MAC address has already been created |
+------------+------------------------------------------------------------------+--------------------------------------------------------------+
| 400        | Nonexistent parameters: plugin <plugin> does not exist           | the selected plugin does not exist or has not been installed |
+------------+------------------------------------------------------------------+--------------------------------------------------------------+
| 400        | Nonexistent parameters: template_id <template_id> does not exist | the selected device template does not exist                  |
+------------+------------------------------------------------------------------+--------------------------------------------------------------+

Example request
---------------

::

   POST /1.1/devices HTTP/1.1
   Host: xivoserver
   Accept: application/json
   Content-Type: application/json

   {
       "ip": "10.0.0.1",
       "mac": "00:00:5e:00:00:01",
       "vendor": "Aastra",
       "model": "6731i",
       "version": "3.2.2",
       "plugin": "xivo-aastra-3.2.2-SP3"
       "template_id": "defaultconfigdevice",
   }

Example response
----------------

::

   HTTP/1.1 201 Created
   Location: /1.1/devices/412c212cff500cc158f373ff00e078f7
   Content-Type: application/json

   {
       "id": "412c212cff500cc158f373ff00e078f7",
       "ip": "10.0.0.1",
       "mac": "00:00:5e:00:00:01",
       "vendor": "Aastra",
       "model": "6731i",
       "version": "3.2.2",
       "status": "configured",
       "plugin": "xivo-aastra-3.2.2-SP3"
       "template_id": "defaultconfigdevice",
       "links" : [
           {
               "rel": "devices",
               "href": "https://xivoserver/1.1/devices/412c212cff500cc158f373ff00e078f7"
           }
       ]
   }


Update a Device
===============

Query
-----

::

   PUT /1.1/devices/<id>

The update does not need to set all the fields for the device. Only the fields that need to be updated
must be set.

Parameters
----------

id
    Device's id

Input
-----

Same as for creating a device. Please see `Create a Device`_

Errors
------

Same as for creating a device. Please see `Create a Device`_

Example request
---------------

::

   PUT /1.1/devices/42 HTTP/1.1
   Host: xivoserver
   Content-Type: application/json

   {
       "ip": "10.0.0.1"
   }

Example response
----------------

::

   HTTP/1.1 204 No Content


Delete a Device
===============

A device can not be deleted if it is linked to a line. You must deassociate the line and the device
first.

Query
-----

::

   DELETE /1.1/devices/<id>

Errors
------

+------------+-----------------------------------------------+------------------------------------------------------------------+
| Error code | Error message                                 | Description                                                      |
+============+===============================================+==================================================================+
| 400        | error while deleting Device: <explanation>    | See error message for more details                               |
+------------+-----------------------------------------------+------------------------------------------------------------------+
| 404        | Not found                                     | The requested device was not found                               |
+------------+-----------------------------------------------+------------------------------------------------------------------+


Example request
---------------

::

   DELETE /1.1/devices/412c212cff500cc158f373ff00e078f7 HTTP/1.1
   Host: xivoserver

Example response
----------------

::

   HTTP/1.1 204 No Content


Reset a device to autoprov
==========================

.. warning:: The device's configuration will be lost when reset to autoprov mode.

Resets a device into 'autoprov' mode. Once in autoprov, a device can be reprovisionned using another provisioning code.


Query
-----

::

    GET /1.1/devices/<id>/autoprov


Parameters
----------

id
    Device's id

Example request
---------------

::

    GET /1.1/devices/412c212cff500cc158f373ff00e078f7/autoprov
    Host: xivoserver

Example response
----------------

::

    HTTP/1.1 204 No Content


Synchronize a device
====================

Synchronize a device's configuration. Used when a configuration has been modified and the changes need to be sent to the device.

Query
-----

::

    GET /1.1/devices/<id>/synchronize

Parameters
----------

id
    Device's id

Example request
---------------

::

    GET /1.1/devices/412c212cff500cc158f373ff00e078f7/synchronize
    Host: xivoserver

Example response
----------------

::

    HTTP/1.1 204 No Content


Associate a line to a device
============================

.. warning:: This feature is not yet accessible nor functional.

After associating a line, the device needs to be synchronized for the changes to take effect. Please
see `Synchronize a device`_

Query
-----

::

    GET /1.1/devices/<id>/associate_line/<lineid>

Parameters
----------

id
    Device's id

line_id
    Line id

Example request
---------------

::

    GET /1.1/devices/412c212cff500cc158f373ff00e078f7/associate_line/2
    Host: xivoserver

Example response
----------------

::

    HTTP/1.1 204 No Content


Remove a line from a device
===========================

.. warning:: This feature is not yet accessible nor functional.

After removing a line, the device needs to be synchronized for the changes to take effect. Please
see `Synchronize a device`_

Query
-----

::

    GET /1.1/devices/<id>/remove_line/<lineid>

Parameters
----------

id
    Device's id

line_id
    Line id

Example request
---------------

::

    GET /1.1/devices/412c212cff500cc158f373ff00e078f7/remove_line/2
    Host: xivoserver

Example response
----------------

::

    HTTP/1.1 204 No Content
