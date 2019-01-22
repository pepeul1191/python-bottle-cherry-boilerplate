# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime
from functools import wraps
from bottle import route, run, template, install, response, hook, request


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


def log_to_logger(fn):
    '''
    Wrap a Bottle request so that a log line is emitted after it's handled.
    (This decorator can be extended to take the desired logger as a param.)
    '''
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        actual_response = fn(*args, **kwargs)
        # modify this to log exactly what you need:
        print(request.method + request.path + str(response.status))
        response.headers['server'] = 'Ubuntu; CherryPy\\8.9.1;'
        return actual_response
    return _log_to_logger


"""
@hook('after_request')
def separator():
    response.headers['server'] = 'Ubuntu; CherryPy\\8.9.1;'
"""

install(log_to_logger)

run(host='localhost',
    port=8080,
    server='cherrypy',
    debug=True,
    reloader=True)
