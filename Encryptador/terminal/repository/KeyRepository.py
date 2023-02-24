from cryptography.fernet import Fernet as ft
from Encryptador.terminal.configuracion.Configuracion import Configuracion
import logging
import os

class KeyRepository(object):

    def generarOCargarArchivoDeCalvesExistente(self, rutaKeysParams = Configuracion.rutaAlArchivoDeCredenciales):
        if(not os.path.exists(rutaKeysParams)):
            self._generarClave(rutaKeysParams)
        self._cargarClave(rutaKeysParams)

    def _generarClave(self,rutaKeyParams: str):
        logging.info('Generando clave')
        with open(rutaKeyParams,'wb') as archivoKey:
            archivoKey.write(ft.generate_key())

    def _cargarClave(self,rutaKeyParams):
        logging.info('Cargando clave')
        archivoKey = open(rutaKeyParams,'rb') 
        key = archivoKey.read()
        archivoKey.close()
        self.fernet = ft(key)

    def encriptarASE(self, palabraAEncriptar):
        return self.fernet.encrypt(palabraAEncriptar.encode())

    def desencriptarASE(self, calveEncriptada):
        return self.fernet.decrypt(calveEncriptada).decode()
