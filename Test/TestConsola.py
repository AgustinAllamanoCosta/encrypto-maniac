#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from ConsolaEncryptoManiac import *
from ComandosManiac import *
from EncryptoManiac import *
import threading as t
import sys

class TestConsolaManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ComandoModificar': ComandoModificar.ejecutar,
			'ComandoAgregar': ComandoAgregar.ejecutar,
			'ComandoListar': ComandoListar.ejecutar,
			'ComandoVerMas': ComandoVerMas.ejecutar,
			'ComandoExit' : ComandoExit.ejecutar,
			'ComandoEliminar' : ComandoEliminar.ejecutar,
			'ComandoMostrar' : ComandoMostrar.ejecutar,
			'ComandoAyuda' : ComandoAyuda.ejecutar,
			'existeCuentaEnBase' :EncryptoManiac.existeCuentaEnBase
		}

	def tearDown(self):
		ComandoModificar.ejecutar = self.funcionesOriginales['ComandoModificar']
		ComandoAgregar.ejecutar = self.funcionesOriginales['ComandoAgregar']
		ComandoListar.ejecutar = self.funcionesOriginales['ComandoListar']
		ComandoVerMas.ejecutar = self.funcionesOriginales['ComandoVerMas']
		ComandoExit.ejecutar = self.funcionesOriginales['ComandoExit']
		ComandoEliminar.ejecutar = self.funcionesOriginales['ComandoEliminar']
		ComandoMostrar.ejecutar = self.funcionesOriginales['ComandoMostrar']
		ComandoAyuda.ejecutar = self.funcionesOriginales['ComandoAyuda']
		EncryptoManiac.existeCuentaEnBase = self.funcionesOriginales['existeCuentaEnBase']

	def test_dadoQueTengoUnaConsolaDeLaConsolaSeVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeBienvenida()

	def test_dadoQueTengoUnaConsolaCuadnoSeIniciaLaConsolaSeVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestrasLaListaDeComandosbasicos()

	def test_dadoQueTengoUnaConsolaCundoSeIngresaElComandoAgregarSeVerificaQueSeEjecutaLaFuncionAgregarCuenta(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoAgregar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada() 
		self.seVerificaQueSeLlamaALaFuncionAgregar()

	def test_dadoQueTengoUnaConsolaCuandoSeIngresaElComandoAgregarSinParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoAgregarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnaConsolaCuandoSeIngresaElComandoAgregarConUnSoloParametroSeVerificaMuestraElMensajeDeAyudaDelComando(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoAgregarConUnParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaMuestraElMensajeDeAyudaDelComando()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoListarSeVerificaQueSeLlamaALaFuncionListar(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoListar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeLlamaALaFuncionListar()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoVerMasSeListanElRestoDeLosComandos(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoVerMas()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeListanElRestoDeLosComandos()
	
	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSeVerificaQueSeLlamaALaFuncionComandoModificar(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoModificar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoModificar()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSinElParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoModificarSinElParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoEliminar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoEliminar()

	def test_dadoQueTengoUnaConsolaCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoEliminarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoMostrar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerficaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoMostrarSinParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaUnComandoQueNoExisteSeVerificaQueSeMuestraElMensajeDeComandosAvanzados(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueIngresaUnComandoQueNoExiste()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeListanElRestoDeLosComandos()

	def test_dadoQueTengoUnaConsolaCuandoSeEnviaUnComandoEnMayusculaLoEjecutoIgual(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEnviaUnComandoEnMayuscula()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeEjecutaIgual()	

	def test_dadoQueEstoyTrabajandoEnSistemaUnixCuandoSeInstanciaUnaConsolaDesdeElFactorySeVerificaQueSeCarganLosComandosDeUnixDeSystema(self):
		self.dadoQueEstoyTrabajandoiEnSistemasUnix()
		self.dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas()
		self.seVerificaQueSeCarganLosComandosDeSystemaUnix()

	def test_dadoQueEstoyTrabajandoEnSistemaWinCuandoSeInstanciaUnaConsolaDesdeElFactorySeVerificaQueSeCarganLosComandosDeWin32DeSystema(self):
		self.dadoQueEstoyTrabajandoiEnSistemasWin()
		self.dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas()
		self.seVerificaQueSeCarganLosComandosDeSystemaWin()

	def test_dadoQueTengoUnaConsolaCuandoSeIngresaElComandoAgregarYLaCuentaExisteEnLaBaseSeVerificaQueSeVerificaLanzaUnErrorYSeMuestraElMensajeEnLaConsola(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoAgregarConUnaCuentaQueExisteEnLaBase()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada() 

	def dadoQueTengoUnaConsola(self):
		self.consola = FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)	

	def dadoQueSeSaleDelContextoAlIniciar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'exit'
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.consola.bucleDeConsola,daemon=True)		

	def dadoQueSeEjecutaElComandoAgregarSinParametros(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar'

	def dadoQueSeEjecutaElComandoAgregarConUnParametro(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar slack'

	def dadoQueSeEjecutaElComandoAgregar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar slack 1234'
		ComandoAgregar.ejecutar = self.observadorFuncionAgregar

	def dadoQueSeEjecutaElComandoAgregarConUnaCuentaQueExisteEnLaBase(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'agregar slack 1234'
		EncryptoManiac.existeCuentaEnBase = self.existeCuentaEnBaseMock

	def dadoQueSeEjecutaElComandoListar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'listar'
		ComandoListar.ejecutar = self.observadorFuncionListar

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
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'eliminar'

	def dadoQueSeEjecutaElComandoMostrar(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'mostrar slack'
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueSeEjecutaElComandoMostrarSinParametro(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'mostrar'

	def dadoQueIngresaUnComandoQueNoExiste(self):		
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'asdasdasdsa'

	def dadoQueSeEnviaUnComandoEnMayuscula(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'MOSTRAR'
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueEstoyTrabajandoiEnSistemasUnix(self):
		self.plataform = 'Linux'

	def dadoQueEstoyTrabajandoiEnSistemasWin(self):
		self.plataform = 'Win32'

	def dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas(self):
		self.consola = FactoryConsolaEncriptoManiac().obtenerConsola(self.plataform)

	def cuandoSeInicia(self):
		self.consolaEnParalelo.start()

	def cuandoSeLlamaALaFuncionAnalizarEntrada(self):
		self.consola.analizarEntrada(self.consola.ingresarEntradas())

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

	def seVerificaQueSeLlamaALaFuncionListar(self):
		assert self.seEjecutoListar == True 

	def seVerificaQueSeListanElRestoDeLosComandos(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosAvanzados

	def seVerifiacaQueSeLlamaALaFuncionComandoModificar(self):
		assert self.seEjecutoModificar == True

	def seVerificaQueSeLlamaALaFuncionAgregar(self):
		assert self.seEjecutoAgregar == True

	def seVerificaQueSeMuestraElMensajeDeError(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeErrorComandoParametros

	def seVerificaMuestraElMensajeDeAyudaDelComando(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeAyudaComandoAgregar		

	def seVerifiacaQueSeLlamaALaFuncionComandoEliminar(self):
		assert self.seEjecutoEliminar == True

	def seVerficaQueSeLlamaALaFuncionMostrar(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeEjecutaIgual(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeCarganLosComandosDeSystemaUnix(self):
		assert isinstance(self.consola.obtenerComandos()['systema'],ComandoUnix)

	def seVerificaQueSeCarganLosComandosDeSystemaWin(self):
		assert isinstance(self.consola.obtenerComandos()['systema'],ComandoWin)

	def seVerificaLanzaUnErrorYSeMuestraElMensajeEnLaConsola(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeErrprComandoDuplicado + 'slack'
#Utilidades 
	def observadorFuncionListar(self):
		self.seEjecutoListar = True

	def observadorFuncionEliminar(self,arg):
		self.seEjecutoEliminar = True

	def observadorFuncionMostrar(self,arg):
		self.seEjecutoMostrar = True

	def observadorFuncionModificar(self,arg):
		self.seEjecutoModificar = True

	def observadorFuncionAgregar(self,arg):
		self.seEjecutoAgregar = True

	def existeCuentaEnBaseMock(self,arg):
		return True

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