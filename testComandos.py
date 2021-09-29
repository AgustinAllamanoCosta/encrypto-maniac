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
			'existeCuentaEnBase': EncriptoManiac.existeCuentaEnBase
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
		self.dadoQueSeLlamaAlComandoBuscarClave().conParametros(['slack'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoBuscarClave()
		self.seVerificaQueSeLlamaALaFuncionBuscarClave()

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

	def dadoQueSeLlamaAlComandoAgregar(self):
		self.comando = ComandoAgregar()
		return self

	def dadoQueSeLlamaAlComandoActualizarClave(self):
		self.comando = ComandoModificar()
		return self

	def dadoQueSeLlamaAlComandoEliminarClave(self):
		self.comando = ComandoEliminar()
		return self

	def dadoQueSeLlamaAlComandoBuscarClave(self):
		self.comando = ComandoMostrar()
		return self

	def dadoQueSeLlamaAlComandoListar(self):
		self.comando = ComandoListar()

	def dadoQueExisteUnaCuentaEnLaBase(self):
		self.seEjecutoExisteCuentaEnBase = False
		EncriptoManiac.existeCuentaEnBase = self.observadorExisteCuentaEnBase

	def dadoQueNoExisteLaCuentaEnLaBase(self):
		self.seEjecutoExisteCuentaEnBase = False
		EncriptoManiac.existeCuentaEnBase = self.observadorNoExisteCuentaEnBase

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

	def cuandoSeLlamanALaFuncionEjecutarDelComandoBuscarClave(self):
		self.seEjecutoBuscarClave = False
		EncriptoManiac.buscarClave = self.observadorBuscarClave
		self.comando.ejecutar(self.parametroComando)	

	def cuandoSeLlamanALaFuncionEjecutarDelComandoListar(self):
		self.seEjecutoListarCuentas = False
		EncriptoManiac.listarCuentas = self.observadorListarCuentas
		self.comando.ejecutar()

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

	def buscarClaveMock(self,nombre):
		return ['slack','']

	def seVerificaQueSeLlamaALaFuncionIngresarClave(self):
		assert self.seEjecutoIngresarClave == True
		assert self.seEjecutoExisteCuentaEnBase == True

	def seVerificaQueSeLlamaALaFuncionActualizarClave(self):
		assert self.seEjecutoActualizarClave == True

	def seVerificaQueSeLlamaALaFuncionEliminarClave(self):
		assert self.seEjecutoEliminarClave == True

	def seVerificaQueSeLlamaALaFuncionBuscarClave(self):
		assert self.seEjecutoBuscarClave == True

	def seVerificaQueSeLlamaALaFuncionListarCuentas(self):
		assert self.seEjecutoListarCuentas == True

	def seVerificaQueSeLanzaLaExcepcionDeCuentaDuplicada(self):
		assert self.seEjecutoExisteCuentaEnBase == True
		assert self.seEjecutoIngresarClave == False

		
if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestComandosManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)