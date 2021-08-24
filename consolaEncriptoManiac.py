#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encriptoManiac import EncriptoManiac 
from CustomException import *
from constantesEncriptoManiac import *
from comandosManiac import *
import re

class ConsolaEncryptoManiac():

	def __init__(self):
		self.historial = HistorialConsola()
		self.patronConsola = re.compile('\S+')
		self.correrConsola = True		

	def bucleDeConsola(self):
		self.escribirCabeceraDeConsola()
		while self.correrConsola:
			self.analizarEntrada(self.ingresarEntradas())

	def escribirCabeceraDeConsola(self):
		self.escribirEnConsola(ConstanteConsola.mensajeBienvenida)
		self.escribirEnConsola(ConstanteConsola.mensajeComandosBasicos)

	def analizarEntrada(self,entrada):
		valoresEntrada = self.patronConsola.findall(entrada)
		try:
			comando = self.operacionesConsola(valoresEntrada[0].lower(),valoresEntrada[1:])	
			resultado = comando.ejecutar()

			if(resultado != None):
				self.escribirEnConsola(resultado)

		except ParametrosComandoIncompletos as expt:
			self.escribirEnConsola(expt.mensaje)
		except ParametrosComandosNullos:
			self.escribirEnConsola(ConstanteConsola.mensajeErrorComandoParametros)
		except InterrumpirConsola:
			self.correrConsola = False
		except ComandoNoEncontradoExcepcion:
			self.escribirEnConsola(ConstanteConsola.mensajeComandosAvanzados)
		except IndexError:
			self.escribirEnConsola(ConstanteConsola.mensajeAyudaComandoAgregar)

		self.historial.agregarEntrada(entrada)

	def operacionesConsola(self,operacion,argumentos=[]):
		if operacion == 'exit':
			return ComandoExit()
		elif operacion == 'listar':
			return ComandoListar()
		elif operacion == 'vermas':
			return ComandoVerMas()
		elif operacion == 'agregar':
			return ComandoAgregar(argumentos)		
		elif operacion  == 'modificar':
			return ComandoModificar(argumentos)
		elif operacion == 'eliminar':
			return ComandoEliminar(argumentos)
		elif operacion == 'mostrar':
			return ComandoMostrar(argumentos)
		else:
			raise ComandoNoEncontradoExcepcion()

	def ingresarEntradas(self):
		return input()

	def escribirEnConsola(self,mensaje):
		print(mensaje)
		self.historial.agregarEntrada(mensaje)
 
	def obtenerHistorial(self):
		return self.historial.obtener()

class ConsolaEncryptoManiacWin(ConsolaEncryptoManiac):
	pass

class ConsolaEncryptoManiacLinux(ConsolaEncryptoManiac):
	pass

class HistorialConsola(object):
	
	def __init__(self):
		self.entradas = []

	def agregarEntrada(self,entrada):
		self.entradas.append(entrada)

	def obtener(self):
		return self.entradas