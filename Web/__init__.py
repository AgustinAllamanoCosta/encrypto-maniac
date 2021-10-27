#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Encryptador.EncryptoManiac import EncryptoManiac

baseDeDatos = SQLAlchemy()
encriptador = EncryptoManiac()

def crearAplicacionWeb():
    aplicacion = Flask(__name__)
    encriptador.configurarRutaBBDD('..\\EncryptoManiac\\Web\\app\\')
    
    aplicacion.config['SECRET_KEY'] = '3ncrypt0m4n14c'
    aplicacion.config['SQLALCHEMYY_DATABASE_URI'] = 'sqlite:///'+encriptador.rutaBBDD
    aplicacion.config['EncryptoManiac'] = encriptador
    
    baseDeDatos.init_app(aplicacion)
    
    # Template para las rutas de la aplicacion con auteticacion
    
    from .auth import auth as authBlueprint
    aplicacion.register_blueprint(authBlueprint)
    
    # Template para las rutas de la aplicacion sin autenticacion
    from .main import main as mainBlueprint
    aplicacion.register_blueprint(mainBlueprint)
    
    return aplicacion