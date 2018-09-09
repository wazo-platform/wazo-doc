.. _applications:

************
Applications
************

Wazo allows its users to use its API to build applications to manage their communications with great
flexibility.


Voice applications
==================

A voice application can handle calls that have been made to you UC engine.  Once the application is created
you can configure an incoming call to route a number to that application. From there what you do with that
call is up to you.

Applications can be used to implement complex task like a call manager call queue with agents to take calls
and call distribution strategies to fit your needs, or a much more simpler task like answering the call, playing
a sound file and hanging up.


How it works
------------

The basic model of any application listen for events on the :ref:`Wazo WebSocket <wazo-websocketd>` and
do the proper opperations based on the recieved events using the REST APIs.


Examples:
---------

A voicemail application
^^^^^^^^^^^^^^^^^^^^^^^

To create a replacement for the Asterisk voicemail application we would need an application that does the
following.

1. Answer incoming calls that have not been answered by the user.
2. Announce that the called user is busy.
3. Record the callers message.

The application would also need an entrypoint for the user to listen to its voicemails. This could be either
another voice entrypoint to allow the user to call into its voicemail and use an interactive menu to listen
and manage its messages, or a REST API could be implemented to allow the user to manage its voicemails from
a REST API and eventually from one or many GUIs.


