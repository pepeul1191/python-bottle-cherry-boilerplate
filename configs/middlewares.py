# !/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps
from bottle import request


def logs(fn):
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        actual_response = fn(*args, **kwargs)
        print(
            request.method
            + ' -> '
            + request.fullpath + ' '
            + str(actual_response.status)
        )
        return actual_response
    return _log_to_logger


def headers(fn):
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        actual_response = fn(*args, **kwargs)
        actual_response.headers['server'] = 'Ubuntu; CherryPy\\8.9.1;'
        return actual_response
    return _log_to_logger
