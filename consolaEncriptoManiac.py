#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encriptoManiac import EncriptoManiac 
import CustomException as cust

class ContextoConsolaManiac(object):

	def __init__(self):
		self.consola = ConsolaEncryptoManiac()
		self.historial = HistorialConsola()

	def bucleDeConsola(self):
		self.escribirEnConsola(ConstanteConsola.mensajeBienvenida)
		self.escribirEnConsola(ConstanteConsola.mensajeComandosBasicos)
		while self.consola.correrLoop:
			self.analizarEntrada(self.ingresarEntradas())

	def ingresarEntradas(self):
		return input()

	def analizarEntrada(self,entrada):
		self.consola.operacionesConsola(entrada)
		self.historial.agregarEntrada(entrada)

	def escribirEnConsola(self,mensaje):
		print(mensaje)
		self.historial.agregarEntrada(mensaje)

	def obtenerHistorial(self):
		return self.historial.obtener()

class HistorialConsola(object):
	
	def __init__(self):
		self.entradas = []

	def agregarEntrada(self,entrada):
		self.entradas.append(entrada)

	def obtener(self):
		return self.entradas

class ConsolaEncryptoManiac():

	def __init__(self):
		self.correrLoop = True

	def operacionesConsola(self,numeroOperacion):
		if numeroOperacion == 'exit':
			self.correrLoop = False

class ConstanteConsola:
	mensajeBienvenida = 'ENCRYPTO MANIAC'
	mensajeComandosBasicos = 'Para agregar una contraseña escribi agregarCon para ver las contraseñas escribi listar'