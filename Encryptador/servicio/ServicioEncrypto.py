import logging
from Encryptador.servicio.Autorisador import Autorisador
from Encryptador.exceptions.CuentaEnBaseDuplicadaException import CuentaEnBaseDuplicadaException
from Encryptador.servicio.CredencialesManiac import Credenciales
from Encryptador.servicio.EncryptoManiac import EncryptoManiac

class ServicioEncrypto(object):

	def __init__(self,autorisadorParam: Autorisador, encryptoParam: EncryptoManiac) -> None:
		self.autorisador: Autorisador = autorisadorParam
		self.encryptador: EncryptoManiac = encryptoParam
		
	def ingresarClave(self,nombreApp,clave, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		if(self.encryptador.existeCuentaEnBase(nombreApp) != True):
				self.encryptador.ingresarClave(nombreApp,clave)
		else:
			logging.debug('La cuenta esta duplicada')
			raise CuentaEnBaseDuplicadaException(nombreApp)

	def buscarClave(self,nombreApp, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.encryptador.buscarClave(nombreApp)

	def listarCuentas(self, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.encryptador.listarCuentas()

	def eliminarClave(self,parametro,credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.encryptador.eliminarClave(parametro)

	def actualizarClave(self,nombreApp,claveNueva, credenciales: Credenciales):
		self.autorisador.validarUsuario(credenciales)
		return self.encryptador.actualizarClave(nombreApp,claveNueva)

	def obtenerSesion(self):
		return self.autorisador.estadoSesion

	def iniciarSesion(self,usuario: str, contrasena: str):
		self.autorisador.iniciarSesion(usuario,contrasena)

	def registrarNuevoUsuario(self,usuario: str,contrasena: str,contrasenaDeRecupero: str):
		self.autorisador.registrarUsuario(usuario,contrasena,contrasenaDeRecupero)
	
	def configurarRutaBBDD(self, nuevaRuta: str):
		self.encryptador.configurarRutaBBDD(nuevaRuta)

	def configurarRutaKey(self, nuevaRuta: str):
		self.encryptador.configurarRutaKey(nuevaRuta)
