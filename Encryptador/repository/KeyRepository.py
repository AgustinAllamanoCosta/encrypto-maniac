#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet as ft
from Encryptador.configuracion.Configuracion import Configuracion
import logging
import os

class KeyRepository(object):

    def __init__(self):
        self.baseIniciada = False

    def generarOCargarArchivoDeCalvesExistente(self, rutaKeysParams = Configuracion.rutaAlArchivoDeConfiguracion):
        if(os.path.exists(rutaKeysParams)):
            self.fernet = ft(self._cargarClave(rutaKeysParams))
        else:
            self._generarClave(rutaKeysParams)
            self.fernet = ft(self._cargarClave(rutaKeysParams))

    def _generarClave(self,rutaKeyParams: str):
        logging.info('Generando clave')
        with open(rutaKeyParams,'wb') as archivoKey:
            archivoKey.write(ft.generate_key())

    def _cargarClave(self,rutaKeyParams):
        logging.info('Cargando clave')
        archivoKey = open(rutaKeyParams,'rb') 
        key = archivoKey.read()
        archivoKey.close()
        return key

    def encriptarASE(self, palabraAEncriptar):
        return self.fernet.encrypt(palabraAEncriptar.encode())

    def desencriptarASE(self, calveEncriptada):
        return self.fernet.decrypt(calveEncriptada).decode()
