#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet as ft
from Util import ConstantesEncryptoManiac as CEM
import logging
import os

class KeyRepository(object):

    def __init__(self):
        self.baseIniciada = False
        self.rutaKey =  CEM.ConstantesEM.nombreArchivoKey
        logging.basicConfig(filename='encrypto.log', level=logging.DEBUG)

    def generarOCargarArchivoDeCalvesExistente(self):
        if(os.path.exists(self.rutaKey)):
            self.fernet = ft(self._cargarClave())
        else:
            self._generarClave()
            self.fernet = ft(self._cargarClave())

    def _generarClave(self):
        logging.info('Generando clave')
        with open(self.rutaKey,'wb') as archivoKey:
            archivoKey.write(ft.generate_key())

    def _cargarClave(self):
        logging.info('Cargando clave')
        archivoKey = open(self.rutaKey,'rb') 
        key = archivoKey.read()
        archivoKey.close()
        return key

    def encriptarASE(self, palabraAEncriptar):
        return self.fernet.encrypt(palabraAEncriptar.encode())

    def desencriptarASE(self, calveEncriptada):
        return self.fernet.decrypt(calveEncriptada).decode()

    def configurarRutaKey(self,rutaKey):
        self.rutaKey = rutaKey + CEM.ConstantesEM.nombreArchivoKey
        self.iniciarClaves()
