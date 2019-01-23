#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.constants import CONSTANTS


def access_css():
    switcher = {
        'desarrollo': [
            'bower_components/bootstrap/dist/css/bootstrap.min',
            'bower_components/font-awesome/css/font-awesome.min',
            'css/style'
            ],
        'produccion': ['dist/estacion.min'],
    }
    return switcher.get(CONSTANTS['env_static'])


def access_js():
    switcher = {
        'desarrollo': [
            'bower_components/jquery/dist/jquery.min',
            'bower_components/bootstrap/dist/js/bootstrap.min',
            'js/app'
        ],
        'produccion': ['dist/estacion.min'],
    }
    return switcher.get(CONSTANTS['env_static'])
