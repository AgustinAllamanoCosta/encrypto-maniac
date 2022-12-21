from getpass import getpass
from Encryptador.comandos.Comando import Comando

class ComandoSensibles(Comando):

	def obtenerContraseña(self):
		return getpass("Contraseña:")