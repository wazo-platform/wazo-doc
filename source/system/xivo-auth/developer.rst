.. _xivo-auth-developer:

===========================
XiVO auth developer's guide
===========================

xivo-auth is meant to be easy to extend. This section describes how to add
features to xivo-auth.


backends
========

xivo-auth allow its administrator to configure one or many source of
authentification. Implementing a new kind of authentification is quite simple.

# Create a python module implementing the `backend interface <https://github.com/xivo-pbx/xivo-auth/blob/master/xivo_auth/interfaces.py>`_.
# Install the python module with an entry point *xivo_auth.backends*

An example backend backend implementation is available `here <http://github.com/xivo-pbx/xivo-auth-example-backend>`_.
