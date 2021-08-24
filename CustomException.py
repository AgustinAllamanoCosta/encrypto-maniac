#!/usr/bin/env python
# -*- coding: utf-8 -*-
class InterrumpirConsola(Exception):
	pass

class ParametrosComandosNullos(Exception):
	pass

class ComandoNoEncontradoExcepcion(Exception):
	pass

class ParametrosComandoIncompletos(Exception):
	def __init__(self, mensaje):
		self.mensaje = mensaje
		super().__init__(mensaje)
