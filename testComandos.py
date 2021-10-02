#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from comandosManiac import *
from encriptoManiac import *

class TestComandosManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ingresarClave': EncriptoManiac.ingresarClave,
			'actualizarClave': EncriptoManiac.actualizarClave,
			'eliminarClave': EncriptoManiac.eliminarClave,
			'buscarClave': EncriptoManiac.buscarClave,
			'listarCuentas': EncriptoManiac.listarCuentas,
			'existeCuentaEnBase': EncriptoManiac.existeCuentaEnBase,
		}

	def tearDown(self):
		EncriptoManiac.ingresarClave = self.funcionesOriginales['ingresarClave']
		EncriptoManiac.actualizarClave = self.funcionesOriginales['actualizarClave']
		EncriptoManiac.eliminarClave = self.funcionesOriginales['eliminarClave']
		EncriptoManiac.buscarClave = self.funcionesOriginales['buscarClave']
		EncriptoManiac.listarCuentas = self.funcionesOriginales['listarCuentas']
		EncriptoManiac.existeCuentaEnBase = self.funcionesOriginales['existeCuentaEnBase']

	def test_dadoQueSeLlamaAlComandoModificarConParametrosNombreDeCuentaYContraseñaSeVerifiacaQueSeLlamaALaFuncionActualizarClave(self):
		self.dadoQueSeLlamaAlComandoActualizarClave().conParametros(['slack','456'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoActualizarClave()
		self.seVerificaQueSeLlamaALaFuncionActualizarClave()

	def test_dadoQueSeLlamaAlComandoEliminarConParametrosNombreDeCuentaSeVerifiacaQueSeLlamaALaFuncionEliminarClave(self):
		self.dadoQueSeLlamaAlComandoEliminarClave().conParametros(['slack'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoEliminarClave()
		self.seVerificaQueSeLlamaALaFuncionEliminarClave()

	def test_dadoQueSeLlamaComandoMostrarConParametroNombreDeCuentaSeVerifiacaQueSeLlamanALaFuncionBuscarClave(self):
		self.dadoQueSeLlamaAlComandoMostrar().conParametros(['slack'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoMostrar()
		self.seVerificaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueSeLlamaComandoListarSeVerifiacaQueSeLlamanALaFuncionListarCuentas(self):
		self.dadoQueSeLlamaAlComandoListar()
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoListar()
		self.seVerificaQueSeLlamaALaFuncionListarCuentas()

	def test_dadoQueSeLlamaAlComandoAgregarConParametrosDeNombreDeCuentaYContraseniaSeVerificaQueSeLlamaALaFuncionIngresarClave(self):
		self.dadoQueSeLlamaAlComandoAgregar().conParametros(['slack','123'])
		self.dadoQueNoExisteLaCuentaEnLaBase()
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar()
		self.seVerificaQueSeLlamaALaFuncionIngresarClave()

	def test_dadoQueExisteUnaCuentaLaBaseCuandoSeVaAIngresarUnaCuentaConElMismoNombreSeVerificaQueSeLanzaUnaExcepcion(self):
		self.dadoQueSeLlamaAlComandoAgregar().conParametros(['slack','123'])
		self.dadoQueExisteUnaCuentaEnLaBase()
		with self.assertRaises(CuentaEnBaseDuplicadaException):
			self.cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar()
		self.seVerificaQueSeLanzaLaExcepcionDeCuentaDuplicada()

	def test_dadoQueSeEjecutaElComandoMostrarDadoQueSeMuestraSeVerficaQueSeMuestraUnPopUpConLaMisma(self):
		self.dadoQueSeLlamaAlComandoMostrar().conParametros(['slack'])
		self.dadoQueSeMuestraLaContraseña()
		self.cuandoSeLlamaALaFuncionEscribirDelComando()
		self.seVerficaQueSeMuestraUnPopUpConLaMisma()

	def dadoQueSeLlamaAlComandoAgregar(self):
		self.comando = ComandoAgregar()
		return self

	def dadoQueSeLlamaAlComandoActualizarClave(self):
		self.comando = ComandoModificar()
		return self

	def dadoQueSeLlamaAlComandoEliminarClave(self):
		self.comando = ComandoEliminar()
		return self

	def dadoQueSeLlamaAlComandoListar(self):
		self.comando = ComandoListar()

	def dadoQueSeLlamaAlComandoMostrar(self):
		self.comando = ComandoMostrar()
		return self

	def dadoQueExisteUnaCuentaEnLaBase(self):
		self.seEjecutoExisteCuentaEnBase = False
		EncriptoManiac.existeCuentaEnBase = self.observadorExisteCuentaEnBase

	def dadoQueNoExisteLaCuentaEnLaBase(self):
		self.seEjecutoExisteCuentaEnBase = False
		EncriptoManiac.existeCuentaEnBase = self.observadorNoExisteCuentaEnBase

	def dadoQueSeMuestraLaContraseña(self):
		self.comando.ejecutar = self.ejecutarMostrarMock

	def conParametros(self,parametros):
		self.parametroComando = parametros

	def cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar(self):
		self.seEjecutoIngresarClave = False
		EncriptoManiac.ingresarClave = self.observadorIngresarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoActualizarClave(self):
		self.seEjecutoActualizarClave = False
		EncriptoManiac.actualizarClave = self.observadorActualizarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoEliminarClave(self):
		self.seEjecutoEliminarClave = False
		EncriptoManiac.eliminarClave = self.observadorEliminarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoMostrar(self):
		self.seEjecutoBuscarClave = False
		EncriptoManiac.buscarClave = self.observadorBuscarClave
		self.comando.ejecutar(self.parametroComando)	

	def cuandoSeLlamanALaFuncionEjecutarDelComandoListar(self):
		self.seEjecutoListarCuentas = False
		EncriptoManiac.listarCuentas = self.observadorListarCuentas
		self.comando.ejecutar()

	def cuandoSeLlamaALaFuncionEscribirDelComando(self):
		self.comando.escribirEnConsolaStrategy(None)

	def buscarClaveMock(self,nombre):
		return ['slack','']

	def seVerificaQueSeLlamaALaFuncionIngresarClave(self):
		assert self.seEjecutoIngresarClave == True
		assert self.seEjecutoExisteCuentaEnBase == True

	def seVerificaQueSeLlamaALaFuncionActualizarClave(self):
		assert self.seEjecutoActualizarClave == True

	def seVerificaQueSeLlamaALaFuncionEliminarClave(self):
		assert self.seEjecutoEliminarClave == True

	def seVerificaQueSeLlamaALaFuncionMostrar(self):
		assert self.seEjecutoBuscarClave == True

	def seVerificaQueSeLlamaALaFuncionListarCuentas(self):
		assert self.seEjecutoListarCuentas == True

	def seVerificaQueSeLanzaLaExcepcionDeCuentaDuplicada(self):
		assert self.seEjecutoExisteCuentaEnBase == True
		assert self.seEjecutoIngresarClave == False

	def seVerficaQueSeMuestraUnPopUpConLaMisma(self):
		assert self.comando.mensajeComando == '123455'

	#UTIL

	def observadorActualizarClave(self,param1,param2):
		self.seEjecutoActualizarClave = True

	def observadorIngresarClave(self,param1,param2):
		self.seEjecutoIngresarClave = True

	def observadorEliminarClave(self,parametro):
		self.seEjecutoEliminarClave = True

	def observadorBuscarClave(self,parametro):
		self.seEjecutoBuscarClave = True

	def observadorListarCuentas(self):
		self.seEjecutoListarCuentas = True

	def observadorExisteCuentaEnBase(self, nombreCuenta):
		self.seEjecutoExisteCuentaEnBase = True
		return True

	def observadorNoExisteCuentaEnBase(self,nombreCuenta):
		self.seEjecutoExisteCuentaEnBase = True
		return False
	
	def observadorComandoSystema(self):
		self.seEejecutoElComandoDelSystema = True

	def ejecutarMostrarMock(self):
		self.mensajeComando = '123455'

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestComandosManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)