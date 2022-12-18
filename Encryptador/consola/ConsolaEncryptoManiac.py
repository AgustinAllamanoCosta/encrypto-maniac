#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Encryptador.comandos.ComandosManiac import *
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.consola.Historial import HistorialConsola
from Encryptador import EncryptoManiac
from Util.CustomException import ContraseniaNoValidaException, InterrumpirConsola,ComandoNoEncontradoExcepcion,ParametrosComandoIncompletos,ParametrosComandosNullos,CuentaEnBaseDuplicadaException
import logging
import re

class ConsolaEncryptoManiac():

	def __init__(self, historalParam: HistorialConsola, encryptadorParam: EncryptoManiac, estadoDeSesionParam: EstadoDeSesion):
		logging.info('Iniciando consola')
		self.historial: HistorialConsola = historalParam
		self.estadoDeSesion: EstadoDeSesion = estadoDeSesionParam
		self.patronConsola = re.compile('\S+')
		self.correrConsola = True
		self.prompt = "EM>>"

		self.comandosEstandar: dict[str,Comando] = {
			'listar': ComandoListar(encryptadorParam),
			'agregar': ComandoAgregar(encryptadorParam),
			'modificar': ComandoModificar(encryptadorParam),
			'eliminar': ComandoEliminar(encryptadorParam),
			'mostrar': ComandoMostrar(encryptadorParam),
			'cabecera': ComandoEscribirCabeceraDeConsola(encryptadorParam),
			'vermas': ComandoVerMas(),
		}

		self.comandosSinSession: dict[str,Comando] = {
			'login': ComandoLogin(encryptadorParam,self.estadoDeSesion),
			'exit': ComandoExit(encryptadorParam),
			'ayuda': ComandoAyuda(),
		}

	def analizarEntrada(self,entrada):
		valoresEntrada: list[str] = self.patronConsola.findall(entrada)
		try:
			self.historial.agregarEntrada(entrada)
			comando: Comando = self.obtenerComando(valoresEntrada[0].lower())
			comando.ejecutar(valoresEntrada[1:])
			self.comandosEstandar.get('systema').ejecutar([])
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
		except ContraseniaNoValidaException as expt:
			logging.debug('Contrasenia no valida')
			self.escribirError(expt.mensaje)

	def obtenerComando(self,entrada):
		if(entrada in self.comandosEstandar.keys() and self.estadoDeSesion.sesionActiva):
			return self.comandosEstandar.get(entrada)
		elif(entrada in self.comandosSinSession.keys()):
			return self.comandosSinSession.get(entrada)
		else:
			raise ComandoNoEncontradoExcepcion()

	def bucleDeConsola(self):
		self.escribirCabeceraDeConsola()
		while self.correrConsola:
			self.analizarEntrada(self.ingresarEntradas())

	def escribirCabeceraDeConsola(self):
		comando = self.comandosEstandar['cabecera']
		comando.escribirEnConsolaStrategy(self.historial)

	def ingresarEntradas(self):
		return input(self.prompt)

	def escribirError(self,mensaje):
		print(mensaje)
		self.historial.agregarEntrada(mensaje)
 
	def obtenerHistorial(self):
		return self.historial.obtener()

	def obtenerComandos(self):
		return self.comandosEstandar
