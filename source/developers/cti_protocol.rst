************
CTI protocol
************

Message flow
============

Received messages from the CTI clients to the server are received by the CTIServer class. The CTIServer then calls ``interface_cti.CTI`` class ``manage_connection`` method. The ``interface_cti`` uses his ``_cti_command_handler`` member to parse and run the command. The ``CTICommandHandler`` get a list of classes that handle this message from the ``CTICommandFactory``. Then the the ``interface_cti.CTI`` calls ``run_commands`` on the handler, which returns a list of all commands replies.

To implement a new message in the protocol you have to create a new class that inherits the ``CTICommand`` class. Your new class should have a static member caller ``required_fields`` which is a list of required fields for this class. Your class should also have a ``conditions`` static member which is a list of tupples of conditions to detect that an incoming message matches this class. The ``__init__`` of your class is responsible for the initialization of it's fields and should call ``super(<ClassName>, self).__init__(msg)``. Your class should register itself to the ``CTICommandFactory``.

.. code-block:: python

    from xivo_cti.cti.cti_command import CTICommand
    from xivo_cti.cti.cti_command_factory import CTICommandFactory

    class InviteConfroom(CTICommand):
        required_fields = ['class', 'invitee']
        conditions = [('class', 'invite_confroom')]
        def __init__(self):
            super(InviteConfroom, self).__init__(msg)
            self._invitee = msg['invitee']

    CTICommandFactory.register_class(InviteConfroom)

Each CTI commands has a callback list that you can register to from anywhere. Each callback function will be called when this message is received with the command as parameter.

Refer to ``MeetmeList.__init__`` for a callback registration example and to ``MeetmeList.invite`` for the implementation of a callback.

.. code-block:: python

    from xivo_cti.cti.commands.invite_confroom import InviteConfroom

    class MySuperClass(object):
        def __init__(self):
            InviteConfroom.register_callback(self.invite_confroom_handler)

        def invite_confroom_handler(self, invite_confroom_command):
            # Do your stuff here.
            if ok:
                return invite_confroom_command.get_message('Everything is fine')
            else:
                return invite_confroom_command.get_warning('I don't know you, go away', True)

Note: The client's connection is injected in the command instance before calling callbacks functions. The client's connection is an ``interface_cti.CTI`` instance.
