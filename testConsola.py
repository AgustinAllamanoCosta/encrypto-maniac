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
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeBienvenida()

	def test_dadoQueSeIniciaElContextoCuadnoSeIniciaLaConsolaSeVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeSaleDelContextoAlIniciar();
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestrasLaListaDeComandosbasicos()

	def test_dadoQueSeIniciaElContextoCundoSeIngresaElComandoAgregarSeVerificaQueSeMuestrLaPeticionDeNombreDeCuenta(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeIngresaElComandoAgregar()
		self.cuandoSeInicia()
		self.seVerificaQueSuMuestraLaPeticionDeNombreDeCuenta()

	def test_dadoQueSeIniciaElContextoCundoSeIngresaElComandoAgregarCuadoSeAgregaUnNombreDeCuentaSeVerificaQueSeMuestrLaPeticionDeContraseña(self):
		self.dadoQueSeTieneUnContexto()
		self.dadoQueSeIngresaElComandoAgregarConUnNombreDeCuenta()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraLaPeticionDeContraseña()	

	def dadoQueSeTieneUnContexto(self):
		self.contexto = ContextoConsolaManiac()	

	def dadoQueSeSaleDelContextoAlIniciar(self):
		administrador =  AdministradorDeMensajes(['exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeIngresaElComandoAgregar(self):
		administrador =  AdministradorDeMensajes(['agregar','','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def dadoQueSeIngresaElComandoAgregarConUnNombreDeCuenta(self):
		administrador =  AdministradorDeMensajes(['agregar','slack','exit'])
		ContextoConsolaManiac.ingresarEntradas = administrador.enviarMensajes

	def cuandoSeInicia(self):
		self.contexto.bucleDeConsola()

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		assert self.contexto.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		assert self.contexto.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

	def seVerificaQueSuMuestraLaPeticionDeNombreDeCuenta(self):
		assert self.contexto.obtenerHistorial()[2] == ConstanteConsola.mensajePedirNombre

	def seVerificaQueSeMuestraLaPeticionDeContraseña(self):
		assert self.contexto.obtenerHistorial()[3] == ConstanteConsola.mensajePedirContraseña

class AdministradorDeMensajes(object):

	def __init__(self,mensajesAEnviar):
		self.cantidadDeMensajesEnviados = 0
		self.mensajes = mensajesAEnviar

	def enviarMensajes(self):
		if(len(self.mensajes)>=self.cantidadDeMensajesEnviados):
			mensaje = self.mensajes[self.cantidadDeMensajesEnviados]
			self.cantidadDeMensajesEnviados+=1
		print(self.mensajes)
		print("Indice mensaje "+str(self.cantidadDeMensajesEnviados))
		return mensaje;

if __name__ == "__main__":
	unittest.main()