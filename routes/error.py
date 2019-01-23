#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import Bottle, HTTPResponse, template
from configs.middlewares import logs, headers
from configs.constants import CONSTANTS
from configs.helpers import load_css, load_js
from helpers.error_helper import access_css, access_js

route = Bottle()
# install middlewares
route.install(logs)
route.install(headers)


@route.route('/access/<num_error>', method='GET')
def access(num_error):
    helpers = {}
    helpers['css'] = load_css(access_css())
    helpers['js'] = load_js(access_js())
    errores = {
        '404': {
            'mensaje': 'Archivo no encontrado',
            'numero': '404',
            'descripcion': 'La página que busca no se'
            + ' encuentra en el servidor',
        },
        '505': {
            'mensaje': 'Acceso restringido',
            'numero': '505',
            'descripcion': 'Necesita estar logueado',
        },
    }
    if num_error[0] != '4':
        num_error == 500
    else:
        num_error = int(num_error)
    locals = {
        'constants': CONSTANTS,
        'title': 'Error',
        'mensaje': errores[str(num_error)]['mensaje'],
        'numero': errores[str(num_error)]['numero'],
        'descripcion': errores[str(num_error)]['descripcion'],
    }
    boby_template = template(
        'templates/error/access',
        locals=locals,
        helpers=helpers
    )
    return HTTPResponse(status=num_error, body=boby_template)
