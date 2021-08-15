#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import threading 
from consolaEncriptoManiac import *
from os import system

class TestConsolaManiac(unittest.TestCase):

	#Test de interfaz de consola
	def test_dadoQueSeIniciaElContextoDeLaConsolaSeVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeBienvenida()

	def test_dadoQueSeIniciaElContextoCuadnoSeIniciaLaConsolaSeVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestrasLaListaDeComandosbasicos()

	def test_dadoQueSeIniciaElContextoCundoSeIngresaElComandoAgregarSeVerificaQueSeEjecutaLaFuncionAgregarCuenta(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregar()
		self.cuandoSeInicia()
		self.seVerificaQueSeLlamaALaFuncionAgregar()

	def test_dadoQueSeIniciaElContextoCuandoSeIngresaElComandoAgregarSinParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarSinParametros()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueSeIniciaElContextoCuandoSeIngresaElComandoAgregarConUnSoloParametroSeVerificaMuestraElMensajeDeAyudaDelComando(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarConUnParametro()
		self.cuandoSeInicia()
		self.seVerificaMuestraElMensajeDeAyudaDelComando()

	def test_dadoQueSeIniciaElContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoListarSeVerificaQueSeLlamaALaFuncionListar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoListar()
		self.cuandoSeInicia()
		self.seVerificaQueSeLlamaALaFuncionListar()

	def test_dadoQueSeIniciaElContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoVerMasSeListanElRestoDeLosComandos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoVerMas()
		self.cuandoSeInicia()
		self.seVerificaQueSeListanElRestoDeLosComandos()

	def test_dadoQueSeIniciaElContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSeVerificaQueSeLlamaALaFuncionComandoModificar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificar()
		self.cuandoSeInicia()
		self.seVerifiacaQueSeLlamaALaFuncionComandoModificar()

	def dadoQueSeTieneUnContexto(self):
		self.contexto = ContextoConsolaManiac()	

	def dadoQueSeSaleDelContextoAlIniciar(self):
		administrador =  AdministradorDeMensajes(['exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutaElComandoAgregar(self):
		self.seEjecutoAgregar = False
		administrador =  AdministradorDeMensajes(['agregar slack 1234','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ConsolaEncryptoManiac.comandoAgregarCuenta = self.observadorFuncionAgregar

	def dadoQueSeEjecutaElComandoAgregarSinParametros(self):
		administrador =  AdministradorDeMensajes(['agregar','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutaElComandoListar(self):
		self.seEjecutoListar = False
		administrador =  AdministradorDeMensajes(['listar','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ConsolaEncryptoManiac.comandoListar = self.observadorFuncionListar	

	def dadoQueSeEjecutaElComandoVerMas(self):
		administrador =  AdministradorDeMensajes(['vermas','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutarElComandoModificar(self):
		self.seEjecutoModificar = False
		administrador =  AdministradorDeMensajes(['modificar','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ConsolaEncryptoManiac.comandoModificar = self.observadorFuncionModificar

	def dadoQueSeEjecutaElComandoAgregarConUnParametro(self):
		administrador =  AdministradorDeMensajes(['agregar slack','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes		

	def observadorFuncionListar(self):
		self.seEjecutoListar = True

	def observadorFuncionModificar(self):
		self.seEjecutoModificar = True

	def observadorFuncionAgregar(self,nombre,contrasenia):
		self.seEjecutoAgregar = True

	def cuandoSeInicia(self):
		self.contexto.bucleDeConsola()

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		assert self.contexto.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		assert self.contexto.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

	def seVerificaQueSeLlamaALaFuncionListar(self):
		assert self.seEjecutoListar == True

	def seVerificaQueSeListanElRestoDeLosComandos(self):
		assert self.contexto.obtenerHistorial()[2] == ConstanteConsola.mensajeComandosAvanzados

	def seVerifiacaQueSeLlamaALaFuncionComandoModificar(self):
		assert self.seEjecutoModificar == True

	def seVerificaQueSeLlamaALaFuncionAgregar(self):
		assert self.seEjecutoAgregar == True

	def seVerificaQueSeMuestraElMensajeDeError(self):
		assert self.contexto.obtenerHistorial()[2] == ConstanteConsola.mensajeErrorComandoParametros

	def seVerificaMuestraElMensajeDeAyudaDelComando(self):
		assert self.contexto.obtenerHistorial()[2] == ConstanteConsola.mensajeAyudaComandoAgregar		

class AdministradorDeMensajes(object):

	def __init__(self,mensajesAEnviar):
		self.cantidadDeMensajesEnviados = 0
		self.mensajes = mensajesAEnviar

	def enviarMensajes(self):
		if(len(self.mensajes)>=self.cantidadDeMensajesEnviados):
			mensaje = self.mensajes[self.cantidadDeMensajesEnviados]
			self.cantidadDeMensajesEnviados+=1
		return mensaje;

if __name__ == "__main__":
	unittest.main()