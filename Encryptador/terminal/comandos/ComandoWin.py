from os import system
from Encryptador.terminal.comandos.Comando import Comando

class ComandoWin(Comando):
	def __init__(self):
		pass

	def ejecutar(self, parametros):
		system('cls')