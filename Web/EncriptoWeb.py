#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
#from Encryptador import EncryptoManiac as EM
#from Util.ConstantesEncryptoManiac import ConstantesEM

aplicacion = Flask(__name__)

#encriptador = EM.EncryptoManiac([ConstantesEM.rutaARecursosWeb,ConstantesEM.rutaARecursosWeb])    
#aplicacion.config['EncryptoManiac'] = encriptador

@aplicacion.route('/hola')
def hola():
    return "<p>Hola</p>"

#if __name__ == "__main__":
#    aplicacion.run()