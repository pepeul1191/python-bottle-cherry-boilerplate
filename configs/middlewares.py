# !/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from bottle import response, request


def logs(fn):
    '''
    Wrap a Bottle request so that a log line is emitted after it's handled.
    (This decorator can be extended to take the desired logger as a param.)
    '''
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        actual_response = fn(*args, **kwargs)
        print(request.method + request.path + str(response.status))
        return actual_response
    return _log_to_logger


def headers(fn):
    '''
    Wrap a Bottle request so that a log line is emitted after it's handled.
    (This decorator can be extended to take the desired logger as a param.)
    '''
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        actual_response = fn(*args, **kwargs)
        response.headers['server'] = 'Ubuntu; CherryPy\\8.9.1;'
        return actual_response
    return _log_to_logger
