#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from consolaEncriptoManiac import *

class TestContextoManiac(unittest.TestCase):
	
	def setUp(self):
		self.funcionesOriginales = {
			'ingresarEntradas': ContextoConsolaManiac.ingresarEntradas
		}

	def test_dadoQueTengoUnContextoConUnaConsolaCuandoSeIngresaUnaFraseSeVerificaQueSeGuardaEnElHistorial(self):
		self.dadoQueTengoUnContexto()
		self.dadoQueSeIngresaUnaFrase()
		self.cuandoSeInicia()
		self.seVerificaQueSeGuardoLaFraseEnHistorial()

	def test_dadoQueTengoUnContextoConUnaConsolaQueSeIniciaEnWindowsSeVerificaQueSeConfiguroLosComandosDeSystemasWindows(self):
		self.dadoQueTengoUnContexto()
		self.dadoQueSeIniciaEnWindowsYSeSale()
		self.cuandoSeInicia()
		self.seVerificaQueSeConfiguroLosComandosDeSystemasWindows()

	def dadoQueTengoUnContexto(self):
		self.contexto = ContextoConsolaManiac()	

	def dadoQueSeIngresaUnaFrase(self):
		self.frase = 'exit'
		administrador =  AdministradorDeMensajes([self.frase])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeIniciaEnWindowsYSeSale(self):
		self.contexto.plataformaActual = 'win32'
		administrador =  AdministradorDeMensajes(['exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def cuandoSeInicia(self):
		self.contexto.bucleDeConsola()

	def seVerificaQueSeGuardoLaFraseEnHistorial(self):
		assert self.frase == self.contexto.obtenerHistorial()[2]

	def seVerificaQueSeConfiguroLosComandosDeSystemasWindows(self):
		assert(isinstance(self.contexto.consola,ConsolaEncryptoManiacWin)) 

	def tearDown(self): 
		ContextoConsolaManiac.ingresarEntradas = self.funcionesOriginales['ingresarEntradas']

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
	suite = unittest.TestLoader().loadTestsFromTestCase(TestContextoManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)