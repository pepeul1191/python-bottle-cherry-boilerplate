# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, run, static_file
from configs.middlewares import logs, headers
from routes.demo import route as _demo
from routes.error import route as _error

app = Bottle()
# install middlewares
app.install(logs)
app.install(headers)


@app.route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


# static files
@app.route('/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./static')


if __name__ == '__main__':
    # routes
    app.mount('/demo', _demo)
    app.mount('/error', _error)
    # start app
    run(
        app,
        host='localhost',
        port=8080,
        server='cherrypy',
        debug=True,
        reloader=True)
