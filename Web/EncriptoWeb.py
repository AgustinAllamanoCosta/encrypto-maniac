#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

@aplicacion.route('/consultFrom', methods=['POST','GET'])
def consultFrom():
    return render_template('consult.html',cuentas=buscarCuentas())

@aplicacion.route('/addCount', methods=['POST'])
def addCount():
    if(request.form["primeraContrasenia"] == request.form["segundaContrasenia"]):
        encriptador.ingresarClave(request.form["nombreCuenta"],request.form["segundaContrasenia"])
    return render_template('consult.html',cuentas=buscarCuentas())

@aplicacion.route('/acountsFrom', methods=['POST'])
def acountForm():
    return encriptador.buscarClave(request.form["nombreCuenta"])

def buscarCuentas():
    cuentasUsuario = []
    if(encriptador.existenCuentasEnLaBase()):
        cuentasUsuario = encriptador.obtenerCuentasDeLaBase()
    return cuentasUsuario