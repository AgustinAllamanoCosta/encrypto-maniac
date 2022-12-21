#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Encryptador.comandos.ComandoMostrar import ComandoMostrar
from Encryptador.comandos.ComandoAyuda import ComandoAyuda
from Encryptador.comandos.ComandoExit import ComandoExit
from Encryptador.comandos.ComandoLogin import ComandoLogin
from Encryptador.comandos.ComandoRegistrar import ComandoRegistrar
from Encryptador.comandos.ComandoVerMas import ComandoVerMas
from Encryptador.comandos.ComandoEscribirCabeceraDeConsola import ComandoEscribirCabeceraDeConsola
from Encryptador.comandos.ComandoEliminar import ComandoEliminar
from Encryptador.comandos.ComandoModificar import ComandoModificar
from Encryptador.comandos.ComandoAgregar import ComandoAgregar
from Encryptador.comandos.ComandoListar import ComandoListar
from Encryptador.comandos.Comando import Comando
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.consola.Historial import HistorialConsola
from Encryptador.EncryptoManiac import EncryptoManiac
from Util.ConstantesEncryptoManiac import ConstanteConsola
from Util.CustomException import InterrumpirConsola,ComandoNoEncontradoExcepcion,ParametrosComandoIncompletos,ParametrosComandosNullos,CuentaEnBaseDuplicadaException, UsuarioNoAutorizadoException
import logging
import re

class ConsolaEncryptoManiac():

	def __init__(self, historalParam: HistorialConsola, encryptadorParam: EncryptoManiac):
		logging.info('Iniciando consola')
		self.historial: HistorialConsola = historalParam
		self.estadoDeSesion: EstadoDeSesion = encryptadorParam.estadoSesion
		self.encriptador: EncryptoManiac = encryptadorParam
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
			'ayuda': ComandoAyuda(),
		}

		self.comandosSinSession: dict[str,Comando] = {
			'login': ComandoLogin(encryptadorParam),
			'registrar' : ComandoRegistrar(encryptadorParam),
			'exit': ComandoExit(encryptadorParam),
		}

	def analizarEntrada(self,entrada):
		valoresEntrada: list[str] = self.patronConsola.findall(entrada)
		try:
			self.historial.agregarEntrada(entrada)
			if(self.estadoDeSesion is None):
				print('Parece que no estas registrado, vamos a hacerlo antes de continuar.')
				self.comandosSinSession['registrar'].ejecutar([])
				self.estadoDeSesion = EstadoDeSesion(self.encriptador.obtenerUsuarioRegistrado())

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
		except UsuarioNoAutorizadoException as expt:
			logging.debug('Usuario no Autorisado para hacer esta accion')
			self.escribirError('Usuario no Autorisado para hacer esta accion, porfavor registrese o ingrese antes de continuar')

	def obtenerComando(self,entrada):
		if(entrada in self.comandosEstandar.keys() and not self.estadoDeSesion.sesionActiva):
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
