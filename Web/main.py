#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from . import maniacDB

main = Blueprint('main',__name__)

@main.route('/')
def indexSitio():
    return 'Index de flask'

@main.route('/profile')
def perfiles():
    return 'Perfiles'

if __name__ == '__main__':
    pass