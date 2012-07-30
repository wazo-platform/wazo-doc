************
Introduction
************

XiVO History
============

XiVO has been created in 2005 by Proformatique.

`XiVO 1.2 was released <https://projects.xivo.fr/news/49>`_ on February 3, 2012.


Known Bugs and Limitations
==========================

The list of current bugs can be found on
`the official XiVO issue tracker <https://projects.xivo.fr/issues?set_filter=1&tracker_id=1>`_.


Transfers using DTMF
--------------------

When transfering a call using DTMF (\*1) you get an *invalid extension* error when dialing the
extension.

The work around to this problem is to create a preprocess subroutine and assign it the the destinations
where you have the problem.

Under :menuselection:`Services --> IPBX --> IPBX configuration --> Configuration files` add a new file
containing the following dialplan::

    [allow-transfer]
    exten = s,1,NoOp(## Setting transfer context ##)
    same = n,Set(__TRANSFER_CONTEXT=<internal-context>)
    same = n,Return()

Do not forget to substitute <internal-context> with your internal context.

Some places where you might want to add this preprocess subroutine is on queues and outgoing calls
to be able to transfer the called person to another extension.
