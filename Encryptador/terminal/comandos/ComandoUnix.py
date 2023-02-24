from os import system
from Encryptador.terminal.comandos.Comando import Comando

class ComandoUnix(Comando):
	def __init__(self):
		pass

	def ejecutar(self, parametros):
		system('clear')