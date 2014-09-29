*********
CLI Tools
*********

XiVO comes with a collection of console (CLI) tools to help administer the server.

.. _xivo_dist:

xivo-dist
---------

xivo-dist is the xivo repository sources manager. It is used to switch between distributions
(production, development, release candidate, archived version). Example use cases :
 * switch to production repository : ``xivo-dist xivo-five``
 * switch to development repository : ``xivo-dist xivo-dev``
 * switch to release candidate repository : ``xivo-dist xivo-rc``
 * switch to an archived version's repository (here 14.18) : ``xivo-dist xivo-14.18``
