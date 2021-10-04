#!/usr/bin/env python
# -*- coding: utf-8 -*-

import EncryptoManiac 
from CustomException import *
import ConstantesEncryptoManiac 
from ComandosManiac import *
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
		'ayuda':ComandoAyuda(),
		'cabecera':ComandoEscribirCabeceraDeConsola()
		}

	def bucleDeConsola(self):
		self.escribirCabeceraDeConsola()
		while self.correrConsola:
			self.analizarEntrada(self.ingresarEntradas())

	def escribirCabeceraDeConsola(self):
		comando = self.comandosEstandar['cabecera']
		comando.escribirEnConsolaStrategy(self.historial)


	def analizarEntrada(self,entrada):
		valoresEntrada = self.patronConsola.findall(entrada)
		try:
			self.historial.agregarEntrada(entrada)
			comando = self.comandosEstandar.get(valoresEntrada[0].lower())
			resultado = None

			if isinstance(comando,ComandoConsolaSinParametros):
				resultado = comando.ejecutar()
			elif isinstance(comando,ComandoConsola):
				resultado = comando.ejecutar(valoresEntrada[1:])
			else:
				raise ComandoNoEncontradoExcepcion()

			self.comandosEstandar.get('systema').ejecutar()
			comando.escribirEnConsolaStrategy(self.historial)

		except InterrumpirConsola:
			logging.debug('Saliendo de la consola')
			self.correrConsola = False
		except ComandoNoEncontradoExcepcion:
			logging.debug('Comando no encontrado '+entrada)
			self.escribirError(ConstanteConsola.mensajeComandosAvanzados)
		except ParametrosComandoIncompletos as expt:
			logging.debug('Paramentros incompletos '+entrada)
			self.escribirError(expt.mensaje)
		except ParametrosComandosNullos:
			logging.debug('Error en los parametros del comando'+entrada)
			self.escribirError(ConstanteConsola.mensajeErrorComandoParametros)
		except IndexError:
			logging.debug('Index error '+entrada)
			self.escribirError(ConstanteConsola.mensajeAyudaComandoAgregar)
		except CuentaEnBaseDuplicadaException as expt:
			logging.debug('Cuenta en base duplicada '+expt.mensaje)
			self.escribirError(expt.mensaje)

	def ingresarEntradas(self):
		return input()

	def escribirError(self,mensaje):
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
