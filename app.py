# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from bottle import route, run, template, install, response, hook


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@hook('after_request')
def separator():
    response.headers['server'] = 'Ubuntu; CherryPy\\8.9.1;'


run(host='localhost',
    port=8080,
    server='cherrypy',
    debug=True,
    reloader=True)
