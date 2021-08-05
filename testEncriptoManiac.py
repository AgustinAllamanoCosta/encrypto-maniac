#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sqlite3
import encriptoManiac as em
import os 

class TestEncriptoManiac(unittest.TestCase):

	def test_DadoQueCorroElProgramaDosVecesLaSegundaFallaPorqueLaBaseYaEstaCreada(self):
		encriptoManiac = em.EncriptoManiac()
		
		encriptoManiac.iniciarBaseDeClaves()
		encriptoManiac.iniciarBaseDeClaves()

		self.assertEqual(encriptoManiac.baseIniciada, True)


	def test_CunadoSeEjecutaElMetodoGenerarClaveSeGeneraUnArchivoPunotKey(self):
		encriptoManiac = em.EncriptoManiac()
		encriptoManiac.generarClave()

		self.assertTrue(os.path.exists(encriptoManiac.nombreArchivoKey))


	def test_CuandoInicioElEncriptadorSeCargaUnaClave(self):
		encriptoManiac = em.EncriptoManiac()

		self.assertNotEqual(encriptoManiac.fernet, None)

	def test_DadoQueIngresoUnaPalabraALaFuncionEncriptarASEMeLaRetornaEncriptada(self):
		encriptoManiac = em.EncriptoManiac()
		palabraAEncriptar = "holaMundoCripto123"

		self.assertNotEqual(encriptoManiac.encriptarASE(palabraAEncriptar),palabraAEncriptar)	

	# Test de integracion con base de datos mejorar 
	def test_DadoQueSeEjecutaLaFuncionIngresarClaveSeEncriptaYSeInsertaEnLaBaseDeDatos(self):
		self.limpiarBase()
		encriptoManiac = em.EncriptoManiac()
		nombreAPP = 'slack'
		encriptoManiac.ingresarClave(nombreAPP,'1234Allamano')

		baseDeDatos = sqlite3.connect(encriptoManiac.baseEncriptoManiac)
		cursor = baseDeDatos.execute('SELECT * FROM clavesYAplicaciones WHERE nombreApp == ?',(nombreAPP,))

		self.assertNotEqual(len(cursor.fetchall()),0)
		baseDeDatos.close()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveSeEsperaQueRetorneLaClaveDesencryptada(self):
		self.limpiarBase()
		encriptoManiac = em.EncriptoManiac()
		nombreAPP = 'slack'
		clave = 'aaaa'
		encriptoManiac.ingresarClave(nombreAPP,clave)

		self.assertEqual(encriptoManiac.buscarClave(nombreAPP),clave)

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveConUnNombreDeAppQueNoExisteEnLaBaseSeEsperaQueRetorneNone(self):
		self.limpiarBase()
		encriptoManiac = em.EncriptoManiac()
		nombreAPP = 'Hola'

		self.assertEqual(encriptoManiac.buscarClave(nombreAPP),None)


	def test_DadoQueSeEjecutaLaFuncionListarCuentasYQueExistenCuentasEnLaBBDDSeVerificaQueLaFuncionRetornasLasCuentas(self):
		self.limpiarBase()
		encriptoManiac = em.EncriptoManiac()
		nombreAPP = 'slack'
		respuestaEsperada = ' '+nombreAPP+',\n'
		clave = '1234Allamano'
		encriptoManiac.ingresarClave(nombreAPP,clave)

		self.assertEqual(encriptoManiac.listarCuentas(),respuestaEsperada)

	def test_DadoQueSeEjecutaLaFuncionActualizarClaveYQueExisteUnRegistroEnLaBBDDSeVerificaQueLaClaveDeEseRegistroSeActualiza(self):
		self.limpiarBase()
		encriptoManiac = em.EncriptoManiac()
		nombreAPP = 'slack'
		respuestaEsperada = ' '+nombreAPP+',\n'
		clave = '1234Allamano'
		nuevaClave = '4444'
		encriptoManiac.ingresarClave(nombreAPP,clave)

		encriptoManiac.actualizarClave(nombreAPP,nuevaClave)

		self.assertEqual(encriptoManiac.buscarClave(nombreAPP),nuevaClave)

	def limpiarBase(self):
		encriptoManiac = em.EncriptoManiac()
		baseDeDatos = sqlite3.connect(encriptoManiac.baseEncriptoManiac)
		baseDeDatos.execute('DELETE FROM clavesYAplicaciones')
		baseDeDatos.commit()
		baseDeDatos.close()

if __name__ == "__main__":
	unittest.main()