# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime
from functools import wraps
from bottle import route, run, template, install, response, hook, request
from configs.middlewares import logs, headers


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


install(logs)
install(headers)

run(host='localhost',
    port=8080,
    server='cherrypy',
    debug=True,
    reloader=True)
