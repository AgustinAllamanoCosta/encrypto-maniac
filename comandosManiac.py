#!/usr/bin/env python
# -*- coding: utf-8 -*
from CustomException import *
from constantesEncriptoManiac import *

class ComandoConsola(object):

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
		return None

class ComandoEliminar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		if(len(parametros)==1):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		return None

class ComandoMostrar(ComandoConsola):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		if(len(parametros)==1):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		return None

class ComandoListar(ComandoConsola):
	pass