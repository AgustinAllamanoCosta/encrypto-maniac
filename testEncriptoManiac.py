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
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveSeEsperaQueRetorneLaClaveDesencryptada(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoBuscoPorSuNombre()
		self.seVerificaQueSeObtieneLaCalveIngresada()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveConUnNombreDeAppQueNoExisteEnLaBaseSeEsperaQueRetorneNone(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoEjecutoElMetodoBuscarConUnNombreQueCuentaQueNoEstaEnLaBase()
		self.seVerificaQueLaRespuestaEsNone()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionListarCuentasYQueExistenCuentasEnLaBBDDSeVerificaQueLaFuncionRetornasLasCuentas(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeEjecutaListarCuentas()
		self.seVerificaQueSeListenLasCuentas()
		self.limpiarBase()	

	def test_DadoQueSeEjecutaLaFuncionActualizarClaveYQueExisteUnRegistroEnLaBBDDSeVerificaQueLaClaveDeEseRegistroSeActualiza(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeActualizaLaClave('4444')
		self.seVerificaQueSeActualizo()
		self.limpiarBase()		

	def test_DadoQueSeEjecutaLaFuncionEliminarYQueExisteUnRegistroEnLaBBDDQueCoincideConElValorAEliminarSeVerificaQueSeEliminaDeLaBase(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeIngresaLaCuenta('slack').conlaClave('1234Admin')
		self.cuandoQueSeEjecutaLaFuncionEliminar()
		self.seVerficaQueSeEliminoLaCuentaSlack()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionExisteCuentaEnBaseYQueNoExisteLaCuentaBuscadaEnLaBaseSeVerificaQueLaFuncionRetornaFalse(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteLaCuenta('slack').conlaClave('1234Admin')
		self.cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase('slack')
		self.seVerficaQueLaFuncionRetornaTrue()
		self.limpiarBase()

#Utilidades

	def dadoQueInicioCryptoManiac(self):
		self.encriptoManiac = EncriptoManiac()
	
	def dadoQueExisteUnaCuentaEnLaBase(self):
		self.nombreAPP = 'slack'
		self.claveAIngresar = 'aaaa'
		self.encriptoManiac.ingresarClave(self.nombreAPP,self.claveAIngresar)

	def dadoQueExisteLaCuenta(self,nombre):
		self.nombreAPP = nombre
		return self

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

	def cuandoQueSeEjecutaLaFuncionEliminar(self):
		self.encriptoManiac.eliminarClave('slack')

	def cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase(self,nombreCuenta):
		self.existeCuenta = self.encriptoManiac.existeCuentaEnBase(nombreCuenta)

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

	def seVerficaQueSeEliminoLaCuentaSlack(self):
		baseDeDatos = sqlite3.connect(cem.baseEncriptoManiac)
		cursor = baseDeDatos.execute('SELECT * FROM clavesYAplicaciones WHERE nombreApp == ?',('slack',))
		self.assertEqual(len(cursor.fetchall()),0)
		baseDeDatos.close()	

	def seVerficaQueLaFuncionRetornaTrue(self):
		assert self.existeCuenta == True

	def limpiarBase(self):
		baseDeDatos = sqlite3.connect(cem.baseEncriptoManiac)
		baseDeDatos.execute('DELETE FROM clavesYAplicaciones')
		baseDeDatos.commit()
		baseDeDatos.close()

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestEncriptoManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)