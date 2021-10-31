#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from Web.aplicacionWeb import aplicacion 

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('singup.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')