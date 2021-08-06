#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from cryptography.fernet import Fernet as ft
import os

class EncriptoManiac(object):

	def __init__(self):
		self.baseIniciada = False
		self.iniciarClaves()
		self.iniciarBaseDeClaves()

	def iniciarBaseDeClaves(self):
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		try:
			baseDeDatos.execute("""create table clavesYAplicaciones ( codigo integer primary key autoincrement,
								nombreApp text,
								clave text)""")
		except sqlite3.OperationalError:
			pass
		self.baseIniciada = True
		baseDeDatos.close()

	def iniciarClaves(self):
		if(os.path.exists(ConstantesEncryptoManiac.nombreArchivoKey)):
			self.fernet = ft(self.cargarClave())
		else:
			self.generarClave()
			self.fernet = ft(self.cargarClave())

	def generarClave(self):
		with open(ConstantesEncryptoManiac.nombreArchivoKey,'wb') as archivoKey:
			archivoKey.write(ft.generate_key())

	def cargarClave(self):
		archivoKey = open(ConstantesEncryptoManiac.nombreArchivoKey,'rb') 
		key = archivoKey.read()
		archivoKey.close()
		return key

	def encriptarASE(self, palabraAEncriptar):
		return self.fernet.encrypt(palabraAEncriptar.encode())
		
	def ingresarClave(self,nombreApp,clave):
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		baseDeDatos.execute('INSERT INTO clavesYAplicaciones(nombreApp,clave) VALUES (?,?)',(nombreApp,self.encriptarASE(clave)))
		baseDeDatos.commit()
		baseDeDatos.close()

	def buscarClave(self,nombreApp):
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		cursor = baseDeDatos.execute('SELECT clave FROM clavesYAplicaciones WHERE nombreApp == ?',(nombreApp,))
		respuesta = cursor.fetchone()
		baseDeDatos.close()
		if( respuesta != None and len(respuesta)>0):
			return self.fernet.decrypt(respuesta[0]).decode()
		else:
			return None

	def listarCuentas(self):
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		cursor = baseDeDatos.execute('SELECT nombreApp FROM clavesYAplicaciones')
		respuesta = cursor.fetchall()
		baseDeDatos.close()
		if(len(respuesta)>0):
			lista = ''
			for app in respuesta:
				lista += ' '+app[0]+',\n' 
			return lista
		else:
			return None
			
	def actualizarClave(self,nombreApp,calveNueva):
		baseDeDatos = sqlite3.connect(ConstantesEncryptoManiac.baseEncriptoManiac)
		baseDeDatos.execute('UPDATE clavesYAplicaciones SET clave = ? WHERE nombreApp = ?',(self.encriptarASE(calveNueva),nombreApp))
		baseDeDatos.commit()
		baseDeDatos.close()

class ConstantesEncryptoManiac:
	baseEncriptoManiac = "manicaDB.db"
	nombreArchivoKey = 'encriptoKey.key'
