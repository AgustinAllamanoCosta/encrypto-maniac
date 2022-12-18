#!/usr/bin/env python
# -*- coding: utf-8 -*
from Encryptador import EncryptoManiac as EM
from Encryptador.consola.Historial import HistorialConsola
from Util.CustomException import ParametrosComandosNullos

class Comando(object):

	def __init__(self, encryptador: EM.EncryptoManiac):
		self.encriptoManiac = encryptador
		self.mensajeComando = ""

	def ejecutar(self,parametros = []):
		return 0

	def validarParametros(self,parametros):
		if(parametros == []):
			raise ParametrosComandosNullos()

	def escribirEnConsolaStrategy(self,historial: HistorialConsola):
		if(self.mensajeComando != None):
			print(self.mensajeComando)
			historial.agregarEntrada(self.mensajeComando)
