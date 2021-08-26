#!/usr/bin/env python
# -*- coding: utf-8 -*
from CustomException import *
from constantesEncriptoManiac import *
from encriptoManiac import *

class ComandoConsola(object):

	def __init__(self):
		self.encriptoManiac = EncriptoManiac()

	def ejecutar(self,parametros):
		return None

	def validarParametros(self,parametros):
		if(parametros == []):
			raise ParametrosComandosNullos()

class ComandoAgregar(ComandoConsola):

	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		if(len(parametros)==1):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			self.encriptoManiac.ingresarClave(parametros[0],parametros[1])
		return None

class ComandoVerMas(ComandoConsola):

	def ejecutar(self,parametros):
		return ConstanteConsola.mensajeComandosAvanzados

class ComandoExit(ComandoConsola):

	def ejecutar(self,parametros):
		raise InterrumpirConsola()

class ComandoModificar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		if(len(parametros)==1):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			self.encriptoManiac.actualizarClave(parametros[0],parametros[1])
		return None

class ComandoEliminar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		self.encriptoManiac.eliminarClave(parametros[0])
		return None

class ComandoMostrar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		self.encriptoManiac.buscarClave(parametros[0])
		return None

class ComandoListar(ComandoConsola):
	pass

class ComandoUnix(ComandoConsola):
	pass

class ComandoWin(ComandoConsola):
	pass