#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from consolaEncriptoManiac import *
import threading as t

class TestContextoManiac(unittest.TestCase):
	
	def setUp(self):
		self.funcionesOriginales = {
			'ingresarEntradas': ConsolaEncryptoManiac.ingresarEntradas
		}

	def test_dadoQueTengoUnContextoConUnaConsolaCuandoSeIngresaUnaFraseSeVerificaQueSeGuardaEnElHistorial(self):
		self.dadoQueTengoUnContexto()
		self.dadoQueSeIngresaUnaFrase()
		self.cuandoSeInicia()
		self.seVerificaQueSeGuardoLaFraseEnHistorial()

	def test_dadoQueTengoUnContextoConUnaConsolaQueSeIniciaEnWindowsSeVerificaQueSeConfiguroLosComandosDeSystemasWindows(self):
		self.dadoQueTengoUnContexto()
		self.dadoQueSeIniciaEnWindows()
		self.cuandoSeInicia()
		self.seVerificaQueSeConfiguroLosComandosDeSystemasWindows()

	def test_dadoQueTengoUnContextoConUnaConsolaQueSeIniciaEnLinuxSeVerificaQueSeConfiguroLosComandosDeSystemasLinux(self):
		self.dadoQueTengoUnContexto()
		self.dadoQueSeIniciaEnLinux()
		self.cuandoSeInicia()
		self.seVerificaQueSeConfiguroLosComandosDeSystemasLinux()

	def dadoQueTengoUnContexto(self):
		self.contexto = ContextoConsolaManiac()	

	def dadoQueSeIngresaUnaFrase(self):
		administrador =  AdministradorDeMensajes(['exit'])
		ConsolaEncryptoManiac.ingresarEntradas = administrador.enviarMensajes
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeIniciaEnWindows(self):
		self.consolaEnParalelo = HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)

	def dadoQueSeIniciaEnLinux(self):
		self.contexto.plataforma = 'Linux'
		self.consolaEnParalelo = HiloQueSePuedeDetener(target=self.contexto.bucleDeConsola,daemon=True)		

	def cuandoSeInicia(self):
		self.consolaEnParalelo.start()

	def seVerificaQueSeGuardoLaFraseEnHistorial(self):
		self.consolaEnParalelo.join()
		assert 'exit' == self.contexto.consola.obtenerHistorial()[2]

	def seVerificaQueSeConfiguroLosComandosDeSystemasWindows(self):
		assert(isinstance(self.contexto.consola,ConsolaEncryptoManiacWin))

	def seVerificaQueSeConfiguroLosComandosDeSystemasLinux(self):
		assert(isinstance(self.contexto.consola,ConsolaEncryptoManiacLinux)) 

	def tearDown(self):
		self.consolaEnParalelo.stop()
		ConsolaEncryptoManiac.ingresarEntradas = self.funcionesOriginales['ingresarEntradas']

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
	suite = unittest.TestLoader().loadTestsFromTestCase(TestContextoManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)