#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from Web.aplicacionWeb import aplicacion 

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'