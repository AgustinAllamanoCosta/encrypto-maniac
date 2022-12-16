#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Encryptador.repository.BaseRepository import BaseRepository
from Encryptador.repository.KeyRepository import KeyRepository
from Util import ConstantesEncryptoManiac as CEM
import logging
import sqlite3

class EncryptoManiac(object):

	def __init__(self,baseRepositoryParam: BaseRepository, keyReposioryParam: KeyRepository):
		self.baseIniciada = False
		self.baseRepository: BaseRepository = baseRepositoryParam
		self.keyRepository: KeyRepository = keyReposioryParam
		self.iniciarClaves()
		self.iniciarBaseDeClaves()

	def iniciarBaseDeClaves(self):
		logging.info('Iniciando base de claves.....')
		try:
			self.baseRepository.ejecutarConsulta(CEM.ConsultaDB.crearTablaClaves)
		except sqlite3.OperationalError:
			logging.info('Tabla de calves ya existente, no se creo')
		try:
			self.baseRepository.ejecutarConsulta(CEM.ConsultaDB.crearTablaUsuario)
		except sqlite3.OperationalError:
			logging.info('Tabla de usuarios ya existente, no se creo')
		self.baseIniciada = True
		logging.info('Base de datos iniciada con exito.')

	def iniciarClaves(self):
		logging.info('Iniciando archivos de clave......')
		self.keyRepository.generarOCargarArchivoDeCalvesExistente()
		logging.info('Archivos de calve iniciado')
		
	def ingresarClave(self,nombreApp,clave):
		logging.info('Ingresando clave para '+nombreApp)
		nuevaClave = self.keyRepository.encriptarASE(clave)
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.ingresarClave,(nombreApp,nuevaClave))

	def buscarClave(self,nombreApp):
		logging.info('Buscando clave para '+nombreApp)
		respuesta = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarClave,(nombreApp,))
		if( respuesta != None and len(respuesta)>0):
			return self.keyRepository.desencriptarASE(respuesta[0])
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
		nuevaClave = self.keyRepository.encriptarASE(calveNueva)
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.actualizarClave,(nuevaClave,nombreApp))

	def iniciarSesion(self,usuario,contrasenia):
		contraseniaEnBase = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarUsuario,(usuario,))[0]	
		if(contraseniaEnBase is not None or contraseniaEnBase is not ''):
			contraseniaLimpia = self.keyRepository.desencriptarASE(contraseniaEnBase)
			return contraseniaLimpia == contrasenia
