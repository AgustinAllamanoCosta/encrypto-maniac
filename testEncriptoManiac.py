#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sqlite3
from encriptoManiac import EncriptoManiac 
from encriptoManiac import ConstantesEncryptoManiac as cem
import os 

class TestEncriptoManiac(unittest.TestCase):

	def test_DadoQueCorroElProgramaDosVecesLaSegundaFallaPorqueLaBaseYaEstaCreada(self):
		self.dadoQueInicioCryptoManiac()
		self.dadoQueInicioCryptoManiac()
		self.serVerificaQueSeIniciaLaBase()

	def test_CunadoSeEjecutaElMetodoGenerarClaveSeGeneraUnArchivoPunotKey(self):
		self.dadoQueInicioCryptoManiac()
		self.caundoGeneraLaClave()
		self.seVerificaQueSeCrearElArchivoPuntoKey()

	def test_CuandoInicioElEncriptadorSeCargaUnaClave(self):
		self.dadoQueInicioCryptoManiac()
		self.seVerificaQueSeCargaUnaClave()
		
	def test_DadoQueIngresoUnaPalabraALaFuncionEncriptarASEMeLaRetornaEncriptada(self):
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeEncryptaLaPalabra("holaMundoCripto123")
		self.seVerificaQueSeEncryptoExitosamente()
			
	# Test de integracion con base de datos mejorar 
	def test_DadoQueSeEjecutaLaFuncionIngresarClaveSeEncriptaYSeInsertaEnLaBaseDeDatos(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeIngresaLaCuenta('slack').conlaClave('1234Allamano')
		self.seVerificaQueSeInsertoCorrectamenteEnLaBase()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveSeEsperaQueRetorneLaClaveDesencryptada(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoBuscoPorSuNombre()
		self.seVerificaQueSeObtieneLaCalveIngresada()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveConUnNombreDeAppQueNoExisteEnLaBaseSeEsperaQueRetorneNone(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoEjecutoElMetodoBuscarConUnNombreQueCuentaQueNoEstaEnLaBase()
		self.seVerificaQueLaRespuestaEsNone()

	def test_DadoQueSeEjecutaLaFuncionListarCuentasYQueExistenCuentasEnLaBBDDSeVerificaQueLaFuncionRetornasLasCuentas(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeEjecutaListarCuentas()
		self.seVerificaQueSeListenLasCuentas()	

	def test_DadoQueSeEjecutaLaFuncionActualizarClaveYQueExisteUnRegistroEnLaBBDDSeVerificaQueLaClaveDeEseRegistroSeActualiza(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeActualizaLaClave('4444')
		self.seVerificaQueSeActualizo()		
	
#Utilidades

	def dadoQueInicioCryptoManiac(self):
		self.encriptoManiac = EncriptoManiac()
	
	def dadoQueExisteUnaCuentaEnLaBase(self):
		self.nombreAPP = 'slack'
		self.claveAIngresar = 'aaaa'
		self.encriptoManiac.ingresarClave(self.nombreAPP,self.claveAIngresar)

	def caundoGeneraLaClave(self):
		self.encriptoManiac.generarClave()

	def cuandoSeEncryptaLaPalabra(self,palabra):
		self.palabraAEncryptar = palabra
		self.palabraEncryptada = self.encriptoManiac.encriptarASE(self.palabraAEncryptar)

	def cuandoSeIngresaLaCuenta(self,nombre):
		self.nombreAPP = nombre
		return self
	
	def cuandoBuscoPorSuNombre(self):
		self.claveIngresada = self.encriptoManiac.buscarClave(self.nombreAPP)

	def cuandoEjecutoElMetodoBuscarConUnNombreQueCuentaQueNoEstaEnLaBase(self):
		self.claveIngresada = self.encriptoManiac.buscarClave('adadsasdadasdasds')

	def cuandoSeEjecutaListarCuentas(self):
		self.cuentaListadas = self.encriptoManiac.listarCuentas()

	def cuandoSeActualizaLaClave(self,clave):
		self.nuevaClave = clave
		self.encriptoManiac.actualizarClave(self.nombreAPP,self.nuevaClave)

	def conlaClave(self,clave):
		self.claveAIngresar = clave
		self.encriptoManiac.ingresarClave(self.nombreAPP,self.claveAIngresar)

	def serVerificaQueSeIniciaLaBase(self):
		self.assertEqual(self.encriptoManiac.baseIniciada, True)

	def seVerificaQueSeCrearElArchivoPuntoKey(self):
		self.assertTrue(os.path.exists(cem.nombreArchivoKey))

	def seVerificaQueSeCargaUnaClave(self):
		self.assertNotEqual(self.encriptoManiac.fernet, None)

	def seVerificaQueSeEncryptoExitosamente(self):
		self.assertNotEqual(self.palabraEncryptada,self.palabraAEncryptar)

	def seVerificaQueSeInsertoCorrectamenteEnLaBase(self):
		baseDeDatos = sqlite3.connect(cem.baseEncriptoManiac)
		cursor = baseDeDatos.execute('SELECT * FROM clavesYAplicaciones WHERE nombreApp == ?',(self.nombreAPP,))
		self.assertNotEqual(len(cursor.fetchall()),0)
		baseDeDatos.close()

	def seVerificaQueSeObtieneLaCalveIngresada(self):
		self.assertEqual(self.claveIngresada,self.claveAIngresar)

	def seVerificaQueLaRespuestaEsNone(self):
		self.assertEqual(self.claveIngresada,None)

	def seVerificaQueSeListenLasCuentas(self):
		respuestaEsperada = ' '+self.nombreAPP+',\n'
		self.assertEqual(self.cuentaListadas,respuestaEsperada)	

	def seVerificaQueSeActualizo(self):
		self.assertEqual(self.encriptoManiac.buscarClave(self.nombreAPP),self.nuevaClave)

	def limpiarBase(self):
		baseDeDatos = sqlite3.connect(cem.baseEncriptoManiac)
		baseDeDatos.execute('DELETE FROM clavesYAplicaciones')
		baseDeDatos.commit()
		baseDeDatos.close()

if __name__ == "__main__":
	unittest.main()