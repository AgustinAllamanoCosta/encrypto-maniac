#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import Action
import re
from flask import request
from flask import Flask
from flask import render_template
from Encryptador import EncryptoManiac as EM
from Util.ConstantesEncryptoManiac import ConstantesEM

aplicacion = Flask(__name__)
encriptador = EM.EncryptoManiac([ConstantesEM.rutaARecursosWeb,ConstantesEM.rutaARecursosWeb])    

@aplicacion.route('/')
def login():
    return render_template('login.html')

@aplicacion.route('/singUp')
def singUp():
    return render_template('singUp.html')

@aplicacion.route('/consultForm', methods=['POST','GET'])
def consultFrom():
    if(request.form.get('action') == 'Mostrar'):
        return encriptador.buscarClave(request.form["nombreCuenta"])
    elif(request.form.get('action') == 'Eliminar'):
        encriptador.eliminarClave(request.form.get('nombreCuenta'))
    elif(request.form.get('action') == 'Agregar'):
        addCount(request)

    return render_template('consult.html',cuentas=buscarCuentas())

def addCount(request):
    if(request.form["primeraContrasenia"] == request.form["segundaContrasenia"]):
        encriptador.ingresarClave(request.form["nombreCuenta"],request.form["segundaContrasenia"])

def buscarCuentas():
    cuentasUsuario = []
    if(encriptador.existenCuentasEnLaBase()):
        cuentasUsuario = encriptador.obtenerCuentasDeLaBase()
    return cuentasUsuario