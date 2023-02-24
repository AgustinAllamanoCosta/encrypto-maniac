from getpass import getpass
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion

class ComandoLogin(ComandoSensibles):

	def ejecutar(self,sesion:EstadoDeSesion,parametros: list = [])-> EstadoDeSesion:
		usuario = self.obtenerUsuario()
		self.encriptoManiac.iniciarSesion(usuario,self.obtenerContraseña())
		self.mensajeComando = 'Login correcto :)'
		estadoDeSession = EstadoDeSesion()
		estadoDeSession.usuario = usuario
		estadoDeSession.sesionActiva = True
		estadoDeSession.tokenDelUsuario = self.encriptoManiac.obtenerToken(usuario)
		return estadoDeSession