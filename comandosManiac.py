#!/usr/bin/env python
# -*- coding: utf-8 -*
from CustomException import *
from constantesEncriptoManiac import *
class ComandoConParametro(object):

	def __init__(self,parametros):
		self.parametroComadno = parametros

	def ejecutar(self):
		if(self.parametroComadno == []):
			raise ParametrosComandosNullos()

class ComandoAgregar(ComandoConParametro):
	
	def ejecutar(self):
		super().ejecutar()
		if(len(self.parametroComadno)==1):
			raise ParametrosComandoIncompletos(ConstanteConsola.mensajeAyudaComandoAgregar)
		return None

class ComandoModificar(ComandoConParametro):
	pass

class ComandoEliminar(ComandoConParametro):
	pass

class ComandoMostrar(ComandoConParametro):
	pass

class ComandoConsola(object):

	def ejecutar(self):
		return None

class ComandoVerMas(ComandoConsola):

	def ejecutar(self):
		return ConstanteConsola.mensajeComandosAvanzados

class ComandoExit(ComandoConsola):

	def ejecutar(self):
		raise InterrumpirConsola()

class ComandoListar(ComandoConsola):
	pass