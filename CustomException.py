#!/usr/bin/env python
# -*- coding: utf-8 -*-
class InterrumpirConsola(Exception):
	pass

class ParametrosComandosNullos(Exception):
	pass

class ComandoNoEncontradoExcepcion(Exception):
	pass

class CuentaEnBaseDuplicadaException(Exception):
	def __init__(self, nombreCuenta):
		mensaje ='Cuenta ya existente en la base, eliminela o modifiquela antes de volver a ingres. Nombre de cuenta: '+ nombreCuenta
		super().__init__(mensaje)

class ParametrosComandoIncompletos(Exception):
	def __init__(self, mensaje):
		self.mensaje = mensaje
		super().__init__(mensaje)
