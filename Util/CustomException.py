#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Util.ConstantesEncryptoManiac import ConstanteConsola


class InterrumpirConsola(Exception):
	pass

class ParametrosComandosNullos(Exception):
	pass

class ComandoNoEncontradoExcepcion(Exception):
	pass

class UsuarioNoAutorizadoException(Exception):
	pass

class NoExisteUsuarioEnLaBaseException(Exception):
	def __init__(self):
		self.mensaje = ConstanteConsola.mensajeUsuarioInexsistente
		super().__init__(self.mensaje)

class CuentaEnBaseDuplicadaException(Exception):
	def __init__(self, nombreCuenta):
		self.mensaje = ConstanteConsola.mensajeErrprComandoDuplicado + nombreCuenta
		super().__init__(self.mensaje)

class ParametrosComandoIncompletos(Exception):
	def __init__(self, mensaje):
		self.mensaje = mensaje
		super().__init__(mensaje)
