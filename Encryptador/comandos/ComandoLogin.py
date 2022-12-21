from getpass import getpass
from Encryptador.comandos.Comando import Comando

class ComandoLogin(Comando):

	def ejecutar(self,parametros):
		usuario = self.obtenerUsuario()
		self.encriptoManiac.iniciarSesion(usuario,self.obtenerContrasenia())
		self.mensajeComando = 'Login correcto :)'

	def obtenerUsuario(self):
		return input('Usuario: ')

	def obtenerContrasenia(self):
		return getpass('Contrasenia: ')