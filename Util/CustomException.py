#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Util.ConstantesEncryptoManiac import *

class InterrumpirConsola(Exception):
	pass

class ParametrosComandosNullos(Exception):
	pass

class ComandoNoEncontradoExcepcion(Exception):
	pass

class CuentaEnBaseDuplicadaException(Exception):
	def __init__(self, nombreCuenta):
		self.mensaje =ConstanteConsola.mensajeErrprComandoDuplicado + nombreCuenta
		super().__init__(self.mensaje)

class ParametrosComandoIncompletos(Exception):
	def __init__(self, mensaje):
		self.mensaje = mensaje
		super().__init__(mensaje)
