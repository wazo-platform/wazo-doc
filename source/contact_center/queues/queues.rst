******
Queues
******

Call queues are managed on the
:menuselection:`Services --> Call Center --> Queues` page:

.. figure:: add-queue.png
   :scale: 85%

   :menuselection:`Services --> Call Center --> Queues`


Ring strategy
   Define how queue members are called when a call enters the queue.

   * Name : used as an unique id, cannot be ``general``
   * Display name : Displayed on the supervisor screens
   * Linear: for each call, call the first member, then the second, etc.
   * Least recent: call the member who has least recently hung up a call.
   * Fewest calls: call the member with the fewest completed calls.
   * Round robin memory: call the "next" member after the one who answered.
   * Random: call a member at random
   * Weight random: same as random, but taking the member penalty into account.
   * Ring all: call all members at the same time.

   .. warning::

      When editing a queue, you can't change the ring strategy to linear. This
      is due to an asterisk limitation. Unfortunately, if you want to change the
      ring strategy of a queue to linear, you'll have to delete and create a new
      queue with the right strategy.


Timers
======

You may control how long a call has to stay in the queue using different timers

   * Member reachabillity time out (Advanced tab) : This is the agent ringing maximum time, if a call is not answered within this time call is
     forwareded to an other agent.
   * Time before retrying a call to a member (Advanced tab) : When an agent does not answer the call will not be placed during that time
   * Ringing time (Application tab) : The total time the call will stay in the queue
   * Timeout priority (Application tab) : If set to configuration, call will wait the last agent ringing timeout expires before beeing diverted
      If set to dialplan (application), at the end of the ringing time the call is diverted.

.. figure:: queue_timers.jpg
   :scale: 85%


Diversions
==========

Diversions can be used to specify distribution options on a given scenario.

.. figure:: diversions.png
    :scale: 85%


Estimated Wait Time Overrun
---------------------------

When this option is used, the administrator can set a destination for calls
when the average waiting time is over the specified number.



Waiting Calls / Available Agents Ratio
--------------------------------------

When this option is used, the administrator can set a destination for calls
when the number of waiting calls is over the number of logged agents.

A Threshold of 100% means that there should not be more than one waiting call
for each logged agents. A higher ratio means more waiting calls will be received.

.. warning::

  With a threshold under 100% and only one agent logged, no call will distributed
  since one waiting call / one agent = 100%
