#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encriptoManiac import EncriptoManiac 
import CustomException as ce
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
		try:
			if(len(valoresEntrada)==1):
				self.consola.operacionesConsola(valoresEntrada[0])		
			else:
				self.consola.operacionesConsola(valoresEntrada[0],valoresEntrada[1:])
		except ce.ParametrosComandosNullos:
			self.escribirEnConsola(ConstanteConsola.mensajeErrorComandoParametros)
		except IndexError:
			self.escribirEnConsola(ConstanteConsola.mensajeAyudaComandoAgregar)

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
			if(argumentos == []):
				raise ce.ParametrosComandosNullos()
			else:
				self.comandoAgregarCuenta(argumentos[0],argumentos[1])
		elif comando == 'listar':
			self.comandoListar()
		elif comando == 'vermas':
			self.contexto.escribirEnConsola(ConstanteConsola.mensajeComandosAvanzados)
		elif comando  == 'modificar':
			if(argumentos == []):
				raise ce.ParametrosComandosNullos()
			else:
				self.comandoModificar(argumentos[0])

	def comandoAgregarCuenta(self,nombre,contrasenia):
		pass

	def comandoModificar(self,nombreCuenta):
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
	vermas    -> para ver este mensaje :D
	Pd: para ver como usar un comando escribi -> ayuda nombreComando <- ej: ayuda modificar'''
	mensajeErrorComandoParametros = '''Error al ingresar los parametros del comando porfavor vuelva a intentarlo. Si tiene dudas puede usar el comando ayuda'''
	mensajeAyudaComandoAgregar = '''Comando agregar-> agregar parametro1 parametro2 
	parametro1: es el nombre de la cuenta a agregar
	parametro2: es la contraseña de la cuenta
	LOS DOS PARAMETROS SON OBLIGATORIOS'''