#!/usr/bin/env python
# -*- coding: utf-8 -*-
from encriptoManiac import EncriptoManiac 
from CustomException import *
from constantesEncriptoManiac import *
from comandosManiac import *
import re
import logging

class ConsolaEncryptoManiac():

	def __init__(self):
		logging.info('Iniciando consola')
		self.historial = HistorialConsola()
		self.patronConsola = re.compile('\S+')
		self.correrConsola = True

		self.comandosEstandar = {
		'exit':ComandoExit(),
		'listar':ComandoListar(),
		'vermas':ComandoVerMas(),
		'agregar':ComandoAgregar(),
		'modificar':ComandoModificar(),
		'eliminar':ComandoEliminar(),
		'mostrar':ComandoMostrar(),
		'ayuda':ComandoAyuda()
		}

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
			self.historial.agregarEntrada(entrada)
			comando = self.comandosEstandar.get(valoresEntrada[0].lower())
			resultado = None

			if isinstance(comando,ComandoConsolaSinParametros):
				resultado = comando.ejecutar()
				self.comandosEstandar.get('systema').ejecutar()
			elif isinstance(comando,ComandoConsola):
				resultado = comando.ejecutar(valoresEntrada[1:])
				self.comandosEstandar.get('systema').ejecutar()
			else:
				raise ComandoNoEncontradoExcepcion()

			self.escribirEnConsola(resultado)

		except InterrumpirConsola:
			logging.debug('Saliendo de la consola')
			self.correrConsola = False
		except ComandoNoEncontradoExcepcion:
			logging.debug('Comando no encontrado '+entrada)
			self.escribirEnConsola(ConstanteConsola.mensajeComandosAvanzados)
		except ParametrosComandoIncompletos as expt:
			logging.debug('Paramentros incompletos '+entrada)
			self.escribirEnConsola(expt.mensaje)
		except ParametrosComandosNullos:
			logging.debug('Error en los parametros del comando'+entrada)
			self.escribirEnConsola(ConstanteConsola.mensajeErrorComandoParametros)
		except IndexError:
			logging.debug('Index error '+entrada)
			self.escribirEnConsola(ConstanteConsola.mensajeAyudaComandoAgregar)
		except CuentaEnBaseDuplicadaException as expt:
			logging.debug('Cuenta en base duplicada '+expt.mensaje)
			self.escribirEnConsola(expt.mensaje)

	def ingresarEntradas(self):
		return input()

	def escribirEnConsola(self,mensaje):
		if(mensaje != None):
			print(mensaje)
			self.historial.agregarEntrada(mensaje)
 
	def obtenerHistorial(self):
		return self.historial.obtener()

	def obtenerComandos(self):
		return self.comandosEstandar

class ConsolaEncryptoManiacWin(ConsolaEncryptoManiac):

	def __init__(self):
		super().__init__()
		self.comandosEstandar['systema'] = ComandoWin()

class ConsolaEncryptoManiacLinux(ConsolaEncryptoManiac):

	def __init__(self):
		super().__init__()
		self.comandosEstandar['systema'] = ComandoUnix()

class FactoryConsolaEncriptoManiac(object):

	def __init__(self):
		self.tipoDeConsolas = {
		'linux':ConsolaEncryptoManiacLinux(),
		'win32':ConsolaEncryptoManiacWin()
		}

	def obtenerConsola(self,plataforma):
		logging.info('Plataforma '+plataforma)
		return self.tipoDeConsolas[plataforma.lower()]

class HistorialConsola(object):
	
	def __init__(self):
		logging.info('Iniciando historial')
		self.entradas = []

	def agregarEntrada(self,entrada):
		self.entradas.append(entrada)

	def obtener(self):
		return self.entradas
