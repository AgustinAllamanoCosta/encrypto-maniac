from getpass import getpass
from Encryptador.comandos.Comando import Comando
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.servicio.CredencialesManiac import Credenciales

class ComandoSensibles(Comando):

	def ejecutar(self, parametros: list = ..., sesion: EstadoDeSesion = None) -> EstadoDeSesion:
		super().ejecutar(parametros)
		return self.encriptoManiac.obtenerSesion()

	def obtenerUsuario(self):
		return input('Usuario: ')

	def obtenerContraseña(self):
		return getpass("Contraseña:")

	def obtenerCredenciales(self) -> Credenciales:
		print("Necesitamos confirmar que sos vos, asi que escribir la contrasena con la que te logueaste :D ")
		credenciales: Credenciales  = Credenciales()
		sesion: EstadoDeSesion = self.encriptoManiac.obtenerSesion()
		credenciales.contrasena = self.obtenerContraseña()
		credenciales.token = sesion.tokenDelUsuario
		credenciales.usuario = sesion.usuario
		return credenciales