*********************************************
The switchboard's queue preprocess subroutine
*********************************************

The switchboard's queue now uses a preprocess subroutine named *xivo_subr_switchboard*. This preprocess
subroutine will be associated with all queues names *__switchboard* with no preprocess subroutine
defined before the upgrade.

If your switchboard queue is named anything other than *__switchboard* you should add the preprocess
subroutine manually.

If your switchboard queue already has a preprocess subroutine, you should add a Gosub(xivo_subr_switchboard)
to you preprocess subroutine.

.. warning:: This change is only applied to the switchboard distribution queue, not the queue for call on hold.
