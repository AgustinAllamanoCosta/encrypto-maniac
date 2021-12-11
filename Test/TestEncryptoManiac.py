#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Encryptador import EncryptoManiac as EM
from Util import ConstantesEncryptoManiac as CEM
import os 
import sqlite3
import unittest

class TestEncryptoManiac(unittest.TestCase):

	def __init__(self, methodName: str = ...) -> None:
		super().__init__(methodName=methodName)
		self.encryptoManiac=None

	def tearDown(self):
		if os.path.exists(self.encryptoManiac.rutaBBDD):
			os.remove(self.encryptoManiac.rutaBBDD)
		if os.path.exists(self.encryptoManiac.rutaKey):
			os.remove(self.encryptoManiac.rutaKey)

	def test_CunadoSeEjecutaElMetodoGenerarClaveSeGeneraUnArchivoPunotKey(self):
		self.dadoQueInicioiEncriptoManiac()
		self.caundoGeneraLaClave()
		self.seVerificaQueSeCrearElArchivoPuntoKey()

	def test_CuandoInicioElEncriptadorSeCargaUnaClave(self):
		self.dadoQueInicioiEncriptoManiac()
		self.seVerificaQueSeCargaUnaClave()
		
	def test_DadoQueIngresoUnaPalabraALaFuncionEncriptarASEMeLaRetornaEncriptada(self):
		self.dadoQueInicioiEncriptoManiac()
		self.cuandoSeEncryptaLaPalabra("holaMundoCripto123")
		self.seVerificaQueSeEncryptoExitosamente()
			
# Test de integracion con base de datos mejorar 
	def test_DadoQueSeEjecutaLaFuncionIngresarClaveSeEncriptaYSeInsertaEnLaBaseDeDatos(self):
		self.dadoQueInicioiEncriptoManiac()
		self.cuandoSeIngresaLaCuenta('slack').conlaClave('1234Allamano')
		self.seVerificaQueSeInsertoCorrectamenteEnLaBase()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveSeEsperaQueRetorneLaClaveDesencryptada(self):
		self.dadoQueInicioiEncriptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoBuscoPorSuNombre()
		self.seVerificaQueSeObtieneLaCalveIngresada()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveConUnNombreDeAppQueNoExisteEnLaBaseSeEsperaQueRetorneNone(self):
		self.dadoQueInicioiEncriptoManiac()
		self.cuandoEjecutoElMetodoBuscarConUnNombreQueCuentaQueNoEstaEnLaBase()
		self.seVerificaQueLaRespuestaEsNone()

	def test_DadoQueSeEjecutaLaFuncionListarCuentasYQueExistenCuentasEnLaBBDDSeVerificaQueLaFuncionRetornasLasCuentas(self):
		self.dadoQueInicioiEncriptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeEjecutaListarCuentas()
		self.seVerificaQueSeListenLasCuentas()
	
	def test_DadoQueSeEjecutaLaFuncionActualizarClaveYQueExisteUnRegistroEnLaBBDDSeVerificaQueLaClaveDeEseRegistroSeActualiza(self):
		self.dadoQueInicioiEncriptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeActualizaLaClave('4444')
		self.seVerificaQueSeActualizo()
	
	def test_DadoQueSeEjecutaLaFuncionEliminarYQueExisteUnRegistroEnLaBBDDQueCoincideConElValorAEliminarSeVerificaQueSeEliminaDeLaBase(self):
		self.dadoQueInicioiEncriptoManiac()
		self.cuandoSeIngresaLaCuenta('slack').conlaClave('1234Admin')
		self.cuandoQueSeEjecutaLaFuncionEliminar()
		self.seVerficaQueSeEliminoLaCuentaSlack()

	def test_DadoQueSeEjecutaLaFuncionExisteCuentaEnBaseYQueNoExisteLaCuentaBuscadaEnLaBaseSeVerificaQueLaFuncionRetornaFalse(self):
		self.dadoQueInicioiEncriptoManiac()
		self.dadoQueExisteLaCuenta('slack').conlaClave('1234Admin')
		self.cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase('slack')
		self.seVerficaQueLaFuncionRetornaTrue()

	def test_DadoQueSeEjecutaLaFuncionExisteCuentaEnBaseYQueExisteLaCuentaBuscadaEnLaBaseSeVerificaQueLaFuncionRetornaFalse(self):
		self.dadoQueInicioiEncriptoManiac()
		self.cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase('slack')
		self.seVerficaQueLaFuncionRetornaFalse()

	def test_DadoQueSeTieneConfiguradoElDirectorioDeLaBBDDPorDefectocuandoSeEjecutaLaFuncionConfigurarBBDDBBDDSeVerificaQueCambiaElOrigenDeLaBBDD(self):
		self.dadoQueInicioiEncriptoManiac()
		self.cuandoSeEjecutaLaFuncionConfigurarBBDD('..\\EncryptoManiac\\Test\\RecursosTestDos\\')
		self.seVerificaQueCambiaElOrigenDeLaBBDD()
		self.seVerificarQueSeRecargaLaConfiguracionDeLaBBD()

	def test_DadoQueSeTieneConfiguradoElDirectorioDelArchivoDeClavesPorDefectocuandoSeEjecutaLaFuncionConfigurarBBDDKeySeVerificaQueCambiaElOrigenDelArchivoDeClaves(self):
		self.dadoQueInicioiEncriptoManiac()
		self.cuandoSeEjecutaLaFuncionConfigurarKey('..\\EncryptoManiac\\Test\\RecursosTestDos\\')
		self.seVerificaQueCambiaElOrigenDelArchivoDeClaves()
		self.seVerificarQueSeRecargaLaConfiguracionDeLasKey()

