*************
Web Services
*************

This page only describes ways to access XiVO Web services.

If you want the description of the data sent and received from Web Services,
please refer to :ref:`web-services-api`.


Ways to manually query XiVO WS
==============================


Curl
----

The ``curl`` command to query WS is::

   curl -k --data-binary @test_line.txt -u admin:proformatique -H 'Content-Type:application/json' --write-out '%{http_code}\n' 'https://skaro/service/ipbx/json.php/restricted/pbx_settings/lines/?act=edit&id=150'

Explanations:

* ``-k`` disables certificate verification
* ``--data-binary`` ensures there is no interpretation of the data
* ``@test_line.txt`` is the file name that contains the POST data, in JSON format
* ``-u user:password`` handles the authentification, according to the WS access settings in XiVO
* ``-H 'Content-Type:application/json'`` explicits the data type
* ``--write-out '%{http_code}\n'`` makes ``curl`` print the HTTP response code
* ``'https://skaro/service/ipbx/json.php/restricted/pbx_settings/lines/?act=edit&id=150'`` is the WS URL (don't forget the simple quotes to escape the URL from the shell)


xivo_ws
-------

The python package xivo-ws is available on PyPI. It allows you to query XiVO WS
from a Python console or script.

The package contains both a library that can be imported, namely ``xivo_ws``,
and an interactive console, namely ``xivo_ws_debug``.

You can find some examples of the usage of the ``xivo_ws`` library in the
embedded script examples.

``xivo_ws_debug`` is mainly used to ease developement and tinkering with XiVO
WS.
