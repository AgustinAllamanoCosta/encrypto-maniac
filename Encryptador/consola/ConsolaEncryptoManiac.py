#!/usr/bin/env python
# -*- coding: utf-8 -*-
from getpass import getpass
from Encryptador.comandos.ComandosManiac import *
from Encryptador.consola.Historial import HistorialConsola
from Encryptador import EncryptoManiac
from Util.CustomException import InterrumpirConsola,ComandoNoEncontradoExcepcion,ParametrosComandoIncompletos,ParametrosComandosNullos,CuentaEnBaseDuplicadaException
import logging
import re

class ConsolaEncryptoManiac():

	def __init__(self, historalParam: HistorialConsola, encryptadorParam: EncryptoManiac):
		logging.info('Iniciando consola')
		self.historial = historalParam
		self.patronConsola = re.compile('\S+')
		self.correrConsola = True
		self.prompt = "EM>>"

		self.comandosEstandar = { 
		'exit':ComandoExit(encryptadorParam),
		'listar':ComandoListar(encryptadorParam),
		'vermas':ComandoVerMas(),
		'agregar':ComandoAgregar(encryptadorParam),
		'modificar':ComandoModificar(encryptadorParam),
		'eliminar':ComandoEliminar(encryptadorParam),
		'mostrar':ComandoMostrar(encryptadorParam),
		'ayuda':ComandoAyuda(),
		'cabecera':ComandoEscribirCabeceraDeConsola(encryptadorParam)
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

			if isinstance(comando,ComandoConsolaSinParametros):
				comando.ejecutar()
			elif isinstance(comando,ComandoConsola):
				comando.ejecutar(valoresEntrada[1:])
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
		return input(self.prompt)

	def escribirError(self,mensaje):
		print(mensaje)
		self.historial.agregarEntrada(mensaje)
 
	def obtenerHistorial(self):
		return self.historial.obtener()

	def obtenerComandos(self):
		return self.comandosEstandar
