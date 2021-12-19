#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from Encryptador import EncryptoManiac as EM
from Util.ConstantesEncryptoManiac import ConstantesEM

aplicacion = Flask(__name__)
encriptador = EM.EncryptoManiac([ConstantesEM.rutaARecursosWeb,ConstantesEM.rutaARecursosWeb])    

@aplicacion.route('/login')
def login():
    return render_template('login.html')

@aplicacion.route('/singUp')
def singUp():
    return render_template('singUp.html')

@aplicacion.route('/consult')
def consult():
    return render_template('consult.html')