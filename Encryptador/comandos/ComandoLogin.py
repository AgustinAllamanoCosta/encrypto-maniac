from getpass import getpass
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion

class ComandoLogin(ComandoSensibles):

	def ejecutar(self,parametros: list = [], sesion: EstadoDeSesion = None)-> EstadoDeSesion:
		usuario = self.obtenerUsuario()
		self.encriptoManiac.iniciarSesion(usuario,self.obtenerContraseña())
		self.mensajeComando = 'Login correcto :)'
		return self.encriptoManiac.obtenerSesion()