import logging
import sqlite3
from Encryptador.configuracion.Configuracion import Configuracion
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.exceptions.LoginErrorException import LoginErrorException
from Encryptador.repository.BaseRepository import BaseRepository
from Encryptador.repository.KeyRepository import KeyRepository
from Encryptador.exceptions.UsuarioNoAutorizadoException import UsuarioNoAutorizadoException
from Util import ConstantesEncryptoManiac as CEM

class EncryptoManiac(object):

	def __init__(self,baseRepositoryParam: BaseRepository, keyReposioryParam: KeyRepository):
		self.baseRepository: BaseRepository = baseRepositoryParam
		self.keyRepository: KeyRepository = keyReposioryParam
		self.estadoSesion: EstadoDeSesion = None

	def iniciarBaseDeClaves(self):
		logging.info('Iniciando base de claves.....')
		try:
			self.baseRepository.ejecutarConsulta(CEM.ConsultaDB.crearTablaClaves)
		except sqlite3.OperationalError:
			logging.info('Tabla de calves ya existente, no se creo')
		try:
			self.baseRepository.ejecutarConsulta(CEM.ConsultaDB.crearTablaUsuario)
		except sqlite3.OperationalError:
			logging.info('Tabla de usuarios ya existente, no se creo')
		logging.info('Base de datos iniciada con exito.')

	def iniciarClaves(self):
		logging.info('Iniciando archivos de clave......')
		self.keyRepository.generarOCargarArchivoDeCalvesExistente()
		logging.info('Archivos de calve iniciado')
		
	def ingresarClave(self,nombreApp,clave):
		self.validarUsuario()
		logging.info(f'Ingresando clave para {nombreApp}')
		nuevaClave = self.keyRepository.encriptarASE(clave)
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.ingresarClave,(nombreApp,nuevaClave))

	def buscarClave(self,nombreApp):
		self.validarUsuario()
		logging.info('Buscando clave para '+nombreApp)
		respuesta = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarClave,(nombreApp,))
		if( respuesta != None and len(respuesta)>0):
			return self.keyRepository.desencriptarASE(respuesta[0])
		else:
			return None

	def listarCuentas(self):
		self.validarUsuario()
		respuesta = self.baseRepository.obtenerTodos(CEM.ConsultaDB.listarCuentas)
		if(len(respuesta)>0):
			lista = ''
			for app in respuesta:
				lista += ' '+app[0]+',\n' 
			return lista
		else:
			return None

	def existeCuentaEnBase(self,nombreCuenta):
		self.validarUsuario()
		logging.info('Existe la cuenta'+nombreCuenta)
		respuesta = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.buscarCuenta,(nombreCuenta,))
		if(len(respuesta)>0):
			return True
		else:
			return False

	def configurarRutaBBDD(self,rutaBBDD):
		self.validarUsuario()
		self.rutaBBDD = rutaBBDD + CEM.ConstantesEM.baseEncryptoManiac
		self.iniciarBaseDeClaves()

	def configurarRutaKey(self,rutaKey):
		self.validarUsuario()
		self.rutaKey = rutaKey + CEM.ConstantesEM.nombreArchivoKey
		self.keyRepository.generarOCargarArchivoDeCalvesExistente(self.rutaKey)

	def eliminarClave(self,parametro):
		self.validarUsuario()
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.eliminarClave,(parametro,))

	def actualizarClave(self,nombreApp,calveNueva):
		self.validarUsuario()
		logging.info(f'Se va a actualizar la clave de la cuenta {nombreApp}')
		nuevaClave = self.keyRepository.encriptarASE(calveNueva)
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.actualizarClave,(nuevaClave,nombreApp))

	def iniciarSesion(self,usuario,contrasenia):
		if(self.existeUnUsuarioRegistrado()):
			archivoDelUsuario = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarArchivo,(usuario,))[0]
			self.keyRepository._cargarClave(archivoDelUsuario)
			contraseniaEnBase = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarUsuario,(usuario,))[0]
			if(contraseniaEnBase is not None or contraseniaEnBase is not ''):
				contraseniaLimpia = self.keyRepository.desencriptarASE(contraseniaEnBase)
				self.estadoSesion.sesionActiva = contraseniaLimpia == contrasenia
			else:
				raise LoginErrorException('Usuario o contrasena incorrectos')
		else:
			self.estadoSesion.sesionActiva = False
			raise LoginErrorException('Usuario o contrasena incorrectos')

	def registrarUsuario(self,usuario: str,contrasenia: str, contraseniaRecupero: str):
		self.iniciarClaves()
		contraseniaEncriptada = self.keyRepository.encriptarASE(contrasenia)
		contraseniaRecuperoEncriptada = self.keyRepository.encriptarASE(contraseniaRecupero)
		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.ingresarUsuario,(usuario,contraseniaEncriptada,contraseniaRecuperoEncriptada, Configuracion.rutaAlArchivoDeConfiguracion))
		self.estadoSesion = EstadoDeSesion(usuario)

	def existeUnUsuarioRegistrado(self):
		respuestaBase = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.listarUsuarios,())
		return len(respuestaBase)>0 and respuestaBase[0] is not None

	def obtenerUsuarioRegistrado(self):
		respuestaBase = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.listarUsuarios,())
		return respuestaBase[0]

	def estaAutorizadoElUsuario(self):
		return self.estadoSesion is not None and self.estadoSesion.sesionActiva

	def cargarSesionSiExiste(self):
		if(self.existeUnUsuarioRegistrado()):
			self.estadoSesion = EstadoDeSesion(self.obtenerUsuarioRegistrado())

	def validarUsuario(self):
		if(not self.estaAutorizadoElUsuario()):
			raise UsuarioNoAutorizadoException()
