# -*- coding: utf-8 -*-

import json
import logging

from flask import Flask
from flask.helpers import make_response


logger = logging.getLogger(__name__)
app = Flask(__name__)

VERSION = 0.1


@app.route('/{version}/ping'.format(version=VERSION))
def ping():
    res = json.dumps({'Message': 'Pong'})
    return make_response(res, 200, None, 'application/json')
