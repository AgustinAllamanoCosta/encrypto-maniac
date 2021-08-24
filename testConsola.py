#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from consolaEncriptoManiac import *
import threading as t
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

	def tearDown(self):
		ComandoModificar.ejecutar = self.funcionesOriginales['ComandoModificar']
		ComandoAgregar.ejecutar = self.funcionesOriginales['ComandoAgregar']
		ComandoListar.ejecutar = self.funcionesOriginales['ComandoListar']
		ComandoVerMas.ejecutar = self.funcionesOriginales['ComandoVerMas']
		ComandoExit.ejecutar = self.funcionesOriginales['ComandoExit']
		ComandoEliminar.ejecutar = self.funcionesOriginales['ComandoEliminar']
		ComandoMostrar.ejecutar = self.funcionesOriginales['ComandoMostrar']

	def test_dadoQueTengoUnContextoDeLaConsolaSeVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeBienvenida()

	def test_dadoQueTengoUnContextoCuadnoSeIniciaLaConsolaSeVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestrasLaListaDeComandosbasicos()

	def test_dadoQueTengoUnContextoCundoSeIngresaElComandoAgregarSeVerificaQueSeEjecutaLaFuncionAgregarCuenta(self):
		self.dadoQueSeTieneUnContexto()
		self.cuandoSeLlamaALaFuncionOperacionesConsola('agregar', ['slack', '1234'])
		self.seVerificaQueSeLlamaALaFuncionAgregar()

	def test_dadoQueTengoUnContextoCuandoSeIngresaElComandoAgregarSinParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoCuandoSeIngresaElComandoAgregarConUnSoloParametroSeVerificaMuestraElMensajeDeAyudaDelComando(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarConUnParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaMuestraElMensajeDeAyudaDelComando()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoListarSeVerificaQueSeLlamaALaFuncionListar(self):
		self.dadoQueSeTieneUnContexto()
		self.cuandoSeLlamaALaFuncionOperacionesConsola('listar')
		self.seVerificaQueSeLlamaALaFuncionListar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoVerMasSeListanElRestoDeLosComandos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoVerMas()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeListanElRestoDeLosComandos()
	
	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSeVerificaQueSeLlamaALaFuncionComandoModificar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoModificar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSinElParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificarSinElParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoEliminar()

	def test_dadoQueTengoUnContextoCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerficaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrarSinParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def _dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaUnComandoQueNoExisteSeVerificaQueSeMuestraElMensajeDeComandosAvanzados(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueIngresaUnComandoQueNoExiste()
		self.cuandoSeInicia()
		self.seVerificaQueSeListanElRestoDeLosComandos()

	def _dadoQueTengoUnContextoCuandoSeEnviaUnComandoEnMayusculaLoEjecutoIgual(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEnviaUnComandoEnMayuscula()
		self.cuandoSeInicia()
		self.seVerificaQueSeEjecutaIgual()	

	def dadoQueSeTieneUnContexto(self):
		self.consola = ConsolaEncryptoManiac()	

	def dadoQueSeSaleDelContextoAlIniciar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'exit'
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.consola.bucleDeConsola,daemon=True)		

	def dadoQueSeEjecutaElComandoAgregarSinParametros(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar'

	def dadoQueSeEjecutaElComandoAgregarConUnParametro(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar slack'

	def dadoQueSeEjecutaElComandoListar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'listar'

	def dadoQueSeEjecutaElComandoVerMas(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'vermas'

	def dadoQueSeEjecutarElComandoModificar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'modificar slack'
		ComandoModificar.ejecutar = self.observadorFuncionModificar

	def dadoQueSeEjecutarElComandoModificarSinElParametro(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'modificar'

	def dadoQueSeEjecutarElComandoEliminar(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'eliminar slack'
		ComandoEliminar.ejecutar = self.observadorFuncionEliminar
	
	def dadoQueSeEjecutarElComandoEliminarSinParametros(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'eliminar '

	def dadoQueSeEjecutaElComandoMostrar(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'mostrar slack'
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueSeEjecutaElComandoMostrarSinParametro(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'mostrar '

	def dadoQueIngresaUnComandoQueNoExiste(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'asdasdasdsa '
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.consola.bucleDeConsola,daemon=True)

	def dadoQueSeEnviaUnComandoEnMayuscula(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'MOSTRAR '
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.consola.bucleDeConsola,daemon=True)

	def observadorFuncionListar(self):
		self.seEjecutoListar = True

	def observadorFuncionEliminar(self):
		self.seEjecutoEliminar = True

	def observadorFuncionMostrar(self):
		self.seEjecutoMostrar = True

	def observadorFuncionModificar(self):
		self.seEjecutoModificar = True

	def cuandoSeInicia(self):
		self.consolaEnParalelo.start()

	def cuandoSeLlamaALaFuncionAnalizarEntrada(self):
		self.consola.analizarEntrada(self.consola.ingresarEntradas())

	def cuandoSeLlamaALaFuncionOperacionesConsola(self,comando,argumentos=[]):
		self.respuestaACompararConsola = self.consola.operacionesConsola(comando,argumentos)

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

	def seVerificaQueSeLlamaALaFuncionListar(self):
		assert(isinstance(self.respuestaACompararConsola,ComandoListar)) 

	def seVerificaQueSeListanElRestoDeLosComandos(self):
		assert self.consola.obtenerHistorial()[0] == ConstanteConsola.mensajeComandosAvanzados

	def seVerifiacaQueSeLlamaALaFuncionComandoModificar(self):
		assert self.seEjecutoModificar == True

	def seVerificaQueSeLlamaALaFuncionAgregar(self):
		assert(isinstance(self.respuestaACompararConsola,ComandoAgregar)) 

	def seVerificaQueSeMuestraElMensajeDeError(self):
		assert self.consola.obtenerHistorial()[0] == ConstanteConsola.mensajeErrorComandoParametros

	def seVerificaMuestraElMensajeDeAyudaDelComando(self):
		assert self.consola.obtenerHistorial()[0] == ConstanteConsola.mensajeAyudaComandoAgregar		

	def seVerifiacaQueSeLlamaALaFuncionComandoEliminar(self):
		assert self.seEjecutoEliminar == True

	def seVerficaQueSeLlamaALaFuncionMostrar(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeEjecutaIgual(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.seEjecutoMostrar == True

class HiloQueSePuedeDetener(t.Thread):

    def __init__(self,  *args, **kwargs):
        super(HiloQueSePuedeDetener, self).__init__(*args, **kwargs)
        self.frenarHilo = t.Event()

    def stop(self):
        self.frenarHilo.set()

    def stopped(self):
        return self.frenarHilo.is_set()

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestConsolaManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)