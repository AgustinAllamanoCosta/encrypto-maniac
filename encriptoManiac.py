#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from cryptography.fernet import Fernet as ft
from constantesEncriptoManiac import *
import os
import logging

class EncriptoManiac(object):

	def __init__(self):
		self.baseIniciada = False
		self.iniciarClaves()
		self.iniciarBaseDeClaves()
		logging.basicConfig(filanme='encrypto.log', encoding='utf-8', level=logging.DEBUG)

	def iniciarBaseDeClaves(self):
		logging.info('Iniciando base de claves.....')
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		try:
			baseDeDatos.execute(ConsultaDB.crearTabla)
		except sqlite3.OperationalError:
			logging.info('Tabla ya existente, no se creo')
			
		self.baseIniciada = True
		baseDeDatos.close()
		logging.info('Base de datos iniciada con exito.')

	def iniciarClaves(self):
		logging.info('Iniciando archivos de clave......')
		if(os.path.exists(ConstantesEncryptoManiac.nombreArchivoKey)):
			self.fernet = ft(self.cargarClave())
		else:
			self.generarClave()
			self.fernet = ft(self.cargarClave())
		logging.info('Archivos de calve iniciado')

	def generarClave(self):
		logging.info('Generando clave')
		with open(ConstantesEncryptoManiac.nombreArchivoKey,'wb') as archivoKey:
			archivoKey.write(ft.generate_key())

	def cargarClave(self):
		logging.info('Cargando clave')
		archivoKey = open(ConstantesEncryptoManiac.nombreArchivoKey,'rb') 
		key = archivoKey.read()
		archivoKey.close()
		return key

	def encriptarASE(self, palabraAEncriptar):
		return self.fernet.encrypt(palabraAEncriptar.encode())
		
	def ingresarClave(self,nombreApp,clave):
		logging.info('Ingresando clave para '+nombreApp)
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		baseDeDatos.execute(ConsultaDB.ingresarClave,(nombreApp,self.encriptarASE(clave)))
		baseDeDatos.commit()
		baseDeDatos.close()

	def buscarClave(self,nombreApp):
		logging.info('Buscando clave para '+nombreApp)
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		cursor = baseDeDatos.execute(ConsultaDB.buscarClave,(nombreApp,))
		respuesta = cursor.fetchone()
		baseDeDatos.close()
		if( respuesta != None and len(respuesta)>0):
			return self.fernet.decrypt(respuesta[0]).decode()
		else:
			return None

	def listarCuentas(self):
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		cursor = baseDeDatos.execute(ConsultaDB.listarCuentas)
		respuesta = cursor.fetchall()
		baseDeDatos.close()
		if(len(respuesta)>0):
			lista = ''
			for app in respuesta:
				lista += ' '+app[0]+',\n' 
			return lista
		else:
			return None

	def existeCuentaEnBase(self,nombreCuenta):
		logging.info('Existe la cuenta'+nombreCuenta)
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		cursor = baseDeDatos.execute(ConsultaDB.buscarCuenta,(nombreCuenta,))
		respuesta = cursor.fetchall()
		baseDeDatos.close()
		if(len(respuesta)>0):
			return True
		else:
			return False


	def eliminarClave(self,parametro):
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		baseDeDatos.execute(ConsultaDB.eliminarClave,(parametro,))
		baseDeDatos.commit()
		baseDeDatos.close()
			
	def actualizarClave(self,nombreApp,calveNueva):
		logging.info('Se va a actualizar la clave de la cuenta'+nombreCuenta)
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		baseDeDatos.execute(ConsultaDB.actualizarClave,(self.encriptarASE(calveNueva),nombreApp))
		baseDeDatos.commit()
		baseDeDatos.close()

