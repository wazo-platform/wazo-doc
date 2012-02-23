****************
Fax Transmission
****************

It's possible to send faxes from XiVO using the fax Xlet in the XiVO client.
Sending and receiving a fax on the same XiVO

It's possible to send a fax to the same XiVO you use to receive it. 
This is mostly useful for testing purpose.

* create a new context named fax-context of type "external".
* add an incoming call number to the fax-context context which will be used as the fax extension.
* modify the default context so that it includes the fax-context context
* add an incoming call using the following information::

   DID: the fax extension
   Context: fax-context
   Destination: Application
   Application: FaxToMail
   Email: as you wish 

You'll then be able to use your fax extension from your XiVO client 
to send a fax to the same XiVO that you use to receive it. 
