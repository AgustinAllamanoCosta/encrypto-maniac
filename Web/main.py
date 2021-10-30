#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from Web.aplicacionWeb import aplicacion 

main = Blueprint('main',__name__)

@main.route('/')
def indexSitio():
    return 'Index de flask'

@main.route('/profile')
def perfiles():
    return 'Perfiles'
