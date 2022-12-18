#!/usr/bin/env python
# -*- coding: utf-8 -*
from getpass import getpass
from os import system
from Encryptador import EncryptoManiac as EM
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Util.ConstantesEncryptoManiac import ConstanteConsola
from Util.CustomException import ParametrosComandosNullos, ParametrosComandoIncompletos, CuentaEnBaseDuplicadaException, InterrumpirConsola
from Util.UIManiac import PopUpManiac
import logging

class Comando(object):

	def __init__(self, encryptador: EM.EncryptoManiac):
		self.encriptoManiac = encryptador
		self.mensajeComando = ""

	def ejecutar(self,parametros = []):
		return 0

	def validarParametros(self,parametros):
		if(parametros == []):
			raise ParametrosComandosNullos()


	def escribirEnConsolaStrategy(self,historial):
		if(self.mensajeComando != None):
			print(self.mensajeComando)
			historial.agregarEntrada(self.mensajeComando)

class ComandoSensibles(Comando):

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

class ComandoEliminar(Comando):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando eliminar')
		self.encriptoManiac.eliminarClave(parametros[0])
		return 0

class ComandoMostrar(Comando):
	
	def __init__(self,encripto):
		super().__init__(encripto)
		self.popUp = PopUpManiac(True,4000)

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

class ComandoAyuda(Comando):

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

class ComandoListar(Comando):

	def ejecutar(self, parametros = []):
		logging.info('Ejecutando el comando listar')
		self.mensajeComando = self.encriptoManiac.listarCuentas()
		return 0

class ComandoExit(Comando):

	def ejecutar(self, parametros = []):
		logging.info('Ejecutando el comando exit')
		raise InterrumpirConsola()

class ComandoVerMas(Comando):

	def __init__(self):
		pass

	def ejecutar(self,parametros = []):
		self.mensajeComando = ConstanteConsola.mensajeComandosAvanzados
		return 0

class ComandoEscribirCabeceraDeConsola(Comando):

	def escribirEnConsolaStrategy(self,historial):
		print(ConstanteConsola.mensajeBienvenida)
		print(ConstanteConsola.mensajeComandosBasicos)
		historial.agregarEntrada(ConstanteConsola.mensajeBienvenida)
		historial.agregarEntrada(ConstanteConsola.mensajeComandosBasicos)

class ComandoConfigurar(Comando):
	
	def ejecutar(self,parametros):
		
		for index, param in enumerate(parametros):
			if(param.lower() == '-p'):
				self.encriptoManiac.configurarRutaBBDD(parametros[index + 1 ])
			elif(param.lower() == '-a'):
				self.encriptoManiac.configurarRutaKey(parametros[index + 1])
		return 0		

class ComandoLogin(Comando):

	def __init__(self, encryptador: EM.EncryptoManiac, sesionUsuarioParam: EstadoDeSesion ):
		self.encriptoManiac: EM.EncryptoManiac = encryptador
		self.sesionUsuario: EstadoDeSesion = sesionUsuarioParam
		self.mensajeComando = ""

	def ejecutar(self):
		self.sesionUsuario.sesionActiva = self.encriptoManiac.iniciarSesion(self.obtenerUsuario(),self.obtenerContrasenia())

	def obtenerUsuario(self):
		return input('Usuario: ')
	
	def obtenerContrasenia(self):
		return getpass('Contrasenia: ')

class ComandoUnix(Comando):
	def __init__(self):
		pass

	def ejecutar(self, parametros):
		system('clear')

class ComandoWin(Comando):
	def __init__(self):
		pass

	def ejecutar(self, parametros):
		system('cls')