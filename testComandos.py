#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from comandosManiac import *
from encriptoManiac import *

class TestComandosManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ingresarClave': EncriptoManiac.ingresarClave
		}

	def tearDown(self):
		EncriptoManiac.ingresarClave = self.funcionesOriginales['ingresarClave']

	def test_dadoQueSeLlamaAlComandoAgregarConParametrosDeNombreDeCuentaYContraseniaSeVerificaQueSeLlamaALaFuncionIngresarClave(self):
		self.dadoQueSeLlamaAlComandoAgregar().conParametros(['slack','123'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComando()
		self.seVerificaQueSeLlamaALaFuncionIngresarClave()

	def dadoQueSeLlamaAlComandoAgregar(self):
		self.comando = ComandoAgregar()
		return self

	def conParametros(self,parametros):
		self.parametroComando = parametros

	def cuandoSeLlamanALaFuncionEjecutarDelComando(self):
		self.seEjecutoIngresarClave = False
		EncriptoManiac.ingresarClave = self.observadorIngresarClave
		self.comando.ejecutar(self.parametroComando)

	def observadorIngresarClave(self,param1,param2):
		self.seEjecutoIngresarClave = True

	def seVerificaQueSeLlamaALaFuncionIngresarClave(self):
		assert self.seEjecutoIngresarClave == True

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestComandosManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)