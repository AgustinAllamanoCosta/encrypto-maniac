from getpass import getpass
from Encryptador.comandos.Comando import Comando
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.servicio.CredencialesManiac import Credenciales

class ComandoSensibles(Comando):

	def ejecutar(self, sesion: EstadoDeSesion ,parametros: list = ...) -> EstadoDeSesion:
		super().ejecutar(parametros)
		
	def obtenerUsuario(self):
		return input('Usuario: ')

	def obtenerContraseña(self):
		return getpass("Contraseña:")

	def obtenerCredenciales(self,sesion: EstadoDeSesion) -> Credenciales:
		print("Necesitamos confirmar que sos vos, asi que escribir la contrasena con la que te logueaste :D ")
		credenciales: Credenciales  = Credenciales()
		credenciales.contrasena = self.obtenerContraseña()
		credenciales.usuario = sesion.usuario
		credenciales.token = sesion.tokenDelUsuario
		return credenciales