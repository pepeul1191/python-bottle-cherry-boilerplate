#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from bottle import Bottle, HTTPResponse
from configs.middlewares import logs, headers

route = Bottle()
# install middlewares
route.install(logs)
route.install(headers)


@headers
@route.route('/api', method='GET')
def listar():
    rpta = None
    status = 200
    try:
        rpta = '=)'
    except Exception as e:
        rpta = {
            'tipo_mensaje': 'error',
            'mensaje': [
                'Se ha producido un error en listar los sistemas',
                str(e)
            ],
        }
        status = 500
    return HTTPResponse(status=status, body=json.dumps(rpta))
