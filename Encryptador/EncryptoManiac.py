#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet as ft
from Util import ConstantesEncryptoManiac as CEM
import logging
import os
import sqlite3

class EncryptoManiac(object):

	def __init__(self):
		self.baseIniciada = False
		self.rutaBBDD = CEM.ConstantesEM.baseEncryptoManiac
		self.rutaKey =  CEM.ConstantesEM.nombreArchivoKey
		self.iniciarClaves()
		self.iniciarBaseDeClaves()
		#logging.basicConfig(filanme='./encrypto.log', encoding='utf-8', level=logging.INFO)
	
	def iniciarBaseDeClaves(self):
		logging.info('Iniciando base de claves.....')
		baseDeDatos = self.conectarBBDD()
		try:
			baseDeDatos.execute(CEM.ConsultaDB.crearTabla)
		except sqlite3.OperationalError:
			logging.info('Tabla ya existente, no se creo')
			
		self.baseIniciada = True
		baseDeDatos.close()
		logging.info('Base de datos iniciada con exito.')

	def iniciarClaves(self):
		logging.info('Iniciando archivos de clave......')
		if(os.path.exists(self.rutaKey)):
			self.fernet = ft(self.cargarClave())
		else:
			self.generarClave()
			self.fernet = ft(self.cargarClave())
		logging.info('Archivos de calve iniciado')

	def generarClave(self):
		logging.info('Generando clave')
		with open(self.rutaKey,'wb') as archivoKey:
			archivoKey.write(ft.generate_key())

	def cargarClave(self):
		logging.info('Cargando clave')
		archivoKey = open(self.rutaKey,'rb') 
		key = archivoKey.read()
		archivoKey.close()
		return key

	def encriptarASE(self, palabraAEncriptar):
		return self.fernet.encrypt(palabraAEncriptar.encode())
		
	def ingresarClave(self,nombreApp,clave):
		logging.info('Ingresando clave para '+nombreApp)
		baseDeDatos = self.conectarBBDD()
		baseDeDatos.execute(CEM.ConsultaDB.ingresarClave,(nombreApp,self.encriptarASE(clave)))
		baseDeDatos.commit()
		baseDeDatos.close()

	def buscarClave(self,nombreApp):
		logging.info('Buscando clave para '+nombreApp)
		baseDeDatos = self.conectarBBDD()
		cursor = baseDeDatos.execute(CEM.ConsultaDB.buscarClave,(nombreApp,))
		respuesta = cursor.fetchone()
		baseDeDatos.close()
		if( respuesta != None and len(respuesta)>0):
			return self.fernet.decrypt(respuesta[0]).decode()
		else:
			return None

	def listarCuentas(self):
		baseDeDatos = self.conectarBBDD()
		cursor = baseDeDatos.execute(CEM.ConsultaDB.listarCuentas)
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
		baseDeDatos = self.conectarBBDD()
		cursor = baseDeDatos.execute(CEM.ConsultaDB.buscarCuenta,(nombreCuenta,))
		respuesta = cursor.fetchall()
		baseDeDatos.close()
		if(len(respuesta)>0):
			return True
		else:
			return False

	def configurarRutaBBDD(self,rutaBBDD):
		self.rutaBBDD = rutaBBDD + CEM.ConstantesEM.baseEncryptoManiac
		self.iniciarBaseDeClaves()

	def configurarRutaKey(self,rutaKey):
		self.rutaKey = rutaKey + CEM.ConstantesEM.nombreArchivoKey
		self.iniciarClaves()

	def eliminarClave(self,parametro):
		baseDeDatos = self.conectarBBDD()
		baseDeDatos.execute(CEM.ConsultaDB.eliminarClave,(parametro,))
		baseDeDatos.commit()
		baseDeDatos.close()
			
	def actualizarClave(self,nombreApp,calveNueva):
		logging.info('Se va a actualizar la clave de la cuenta '+nombreApp)
		baseDeDatos = self.conectarBBDD()
		baseDeDatos.execute(CEM.ConsultaDB.actualizarClave,(self.encriptarASE(calveNueva),nombreApp))
		baseDeDatos.commit()
		baseDeDatos.close()

	def conectarBBDD(self):
		logging.warn('Se va a conectar a la base de datos'+self.rutaBBDD) 	
		return sqlite3.connect(self.rutaBBDD)

