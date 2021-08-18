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
		self.dadoQueSeEjecutaElComandoAgregar()
		self.cuandoSeInicia()
		self.seVerificaQueSeLlamaALaFuncionAgregar()

	def test_dadoQueTengoUnContextoCuandoSeIngresaElComandoAgregarSinParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarSinParametros()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoCuandoSeIngresaElComandoAgregarConUnSoloParametroSeVerificaMuestraElMensajeDeAyudaDelComando(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoAgregarConUnParametro()
		self.cuandoSeInicia()
		self.seVerificaMuestraElMensajeDeAyudaDelComando()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoListarSeVerificaQueSeLlamaALaFuncionListar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoListar()
		self.cuandoSeInicia()
		self.seVerificaQueSeLlamaALaFuncionListar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoVerMasSeListanElRestoDeLosComandos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoVerMas()
		self.cuandoSeInicia()
		self.seVerificaQueSeListanElRestoDeLosComandos()
	
	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSinElParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificarSinElParametro()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSeVerificaQueSeLlamaALaFuncionComandoModificar(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoModificar()
		self.cuandoSeInicia()
		self.seVerifiacaQueSeLlamaALaFuncionComandoModificar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminar()
		self.cuandoSeInicia()
		self.seVerifiacaQueSeLlamaALaFuncionComandoEliminar()

	def test_dadoQueTengoUnContextoCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutarElComandoEliminarSinParametros()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrar()
		self.cuandoSeInicia()
		self.seVerficaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEjecutaElComandoMostrarSinParametro()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnContextoConCuentasAgregadasEnLaBaseCuandoSeIngresaUnComandoQueNoExisteSeVerificaQueSeMuestraElMensajeDeComandosAvanzados(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueIngresaUnComandoQueNoExiste()
		self.cuandoSeInicia()
		self.seVerificaQueSeListanElRestoDeLosComandos()

	def test_dadoQueTengoUnContextoCuandoSeEnviaUnComandoEnMayusculaLoEjecutoIgual(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeEnviaUnComandoEnMayuscula()
		self.cuandoSeInicia()
		self.seVerificaQueSeEjecutaIgual()

	def tearDown(self):
		self.consolaEnParalelo.stop()
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
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutaElComandoAgregar(self):
		self.seEjecutoAgregar = False
		administrador =  AdministradorDeMensajes(['agregar slack 1234'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoAgregar.ejecutar = self.observadorFuncionAgregar
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutaElComandoAgregarSinParametros(self):
		administrador =  AdministradorDeMensajes(['agregar'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutaElComandoListar(self):
		self.seEjecutoListar = False
		administrador =  AdministradorDeMensajes(['listar'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoListar.ejecutar = self.observadorFuncionListar	
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutaElComandoVerMas(self):
		administrador =  AdministradorDeMensajes(['vermas'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutarElComandoModificar(self):
		self.seEjecutoModificar = False
		administrador =  AdministradorDeMensajes(['modificar slack'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoModificar.ejecutar = self.observadorFuncionModificar
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutaElComandoAgregarConUnParametro(self):
		administrador =  AdministradorDeMensajes(['agregar slack'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutarElComandoModificarSinElParametro(self):		
		administrador =  AdministradorDeMensajes(['modificar'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutarElComandoEliminar(self):		
		administrador =  AdministradorDeMensajes(['eliminar slack'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoEliminar.ejecutar = self.observadorFuncionEliminar
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)
	
	def dadoQueSeEjecutarElComandoEliminarSinParametros(self):		
		administrador =  AdministradorDeMensajes(['eliminar '])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutaElComandoMostrar(self):		
		administrador =  AdministradorDeMensajes(['mostrar slack'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEjecutaElComandoMostrarSinParametro(self):		
		administrador =  AdministradorDeMensajes(['mostrar '])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueIngresaUnComandoQueNoExiste(self):		
		administrador =  AdministradorDeMensajes(['asdasdasdsa '])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeEnviaUnComandoEnMayuscula(self):
		administrador =  AdministradorDeMensajes(['MOSTRAR '])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

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
		self.consolaEnParalelo.start()

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.consolaEnParalelo.join()
		assert self.contexto.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.consolaEnParalelo.join()
		assert self.contexto.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

	def seVerificaQueSeLlamaALaFuncionListar(self):
		self.consolaEnParalelo.join()
		assert self.seEjecutoListar == True

	def seVerificaQueSeListanElRestoDeLosComandos(self):
		self.consolaEnParalelo.join()
		assert self.contexto.obtenerHistorial()[2] == ConstanteConsola.mensajeComandosAvanzados

	def seVerifiacaQueSeLlamaALaFuncionComandoModificar(self):
		self.consolaEnParalelo.join()
		assert self.seEjecutoModificar == True

	def seVerificaQueSeLlamaALaFuncionAgregar(self):
		self.consolaEnParalelo.join()
		assert self.seEjecutoAgregar == True

	def seVerificaQueSeMuestraElMensajeDeError(self):
		self.consolaEnParalelo.join()
		assert self.contexto.obtenerHistorial()[2] == ConstanteConsola.mensajeErrorComandoParametros

	def seVerificaMuestraElMensajeDeAyudaDelComando(self):
		self.consolaEnParalelo.join()
		assert self.contexto.obtenerHistorial()[2] == ConstanteConsola.mensajeAyudaComandoAgregar		

	def seVerifiacaQueSeLlamaALaFuncionComandoEliminar(self):
		self.consolaEnParalelo.join()
		assert self.seEjecutoEliminar == True

	def seVerficaQueSeLlamaALaFuncionMostrar(self):
		self.consolaEnParalelo.join()
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeEjecutaIgual(self):
		self.consolaEnParalelo.join()
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