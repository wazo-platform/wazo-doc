***************
Getting Started
***************

The getting started section aims to help you to simply create a user with a SIP line. This simple case cover what a lot of people want to do.
If you want to connect a softphone, a Linksys PAP2 or simply a SIP phone that you can manage via a web interface, follow us during these steps.

This tutorial doesn't cover how to provision automatically a supported device. For this, you must refer to the :ref:`provisionning section. <intro-provisioning>`

We first need to log into the convivial XiVO web interface. The web interface is the place from where you can administer the whole system.

.. figure:: images/step-01.png

   Logging into the XiVO

What is presented to you on the first page when you're logged in, is all the status informations about your system. This page help you
to monitor the health of your system and gives you network informations. A very important information you get on this page is the IP address
of your server. You will need this information later on when you will configure the device that will connect to it.

.. figure:: images/step-02.png

  System informations

We now navigate to IPBX menu. A bunch of menu offered to you. The option we are interested by for now is 'Users' under the 'IPBX settings'.

.. figure:: images/step-03.png

   Menu IPBX

Go select the Users settings.

.. figure:: images/step-05.png

   Users settings

From here, you need to press the "plus" sign that will pop up a subtile menu and then click Add.

.. figure:: images/step-04.png

   Adding a new line

We now have in front of us the form that will allow us to create a new user. The three most important fields are 'First name', 'Last name' and 'Language'.
Fill up the fields with what you want, and wait for the next step.
 
.. figure:: images/step-06.png

   User information

Click on the "Lines" button.

.. figure:: images/step-07.png

   Lines menu

If you click in the 'Number' field, you will see the range of telephone number you can create.

.. figure:: images/step-08.png

   Line information

By default, the selected protocol is SIP, which is what we want for now. Put the line number you want and then save.

.. figure:: images/step-09.png

   Save

Yahoo ! we now have a user named 'Alice Wonderland' the the phone number '1000' !

.. figure:: images/step-10.png

   User added information

Now go back in the main IPBX menu, and click on 'Lines'.

.. figure:: images/step-11.png

   Lines information

You see the line associated with the user we just created. Now click on the 'pencil' to 'Edit' the line.

.. figure:: images/step-12.png

   Edit line

There we are ! What we see here is the username and password for the SIP line. Now, you can configure your softphone, your linksys PAP2 or your SIP device by using the IP for your server and this username and password.

.. figure:: images/step-13.png

   General line information
