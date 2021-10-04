#!/usr/bin/env python
# -*- coding: utf-8 -*-
class ConstanteConsola:

	mensajeBienvenida = 'ENCRYPTO MANIAC'
	mensajeComandosBasicos = '''Para agregar una contraseña escribi agregar.\nPara ver las cuentas escribi listar.\nPara ver la lista completa de comandos escribi vermas'''
	mensajeComandosAvanzados = '''Escribi: 
	modificar -> para cambiar la clave de una cuenta
	eliminar  -> para borrar una cuenta
	mostrar   -> para ver la contraseña de una cuenta
	listar    -> para ver todas las cuentas en la base
	agregar   -> para agregar una nueva cuenta y contraseña en la base
	vermas    -> para ver este mensaje :D
	Pd: para ver como usar un comando escribi -> ayuda nombreComando <- ej: ayuda modificar'''
	
	
	mensajeAyudaComandoAgregar = '''Comando agregar-> agregar parametro1 parametro2 
	parametro1: es el nombre de la cuenta a agregar
	parametro2: es la contraseña de la cuenta
	LOS DOS PARAMETROS SON OBLIGATORIOS'''
	mensajeAyudaComandoListar= '''Comando listar-> se utiliza para listar todo el contenido de la base, no utiliza parametros para hacerlo :D'''
	mensajeAyudaComandoExit='''Comando exit-> se utiliza para salir del sistema, todas las contraseñas quedaran guardades en la base de datos, asi que cundo vuelvas todo estara como si nunca te hubieras ido :D'''
	mensajeAyudaComandoMostrar = '''Comando mostrar-> mostrar parametro1 \n parametro1: el nombre de la cuenta a mostrar la clave, si no existe la cuenta no se mostrara nada :D'''
	mensajeAyudaComandoVerMas = '''Comando vermas-> muestra la lista de comando disponibles :D'''
	mensajeAyudaComandoEliminar = '''Comando eliminar-> eliminar parametro1 \n parametro1: nombre de la cuenta a elimnar de la base, la misma despues no se puede recuperar :D'''
	mensajeAyudaComandoModificar = '''Comando modificar-> modificar parametro1 parametro2 \n parametro1: nombre de la cuenta a modificar \n parametro2 nueva calve a ingresar'''

	mensajeErrorComandoParametros = '''Error al ingresar los parametros del comando porfavor vuelva a intentarlo. Si tiene dudas puede usar el comando ayuda'''
	mensajeErrprComandoDuplicado = 'Cuenta ya existente en la base, eliminela o modifiquela antes de volver a ingres. Nombre de cuenta: '

class ConstantesEM:
	baseEncryptoManiac = "manicaDB.db"
	nombreArchivoKey = 'encriptoKey.key'

class ConsultaDB:
	actualizarClave = 'UPDATE clavesYAplicaciones SET clave = ? WHERE nombreApp = ?'
	listarCuentas = 'SELECT nombreApp FROM clavesYAplicaciones'
	buscarCuenta = 'SELECT nombreApp FROM clavesYAplicaciones WHERE nombreApp == ?'
	buscarClave = 'SELECT clave FROM clavesYAplicaciones WHERE nombreApp == ?'
	ingresarClave = 'INSERT INTO clavesYAplicaciones(nombreApp,clave) VALUES (?,?)'
	eliminarClave = 'DELETE FROM clavesYAplicaciones WHERE nombreApp = ?'
	crearTabla = 'CREATE TABLE clavesYAplicaciones ( codigo integer PRIMARY KEY autoincrement,nombreApp text,clave text)'