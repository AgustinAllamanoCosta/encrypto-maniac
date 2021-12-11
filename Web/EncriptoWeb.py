#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from Encryptador import EncryptoManiac as EM
from Util.ConstantesEncryptoManiac import ConstantesEM
from flask import Blueprint, render_template
from Web.main import main as mainBlueprint
import os

aplicacion = Flask(__name__)

def create_app():
    encriptador = EM.EncryptoManiac([ConstantesEM.rutaARecursosWeb,ConstantesEM.rutaARecursosWeb])    

    aplicacion.config['EncryptoManiac'] = encriptador
    aplicacion.register_blueprint(mainBlueprint)
    return aplicacion

@aplicacion.route('/')
def index():
    return "<p>Hola</p>"
    #return render_template('index.html')
    
