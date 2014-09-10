# -*- coding: utf-8 -*-

import logging
import os
import signal
import thread

from flup.server.fcgi import WSGIServer

from xivo.daemonize import pidfile_context
from xivo.user_rights import change_user
from xivo.xivo_logging import setup_logging
from xivo_test import rest_api
from xivo_test import config

logger = logging.getLogger(__name__)


def main():
    config = config.fetch_and_merge_config()

    setup_logging(config.LOG_FILENAME, config.foreground, config.debug)
    if config.user:
        change_user(config.user)

    with pidfile_context(config.PID_FILENAME, config.foreground):
        _run(config)


def _run(config):
    _init_signal()

    ...

    logger.debug('WSGIServer starting with uid %s', os.getuid())
    WSGIServer(rest_api.app,
               bindAddress=config.SOCKET_FILENAME,
               multithreaded=True,
               multiprocess=False,
               debug=config.debug).run()


def _init_signal():
    signal.signal(signal.SIGTERM, _handle_sigterm)


def _handle_sigterm(signum, frame):
    raise SystemExit()


if __name__ == '__main__':
    main()
