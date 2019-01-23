# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, template, run
from configs.middlewares import logs, headers
from routes.demo import route as _demo

app = Bottle()
# install middlewares
app.install(logs)
app.install(headers)


@app.route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


if __name__ == '__main__':
    # routes
    app.mount('/demo', _demo)
    # start app
    run(
        app,
        host='localhost',
        port=8080,
        server='cherrypy',
        debug=True,
        reloader=True)
