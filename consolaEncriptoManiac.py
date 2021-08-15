#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encriptoManiac import EncriptoManiac 
import CustomException as cust
import re

class ContextoConsolaManiac(object):

	def __init__(self):
		self.consola = ConsolaEncryptoManiac(self)
		self.historial = HistorialConsola()
		self.patronConsola = re.compile('\S+')

	def bucleDeConsola(self):
		self.escribirEnConsola(ConstanteConsola.mensajeBienvenida)
		self.escribirEnConsola(ConstanteConsola.mensajeComandosBasicos)
		while self.consola.correrLoop:
			self.analizarEntrada(self.ingresarEntradas())

	def ingresarEntradas(self):
		return input()

	def analizarEntrada(self,entrada):
		valoresEntrada = self.patronConsola.findall(entrada)
		if(len(valoresEntrada)==1):
			self.consola.operacionesConsola(valoresEntrada[0])		
		else:
			self.consola.operacionesConsola(valoresEntrada[0],valoresEntrada[1:])
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

	def __init__(self,contexto):
		self.correrLoop = True
		self.contexto = contexto

	def operacionesConsola(self,comando,argumentos=[]):
		if comando == 'exit':
			self.correrLoop = False
		elif comando == 'agregar':
			self.comandoAgregarCuenta()
		elif comando == 'listar':
			self.comandoListar()
		elif comando == 'vermas':
			self.contexto.escribirEnConsola(ConstanteConsola.mensajeComandosAvanzados)
		elif comando  == 'modificar':
			self.comandoModificar()

	def comandoAgregarCuenta(self):
		pass

	def comandoModificar(self):
		pass

	def comandoListar(self):
		pass

class ConstanteConsola:
	mensajeBienvenida = 'ENCRYPTO MANIAC'
	mensajeComandosBasicos = 'Para agregar una contraseña escribi agregar para ver las cuentas escribi listar'
	mensajeComandosAvanzados = '''Escribi: 
	modificar -> para cambiar la clave de una cuenta
	eliminar  -> para borrar una cuenta
	mostrar   -> para ver la contraseña de una cuenta
	listar    -> para ver todas las cuentas en la base
	agregar   -> para agregar una nueva cuenta y contraseña en la base
	vermas    -> para ver este mensaje :D'''