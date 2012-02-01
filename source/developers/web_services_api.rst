***************
WebServices API
***************

**Using web services XiVO to develop applications around XiVO.**

HTTP status codes
-----------------

- 200: Success
- 204: No data (only for list and search queries)
- 304: Document not changed (only for requests list, search and see)
- 400: Incorrect syntax (only for requests to add)
- 401: Authentication required
- 403: Authentication refused
- 404: Resource not found (for queries only view and delete)
- 500: Internal error

Configuration
-------------

Gestion
^^^^^^^

Entity
******

List :
https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=list

Search :
https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=search&search=[string]

.. code-block:: none

   Search Attributes :

    - name
    - displayname
    - phonenumber
    - faxnumber
    - email
    - url
    - address1
    - address2
    - city
    - state
    - zipcode
    - country
    - description

View :
https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=view&id=[entity_id] 

Add :
https://[ip_xivo]/xivo/configuration/json.php/restricted/manage/entity/?act=add


.. code-block:: javascript

   {
        "name": "proformatique",
        "displayname": "Proformatique",
        "phonenumber": "0033141389960",
        "faxnumber": "0033141389970",
        "email": "contact@proformatique.com",
        "url": "http://www.proformatique.com",
        "address1": "10 bis, rue Lucien VOILIN",
        "address2": "",
        "city": "Puteaux",
        "state": "Hauts de Seine",
        "zipcode": "92800",
        "country": "FR",
        "description": ""
   }
   
   
Network
^^^^^^^

Mail
****

View :
https://[ip_xivo]/xivo/configuration/json.php/restricted/network/mail/?act=view

Return code example:

.. code-block:: javascript

   {
    "id": "1",
    "mydomain": "proformatique.com",
    "origin": "devel.proformatique.com",
    "relayhost": "smtp.free.fr",
    "fallback_relayhost": "smtp.orange.fr",
    "canonical": [
      {
         "pattern": "@proformatique.com",
         "result" : "support@proformatique.com"
      }
    ]
   }

Description des champs:

- id: identifiant de la ressource (toujours égal à 1)
- mydomain: nom de domaine mail du serveur
- origin: adresse d'envoi des mails générés par le système
- relayhost: serveur de relai principal des mails
- fallback_relayhost: serveur de relai secondaire des mails
- canonical: règles de réécriture des adresses email 

Modification

https://[ip_xivo]/xivo/configuration/json.php/restricted/network/mail/?act=edit

Format des données à envoyer:

.. code-block:: javascript

   {
    "mydomain": "proformatique.com",
    "origin": "devel.proformatique.com",
    "relayhost": "smtp.free.fr",
    "fallback_relayhost": "smtp.orange.fr",
    "canonical": [
      {
         "pattern": "@proformatique.com",
         "result" : "support@proformatique.com"
      }
    ]
   }
