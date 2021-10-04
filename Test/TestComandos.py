#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from Encryptador.ComandosManiac import *
from Encryptador.EncryptoManiac import *

class TestComandosManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ingresarClave': EncryptoManiac.ingresarClave,
			'actualizarClave': EncryptoManiac.actualizarClave,
			'eliminarClave': EncryptoManiac.eliminarClave,
			'buscarClave': EncryptoManiac.buscarClave,
			'listarCuentas': EncryptoManiac.listarCuentas,
			'existeCuentaEnBase': EncryptoManiac.existeCuentaEnBase,
		}

	def tearDown(self):
		EncryptoManiac.ingresarClave = self.funcionesOriginales['ingresarClave']
		EncryptoManiac.actualizarClave = self.funcionesOriginales['actualizarClave']
		EncryptoManiac.eliminarClave = self.funcionesOriginales['eliminarClave']
		EncryptoManiac.buscarClave = self.funcionesOriginales['buscarClave']
		EncryptoManiac.listarCuentas = self.funcionesOriginales['listarCuentas']
		EncryptoManiac.existeCuentaEnBase = self.funcionesOriginales['existeCuentaEnBase']

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
		EncryptoManiac.existeCuentaEnBase = self.observadorExisteCuentaEnBase

	def dadoQueNoExisteLaCuentaEnLaBase(self):
		self.seEjecutoExisteCuentaEnBase = False
		EncryptoManiac.existeCuentaEnBase = self.observadorNoExisteCuentaEnBase

	def dadoQueSeMuestraLaContraseña(self):
		self.comando.ejecutar = self.ejecutarMostrarMock

	def conParametros(self,parametros):
		self.parametroComando = parametros

	def cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar(self):
		self.seEjecutoIngresarClave = False
		EncryptoManiac.ingresarClave = self.observadorIngresarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoActualizarClave(self):
		self.seEjecutoActualizarClave = False
		EncryptoManiac.actualizarClave = self.observadorActualizarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoEliminarClave(self):
		self.seEjecutoEliminarClave = False
		EncryptoManiac.eliminarClave = self.observadorEliminarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoMostrar(self):
		self.seEjecutoBuscarClave = False
		EncryptoManiac.buscarClave = self.observadorBuscarClave
		self.comando.ejecutar(self.parametroComando)	

	def cuandoSeLlamanALaFuncionEjecutarDelComandoListar(self):
		self.seEjecutoListarCuentas = False
		EncryptoManiac.listarCuentas = self.observadorListarCuentas
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