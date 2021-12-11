#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Encryptador import EncryptoManiac as EM
import os

class aplicacion():
    
    def __init__(self):
        self.baseDeDatos = SQLAlchemy()
        self.encriptador = EM.EncryptoManiac()
        
    def crear(self):
        aplicacion = Flask(__name__)
        self.encriptador.configurarRutaBBDD(os.getcwd()+'\\Web\\')
        
        aplicacion.config['SECRET_KEY'] = '3ncrypt0m4n14c'
        aplicacion.config['SQLALCHEMYY_DATABASE_URI'] = 'sqlite:///'+self.encriptador.rutaBBDD
        aplicacion.config['EncryptoManiac'] = self.encriptador
        
        self.baseDeDatos.init_app(aplicacion)
        
        # Template para las rutas de la aplicacion con auteticacion
        
        from .auth import auth as authBlueprint
        aplicacion.register_blueprint(authBlueprint)
        
        # Template para las rutas de la aplicacion sin autenticacion
        from .main import main as mainBlueprint
        aplicacion.register_blueprint(mainBlueprint)
        
        return aplicacion
