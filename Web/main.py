#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from Web.aplicacionWeb import aplicacion 

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')
