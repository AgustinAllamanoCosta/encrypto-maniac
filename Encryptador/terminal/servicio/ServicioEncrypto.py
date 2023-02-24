import logging
from Encryptador.terminal.servicio.Autorisador import Autorisador
from Encryptador.terminal.exceptions.CuentaEnBaseDuplicadaException import CuentaEnBaseDuplicadaException
from Encryptador.terminal.servicio.CredencialesManiac import Credenciales
from Encryptador.terminal.servicio.EncryptoManiac import EncryptoManiac

class ServicioEncrypto(object):

	def __init__(self,autorisadorParam: Autorisador, encryptoParam: EncryptoManiac) -> None:
		self.autorisador: Autorisador = autorisadorParam
		self.encryptador: EncryptoManiac = encryptoParam
		
	def ingresarClave(self,nombreApp,clave, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		if(self.Encryptador.terminal.existeCuentaEnBase(nombreApp) != True):
				self.Encryptador.terminal.ingresarClave(nombreApp,clave)
		else:
			logging.debug('La cuenta esta duplicada')
			raise CuentaEnBaseDuplicadaException(nombreApp)

	def buscarClave(self,nombreApp, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.Encryptador.terminal.buscarClave(nombreApp)

	def listarCuentas(self, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.Encryptador.terminal.listarCuentas()

	def eliminarClave(self,parametro,credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.Encryptador.terminal.eliminarClave(parametro)

	def actualizarClave(self,nombreApp,claveNueva, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.Encryptador.terminal.actualizarClave(nombreApp,claveNueva)

	def obtenerToken(self,nombreUsuario):
		return self.autorisador.obtenerSesionToken(nombreUsuario)

	def iniciarSesion(self,usuario: str, contrasena: str):
		self.autorisador.iniciarSesion(usuario,contrasena)

	def registrarNuevoUsuario(self,usuario: str,contrasena: str,contrasenaDeRecupero: str):
		self.autorisador.registrarUsuario(usuario,contrasena,contrasenaDeRecupero)
	
	def configurarRutaBBDD(self, nuevaRuta: str):
		self.Encryptador.terminal.configurarRutaBBDD(nuevaRuta)

	def configurarRutaKey(self, nuevaRuta: str):
		self.Encryptador.terminal.configurarRutaKey(nuevaRuta)
