#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import threading 
from consolaEncriptoManiac import *
from os import system

class TestConsolaManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ComandoModificar': ComandoModificar.ejecutar,
			'ComandoAgregar': ComandoAgregar.ejecutar,
			'ComandoListar': ComandoListar.ejecutar,
			'ComandoVerMas': ComandoVerMas.ejecutar,
			'ComandoExit' : ComandoExit.ejecutar,
			'ComandoEliminar' : ComandoEliminar.ejecutar,
			'ComandoMostrar' : ComandoMostrar.ejecutar
		}

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
	
	def test_dadoQueSeIniciaElContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSinElParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificarSinElParametro()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueSeIniciaElContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSeVerificaQueSeLlamaALaFuncionComandoModificar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificar()
		self.cuandoSeInicia()
		self.seVerifiacaQueSeLlamaALaFuncionComandoModificar()

	def test_dadoQueSeIniciarElContestoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminar()
		self.cuandoSeInicia()
		self.seVerifiacaQueSeLlamaALaFuncionComandoEliminar()

	def test_dadoQueSeIniciarElContestoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminarSinParametros()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueSeIniciarElContestoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrar()
		self.cuandoSeInicia()
		self.seVerficaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueSeIniciarElContestoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrarSinParametro()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueSeIniciarElContestoConCuentasAgregadasEnLaBaseCuandoSeIngresaUnComandoQueNoExisteSeVerificaQueSeMuestraElMensajeDeComandosAvanzados(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueIngresaUnComandoQueNoExiste()
		self.cuandoSeInicia()
		self.seVerificaQueSeListanElRestoDeLosComandos()

	def test_dadoQueSeIniciarElContextoCuandoSeEnviaUnComandoEnMayusculaLoEjecutoIgual(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEnviaUnComandoEnMayuscula()
		self.cuandoSeInicia()
		self.seVerificaQueSeEjecutaIgual()

	def tearDown(self):
		ComandoModificar.ejecutar = self.funcionesOriginales['ComandoModificar']
		ComandoAgregar.ejecutar = self.funcionesOriginales['ComandoAgregar']
		ComandoListar.ejecutar = self.funcionesOriginales['ComandoListar']
		ComandoVerMas.ejecutar = self.funcionesOriginales['ComandoVerMas']
		ComandoExit.ejecutar = self.funcionesOriginales['ComandoExit']
		ComandoEliminar.ejecutar = self.funcionesOriginales['ComandoEliminar']
		ComandoMostrar.ejecutar = self.funcionesOriginales['ComandoMostrar']	

	def dadoQueSeTieneUnContexto(self):
		self.contexto = ContextoConsolaManiac()	

	def dadoQueSeSaleDelContextoAlIniciar(self):
		administrador =  AdministradorDeMensajes(['exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutaElComandoAgregar(self):
		self.seEjecutoAgregar = False
		administrador =  AdministradorDeMensajes(['agregar slack 1234','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoAgregar.ejecutar = self.observadorFuncionAgregar

	def dadoQueSeEjecutaElComandoAgregarSinParametros(self):
		administrador =  AdministradorDeMensajes(['agregar','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutaElComandoListar(self):
		self.seEjecutoListar = False
		administrador =  AdministradorDeMensajes(['listar','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoListar.ejecutar = self.observadorFuncionListar	

	def dadoQueSeEjecutaElComandoVerMas(self):
		administrador =  AdministradorDeMensajes(['vermas','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutarElComandoModificar(self):
		self.seEjecutoModificar = False
		administrador =  AdministradorDeMensajes(['modificar slack','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoModificar.ejecutar = self.observadorFuncionModificar

	def dadoQueSeEjecutaElComandoAgregarConUnParametro(self):
		administrador =  AdministradorDeMensajes(['agregar slack','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutarElComandoModificarSinElParametro(self):		
		administrador =  AdministradorDeMensajes(['modificar','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutarElComandoEliminar(self):		
		administrador =  AdministradorDeMensajes(['eliminar slack','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoEliminar.ejecutar = self.observadorFuncionEliminar
	
	def dadoQueSeEjecutarElComandoEliminarSinParametros(self):		
		administrador =  AdministradorDeMensajes(['eliminar ','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEjecutaElComandoMostrar(self):		
		administrador =  AdministradorDeMensajes(['mostrar slack','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueSeEjecutaElComandoMostrarSinParametro(self):		
		administrador =  AdministradorDeMensajes(['mostrar ','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueIngresaUnComandoQueNoExiste(self):		
		administrador =  AdministradorDeMensajes(['asdasdasdsa ','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeEnviaUnComandoEnMayuscula(self):
		administrador =  AdministradorDeMensajes(['MOSTRAR ','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def observadorFuncionListar(self):
		self.seEjecutoListar = True

	def observadorFuncionModificar(self):
		self.seEjecutoModificar = True

	def observadorFuncionAgregar(self):
		self.seEjecutoAgregar = True

	def observadorFuncionEliminar(self):
		self.seEjecutoEliminar = True

	def observadorFuncionMostrar(self):
		self.seEjecutoMostrar = True

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

	def seVerifiacaQueSeLlamaALaFuncionComandoEliminar(self):
		assert self.seEjecutoEliminar == True

	def seVerficaQueSeLlamaALaFuncionMostrar(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeEjecutaIgual(self):
		assert self.seEjecutoMostrar == True

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
	suite = unittest.TestLoader().loadTestsFromTestCase(TestConsolaManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)