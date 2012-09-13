******
Paging
******

With XiVO, you can define paging (i.e. intercom) extensions to page a
group of users. When calling a paging extension, the user's phones will
auto-answer if they support it.

You can manage your paging extensions via the :menuselection:`Services --> IPBX --> Paging`
page. When adding a new paging extension, the number can be anything; to call it,
you just need to prefix the paging number with ``*11``.


.. warning:: disabling option "Only dial a channel if its device state says that it is 'NOT_INUSE':" will cause problem with SCCP phones trying to call a paging extension. When this scenario happens, the caller SCCP phone will also be called, a second line will be opened and automatically activated, giving the impression that paging does not work, untill the phone is switched back to the original line.
