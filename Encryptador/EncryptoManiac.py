#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cryptography.fernet import Fernet as ft
from Encryptador.Repository import Repository
from Util import ConstantesEncryptoManiac as CEM
import logging
import os
import sqlite3

class EncryptoManiac(object):

	def __init__(self):
		self.baseIniciada = False
		self.rutaKey =  CEM.ConstantesEM.nombreArchivoKey
		self.baseRepository = Repository()
		self.iniciarClaves()
		self.iniciarBaseDeClaves()
		logging.basicConfig(filanme='encrypto.log', encoding='utf-8', level=logging.DEBUG)

	def iniciarBaseDeClaves(self):
		logging.info('Iniciando base de claves.....')
		try:
			self.baseRepository.ejecutarConsulta(CEM.ConsultaDB.crearTabla)
		except sqlite3.OperationalError:
			logging.info('Tabla ya existente, no se creo')
		self.baseIniciada = True
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
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.ingresarClave,(nombreApp,self.encriptarASE(clave)))

	def buscarClave(self,nombreApp):
		logging.info('Buscando clave para '+nombreApp)
		respuesta = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarClave,(nombreApp,))
		if( respuesta != None and len(respuesta)>0):
			return self.fernet.decrypt(respuesta[0]).decode()
		else:
			return None

	def listarCuentas(self):
		respuesta = self.baseRepository.obtenerTodos(CEM.ConsultaDB.listarCuentas)
		if(len(respuesta)>0):
			lista = ''
			for app in respuesta:
				lista += ' '+app[0]+',\n' 
			return lista
		else:
			return None

	def existeCuentaEnBase(self,nombreCuenta):
		logging.info('Existe la cuenta'+nombreCuenta)
		respuesta = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.buscarCuenta,(nombreCuenta,))
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
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.eliminarClave,(parametro,))

	def actualizarClave(self,nombreApp,calveNueva):
		logging.info('Se va a actualizar la clave de la cuenta'+nombreApp)
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.actualizarClave,(self.encriptarASE(calveNueva),nombreApp))
