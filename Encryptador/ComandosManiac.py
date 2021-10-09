#!/usr/bin/env python
# -*- coding: utf-8 -*
from Util.CustomException import *
from Util.ConstantesEncryptoManiac import *
from Util.UIManiac import *
from Encryptador import EncryptoManiac as EM
from os import system
from getpass import getpass
import logging
import tkinter

class Comando(object):

	def __init__(self):
		self.encriptoManiac = EM.EncryptoManiac()
		self.mensajeComando = ""

	def escribirEnConsolaStrategy(self,historial):
		if(self.mensajeComando != None):
			print(self.mensajeComando)
			historial.agregarEntrada(self.mensajeComando)

class ComandoConsola(Comando):

	def ejecutar(self,parametros):
		return 0

	def validarParametros(self,parametros):
		if(parametros == []):
			raise ParametrosComandosNullos()

class ComandoConsolaSinParametros(Comando):
	
	def ejecutar(self):
		return 0

class ComandoSensibles(ComandoConsola):

	def obtenerContraseña(self):
		return getpass("Contraseña:")

class ComandoAgregar(ComandoSensibles):

	def ejecutar(self,parametros):
		logging.info('Se ejecuta comando agregar.')
		if(len(parametros)==0):
			logging.debug('Parametros insuficiente para el comando agregar.')
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			if(self.encriptoManiac.existeCuentaEnBase(parametros[0]) != True):
				self.encriptoManiac.ingresarClave(parametros[0],self.obtenerContraseña())
			else:
				logging.debug('La cuenta esta duplicada')
				raise CuentaEnBaseDuplicadaException(parametros[0])
		self.mensajeComando = "Se agrego la contraseña"
		return 0

class ComandoModificar(ComandoSensibles):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando modificar')
		if(len(parametros)==0):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoModificar)
		else:
			self.encriptoManiac.actualizarClave(parametros[0],self.obtenerContraseña())
		self.mensajeComando = "Se modifico la contraseña de la cuenta "+parametros[0]
		return 0

class ComandoEliminar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando eliminar')
		self.encriptoManiac.eliminarClave(parametros[0])
		return 0

class ComandoMostrar(ComandoConsola):
	
	def __init__(self):
		super().__init__()
		self.popUp = PopUpManiac()

	def ejecutar(self,parametros):
		logging.info('Ejecutando el comando mostrar')
		super().validarParametros(parametros)
		self.mensajeComando = self.encriptoManiac.buscarClave(parametros[0])
		self.popUp.setMensaje(self.mensajeComando)
		return 0

	def escribirEnConsolaStrategy(self,historial):
		try:
			self.popUp.mostrarPopUp()
		except:
			pass

class ComandoAyuda(ComandoConsola):

	def __init__(self):
		self.mensajeComando = ""
		self.mensajeAyuda = {
		'listar': ConstanteConsola.mensajeAyudaComandoListar,
		'agregar':ConstanteConsola.mensajeAyudaComandoAgregar,
		'exit':ConstanteConsola.mensajeAyudaComandoExit,
		'mostrar':ConstanteConsola.mensajeAyudaComandoMostrar,
		'vermas':ConstanteConsola.mensajeAyudaComandoVerMas,
		'eliminar':ConstanteConsola.mensajeAyudaComandoEliminar,
		'modificar':ConstanteConsola.mensajeAyudaComandoModificar
		}

	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando ayuda')
		self.mensajeComando = self.mensajeAyuda[parametros[0]]
		return 0

class ComandoListar(ComandoConsolaSinParametros):

	def ejecutar(self):
		logging.info('Ejecutando el comando listar')
		self.mensajeComando = self.encriptoManiac.listarCuentas()
		return 0

class ComandoExit(ComandoConsolaSinParametros):

	def ejecutar(self):
		logging.info('Ejecutando el comando exit')
		raise InterrumpirConsola()

class ComandoVerMas(ComandoConsolaSinParametros):

	def __init__(self):
		pass

	def ejecutar(self):
		self.mensajeComando = ConstanteConsola.mensajeComandosAvanzados
		return 0

class ComandoEscribirCabeceraDeConsola(ComandoConsolaSinParametros):

	def escribirEnConsolaStrategy(self,historial):
		print(ConstanteConsola.mensajeBienvenida)
		print(ConstanteConsola.mensajeComandosBasicos)
		historial.agregarEntrada(ConstanteConsola.mensajeBienvenida)
		historial.agregarEntrada(ConstanteConsola.mensajeComandosBasicos)

class ComandoUnix(ComandoConsolaSinParametros):
	def __init__(self):
		pass

	def ejecutar(self):
		system('clear')

class ComandoWin(ComandoConsolaSinParametros):
	def __init__(self):
		pass

	def ejecutar(self):
		system('cls')