#Utilidades

	def dadoQueInicioiEncriptoManiac(self):
		self.encryptoManiac = EM.EncryptoManiac([CEM.ConstantesEM.rutaARecursosTest,CEM.ConstantesEM.rutaARecursosTest])

	def dadoQueExisteUnaCuentaEnLaBase(self):
		self.nombreAPP = 'slack'
		self.claveAIngresar = 'aaaa'
		self.encryptoManiac.ingresarClave(self.nombreAPP,self.claveAIngresar)

	def dadoQueExisteLaCuenta(self,nombre):
		self.nombreAPP = nombre
		return self

	def caundoGeneraLaClave(self):
		self.encryptoManiac.generarClave()

	def cuandoSeEncryptaLaPalabra(self,palabra):
		self.palabraAEncryptar = palabra
		self.palabraEncryptada = self.encryptoManiac.encriptarASE(self.palabraAEncryptar)

	def cuandoSeIngresaLaCuenta(self,nombre):
		self.nombreAPP = nombre
		return self
	
	def cuandoBuscoPorSuNombre(self):
		self.claveIngresada = self.encryptoManiac.buscarClave(self.nombreAPP)

	def cuandoEjecutoElMetodoBuscarConUnNombreQueCuentaQueNoEstaEnLaBase(self):
		self.claveIngresada = self.encryptoManiac.buscarClave('adadsasdadasdasds')

	def cuandoSeEjecutaListarCuentas(self):
		self.cuentaListadas = self.encryptoManiac.listarCuentas()

	def cuandoSeActualizaLaClave(self,clave):
		self.nuevaClave = clave
		self.encryptoManiac.actualizarClave(self.nombreAPP,self.nuevaClave)

	def conlaClave(self,clave):
		self.claveAIngresar = clave
		self.encryptoManiac.ingresarClave(self.nombreAPP,self.claveAIngresar)

	def cuandoQueSeEjecutaLaFuncionEliminar(self):
		self.encryptoManiac.eliminarClave('slack')

	def cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase(self,nombreCuenta):
		self.existeCuenta = self.encryptoManiac.existeCuentaEnBase(nombreCuenta)

	def cuandoSeEjecutaLaFuncionConfigurarBBDD(self,parametros):
		self.baseIniciada = False
		self.encryptoManiac.iniciarBaseDeClaves = self.mockIniciarBase
		self.encryptoManiac.configurarRutaBBDD(parametros)

	def cuandoSeEjecutaLaFuncionConfigurarKey(self,parametros):
		self.archvioIniciado = False 
		self.encryptoManiac.iniciarClaves = self.mockArchivoKey
		self.encryptoManiac.configurarRutaKey(parametros)

	def serVerificaQueSeIniciaLaBase(self):
		self.assertEqual(self.encryptoManiac.baseIniciada, True)

	def seVerificaQueSeCrearElArchivoPuntoKey(self):
		self.assertTrue(os.path.exists(CEM.ConstantesEM.rutaARecursosTest+CEM.ConstantesEM.nombreArchivoKey))

	def seVerificaQueSeCargaUnaClave(self):
		self.assertNotEqual(self.encryptoManiac.fernet, None)

	def seVerificaQueSeEncryptoExitosamente(self):
		self.assertNotEqual(self.palabraEncryptada,self.palabraAEncryptar)

	def seVerificaQueSeInsertoCorrectamenteEnLaBase(self):
		baseDeDatos = self.encryptoManiac.conectarBBDD()
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
		self.assertEqual(self.encryptoManiac.buscarClave(self.nombreAPP),self.nuevaClave)

	def seVerficaQueSeEliminoLaCuentaSlack(self):
		baseDeDatos = self.encryptoManiac.conectarBBDD()
		cursor = baseDeDatos.execute('SELECT * FROM clavesYAplicaciones WHERE nombreApp == ?',('slack',))
		self.assertEqual(len(cursor.fetchall()),0)
		baseDeDatos.close()	

	def seVerficaQueLaFuncionRetornaTrue(self):
		assert self.existeCuenta == True

	def seVerficaQueLaFuncionRetornaFalse(self):
		assert self.existeCuenta == False

	def seVerificaQueCambiaElOrigenDeLaBBDD(self):
		assert self.encryptoManiac.rutaBBDD != ""

	def seVerificarQueSeRecargaLaConfiguracionDeLaBBD(self):
		assert self.baseIniciada == True
		
	def seVerificarQueSeRecargaLaConfiguracionDeLasKey(self):
		assert self.archvioIniciado == True

	def seVerificaQueCambiaElOrigenDelArchivoDeClaves(self):
		assert self.encryptoManiac.rutaKey != CEM.ConstantesEM.baseEncryptoManiac

	def mockIniciarBase(self):
		self.baseIniciada = True

	def mockArchivoKey(self):
		self.archvioIniciado = True
if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptoManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)