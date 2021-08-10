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
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeBienvenida()

	def test_dadoQueSeIniciaElContextoCuadnoSeIniciaLaConsolaSeVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.dadoQueSeTieneUnContexto()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestrasLaListaDeComandosbasicos()

	def dadoQueSeTieneUnContexto(self):
		ContextoConsolaManiac.ingresarEntradas = lambda x: 'exit'
		self.contexto = ContextoConsolaManiac()	

	def cuandoSeInicia(self):
		self.contexto.bucleDeConsola()

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		assert self.contexto.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		assert self.contexto.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

if __name__ == "__main__":
	unittest.main()