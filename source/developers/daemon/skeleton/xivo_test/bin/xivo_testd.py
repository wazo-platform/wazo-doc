# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

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
